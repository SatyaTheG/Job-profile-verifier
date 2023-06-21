from model import model,vectorizer
import streamlit as st

import PyPDF2

def extract_text_from_pdf(pdf_file):
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

# Define the app
def app():
    st.set_page_config(page_title='Job Profile Verifier',
                       page_icon=':clipboard:', layout='wide')
    st.title('Job Profile Verifier :sleuth_or_spy:')


    # Upload the resume file
    resume_file = st.sidebar.file_uploader("Upload your PDF file")

    # If the resume file is uploaded
    if resume_file is not None:
        # Read the resume file
        text = extract_text_from_pdf(resume_file)
        X = vectorizer.transform([text])
        result = model.predict(X)

        with st.spinner('Analyzing resume... :mag_right::hourglass_flowing_sand:'):

            with st.expander("The job profile for your resume is:"):
                st.markdown( result)

if __name__ == "__main__":
    app()
