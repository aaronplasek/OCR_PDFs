## description
This jupyter notebook script does the following:
1. preprocesses PDFs for OCR (i.e., deskew, auto-rotate, de-background, clean using *ocrmypdf* and *unpaper*), 
2. OCRs the PDFs (using ocrmypdf/tesseract 4.1), 
3. outputs the following files for every PDF in the directory except PDFs with extension `.processed.pdf`.
   - OCRed PDF/A with processing applyed (`filename.processed.pdf`)
   - text file with the pre-existing OCR of the original PDF if it exists (`filename.original.txt`)
   - the tesseract-generated OCR in a text file (`filename.ocr.txt`) for every PDF in the directory. 
4. The script leaves the original PDFs unchanged.     

## usage 
1. Paste `OCR_PDFs.ipynb` script in same directory with PDFs to be OCRed.
2. Run script by typing `jupyter notebook OCR_PDFs.ipynb` in terminal. (You will need jupyter, ocrmypdf, and tesseract installed.)  
3. Run all code blocks in notebook. 

## nota bene 
 - Script will process all PDFs in the same directory, but will *not* recursively process PDFs in subfolders. 
 - Script uses shell commands (via the jupyter "!" command) alongside python 3 so <b>this code will not work outside of a jupyter notebook</b>. 
 - Script ignores PDFs named `[filename].processed.pdf`. If keep_processed_PDFs = False, it will overwrite all PDFs ending in `processed.pdf`. 
