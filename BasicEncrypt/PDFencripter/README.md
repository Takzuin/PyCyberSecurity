PDF Encryption Tool

This repository contains a Python script for encrypting PDF files with a password using the PyPDF2 library.
Features

    Encrypt a PDF file with a password
    Use 128-bit encryption for secure protection

Requirements

    Python 3.x
    PyPDF2 library

Installation

    Clone this repository:

sh

git clone https://github.com/yourusername/pdf-encryption-tool.git
cd pdf-encryption-tool

    Install the required library:

sh

pip install PyPDF2

Usage

    Update the script with the path to your original PDF file, the desired path for the encrypted PDF file, and the password you want to use.

    Run the script:
    PDFsecure.py
""""
import PyPDF2

def encrypt_pdf(input_pdf_path, output_pdf_path, password):
    # Open the original PDF file
    with open(input_pdf_path, 'rb') as input_file:
        pdf_reader = PyPDF2.PdfReader(input_file)
        pdf_writer = PyPDF2.PdfWriter()

        # Copy all the pages from the original PDF to the encrypted PDF
        for page_num in range(len(pdf_reader.pages)):
            pdf_writer.add_page(pdf_reader.pages[page_num])

        # Set the password for the encrypted PDF
        pdf_writer.encrypt(user_password=password, owner_password=None, use_128bit=True)

        # Save the new encrypted PDF file
        with open(output_pdf_path, 'wb') as output_file:
            pdf_writer.write(output_file)

    print(f'PDF successfully encrypted and saved to {output_pdf_path}')

# Path to the original and encrypted PDF files
input_pdf_path = 'path/to/original/file.pdf'
output_pdf_path = 'path/to/encrypted/file.pdf'
password = 'your_password'

# Call the function to encrypt the PDF
encrypt_pdf(input_pdf_path, output_pdf_path, password)

    Replace 'path/to/original/file.pdf', 'path/to/encrypted/file.pdf', and 'your_password' with the appropriate paths and the desired password.
"""""


Example

Here is an example of how to use the script:

python
"""""
import PyPDF2

def encrypt_pdf(input_pdf_path, output_pdf_path, password):
    with open(input_pdf_path, 'rb') as input_file:
        pdf_reader = PyPDF2.PdfReader(input_file)
        pdf_writer = PyPDF2.PdfWriter()

        for page_num in range(len(pdf_reader.pages)):
            pdf_writer.add_page(pdf_reader.pages[page_num])

        pdf_writer.encrypt(user_password=password, owner_password=None, use_128bit=True)

        with open(output_pdf_path, 'wb') as output_file:
            pdf_writer.write(output_file)

    print(f'PDF successfully encrypted and saved to {output_pdf_path}')

input_pdf_path = 'example_files/original.pdf'
output_pdf_path = 'example_files/encrypted.pdf'
password = 'my_secure_password'

encrypt_pdf(input_pdf_path, output_pdf_path, password)
"""""

This will encrypt the original.pdf file and save the encrypted version as encrypted.pdf with the password my_secure_password.
License

This project is licensed under the MIT License - see the LICENSE file for details.
Contributing

If you have suggestions for improving the script, feel free to open an issue or submit a pull request.
Acknowledgements

    Thanks to the developers of the PyPDF2 library for providing the tools to manipulate PDF files.
