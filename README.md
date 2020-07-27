# Code Description

This jupyter notebook script does the following:
1. preprocesses PDFs for OCR (i.e., deskew, auto-rotate, de-background, clean using *ocrmypdf* and *unpaper*), 
2. OCRs the PDFs (using ocrmypdf/tesseract 4.1), 
3. outputs an OCRed PDF/A with processing applyed (`filename.processed.pdf`), a text file with the pre-existing OCR of the original PDF if it exists (`filename.original.txt`), and the tesseract-generated OCR in a text file (`filename.ocr.txt`) for every PDF in the directory. The script leaves the original PDFs unchanged.     

INSTRUCTIONS 
 - Paste `OCR_PDFs.ipynb` script in same directory with PDFs to be OCRed.
 - Run script by typing `jupyter notebook OCR_PDFs.ipynb` in terminal. (You will need jupyter, ocrmypdf, tesseract 4.1, etc. installed.)  
 - Run all cells in notebook in order. No changes to notebook are necessary. 

NOTA BENE: 
 - Script will process all PDFs in the same directory, but will *not* recursively process PDFs in subfolders. 
 - Script uses terminal commands via the jupyter magic (i.e., "!" command) alongside python 3 so <b>this code will not work outside of a jupyter notebook</b>. 
 - Script ignores PDFs named `[filename].processed.pdf`. If keep_processed_PDFs = False, it will overwrite all PDFs ending in `processed.pdf`. 
