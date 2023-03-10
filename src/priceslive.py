import pandas as pd
from datetime import timedelta
import matplotlib

#file names for mortgages, rental vaccancy, and inflation
fed_files = ["datasets/MORTGAGE30US.csv", "datasets/RRVRUSQ156N.csv", "datasets/CPIAUCSL.csv" ]

#read them in using list comp
#tell pandas to parse dates into dateTime
#use first column for row indicies
fed_dfs = [pd.read_csv(f, parse_dates=True, index_col=0) for f in fed_files]

#mergining all data into one big dataframe
fed_data = pd.concat(fed_dfs, axis=1)

#need to fix the timelines of all data to be on same timeline (weekly, monthly , biweekly)
 
 #will fill data up - so rental vaccancy monthly so assume for all weeks in month its the same value -- do same for other data
#the ffill does a forward fill for all values missing it takes previous value and applies it forward
fed_data = fed_data.ffill()

#first value has medium sales prices for houses each week, second is zillow computed house index indicating how much it thinks average house value is worth 
zillow_files = ["datasets/Metro_median_sale_price_uc_sfrcondo_week.csv", "datasets/Metro_zhvi_uc_sfrcondo_tier_0.33_0.67_month.csv"]

zillow_dfs = [pd.read_csv(f) for f in zillow_files]

#dataframe takes info for specific regions
#if we doing entire us take [0] row otherwise you can go find regions like chicago, dallas, austin etc


#reformat data to be each row as week and column is price it was sold --- changed first 3 to 0 
zillow_dfs = [pd.DataFrame(df.iloc[3,5:]) for df in zillow_dfs]




#combine house price (weekly) and house value (monthly) dataset togheter 
#converts 
for df in zillow_dfs:
    #convert string to datatime
    df.index = pd.to_datetime(df.index)
    #takes dates and creates month column to combine dataframes
    df["month"] = df.index.to_period("M")

price_data = zillow_dfs[0].merge(zillow_dfs[1], on="month")
price_data.index = zillow_dfs[0].index

del price_data["month"]
price_data.columns = ["price", "value"]

fed_data.index = fed_data.index + timedelta(days=2)

price_data = fed_data.merge(price_data, left_index=True, right_index=True)

price_data.columns = ["interest", "vaccancy", "cpi", "price", "value"]

#plots price as y and x axis is dates
price_data.plot.line(y="price", use_index=True)

price_data["adj_price"] = price_data["price"] / price_data["cpi"] * 100

#plot this adjusted house price that takes out inflation to see how house prices is changing without adjust for inflation
price_data.plot.line(y="adj_price", use_index=True)

price_data.to_csv("datasets/Housing_chicago_dataset.csv")




