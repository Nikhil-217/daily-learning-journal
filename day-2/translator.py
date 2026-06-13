from tkinter import *
from googletrans import Translator

translator = Translator()

def translate_text():
    text = input_box.get("1.0", END)
    translated = translator.translate(text, src='en', dest='te')
    output_box.delete("1.0", END)
    output_box.insert(END, translated.text)

root = Tk()
root.title("English to Telugu Translator")
root.geometry("500x400")

Label(root, text="English Text").pack()

input_box = Text(root, height=5)
input_box.pack()

Button(root, text="Translate", command=translate_text).pack()

Label(root, text="telugu Text").pack()

output_box = Text(root, height=5)
output_box.pack()

root.mainloop()
