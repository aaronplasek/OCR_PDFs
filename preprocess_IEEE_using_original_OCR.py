# 
# Description: Pulls all plain txt from PDFs placed in folders titled by year of publication, and renames plain txt file 
#              as 'XXXX-[PDF name].txt' in the target_folder specified in the script. This script will run fine in a terminal. 
# 
# Instructions: Place this script in top-level folder that contains folders named XXXX, where XXXX = year of publication
#
# Note: Script is recursive in that it will pull ALL PDFs in all sub-folders for each year
#

# libraries
import os, ocrmypdf, time, glob

# stationkeeping
homedir = os.getcwd()  # top-level directory, with subfolder names as publication year
years = glob.glob(homedir+'/*/') # publication year folders
target_folder = '/media/a/data/S4-July2021/raw'
os.mkdir(target_folder) # txt file directory

for year in years:
    pub_year=(year[-5:-1])  # get year of articles as a str
    pdfs_in_year = glob.glob(year + '/*/**/*.pdf', recursive=True)  # pdfs for year, including pdfs in subdirectories

    print(str(len(pdfs_in_year)) + ' articles for ' + pub_year)
    for article in pdfs_in_year:
        pdf_path, pdf_name = os.path.split(article)
        txt_in_pdf = '\''+target_folder+'/'+pub_year+'-'+pdf_name[:-4]+'.txt'+'\''
        #print('\''+article+'\'')
        #print(txt_in_pdf)
        os.system(("pdftotext %s %s") % ('\''+article+'\'', txt_in_pdf))




