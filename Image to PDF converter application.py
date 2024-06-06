import os
from tkinter import Tk, Button, Label, Listbox, Scrollbar, filedialog, messagebox
from PIL import Image

class ImageToPDFConverterApp:
    def __init__(self, master):
        self.master = master
        master.title("Image to PDF Converter")

        self.label = Label(master, text="Select image files to convert:")
        self.label.pack()

        self.listbox = Listbox(master, selectmode="multiple", width=50)
        self.listbox.pack(side="left", fill="both", expand=True)

        self.scrollbar = Scrollbar(master, orient="vertical")
        self.scrollbar.config(command=self.listbox.yview)
        self.scrollbar.pack(side="right", fill="y")

        self.listbox.config(yscrollcommand=self.scrollbar.set)

        self.add_button = Button(master, text="Add Image", command=self.add_image)
        self.add_button.pack()
        
        self.convert_button = Button(master, text="Convert to PDF", command=self.convert_to_pdf)
        self.convert_button.pack()

        self.filepaths = []

    def add_image(self):
        filepaths = filedialog.askopenfilenames(title="Select Image Files", filetypes=[("Image Files", "*.jpg *.jpeg *.png *.gif")])
        if filepaths:
            for filepath in filepaths:
                self.listbox.insert("end", os.path.basename(filepath))
                self.filepaths.append(filepath)

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

if __name__ == "__main__":
    root = Tk()
    app = ImageToPDFConverterApp(root)
    root.mainloop()
