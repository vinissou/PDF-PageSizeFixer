[![ruff](https://github.com/vinissou/PdfPageSizeFixer/actions/workflows/ruff.yml/badge.svg)](https://github.com/vinissou/PdfPageSizeFixer/actions/workflows/ruff.yml)

# PDF-PaperSizeFixer

A quick solution to change PDF files page size, because Ghostscript and every single option I ever tested always messes with the orientation, sometimes in a destructive way. 
This just adjusts the MediaBox value of the file without re-encoding the images to avoid any quality loss. And it also keeps the OCR intact.


## Future Features

- Add an option to resize the images in order to keep a fixed DPI value.
- Auto select the closest paper size from a standard
- Add outdated paper sizes


## Limitations
For now, it can only save PDFs in the 1.7 version, it doesn't seem to have a way to change this in PyMuPDF:
https://github.com/pymupdf/PyMuPDF/discussions/3348

And they do not support PDF/A either:
https://github.com/pymupdf/PyMuPDF/discussions/2169

I used to run MuPDF with the "mutool clean" command after running this command to ensure the PDF/A conformity would not get lost. Mutool can't convert PDFs to PDF/A, but the clean command usually helps to keep a file already formatted as PDF/A as such.
