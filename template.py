import os
from pathlib import Path

list_of_files=[
    "QAWithPDF/__init__.py",
    "QAWithPDF/Data_Ingestion.py",
    "QAWithPDF/Embedding.py",
    "QAWithPDF/Model_Api.py",
    "StreamlitApp.py",
    "logger.py",
    "exception.py",
    'Notebook/notebook.ipynb'
    # "setup.py"
        ]


for filepath in list_of_files:
   filepath = Path(filepath)
   filedir, filename = os.path.split(filepath)

   if filedir !="":
      os.makedirs(filedir, exist_ok=True)

   if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
      with open(filepath, 'w') as f:
         pass

