# Import libraries
from extract import extract_text_from_pdf
import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


# Load the dataset
df = pd.read_csv(r'C:\Users\Satyanarayan Sahoo\Desktop\satya\Rough\UpdatedResumeDataSet.csv')

# Preprocess the text data
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df['Resume'])

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, df['Category'], test_size=0.2, random_state=10)

# Train the model
model = LogisticRegression()
model.fit(X_train, y_train)

# Save the vectorizer
vec_file = 'vectorizer.pickle'
pickle.dump(vectorizer, open(vec_file, 'wb'))

# save the model to disk
filename = 'finalized_model.sav'
pickle.dump(model, open(filename, 'wb'))

# Evaluate the model
y_pred = model.predict(X_test)
print("Accuracy percentage:", (accuracy_score(y_test, y_pred)*100))

