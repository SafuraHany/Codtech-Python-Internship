import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

# Sample dataset
data = {
    "email": [
        "Win money now",
        "Hello friend how are you",
        "Limited offer buy now",
        "Meeting tomorrow at office",
        "Congratulations you won a prize",
        "Let's have lunch tomorrow"
    ],
    "label": ["spam", "ham", "spam", "ham", "spam", "ham"]
}

df = pd.DataFrame(data)

# Convert text to numbers
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df["email"])
y = df["label"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train model
model = MultinomialNB()
model.fit(X_train, y_train)

# Predict
predictions = model.predict(X_test)

print("Model Accuracy:", accuracy_score(y_test, predictions))