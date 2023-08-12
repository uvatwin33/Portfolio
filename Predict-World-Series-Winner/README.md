# **Predicting A World Series Winner**

**Overview**

This project aims to predict a world series winner based on the past baseball data from a given season, mainly using the logistic regression and other classified methods. Also, my model will attempt to find any features of winning a World Series title. My target for this machine learning model is to win a World Series (WSWin).

**Languages Used**

- **Python**

**Packages Used**

- Pandas
- Numpy
- Matplotlib
- Seaborn
- Sklearn

**Models Used**

- Linear Regression
- Logistic Regression
- Decision Tree
- K Nearest Neighbors (KNN)
- Random Forest

**Data**

Datasets were obtained from Sean Lahman's baseball database. Data was cleaned by removing the rows tht did not have any World Series data prior to 1903 as well as the data from 2020 where the season was abbreviated to just 60 games due to the pandemic.

Also, I've decided to drop columns that are not attributable to winning a World Series title such as Division ID, names of parks where team play, and team ID's and their retro ID's. I am also removing Wins and Losses (i.e. Division Win, League Win, & Wild Card Win) since the number of games played in the past seasons vary over time. For example, MLB introduced the Wild Card in 1994 to expand the playoff teams, so for 90 years prior to the inclusion of the Wild Card in the postseason, there were no Wild Card records available for each team. However, I am keeping the the 'WSWin' (World Series Win) column. More importantly, I will select the 'WSWin' column as my target variable so the other 'win' categories are not relevant to this analysis.


**Feature Engineering**

Now we are adding some offensive metrics to the teams data. Two main categories to add are OBP (on-base percentage) and OPS (on-base percentage plus slugging) which are considered important offensive stats in modern baseball. OBP is a statistical formula that indicates how often a batter reaches a base overall. And OPS adds OBP to slugging percentage to get one number. OPS indicates how well a hitter can reach base, with how well he can hit for average and power per MLB.com.

**Modeling Results**

**The following metrics are accuracy scores:**


- Linear Regression: 14.18%
- Decision Tree Classifier: 94.98%
- Logistic Regression Model: 93.93%

When the KNN and Random Forest were added to a Pipeline using a Grid Search and Hypertuning, the best model in terms of accuracy was the Logistic Model, slightly edging the Decision Tree Classifier Model

- Logistic Regression after being hypertuned: 94.98%

After examining the high accuracy score, the target variable ('WSWin') was imbalanced, i.e. the number of losses overwhelmingly outweighing the number wins. Consequently, when the stats for the Kansas City Royals, a winner of the World Series from the 2015 MLB season were input into the model, it did not predict the team as a winner. To address the issue of data imbalance, the following three techniques will need to be explored in the future:

- Under-sampling
- Over-sampling
- Creating synthetic data (SMOTE)

