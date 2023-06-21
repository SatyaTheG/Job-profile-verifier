# Import libraries
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# Load the dataset
df = pd.read_csv('./UpdatedResumeDataSet.csv')

# Preprocess the text data
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df['Resume'])

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, df['Category'], test_size=0.2, random_state=10)

# Train the model
model = LogisticRegression()
model.fit(X_train, y_train)
