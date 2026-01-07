from PyPDF2 import PdfReader
import io
import docx

def get_pdf_text(file):
    file.seek(0)
    if file.name.endswith('.pdf'):
        try:
            reader = PdfReader(file)
            text = ""
            for page in reader.pages:
                text += page.extract_text()
            return text
        except Exception as e:
            raise Exception(f"Error reading PDF file: {str(e)}")
    elif file.name.endswith('.txt'):
        try:
            return file.getvalue().decode('utf-8')
        except Exception as e:
            raise Exception(f"Error reading text file: {str(e)}")

    elif file.name.endswith('.docx'):
        try:
            doc=docx.Document(file)
            full_text=[]
            for para in doc.paragraphs:
                full_text.append(para.text)
            return '\n'.join(full_text)
        except Exception as e:
            raise Exception(f"Error reading DOCX file: {str(e)}")

    else:
        raise Exception("Unsupported file format. Please upload a .pdf or .txt file.")