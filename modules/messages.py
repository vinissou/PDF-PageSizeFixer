help_text = "Developed at: https://github.com/vinissou/PDF-PageSizeFixer"

no_file = "\n\n \033[31m Input file not provided \033[0m \n"

size_error = "\n\n \033[31m Page size needs to be inserted in portrait mode: width < height\033[0m \n"

standard_error = "\n\n \033[31m Page size standard not recognized \033[0m \n"


def options():
    options_text = """

    Listing all available formats...
    Use the following names to select the paper size:

        ISO A    ISO B    ISO C    ISO RA/SRA    ANSI      
                                                           
          A0      B0       C0         SRA0       LETTER    
          A1      B1       C1         SRA1       LEGAL
          A2      B2       C2         SRA2       LEDGER 
          A3      B3       C3         SRA3       TABLOID 
          A4      B4       C4         SRA4       EXECUTIVE
          A5      B5       C5         RA0        ANSI_C
          A6      B6       C6         RA1        ANSI_D
          A7      B7                  RA2        ANSI_E   
          A8      B8
                  B10


    You can choose your own custom size with the command: -c width height
 
     
    """
    print(options_text)
    exit()
