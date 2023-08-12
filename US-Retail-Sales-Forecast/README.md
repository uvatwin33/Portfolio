# Time Series Modeling on the U.S. Retail Sales

This project attempts to forecast the U.S. retail sales based on the monthly retail sales from January 1992 until June 2021 from the us\_retail\_sales.csv.

#
**Languages Used:**

- Python

#
**Packages Used:**

- Deep Learning Modeling (Neural Prophet by Meta)

#
**Time Series Modeling**

We use the model to predict the monthly retail sales on the last year of data by following steps:

- Plot the data with proper labeling and make some observations on the graph.
- Split this data into a training and test set. Use the last year of data (July 2020 – June 2021) of data as your test set and the rest as your training set.
- Use the training set to build a predictive model for the monthly retail sales.
- Use the model to predict the monthly retail sales on the last year of data.
- Report the RMSE of the model predictions on the test set.

#
**Results**

The above graph shows that the retailers suffered a significant drop in sales during the 2008-2009 recession. But during the beginning of the pandemic in 2020, there was even a significant decline in retail sales as indicated by a cliff. Once the retail hit its rock bottom, it slowly rebounded up and climbed past the pre-pandemic high.

Based on the prediction from the forecast of the U.S. Retail Sales, after 2021 the sales reached 475,000, and its upward trend continues. But the prediction would not surpass 500,000 in 2023. Lastly, the following is the RMSE of the model predictions on the test set:

-	SmoothL1Loss: 0.022964
-	MAE: 57319.296875
-	RMSE: 62984.695312
