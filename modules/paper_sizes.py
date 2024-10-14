#  I intend to make a more complete list of builtin options in the 
#  future, but I found some conflicting info from different sources, 
#  so more research will be needed. 
#  Besides, some categories, like newspapers, have varying sizes
#  across the world, so for now I included a custom size option.
#  The most complete list of sizes in PostScript points is here:
#  https://papersizes.io/
#
#  OBS: PDFinfo tool from Poppler seems to detect a few wrong paper size 
#  they are listed in the PSOutputDev.cc file

from modules import messages

ISO = {
    "A0": {"x": 2384, "y": 3370},
    "A1": {"x": 1684, "y": 2384},
    "A2": {"x": 1190, "y": 1684},
    "A3": {"x": 842, "y": 1190},
    "A4": {"x": 595, "y": 842},
    "A5": {"x": 420, "y": 595},
    "A6": {"x": 298, "y": 420},
    "A7": {"x": 210, "y": 298},
    "A8": {"x": 148, "y": 210},
    "B0": {"x": 2835, "y": 4008},
    "B1": {"x": 2004, "y": 2835},
    "B2": {"x": 1417, "y": 2004},
    "B3": {"x": 1001, "y": 1417},
    "B4": {"x": 709, "y": 1001},
    "B5": {"x": 499, "y": 709},
    "B6": {"x": 354, "y": 499},
    "B7": {"x": 249, "y": 354},
    "B8": {"x": 176, "y": 249},
    "B9": {"x": 125, "y": 176},
    "B10": {"x": 88, "y": 125},
    "C2": {"x": 1837, "y": 578},
    "C3": {"x": 578, "y": 919},
    "C4": {"x": 919, "y": 649},
    "C5": {"x": 649, "y": 459},
    "C6": {"x": 459, "y": 323},
}

ANSI = {
    "LETTER": {"x": 612, "y": 792},
    "LEGAL": {"x": 612, "y": 1008},
    "LEDGER ": {"x": 792, "y": 1224},
    "TABLOID": {"x": 1224, "y": 792},
    "EXECUTIVE": {"x": 522, "y": 756},
    "ANSI_C": {"x": 1584, "y": 1224},
    "ANSI_D": {"x": 2448, "y": 1584},
    "ANSI_E": {"x": 3168, "y": 2448},
}


def paper_size(standard):
    if ISO.get(standard) is not None:
        return ISO.get(standard)
    elif ANSI.get(standard) is not None:
        return ANSI.get(standard)
    else:
        raise NameError(messages.standard_error)
