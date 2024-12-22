import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
excel_path = "finalmarks.xlsx"
df = pd.read_excel(excel_path)
print("Original Data:")
print(df)
score_columns = ['Telugu', 'Hindi', 'English', 'Mathematics', 'Science', 'Social']
df['Average'] = np.mean(df[score_columns], axis=1)
print("\nData with Average Scores:")
print(df)
plt.figure(figsize=(10, 6))
plt.bar(df['Name'], df['Average'], color='blue')
plt.xlabel('Student Names')
plt.ylabel('Average Scores')
plt.title('Average Scores of Students')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
plt.figure(figsize=(8, 8))
plt.pie(df[score_columns].mean(), labels=score_columns, autopct='%1.1f%%', startangle=140)
plt.title('Contribution of Each Subject to Average Score')
plt.show()
X = df[['Telugu', 'Hindi', 'English', 'Science', 'Social']]
y = df['Mathematics']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
model = LinearRegression()
model.fit(X_train, y_train)
df['Predicted_Math'] = model.predict(X)
print("\nData with Original and Predicted Math Scores:")
print(df[['Name', 'Mathematics', 'Predicted_Math']])
plt.figure(figsize=(10, 6))
plt.plot(df['Name'], df['Mathematics'], marker='o', label='Original Math Scores')
plt.plot(df['Name'], df['Predicted_Math'], marker='o', linestyle='dashed', label='Predicted Math Scores')
plt.xlabel('Student Names')
plt.ylabel('Math Scores')
plt.title('Original and Predicted Math Scores of Students')
plt.xticks(rotation=45, ha='right')
plt.legend()
plt.tight_layout()
plt.show()
print("\nModel Evaluation:")
print("Mean Absolute Error:", metrics.mean_absolute_error(df['Mathematics'], df['Predicted_Math']))
print("Mean Squared Error:", metrics.mean_squared_error(df['Mathematics'], df['Predicted_Math']))
print("Root Mean Squared Error:", np.sqrt(metrics.mean_squared_error(df['Mathematics'], df['Predicted_Math'])))
