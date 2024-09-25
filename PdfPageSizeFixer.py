import fitz
import argparse

parser = argparse.ArgumentParser()                                               
parser.add_argument("--file", "-f", type=str, required=True)
args = parser.parse_args()


src = fitz.Document(args.file)
doc = fitz.Document()

print('\n ARQUIVO:\n',args.file)

for ipage in src:
    imglist  = src.get_page_images(ipage)[0]
    rotation = ipage.rotation
    ipage.set_rotation(0)


    A4Maior  = 842.0
    A4Menor  = 595.0
    pageH    = imglist[2] 
    pageW    = imglist[3]
    mediaH   = ipage.mediabox[2]
    mediaW   = ipage.mediabox[3]
    mediaMIN = min(ipage.mediabox[2], ipage.mediabox[3])
    mediaMAX = max(ipage.mediabox[2], ipage.mediabox[3])
    
    
    print('\nPÁGINA:', ipage.number+1, '\t Rotação:', rotation)
    
    # verifica se é paisagem, retrato ou quadrado ignorando a rotação
    # pois foi a única forma encontrada de manter a rotação original
    if  pageH < pageW and mediaW == mediaMAX: 
        page = doc.new_page(width=A4Menor, height=A4Maior)
        print('Retrato')
    elif pageH > pageW and mediaH == mediaMAX:
        page = doc.new_page(width=A4Maior, height=A4Menor)
        print('Paisagem')
    elif pageH == pageW:
        page = doc.new_page(width=A4Maior, height=A4Menor)
        print('Quadrado convertido para paisagem')
    else:  
        page = doc.new_page(width=mediaW, height=mediaH)
        print('Padrão não reconhecido > mantendo dimensões originais')
    

    page.show_pdf_page(page.rect, src, ipage.number)

    #restaura rotação original, 
    #é necessários estar depois do page.show_pdf_page
    if  rotation != 0:
        page.set_rotation(rotation)

src.close()
doc.save('./TMP/'+args.file)
print('\n\tARQUIVO FINALIZADO\n')
