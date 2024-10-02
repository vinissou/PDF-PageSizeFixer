import argparse
import fitz
from modules import page_sizes

parser = argparse.ArgumentParser()
parser.add_argument("--file", "-f", type=str, required=True)
args = parser.parse_args()


src = fitz.Document(args.file)
doc = fitz.Document()

print("\n FILE:", args.file)

for page in src:
    imglist = src.get_page_images(page.number)[0]
    rotation = page.rotation
    page.set_rotation(0)

    # TODO: add all formats and remove from here
    page_y = iso["A4"]["y"]
    page_x = iso["A4"]["x"]
    pageH = imglist[2]
    pageW = imglist[3]
    mediaH = page.mediabox[2]
    mediaW = page.mediabox[3]
    mediaMIN = min(page.mediabox[2], page.mediabox[3])
    mediaMAX = max(page.mediabox[2], page.mediabox[3])

    # Checks if it is landscape, portrait ignoring the rotation value
    # as it was the only way found to maintain the original rotation
    print("\nPage:", page.number + 1, "\tRotation:", rotation, end="\t")
    if pageH < pageW and mediaW == mediaMAX:
        new_page = doc.new_page(width=page_x, height=page_y)
        print(">> Portrait")
    elif pageH > pageW and mediaH == mediaMAX:
        new_page = doc.new_page(width=page_y, height=page_x)
        print(">> Landscape")
    elif pageH == pageW:
        new_page = doc.new_page(width=page_y, height=page_x)
        print(">> Perfect square > converting to landscape")
    else:
        new_page = doc.new_page(width=mediaW, height=mediaH)
        print(">> PAGE SIZE NOT RECOGNIZED > keeping the original")

    new_page.show_pdf_page(page.rect, src, page.number)

    # restore original rotation value of the page
    # it needs to be after page.show_pdf_page
    if rotation != 0:
        page.set_rotation(rotation)

src.close()
doc.save("output.pdf")
print("\n\tPDF CONVERTED\n")
