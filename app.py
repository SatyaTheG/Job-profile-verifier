import pickle
from extract import extract_text_from_pdf
from sklearn.feature_extraction.text import TfidfVectorizer
# load the vectorizer
loaded_vectorizer = pickle.load(open('vectorizer.pickle', 'rb'))
# load the model from disk
filename = 'finalized_model.sav'
loaded_model = pickle.load(open(filename, 'rb'))
loaded_vectorizer = pickle.load(open('vectorizer.pickle', 'rb'))
filename = 'finalized_model.sav'
loaded_model = pickle.load(open(filename, 'rb'))

# Define the app
def app():
    # Upload the resume file
    resume_file = st.file_uploader("Upload your resume file")

    # If the resume file is uploaded
    if resume_file is not None:
        # Read the resume file
        resume_data = resume_file.read()

        X = loaded_vectorizer.transform([resume_data])
        result = loaded_model.predict(X)

        # Display the job profile
        st.write("The job profile for your resume is:", result)

if __name__ == "__main__":
    app()
