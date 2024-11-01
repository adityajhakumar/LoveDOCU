import streamlit as st
from PyPDF2 import PdfReader, PdfWriter
import fitz  # PyMuPDF
import os
import openpyxl
from io import BytesIO
from PIL import Image
from reportlab.pdfgen import canvas

# Utility function to clean up files
def clean_up(files):
    for file in files:
        try:
            os.remove(file)
        except Exception as e:
            st.warning(f"Could not delete file {file}: {e}")

# Custom CSS for styling
st.markdown("""
    <style>
        body {
            background-color: #f7f7f7;
        }
        .title {
            text-align: center;
            color: #333;
            font-size: 36px;
            font-weight: bold;
            margin-bottom: 20px;
        }
        .sidebar .sidebar-content {
            background-color: #ffffff;
            padding: 10px;
        }
        .service-button {
            background-color: #007bff;
            color: white;
            padding: 15px;
            border-radius: 5px;
            text-align: center;
            display: inline-block;
            margin: 5px;
            transition: background-color 0.3s;
        }
        .service-button:hover {
            background-color: #0056b3;
        }
        .download-button {
            background-color: #28a745;
            color: white;
            padding: 10px;
            border-radius: 5px;
            margin-top: 10px;
            transition: background-color 0.3s;
        }
        .download-button:hover {
            background-color: #218838;
        }
    </style>
""", unsafe_allow_html=True)

# Function to merge PDFs
def merge_pdfs(uploaded_files):
    if not uploaded_files:
        st.error("Please upload at least one PDF file to merge.")
        return
    output = PdfWriter()
    try:
        for pdf_file in uploaded_files:
            pdf_reader = PdfReader(pdf_file)
            for page in pdf_reader.pages:
                output.add_page(page)
        output_file = "merged.pdf"
        with open(output_file, "wb") as f:
            output.write(f)
        st.success("PDFs merged successfully!")
        with open(output_file, "rb") as f:
            st.download_button("Download Merged PDF", f, "merged.pdf", key="download_merged", css_class='download-button')
        clean_up([output_file])
    except Exception as e:
        st.error(f"An error occurred while merging PDFs: {e}")

# Function to split a PDF
def split_pdf(pdf_file):
    if pdf_file is None:
        st.error("Please upload a PDF file to split.")
        return

    try:
        pdf_reader = PdfReader(pdf_file)
        total_pages = len(pdf_reader.pages)

        # Display PDF page thumbnails
        st.subheader("PDF Pages:")
        thumbnails = []
        for i in range(total_pages):
            img = fitz.open(pdf_file.name)[i]  # Open PDF and get page image
            img.save(f"page_{i + 1}.png")  # Save thumbnail as PNG
            thumbnails.append(f"page_{i + 1}.png")
        
        # Display thumbnails for page selection
        selected_pages = st.multiselect(
            "Select pages to split:", 
            options=[f"Page {i + 1}" for i in range(total_pages)],
            format_func=lambda x: x
        )

        if st.button("Split Selected Pages"):
            if not selected_pages:
                st.error("Please select at least one page to split.")
                return
            
            output = PdfWriter()
            for page in selected_pages:
                page_index = int(page.split()[1]) - 1  # Convert "Page X" to index
                output.add_page(pdf_reader.pages[page_index])
                
            output_file = "split.pdf"
            with open(output_file, "wb") as f:
                output.write(f)
            st.success("PDF split successfully!")
            with open(output_file, "rb") as f:
                st.download_button("Download Split PDF", f, "split.pdf", key="download_split", css_class='download-button')
            clean_up([output_file])
            clean_up(thumbnails)  # Remove thumbnails

    except Exception as e:
        st.error(f"An error occurred while splitting the PDF: {e}")

# Function to compress a PDF
def compress_pdf(pdf_file):
    if pdf_file is None:
        st.error("Please upload a PDF file to compress.")
        return
    
    try:
        output_file = "compressed.pdf"
        with fitz.open(pdf_file) as pdf:
            pdf.save(output_file, garbage=3)  # Optimize and compress PDF
        st.success("PDF compressed successfully!")
        with open(output_file, "rb") as f:
            st.download_button("Download Compressed PDF", f, "compressed.pdf", key="download_compressed", css_class='download-button')
        clean_up([output_file])
    except Exception as e:
        st.error(f"An error occurred while compressing the PDF: {e}")

# Function to convert PDF to Word
def pdf_to_word(pdf_file):
    if pdf_file is None:
        st.error("Please upload a PDF file to convert.")
        return

    try:
        output_file = "converted.docx"
        cv = Converter(pdf_file)
        cv.convert(output_file)
        cv.close()
        st.success("PDF converted to Word successfully!")
        with open(output_file, "rb") as f:
            st.download_button("Download Word Document", f, "converted.docx", key="download_word", css_class='download-button')
        clean_up([output_file])
    except Exception as e:
        st.error(f"An error occurred while converting PDF to Word: {e}")

