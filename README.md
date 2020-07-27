# Code Description

This notebook (1) preprocesses PDFs for OCR (i.e., deskew, auto-rotate, de-background, oversample DPI), (2) OCRs the PDFs using ocrmypdf/tesseract 4.0, and (3) outputs a newly preprocessed PDF/A with tesseract OCR (`filename.processed.pdf`), the pre-existing OCR in a text file if it exists (`filename.original.txt`), and the tesseract-generated OCR in a text file (`filename.ocr.txt`). The script leaves the original PDFs unchanged.     

NOTA BENE: 
 - Instructions: Place `OCR_PDFs.ipynb` script in same directory with PDFs to be OCRed, and then run as a jupyter notebook. 
 - Script will process all PDFs in the same directory, but will *not* recursively process PDFs in subfolders. 
 - Script uses terminal commands via the jupyter magic (i.e., "!" command) alongside python 3 so <b>this code will not work outside of a jupyter notebook</b>. 
 - Script ignores PDFs named `[filename].processed.pdf`. If keep_processed_PDFs = False, it will overwrite all PDFs ending in `processed.pdf`. 
 - Explicitly setting thread limit to 1 appears to yield the best results in trials, but these improvement gains are minimal.
