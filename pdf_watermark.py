import PyPDF2

template = PyPDF2.PdfFileReader(open("pdf/merged_pdf.pdf", "rb"))
watermark = PyPDF2.PdfFileReader(open("pdf/wtr.pdf", "rb"))
output_pdf = PyPDF2.PdfFileWriter()

for i in range(template.getNumPages()):
    page = template.getPage(i)
    page.mergePage(watermark.getPage(0))
    output_pdf.addPage(page)
    with open("pdf/watermark_output.pdf", "wb") as file:
        output_pdf.write(file)
