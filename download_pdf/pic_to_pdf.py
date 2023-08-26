import glob
import os.path
import fitz


# 图片转PDF
def pic2pdf2(doc1):
    Doc=doc1[0:-1]
    doc = fitz.open()
    for img in sorted(glob.glob(doc1), key=os.path.getmtime):
        print(img)
        imgdoc = fitz.open(img)
        imgpdf = imgdoc.convert_to_pdf()
        imgPDF = fitz.open("pdf",imgpdf)
        doc.insert_pdf(imgPDF)
    doc.save(Doc+"Image.pdf")
    doc.close()
    p2="\n操作完成，文件以保存在:\n"+Doc+"Image.pdf"
    return p2

