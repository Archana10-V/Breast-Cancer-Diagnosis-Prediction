import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, classification_report


# Load dataset
data = pd.read_csv("breast_cancer.csv")

# Remove rows where diagnosis is missing
data = data.dropna(subset=["diagnosis"])

# Select 30 input features
X = data.drop(columns=["id", "diagnosis"])

# Target
y = data["diagnosis"]


# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)


# Create ML pipeline
model = Pipeline([
    ("imputer", SimpleImputer(strategy="median")),
    ("scaler", StandardScaler()),
    ("classifier", LogisticRegression(max_iter=5000))
])


# Train model
model.fit(X_train, y_train)


# Test model
y_pred = model.predict(X_test)


# Accuracy
accuracy = accuracy_score(y_test, y_pred)

print("Model Training Completed")
print("Accuracy:", round(accuracy * 100, 2), "%")

print("\nClassification Report:")
print(classification_report(y_test, y_pred))


# Save model
with open("model.pkl", "wb") as file:
    pickle.dump(model, file)

print("\nmodel.pkl created successfully!")