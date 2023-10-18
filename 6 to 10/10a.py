from PyPDF2 import PdfReader, PdfWriter
# PDF file and the list of pages to extract
dictionary = {
'sample1.pdf':[0,1],
'sample2.pdf':[0,1]
}
writer = PdfWriter()
for name, pages in dictionary.items():
    f1 = open(name, "rb")
    reader = PdfReader(f1)
    for n in pages:
        p = reader.pages[n]
        writer.add_page(p)
f1.close()
f2 = open("result.pdf", "wb")
writer.write(f2)
f2.close()