# Function to convert PDF to Excel
def pdf_to_excel(pdf_file):
    if pdf_file is None:
        st.error("Please upload a PDF file to convert.")
        return

    try:
        wb = openpyxl.Workbook()
        ws = wb.active
        pdf_reader = PdfReader(pdf_file)
        
        for i, page in enumerate(pdf_reader.pages):
            text = page.extract_text() or ""
            ws.append([text])  # Each page's text is put in a new row

        output_file = "converted.xlsx"
        wb.save(output_file)
        st.success("PDF converted to Excel successfully!")
        with open(output_file, "rb") as f:
            st.download_button("Download Excel Document", f, "converted.xlsx", key="download_excel", css_class='download-button')
        clean_up([output_file])
    except Exception as e:
        st.error(f"An error occurred while converting PDF to Excel: {e}")

# Function to convert PDF to JPG
def pdf_to_jpg(pdf_file):
    if pdf_file is None:
        st.error("Please upload a PDF file to convert.")
        return

    try:
        images = fitz.open(pdf_file)
        img_paths = []
        for i in range(len(images)):
            img_path = f"page_{i + 1}.jpg"
            images[i].save(img_path)  # Save each page as JPG
            img_paths.append(img_path)

        st.success("PDF converted to JPG successfully!")
        for img_path in img_paths:
            with open(img_path, "rb") as f:
                st.download_button(f"Download {img_path}", f, img_path, key=f"download_{img_path}", css_class='download-button')
        clean_up(img_paths)
    except Exception as e:
        st.error(f"An error occurred while converting PDF to JPG: {e}")

# Function to add watermark
def add_watermark(pdf_file, watermark_text):
    if pdf_file is None:
        st.error("Please upload a PDF file to add a watermark.")
        return
    if not watermark_text:
        st.error("Please enter watermark text.")
        return

    try:
        output_file = "watermarked.pdf"
        pdf_reader = PdfReader(pdf_file)
        output = PdfWriter()

        for page in pdf_reader.pages:
            output.add_page(page)
        
        # Create watermark as a new PDF
        watermark_pdf = "watermark.pdf"
        c = canvas.Canvas(watermark_pdf)
        c.setFont("Helvetica", 36)
        c.drawString(100, 500, watermark_text)  # Adjust the position as needed
        c.save()

        # Apply watermark
        with open(watermark_pdf, "rb") as wm_file:
            wm_reader = PdfReader(wm_file)
            for i in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[i]
                page.merge_page(wm_reader.pages[0])  # Merge watermark with the original page
                output.add_page(page)
        
        with open(output_file, "wb") as f:
            output.write(f)
        st.success("Watermark added successfully!")
        with open(output_file, "rb") as f:
            st.download_button("Download Watermarked PDF", f, "watermarked.pdf", key="download_watermark", css_class='download-button')
        clean_up([output_file, watermark_pdf])
    except Exception as e:
        st.error(f"An error occurred while adding the watermark: {e}")

# Main Streamlit App
st.title("LoveDocu - PDF Services")

# Add your logo to the top left corner
logo_path = r"C:\Users\adity\Desktop\logo.jpg"
if os.path.exists(logo_path):
    try:
        st.image(logo_path, width=300)  # Adjust the width as desired
    except Exception as e:
        st.error(f"Error loading logo: {e}")
else:
    st.error(f"Logo file does not exist at {logo_path}")

# Sidebar for file upload
st.sidebar.title("Upload PDF Files")
uploaded_files = st.sidebar.file_uploader("Choose PDF files", accept_multiple_files=True, type=["pdf"])

# Select a service
st.sidebar.title("Choose a Service")
service = st.sidebar.radio("Select a service", [
    "Merge PDFs",
    "Split PDF",
    "Compress PDF",
    "Convert PDF to Word",
    "Convert PDF to Excel",
    "Convert PDF to JPG",
    "Add Watermark"
])

# Handle service selection
if service == "Merge PDFs":
    if st.sidebar.button("Merge PDFs"):
        merge_pdfs(uploaded_files)
elif service == "Split PDF":
    pdf_file = st.sidebar.file_uploader("Choose a PDF file to split", type=["pdf"], key="split_pdf_uploader")
    split_pdf(pdf_file)
elif service == "Compress PDF":
    pdf_file = st.sidebar.file_uploader("Choose a PDF file to compress", type=["pdf"], key="compress_pdf_uploader")
    compress_pdf(pdf_file)
elif service == "Convert PDF to Word":
    pdf_file = st.sidebar.file_uploader("Choose a PDF file to convert", type=["pdf"], key="word_pdf_uploader")
    pdf_to_word(pdf_file)
elif service == "Convert PDF to Excel":
    pdf_file = st.sidebar.file_uploader("Choose a PDF file to convert", type=["pdf"], key="excel_pdf_uploader")
    pdf_to_excel(pdf_file)
elif service == "Convert PDF to JPG":
    pdf_file = st.sidebar.file_uploader("Choose a PDF file to convert", type=["pdf"], key="jpg_pdf_uploader")
    pdf_to_jpg(pdf_file)
elif service == "Add Watermark":
    pdf_file = st.sidebar.file_uploader("Choose a PDF file to add watermark", type=["pdf"], key="watermark_pdf_uploader")
    watermark_text = st.sidebar.text_input("Enter watermark text")
    if st.sidebar.button("Add Watermark"):
        add_watermark(pdf_file, watermark_text)
