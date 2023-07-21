import PyPDF2

# f = open('Working_Business_Proposal.pdf', 'rb')

pdf_reader = PyPDF2.PdfReader("Working_Business_Proposal.pdf")

page = pdf_reader.pages[0]
print(page.extract_text(0))

# page_one = pdf_reader.()
# print(page_one)

# page_one_text = page_one.get
# print(page_one_text)