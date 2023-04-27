import os
import tempfile
import subprocess
import requests
from urllib.parse import urlparse
import streamlit as st
from pdf2image import convert_from_path


def latex_to_pdf(latex_code, output_file):
    with tempfile.TemporaryDirectory() as tmpdir:
        tex_file = os.path.join(tmpdir, "latex_code.tex")
        with open(tex_file, "w") as f:
            f.write(latex_code)

        process = subprocess.Popen(
            ["pdflatex", "-output-directory", tmpdir, tex_file],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        process.communicate()

        pdf_file = os.path.join(tmpdir, "latex_code.pdf")
        if os.path.exists(pdf_file):
            os.rename(pdf_file, output_file)


def pdf_to_images(pdf_file):
    return convert_from_path(pdf_file)


def download_code_from_url(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        st.error(
            f"Error {response.status_code}: Could not download the code from the URL."
        )
        return ""


st.title("Python Code to LaTeX Formatter")

default_url = "https://raw.githubusercontent.com/python/mypy/master/mypy/checker.py"

url_input = st.text_input("Enter the URL of a code repository:", value=default_url)
if url_input:
    if st.button("Download Code"):
        code = download_code_from_url(url_input)

        with open("latex_head.tex", "r") as f:
            latex_head = f.read()

        with open("latex_tail.tex", "r") as f:
            latex_tail = f.read()

        latex_code = latex_head + "\n" + code + "\n" + latex_tail
        st.text_area("Generated LaTeX code:", value=latex_code)

        with tempfile.NamedTemporaryFile(suffix=".pdf", delete=False) as output_pdf:
            latex_to_pdf(latex_code, output_pdf.name)

            output_format = st.selectbox("Select output format:", ["PNG", "PDF"])

            if output_format == "PNG":
                images = pdf_to_images(output_pdf.name)
                for i, image in enumerate(images, start=1):
                    st.image(
                        image, caption=f"Output Image (Page {i})", use_column_width=True
                    )
            elif output_format == "PDF":
                with open(output_pdf.name, "rb") as f:
                    pdf_data = f.read()
                st.download_button(
                    label="Download PDF",
                    data=pdf_data,
                    file_name="output.pdf",
                    mime="application/pdf",
                )

            os.unlink(output_pdf.name)
