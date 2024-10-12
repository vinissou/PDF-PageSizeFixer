help_text = "Developed at: https://github.com/vinissou/PDF-PageSizeFixer"

no_file = "\n\n \033[31m Input file not provided \033[0m \n"

size_error = "\n\n \033[31m Page size needs to be inserted in portrait mode: width < height\033[0m \n"

standard_error = "\n\n \033[31m Page size standard not recognized \033[0m \n"


def options():
    options_text = """

    Listing all available formats...
    Use the following names to select the paper size:

        ISO A    ISO B    ISO C    ISO D    ISO RA/SRA

          A0      B0       C0       D0         SRA0
          A1      B1       C1                  SRA1
          A2      B2       C2                  SRA2
          A3      B3       C3                  SRA3
          A4      B4       C4                  SRA4
          A5      B5       C5                  RA0
          A6      B6       C6                  RA1
          A7      B7                           RA2
          A8      B8
                  B10

        ANSI      

        LETTER           
        LEGAL
        LEDGER 
        TABLOID 
        EXECUTIVE
        ANSI_C
        ANSI_D
        ANSI_E

    You can choose your own custom size with the command: -c width height
 
     
    """
    print(options_text)
    exit()
