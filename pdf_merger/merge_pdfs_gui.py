import tkinter as tk
from tkinter import filedialog, messagebox
from PyPDF2 import PdfMerger
from pathlib import Path

def merge_pdfs(pdf_paths, output_path):
    merger = PdfMerger()
    for path in pdf_paths:
        merger.append(path)
    merger.write(output_path)
    merger.close()

def main():
    root = tk.Tk()
    root.withdraw()  # Hide the main Tkinter window

    pdf_paths = filedialog.askopenfilenames(
        title="Select PDF files to merge",
        filetypes=[("PDF files", "*.pdf")],
    )

    if not pdf_paths:
        messagebox.showinfo("No selection", "No PDF files were selected.")
        return

    first_file = Path(pdf_paths[0])
    output_path = first_file.parent / "merged.pdf"

    try:
        merge_pdfs(pdf_paths, output_path)
        messagebox.showinfo("Success", f"Merged PDF created:\n{output_path}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to merge PDFs:\n{e}")

if __name__ == "__main__":
    main()