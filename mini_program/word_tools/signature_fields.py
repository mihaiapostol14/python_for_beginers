from docx import Document
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT

doc = Document()

for i in range(1,20):
    signature_paragraph = doc.add_paragraph()
    signature_paragraph.add_run('Signature:').bold = True
    signature_paragraph.add_run('____________________________').bold = True

    signature_paragraph.alignment = WD_PARAGRAPH_ALIGNMENT.RIGHT

    signature_paragraph = doc.add_paragraph()
    signature_paragraph.add_run('Signature:').bold = True
    signature_paragraph.add_run('____________________________').bold = True


doc.save('Document_with_Signature.docx')

