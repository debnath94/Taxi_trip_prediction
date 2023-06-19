About Dataset
Overview

BigQuery is Google's fully managed, NoOps, low cost analytics database. With BigQuery you can query terabytes and terabytes of data without having any infrastructure to manage, or needing a database administrator.

BigQuery Machine Learning BQML is where data analysts can create, train, evaluate, and predict with machine learning models with minimal coding.

In this you will explore millions of New York City yellow taxi cab trips available in a BigQuery Public Dataset. You will create a machine learning model inside of BigQuery to predict the fare of the cab ride given your model inputs and evaluate the performance of your model and make predictions with it.

perform the following tasks:

Query and explore the public taxi cab dataset.
Create a training and evaluation dataset to be used for batch prediction.
Create a forecasting (linear regression) model in BQML.
Evaluate the performance of your machine learning model.

There are several model types to choose from:

Forecasting numeric values like next month's sales with Linear Regression (linear_reg).
Binary or Multiclass Classification like spam or not spam email by using Logistic Regression (logistic_reg).
k-Means Clustering for when you want unsupervised learning for exploration (kmeans).

Note: There are many additional model types used in Machine Learning (like Neural Networks and decision trees) and available using libraries like TensorFlow. At this time, BQML supports the three listed above. Follow the BQML roadmap for more information.

For reference sake of you we also released notebook which is available in this try to explore from that .use AutoMl foundational Models to automatically selecting important features from dataset and Model selection .

you can also go with spectral clustering algorithms upcourse it is not an unsupervised task but it is correlated ,visualize the Fare trip prices .so that cab drive easily identifies fare trips in their respective locations .

Build a Forecasting model which helps for cab drives like (uber,rapido) which reach their customers easily and short time

Dataset :
⏱️ 'trip_duration': How long did the journey last?[in Seconds]
🛣️ 'distance_traveled': How far did the taxi travel?[in Km]
🧑‍🤝‍🧑 'num_of_passengers': How many passengers were in the taxi?
💵 'fare': What's the base fare for the journey?[In INR]
💲 'tip': How much did the driver receive in tips?[In INR]
🎀 'miscellaneous_fees': Were there any additional charges during the trip?e.g. tolls, convenience fees, GST
etc.[In INR]
💰 'total_fare': The grand total for the ride (this is your prediction target!).[In INR]
⚡ 'surge_applied': Was there a surge pricing applied? Yes or no?