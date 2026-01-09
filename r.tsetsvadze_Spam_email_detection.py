import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# Load dataset
data = pd.read_csv("../data/r_tsertsvadze25_84687.csv")

# Features and label
X = data[["words", "links", "capital_words", "spam_word_count"]]
y = data["is_spam"]

# Split: 70% training, 30% testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# Train Logistic Regression model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Print coefficients
coefficients = pd.Series(model.coef_[0], index=X.columns)
print("Logistic Regression Coefficients:")
print(coefficients)

from sklearn.metrics import confusion_matrix, accuracy_score

# Predict on test data
y_pred = model.predict(X_test)

# Confusion Matrix and Accuracy
cm = confusion_matrix(y_test, y_pred)
accuracy = accuracy_score(y_test, y_pred)

print("\nConfusion Matrix:")
print(cm)
print("\nAccuracy:", accuracy)


def classify_email(words, links, capital_words, spam_word_count):
    features = [[words, links, capital_words, spam_word_count]]
    prediction = model.predict(features)
    return "Spam" if prediction[0] == 1 else "Legitimate"

# Example check
result = classify_email(words=120, links=5, capital_words=20, spam_word_count=8)
print("\nCustom email classification:", result)


import matplotlib.pyplot as plt

# Class distribution
data["is_spam"].value_counts().plot(kind="bar")
plt.title("Spam vs Legitimate Email Distribution")
plt.xlabel("Class")
plt.ylabel("Number of Emails")
plt.show()

coefficients.sort_values().plot(kind="barh")
plt.title("Feature Importance (Logistic Regression)")
plt.xlabel("Coefficient Value")
plt.ylabel("Feature")
plt.show()






