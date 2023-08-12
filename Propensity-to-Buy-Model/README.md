## **Propensity-to-Buy-Model**

Binary Classification

**Languages Used**

- SQL
- Python

**Models Used**

- K Neanerst Neighbors (KNN)
- Logistic Regression
- Decision Tree
- Random Forest Classifier
- TabNet (Neural Network for tabular data)
- Catboost
- Ensemble Model (KNN, Logistic Regression, Decision Tree, and Random Forest)

**Note** : this was a collaborative project with one partner (Sherman)in the class. We both worked on and reviewed models and code, discussed and improved results, and evaluated and presented results.

**Business Problem**

The problem that we were trying to solve was to predict whether a user, who shopped online and got approved for a life insurance policy with my partner's company, would purchase a policy. Given that only 30-40% of users who apply for a policy and get approval, we deemed this group of potential customers important for the company to focus on since they've already cleared a crucial barrier to becoming a policy holder once they receive approval.

**Implications:**

1. The ability to predict who will purchase a policy can help the company better allocate resources as far as following up with approved users but not have purchased a policy. Currently, the marketing team is having an agent contact the approved user via phone to follow up and answer questions.
2. Understanding and knowing the characteristics of users who are likely to bind (or purchase) can lead to an efficient resource allocation in the future for marketing team and its product development.

**Solution:** My partner and I were able to explore and test more models than if we had been working individually. For example, we were able to implement and tune TabNet, CatBoost, and Ensemble models. The following results ensued according to the best metric numbers:

- Best Accuracy (86.4%): CatBoost
- Best Recall (83%): TabNet Classifier
- Best Precision (86%): Random Forest
- Best F1 (83%): CatBoost and Ensemble model

At the end, though, we decided that F1 was the best metric for our business problem, since we wanted to control for both false positives and false negatives and the target variable was imbalanced (about one-third of approved users purchase a policy). And we chose the CatBoost model was perhaps the best option to develop further in the future vs. Ensemble model due to its simplicity of implementation.

We also investigated the feature importance for the difference in premiums that users saw between their quoted price and the price for the product that they were approved for. Using both the raw difference in premiums as well as the difference as a percent of the quoted premium, we found the following results:

- Feature importance in various model

- Recursive feature extraction

- By examining purchase rate across premiums, do users' tendency to purchase at a higher rate when they don't see a higher premium after being approved regardless of the size of the premium? This particular investigation allowed us to separate the issue of the size of the premium difference from the size of the premium in terms of better understanding what influences users' decision to purchase.

This feature was found to be one of the Top 10 features out of 40 in terms of feature importance in these models.
