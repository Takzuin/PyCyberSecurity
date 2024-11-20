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
