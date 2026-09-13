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