# CMSC4383_ML_project
Housing price prediction project


This repo contains all the code for our ML project. The project involves all the steps from EDA of our dataset to training and finetuning the models, and finally testing them at the end.

In order to run, you must have 5 seperate files needed to create our custom dataset.
  - CPIAUCSL.CSV (inflation dataset)
  - MORTGAGE30US.CSV (morgage rates)
  - RRVRUSQ156N.csv (rental vaccancy rates)
  - Metro_median_sale_price_uc_sfrcondo_week.csv (weekly sale price for property provided by Zillow)
  - Metro_zhvi_uc_sfrcondo_tier_0.33_0.67_month.csv (Zillow computed house index value weekly)


The ml_project.ipynb is a jupyter notebook that has code sectioned off based on various parts of the project.
Each section is chronilogical so they need to be run in order otherwises errors will occur.
Install required packages found in the requirements.txt file and the notebook code will run smoothly. 
