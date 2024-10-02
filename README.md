[![ruff](https://github.com/vinissou/PdfPageSizeFixer/actions/workflows/ruff.yml/badge.svg)](https://github.com/vinissou/PdfPageSizeFixer/actions/workflows/ruff.yml)

# PdfPageSizeFixer


A quick and dirty solution for change PDFs print size without re-encoding the images, because Ghostscript and every single option I tested at the time just messed with the orientation. I intend to expand it and add executables soon.


It can only save PDFs in the 1.7 version, it doesn't seem to have a way to change this in PyMuPDF:
https://github.com/pymupdf/PyMuPDF/discussions/3348

And they do not support PDF/A either:
https://github.com/pymupdf/PyMuPDF/discussions/2169

I used to run MuPDF with the "mutool clean" command after running this command to ensure the PDF/A conformity would not get lost. Mutool can't convert PDFs to PDF/A, but the clean command usually helps to keep a file already formatted as PDF/A safe.
