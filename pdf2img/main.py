import fitz

doc = fitz.open("xxx")

page = doc.load_page(0)

pix = page.get_pixmap(dpi=300)
pix.save("xxx")
