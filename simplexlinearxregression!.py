# -*- coding: utf-8 -*-
"""SIMPLExLINEARxREGRESSION!.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1c7Uac48XuoO30UQhmHuqodG1IWX0vGSq

EXPERIMENTx6 BY 229X1A2856
"""



import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
import math

# Load the dataset
data = pd.read_csv('/content/hp_data.csv')

# Display basic dataset information
print("First 5 rows:")
print(data.head())
print("\nLast 5 rows:")
print(data.tail())
print("\nDataset Description:")
print(data.describe())

# Data Preprocessing
# Remove null values
data.dropna(inplace=True)

# Remove duplicates
data.drop_duplicates(inplace=True)

# Encode categorical variables
if 'place' in data.columns:
    enc = LabelEncoder()
    data['place'] = enc.fit_transform(data['place'])

# Define input and output variables
X = data[['sqft', 'place', 'yearsOld', 'totalFloor', 'bhk']]
y = data['price']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=10)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
y_predict = model.predict(X_test)

# Model evaluation
r2 = r2_score(y_test, y_predict)
mae = mean_absolute_error(y_test, y_predict)
mse = mean_squared_error(y_test, y_predict)
rmse = math.sqrt(mse)

# Extract model parameters
intercept = model.intercept_
coefficients = model.coef_

# Print evaluation results
print(f"Intercept: {intercept}")
print(f"Coefficients: {coefficients}")
print(f"R² Score: {r2}")
print(f"MAE: {mae}")
print(f"MSE: {mse}")
print(f"RMSE: {rmse}")

# Scatter plot of actual vs predicted values
plt.figure(figsize=(8, 6))
sns.scatterplot(x=y_test, y=y_predict, color='blue', alpha=0.5)

# Best fit line
sns.regplot(x=y_test, y=y_predict, scatter=False, color='red')

plt.xlabel("Actual Prices")
plt.ylabel("Predicted Prices")
plt.title("Actual vs Predicted House Prices")
plt.show()

"""MULTI-REGRESSION!!!"""

import numpy as np
y_pred_all = model.predict(X)

features = ['sqft', 'place', 'yearsOld', 'totalFloor', 'bhk']
for feature in features:
    plt.figure(figsize=(8, 5))
    plt.scatter(data[feature], data['price'], color='grey', alpha=0.5, label='Actual Data')
    plt.scatter(data[feature], y_pred_all, color='red', alpha=0.5, label='Predicted Data')
    feature_range = np.linspace(data[feature].min(), data[feature].max(), 100)
    temp_data = {col: np.full(100, data[col].mean()) for col in features}
    temp_data[feature] = feature_range
    X_temp = pd.DataFrame(temp_data)
    y_temp = model.predict(X_temp)
    plt.plot(feature_range, y_temp, color='blue', linewidth=2, label='Best Fit (Partial)')
    plt.xlabel(feature)
    plt.ylabel('House Price')
    plt.title(f'House Price vs {feature}')
    plt.legend()
    plt.show()









