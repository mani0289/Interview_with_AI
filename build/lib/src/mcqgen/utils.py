from PyPDF2 import PdfReader
import io

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
        
    else:
        raise Exception("Unsupported file format. Please upload a .pdf or .txt file.")