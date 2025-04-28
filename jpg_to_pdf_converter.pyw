from tkinter import Tk, filedialog, Button, Label
from PIL import Image
from PyPDF2 import PdfMerger

class PDFApp:
    def __init__(self, root):
        self.root = root
        self.root.title("JPG to PDF Converter and Merger")
        x = (self.root.winfo_screenwidth() - 300) // 2
        y = (self.root.winfo_screenheight() - 200) // 2
        self.root.geometry(f'300x100+{x}+{y}')
        self.root.resizable(False, False) 

        self.label = Label(root, text="Select JPGs to convert or PDFs to merge:")
        self.label.pack(pady=10)

        self.convert_button = Button(root, text="Convert JPGs", command=self.convert_jpg_to_pdf)
        self.convert_button.pack(side='left', padx=(40, 10))

        self.merge_button = Button(root, text="Merge PDFs", command=self.merge_pdfs)
        self.merge_button.pack(side='right', padx=(10, 40))      

    def convert_jpg_to_pdf(self):
        jpg_files = filedialog.askopenfilenames(filetypes=[("JPG files", "*.jpg")])
        for jpg_file in jpg_files:
            pdf_file = jpg_file.rsplit('.', 1)[0] + '.pdf'
            with Image.open(jpg_file) as img:
                img.convert('RGB').save(pdf_file, 'PDF')
            print(f"Converted {jpg_file} to {pdf_file}")

    def merge_pdfs(self):
        pdf_files = filedialog.askopenfilenames(filetypes=[("PDF files", "*.pdf")])
        if pdf_files:
            output_file = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
            if output_file:
                merger = PdfMerger()
                for pdf in pdf_files:
                    merger.append(pdf)
                merger.write(output_file)
                merger.close()
                print(f"Merged PDFs into {output_file}")

if __name__ == "__main__":
    root = Tk()
    app = PDFApp(root)
    root.mainloop()