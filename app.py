from model import model,vectorizer
import streamlit as st


# Define the app
def app():
    # Upload the resume file
    resume_file = st.file_uploader("Upload your resume file")

    # If the resume file is uploaded
    if resume_file is not None:
        # Read the resume file
        resume_data = resume_file.read()

        X = vectorizer.transform([resume_data])
        result = model.predict(X)

        # Display the job profile
        st.write("The job profile for your resume is:", result)

if __name__ == "__main__":
    app()
