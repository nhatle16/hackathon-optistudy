import pdfplumber
from langchain.tools import tool

@tool
def extract_syllabus_text(path: str) -> str:
    """
    Extract all the text and table contents from a syllabus in PDF format.

    Args:
        path (str): a file path of the syllabus

    Returns:
        str: the extracted text from the syllabus
    """
    extracted_content = []

    try:
        with pdfplumber.open(path) as pdf:
            for i, page in enumerate(pdf.pages):
                extracted_content.append(f"\n----- PAGE {i+1} -----\n")

                # Extracting text
                text = page.extract_text()
                if text:
                    extracted_content.append(text)

                # Extracting table
                tables = page.extract_tables()
                if tables:
                    extracted_content.append("\n [Discovered Table Content]")
                    for table in tables:
                        for row in table:
                            # Filter None values and concatenate row content
                            row_text = "  |  ".join([str(cell) if cell is not None else "" for cell in row])
                            extracted_content.append(row_text)

        return "\n".join(extracted_content)
    
    except Exception as e:
        return f"Error reading PDF: {str(e)}"
