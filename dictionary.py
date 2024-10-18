#downloaded the docx2txt to  to read dzongkha from Microsoft Word documents.
import docx2txt as d2t

docx_file = 'dzo.docx'
# converting the dzongkha dictionary into txt.file
txt_file = 'dzo.txt'

docx = d2t.process(docx_file)
#used utf-8 to translated into binary numbers to be stored in the computer:

file=open(txt_file, 'w', encoding='utf-8')
file.write(docx)
file.close()