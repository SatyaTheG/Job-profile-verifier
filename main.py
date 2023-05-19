import pickle
from extract import extract_text_from_pdf
from sklearn.feature_extraction.text import TfidfVectorizer
from tkinter import messagebox
from tkinter import *
from tkinter import filedialog
# load the vectorizer
loaded_vectorizer = pickle.load(open('vectorizer.pickle', 'rb'))
# load the model from disk
filename = 'finalized_model.sav'
loaded_model = pickle.load(open(filename, 'rb'))
loaded_vectorizer = pickle.load(open('vectorizer.pickle', 'rb'))
filename = 'finalized_model.sav'
loaded_model = pickle.load(open(filename, 'rb'))

def prerec(old):
    file_types = (("PDF files", "*.pdf"), ("All files","*.*"))
    file_path = filedialog.askopenfilename(filetypes=file_types)
    old.destroy()
    # load the vectorizer

    pdf_text = extract_text_from_pdf(file_path)
    X = loaded_vectorizer.transform([pdf_text])
    result = loaded_model.predict(X)
    messagebox.showinfo("JOB ROLE IDENTIFIER","Eligible job role: {}".format(result))
 

def main():
    # Create a new window for the message box
    message_box = Tk()
    message_box.geometry("480x120+720+480")
    message_box.title("JOB ROLE IDENTIFIER")

 

    # Add "Yes" and "No" buttons to the message box
    button_frame = Frame(message_box)
    yes_button = Button(button_frame, text="Upload Resume", command=lambda:prerec(message_box))
    yes_button.pack(side=LEFT, padx=10, pady=10)
    button_frame.pack()
    message_box.mainloop()


if __name__ == "__main__":
    main()