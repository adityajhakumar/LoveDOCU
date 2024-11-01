![logo](https://github.com/user-attachments/assets/95c379d3-3cfe-4729-abf2-9556258d8e16)


# LoveDocu

Welcome to **LoveDocu** – your all-in-one document solution! LoveDocu provides a suite of PDF and document management tools to streamline your workflow. Our services range from PDF merging and splitting to file conversions, compression, watermarking, and more. With a focus on usability, reliability, and functionality, LoveDocu helps you achieve professional-quality document handling right from your local device.

## Features

- **Merge PDFs**: Combine multiple PDF files into a single document with ease.
- **Split PDF**: Select specific pages to split from a PDF and create a new document.
- **Compress PDF**: Reduce the file size of PDFs while maintaining quality.
- **Convert PDF to Word**: Transform PDF documents into editable Word files.
- **Convert PDF to Excel**: Extract data from PDFs and save it in Excel format.
- **Convert PDF to JPG**: Convert PDF pages to high-quality images.
- **Add Watermark**: Apply text-based watermarks to PDFs for added security and branding.

## Technology Stack

- **Backend**: Python (using `PyMuPDF`, `PyPDF2`, `Pillow`, `ReportLab`, and `OpenPyXL`)
- **Frontend**: Streamlit for interactive user interface
- **Image and PDF Processing**: `PyMuPDF` and `Pillow`
- **File Management**: `io` and `os`

## Installation

To run LoveDocu locally, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/lovedocu.git
   cd lovedocu
   ```

2. **Install dependencies**:
   Make sure you have Python 3.7 or higher installed. Then, install the necessary Python packages:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**:
   Start the Streamlit server to launch LoveDocu:
   ```bash
   streamlit run lovedocu_app.py
   ```

4. **Access the app**:
   Open your web browser and navigate to `http://localhost:8501` to start using LoveDocu.

## Usage

1. **Upload a PDF** file via the interface.
2. **Select a service** from the dropdown menu (e.g., Merge PDFs, Split PDF).
3. **Perform desired actions** by following the prompts and using provided buttons.
4. **Download** your processed files using the download buttons provided after each operation.

## Project Structure

- `lovedocu_app.py`: The main application file containing all services and their implementations.
- `requirements.txt`: Lists the dependencies required to run the app.
- `logo.jpg`: Company logo displayed in the app (ensure your logo is located at `C:/Users/adity/Desktop/LoveDocu/logo.jpg` for correct loading).

## Troubleshooting

- **Logo Not Visible**: Make sure the logo path in the code matches your logo's actual location.
- **PDF Page Issues**: Ensure uploaded PDFs are valid and not corrupted.
- **Dependency Errors**: If `PyMuPDF`, `PyPDF2`, or other libraries cause issues, verify that they’re installed correctly or try reinstalling them.

## License

This project is licensed under the Apache License, Version 2.0. See the [LICENSE](LICENSE) file for more details.

```
                                 Apache License
                           Version 2.0, January 2004
                        http://www.apache.org/licenses/

TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION

1. Definitions.

...

END OF TERMS AND CONDITIONS
```

## Contribution

We welcome contributions to improve and expand LoveDocu. To contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

