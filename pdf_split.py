from sys import path_importer_cache
from PyPDF2 import PdfFileWriter, PdfFileReader

def main():
    path_to_pdf = input("Path to PDF: ")
    print(f"path: {path_to_pdf}")

    pages_to_combine = input("pages to combine: ")

    new_document_name = input("new document name: ")

    print(f"{new_document_name}.pdf")

    pages_to_combine_arr = []

    for i in pages_to_combine.split(" "):
        print(i)
        pages_to_combine_arr.append(int(i))

    print(pages_to_combine_arr)

    inputpdf = PdfFileReader(open(path_to_pdf, "rb"))
    output = PdfFileWriter()

    for i in range(inputpdf.numPages):
        if i+1 in pages_to_combine_arr:
            output.addPage(inputpdf.getPage(i))
        
    with open(f"{new_document_name}.pdf", "wb") as outputStream:
        output.write(outputStream)


if __name__ == "__main__":
    main()