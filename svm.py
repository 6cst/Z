# -*- coding: utf-8 -*-
"""SVM.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1-ga4VvKS9ocaF73fgBtZo3bMCH7REoo0
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score, precision_score, recall_score, f1_score
import warnings
warnings.filterwarnings('ignore')

# Load the iris dataset from CSV
df = pd.read_csv('/content/iris.csv')
# Check the shape of the dataset
print("Shape of the dataset:", df.shape)
# Check for null values in each column and drop them
print("Null values in each column:")
print(df.isnull().sum())
df.dropna(inplace=True)
print("Shape after dropping null values:", df.shape)

# Check for duplicate rows and drop them
print("Number of duplicate rows:", df.duplicated().sum())
df.drop_duplicates(inplace=True)
print("Shape after dropping duplicates:", df.shape)

# Display the first 5 rows of the dataset
print("First 5 rows:")
print(df.head())

# Display the last 5 rows of the dataset
print("Last 5 rows:")
print(df.tail())

# Display descriptive statistics of the dataset
print("Descriptive statistics:")
print(df.describe())

# Print the column names
print("Column names:")
print(df.columns)
print("\n\n")
# Print unique values in the target column (assuming the target column is named 'species')
print("Unique target values:")
print(df['target'].unique())

# Pie Chart for target distribution
target_counts = df['target'].value_counts()
plt.figure(figsize=(6,6))
plt.pie(target_counts, labels=target_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('Distribution of Iris Species')
plt.show()

# Bar Graph for Average Sepal Length per Species
plt.figure(figsize=(8,6))
sns.barplot(x='target', y='sepal_length', data=df)
plt.title('Average Sepal Length per Species')
plt.xlabel('Species')
plt.ylabel('Average Sepal Length')
plt.show()

# Define features and target variable
# Assuming features are all columns except 'species'
X = df.drop('target', axis=1)
y = df['target']

# Split the dataset into training and testing sets (e.g., 70% training, 30% testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Print the shapes of the training and testing sets
print("Shape of X_train:", X_train.shape)
print("Shape of X_test:", X_test.shape)

# Define the SVM model (using a linear kernel; you can change to 'rbf' or other kernels if desired)
svm_model = SVC(kernel='linear', random_state=42)

# Train the SVM model on the training set
svm_model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = svm_model.predict(X_test)

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:")
print(cm)

# Classification Report
cr = classification_report(y_test, y_pred)
print("Classification Report:")
print(cr)

# Calculate Accuracy, Precision, Recall, and F1-Score
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, average='weighted')
recall = recall_score(y_test, y_pred, average='weighted')
f1 = f1_score(y_test, y_pred, average='weighted')

print("Accuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)
print("F1 Score:", f1)

# Perform 5-fold cross-validation on the whole dataset
cv_scores = cross_val_score(svm_model, X, y, cv=5)
print("Cross-Validation Scores:", cv_scores)
print("Mean Cross-Validation Score:", cv_scores.mean())

from collections import Counter
Counter(df.target)

# Parameter Tuning
model = SVC(C=0.1)# c=0.1
model.fit(X_train,y_train)
y_predict = model.predict(X_test)
accuracy_score(y_test,y_predict)

#gamma
model = SVC(gamma=0.01)# gamma=0.01
model.fit(X_train,y_train)
y_predict = model.predict(X_test)
accuracy_score(y_test,y_predict)

model = SVC(kernel='poly')
model.fit(X_train,y_train)
y_predict = model.predict(X_test)
accuracy_score(y_test,y_predict)

import pandas as pd
import matplotlib.pyplot as plt

# Read the iris dataset from CSV file
data = pd.read_csv('/content/iris.csv')
print("First 5 rows of the dataset:")
print(data.head())

# Visualisation:
# Splitting the dataset into three parts (assumed order: first 50 = one species, next 50 = another, final 50 = third)
df0 = data[:50]
df1 = data[50:100]
df2 = data[100:150]

# Optional: Extracting features and target (first 100 rows, first 2 columns and target)
# Adjust 'target' if your CSV column is named differently (e.g., 'species')
x = data.iloc[:100, :2]
y = data['target'][:100]

# Plotting the scatter plots for the three groups
plt.figure(figsize=(8,6))
plt.scatter(df0['sepal_length'], df0['sepal_width'], color='green', marker='+', label='Group 1 (Rows 0-49)')
plt.scatter(df1['sepal_length'], df1['sepal_width'], color='blue', marker='*', label='Group 2 (Rows 50-99)')
plt.scatter(df2['sepal_length'], df2['sepal_width'], color='red', marker='*', label='Group 3 (Rows 100-149)')

plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.title('Iris Dataset: Sepal Length vs Sepal Width')
plt.legend()
plt.show()

"""**EXPx07**"""

#import packages
from sklearn.svm import SVC
import pandas as pd
from sklearn.metrics import accuracy_score,classification_report,confusion_matrix
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

df = pd.read_csv('/content/iris.csv')

data.shape

data.target.unique()

data.info()

data.describe()

data.isnull().sum()

from collections import Counter
Counter(data.target)

df.target.value_counts()

X = data.iloc[:,:-1]
y = data[['target']]





































































































