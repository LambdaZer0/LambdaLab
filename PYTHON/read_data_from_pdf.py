import pdfplumber
from openpyxl import load_workbook
from datetime import datetime
import os 
import re
import shutil
import ast

if os.path.isfile("param.txt"):
    f = open("param.txt", encoding="utf-8")
    if f.mode == "r":
        data = f.read()
        param = ast.literal_eval(data)
else:
    print("Need parameters file!")
    exit()

work_dir = param["working_dir"]

def extract_date(text):
    """Extract date that has the format 'dd/mm/yyyy' from the given text"""
    dt = re.findall(r"[0-9]{2}/[0-9]{2}/[0-9]{4}", text, re.MULTILINE)
    if dt:
        return dt[-1]

def extract_title(text):
    """Extract title from the given text which starts with 'TITRE DU DOCUMENT :'"""
    title = re.findall(r"TITRE DU DOCUMENT :\n+([\s\w'\"#\/\-\(\)\,\;]+)\n(.*:|EPC)", text, flags=re.MULTILINE | re.IGNORECASE)
    title = [x[0] for x in title]
    title = [re.sub(r"\n", " ", x) for x in title]
    if title:
        return title[-1]

def extract_identification(text):
    """Extract indentification which is the last line of the given text"""
    idt = re.findall(r"^(EPC[A-Z0-9\-]+)", text, flags=re.MULTILINE)
    if idt:
        return idt[-1]

   

# Check if path exists
if os.path.isdir(work_dir):
    os.chdir(work_dir)
    if os.path.isfile("template.xlsx"):
        # Create output subdirectories
        ok_dir = "./OK_" + datetime.now().strftime("%d-%m-%Y_%H%M%S")
        ko_dir = "./KO_" + datetime.now().strftime("%d-%m-%Y_%H%M%S")
        os.mkdir(ok_dir)
        os.mkdir(f"{ok_dir}/EXCEL")
        os.mkdir(ko_dir)
        os.mkdir(f"{ko_dir}/KO_ID")
        os.mkdir(f"{ko_dir}/KO_TITLE_or_DATE")
        os.mkdir(f"{ko_dir}/KO_TITLE_or_DATE/EXCEL")
        # Read all PDF files
        for file in os.listdir(work_dir):
            if file.endswith(".pdf"):
                print(file)
                pdf = pdfplumber.open(file)
                for page in pdf.pages:
                    text = page.extract_text()
                    # print (text)
                    extracted_date = extract_date(text)
                    extracted_title = extract_title(text)
                    extracted_id = extract_identification(text)
                    # print(extracted_date)
                    # print(extracted_title)
                    # print(extracted_id)
                    if extracted_id:
                        workbook = load_workbook('template.xlsx')
                        sheet = workbook['Comment sheet']
                        sheet['C9'] = extracted_id
                        sheet['H6'] = extracted_id.split("-")[0]
                        sheet['H7'] = extracted_id
                        sheet['C8'] = extracted_title
                        sheet['C10'] = extracted_date
                        if extracted_date and extracted_title:
                            workbook.save(f"{ok_dir}/EXCEL/{extracted_id}.xlsx")
                            pdf.close()
                            shutil.move(file, ok_dir)
                        else:
                            workbook.save(f"{ko_dir}/KO_TITLE_or_DATE/EXCEL/{extracted_id}.xlsx")
                            pdf.close()
                            shutil.move(file, f"{ko_dir}/KO_TITLE_or_DATE")
                    else:
                        pdf.close()
                        shutil.move(file, f"{ko_dir}/KO_ID")

    else:
        print("template.xlsx is missing!")                  
else:
    print("No working directory is set!")