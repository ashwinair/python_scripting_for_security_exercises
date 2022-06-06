# Use a Python string method to prove which of the following files
# are .pdf files, and which aren't.
# Call the method on each file string and print() Python's response.

file_1 = "operators.pdf"
file_2 = "snowfall.jpg"
file_3 = "uncle-joes-wedding.doc"
file_4 = "invitation.pdf"


# print(len(file_1))
# print(file_1[9:13])

def is_this_a_pdf_file(self):
    length = len(self)
    slice_str = self[length - 4:length]
    if slice_str == ".pdf":
        print("Yes!")
    else:
        print("Nooo!")


is_this_a_pdf_file(file_1)
is_this_a_pdf_file(file_2)
is_this_a_pdf_file(file_3)
is_this_a_pdf_file(file_4)
