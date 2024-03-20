import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load the Iris dataset
iris_df = pd.read_csv('Iris.csv')

# Drop the 'Id' column
iris_df.drop('Id', axis=1, inplace=True)

# Print the column names to verify
print(iris_df.columns)

# Strip column names to remove extra spaces
iris_df.columns = iris_df.columns.str.strip()

# Check the column names again
print(iris_df.columns)

# Split the dataset into features and target variable
X = iris_df.drop('Species', axis=1)  # Correct the column name here
y = iris_df['Species']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Random Forest classifier
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate the model
accuracy = model.score(X_test, y_test)
print("Model Accuracy:", accuracy)

# Save the trained model
joblib.dump(model, 'model.pkl')
