# Image to PDF Converter

## Overview

The Image to PDF Converter is a Python-based desktop application that allows users to select multiple image files and convert them into a single PDF file. The application provides a simple graphical user interface (GUI) for selecting image files and saving the resulting PDF.

## Features

- Browse and select multiple image files (JPG, JPEG, PNG, GIF).
- Display selected image files in a list.
- Convert the selected images into a single PDF file.
- Save the resulting PDF file to a specified location.

## Requirements

- Python 3.x
- tkinter
- Pillow (PIL)

## Installation

1. **Install the required Python packages:**
   ```bash
   pip install tkinter Pillow
   ```

##

## Usage

1. **Run the application:**
   ```bash
   python image_to_pdf_converter.py
   ```

2. **Use the application:**
   - Click the "Add Image" button to select image files you want to convert to PDF. You can select multiple files at once.
   - The selected image files will be displayed in the listbox.
   - Click the "Convert to PDF" button to start the conversion process.
   - Choose the location and filename for the resulting PDF when prompted.

## Script Explanation

### Importing Libraries
```python
import os
from tkinter import Tk, Button, Label, Listbox, Scrollbar, filedialog, messagebox
from PIL import Image
```
- **os**: For interacting with the operating system.
- **tkinter**: For creating the GUI components.
- **Pillow (PIL)**: For handling image operations and saving them as PDF.

### ImageToPDFConverterApp Class
```python
class ImageToPDFConverterApp:
    def __init__(self, master):
        self.master = master
        master.title("Image to PDF Converter")
```
- Initializes the main application window and sets the title.

### Adding GUI Components
```python
        self.label = Label(master, text="Select image files to convert:")
        self.label.pack()

        self.listbox = Listbox(master, selectmode="multiple", width=50)
        self.listbox.pack(side="left", fill="both", expand=True)

        self.scrollbar = Scrollbar(master, orient="vertical")
        self.scrollbar.config(command=self.listbox.yview)
        self.scrollbar.pack(side="right", fill="y")

        self.listbox.config(yscrollcommand=self.scrollbar.set)
```
- Adds a label, listbox, and scrollbar to the main window for displaying selected image files.

### Adding Buttons
```python
        self.add_button = Button(master, text="Add Image", command=self.add_image)
        self.add_button.pack()
        
        self.convert_button = Button(master, text="Convert to PDF", command=self.convert_to_pdf)
        self.convert_button.pack()

        self.filepaths = []
```
- Adds "Add Image" and "Convert to PDF" buttons to the main window and initializes a list to store file paths of selected images.

### Adding Images Function
```python
    def add_image(self):
        filepaths = filedialog.askopenfilenames(title="Select Image Files", filetypes=[("Image Files", "*.jpg *.jpeg *.png *.gif")])
        if filepaths:
            for filepath in filepaths:
                self.listbox.insert("end", os.path.basename(filepath))
                self.filepaths.append(filepath)
```
- Opens a file dialog to select image files and adds them to the listbox and `filepaths` list.

### Converting Images to PDF Function
```python
    def convert_to_pdf(self):
        if not self.filepaths:
            messagebox.showerror("Error", "Please select image files.")
            return

        pdf_filepath = filedialog.asksaveasfilename(title="Save PDF As", defaultextension=".pdf", filetypes=[("PDF Files", "*.pdf")])
        if pdf_filepath:
            images = []
            for filepath in self.filepaths:
                image = Image.open(filepath)
                images.append(image)

            try:
                images[0].save(pdf_filepath, save_all=True, append_images=images[1:])
                messagebox.showinfo("Conversion Complete", "Images converted to PDF successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {str(e)}")

            self.filepaths = []
            self.listbox.delete(0, "end")
```
- Converts the selected images to a single PDF file and saves it to the specified location.

### Running the Application
```python
if __name__ == "__main__":
    root = Tk()
    app = ImageToPDFConverterApp(root)
    root.mainloop()
```
- Initializes and runs the main application loop.

## License

This project is licensed under the MIT License.
