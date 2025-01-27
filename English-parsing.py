# read a pdf file 
from PyPDF2 import PdfReader
reader=PdfReader("English_paragraph.pdf")
text=" "
for page in reader.pages:
    text=page.extract_text()

    print(text)

# print(text)
#  by using this basic split method the sentences are being seperated on the basis of "." only which may conflift with cases like e.g.
#  and words are being seperated on the basis of space 

sentences = text.split('. ')  # Basic splitting on period+space
print(sentences)
words = text.split()  # Splits on spaces
print(words)
