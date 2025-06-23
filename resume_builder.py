# resume_builder.py

from weasyprint import HTML, CSS
from jinja2 import Template
import os
from datetime import datetime

# HTML shablonni yuklaydi
def load_template(language="uz", alphabet="lat"):
    path = f"templates/template_{alphabet}.html"
    with open(path, "r", encoding="utf-8") as f:
        return Template(f.read())

# PDF rezyume yaratadi
def generate_resume_pdf(user_data: dict, output_path: str):
    template = load_template(language=user_data.get("lang", "uz"),
                             alphabet=user_data.get("alphabet", "lat"))

    rendered_html = template.render(**user_data)

    css = CSS(string='''
        @page { size: A4; margin: 2cm; }
        body { font-family: "Times New Roman", serif; }
    ''')

    HTML(string=rendered_html).write_pdf(output_path, stylesheets=[css])
    return output_path
