from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import numpy as np

#260 == 5 years of data
START = 260
#52 weeks in year
STEP = 52

def predict(train, test, predictors, target):
    rf = RandomForestClassifier(min_samples_split=10, random_state=1)
    rf.fit(train[predictors], train[target])
    preds = rf.predict(test[predictors])
    return preds


# cross validaiton should be used as you dont use future to predict the past -- but it gives false sense of model working well

#will do backtesting 
#lets us generate predictions for most data and respect the idea of using past data to predict future and not vice versa 

def backtest(data, predictors, target):
    all_preds=[]
    for i in range(START, data.shape[0], STEP):
        train = price_data.iloc[:i]
        test = price_data.iloc[i: (i+STEP)]
        all_preds.append(predict(train,test,predictors,target))

    preds = np.concatenate(all_preds)
    return preds, accuracy_score(data.iloc[START:][target], preds)
 


 preds, accuracy = backtest(price_data, predictors, target)
