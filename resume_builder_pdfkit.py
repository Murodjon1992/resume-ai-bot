import pdfkit
from jinja2 import Environment, FileSystemLoader
import os
from datetime import datetime

# wkhtmltopdf joylashgan to‘liq yo‘l
path_to_wkhtmltopdf = r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe"
config = pdfkit.configuration(wkhtmltopdf=path_to_wkhtmltopdf)

# Jinja2 templatini yuklash
env = Environment(loader=FileSystemLoader("templates"))
template = env.get_template("resume_template.html")

def generate_resume_pdf(user_data: dict, output_file="resume.pdf"):
    html_out = template.render(user_data)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"resume_{timestamp}.pdf"
    filepath = os.path.join("resumes", filename)

    # Agar papka mavjud bo‘lmasa – yaratamiz
    os.makedirs("resumes", exist_ok=True)

    # HTML'dan PDFga konvertatsiya
    pdfkit.from_string(html_out, filepath, configuration=config)
    return filepath
