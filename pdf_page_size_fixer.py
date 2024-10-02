import argparse
import fitz
from modules.messages import help_text
from modules import page_sizes


parser = argparse.ArgumentParser(
    prog="PDF-PageSizeFixer",
    description="Adjusts a PDF's print paper size",
    epilog=help_text,
)
parser.add_argument("--file", "-f", type=str, required=True, help="input file")
args = parser.parse_args()

src = fitz.Document(args.file)
doc = fitz.Document()

print(args)

print("\n FILE:", args.file)

for page in src:
    imglist = src.get_page_images(page.number)[0]
    rotation = page.rotation
    page.set_rotation(0)

    # TODO: add all formats and remove from here
    page_y = page_sizes.ISO_A["A4"]["y"]
    page_x = page_sizes.ISO_A["A4"]["x"]
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

    new_page.show_pdf_page(new_page.rect, src, page.number)

    # restore original rotation value of the page
    # it needs to be after show_pdf_page
    if rotation != 0:
        new_page.set_rotation(rotation)

src.close()
doc.save("OUTPUT.pdf")  # add size to the file's name
print("\n\tPDF CONVERTED\n")
