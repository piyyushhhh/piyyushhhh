import pyqrcode
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk

root = Tk()
root.title("QR CODE GENERATOR")
root.geometry('400x500')  # width and height

def create():
    input_path = filedialog.asksaveasfilename(filetypes=[('PNG File', ".png"), ('All Files', "*.*")])
    
    # Check if a valid file path was returned
    if input_path:
        if not input_path.endswith(".png"):
            input_path = f'{input_path}.png'

        # Generate QR code
        qr_code = pyqrcode.create(entry.get())
        
        # Save the QR code image
        qr_code.png(input_path, scale=5)
        
        # Open the generated image for displaying
        global get_image
        get_image = ImageTk.PhotoImage(Image.open(input_path))
        
        # Update the label to show the QR code image
        label.config(image=get_image)

        # Update the entry field to indicate that QR code is created
        entry.delete(0, END)
        entry.insert(0, 'Finished!')

def clr():
    # Clear the entry field and reset the label image
    entry.delete(0, END)
    label.config(image='')

# Set background image for the window
img = Image.open(r"C:\Users\Hp\Downloads\WhatsApp Image 2024-12-20 at 8.56.52 PM.jpeg")
resize_img = img.resize((400, 500))
image = ImageTk.PhotoImage(resize_img)
label = Label(root, image=image).place(y=0)

# Entry widget to take URL or text input
entry = Entry(root, font=('Helvetica', 17), bd=5, justify='center')
entry.pack(pady=20)

# Create button to generate the QR code
btn_create = Button(root, text="CREATE QR CODE", font=('Helvetica', 14),  command=create)
btn_create.pack(pady=20)

# Clear button to reset the inputs and image
btn_clear = Button(root, text="CLEAR", font=('Helvetica', 14),command=clr)
btn_clear.pack(pady=20)

# Label to display the QR code image
label = Label(root)
label.pack(pady=10)

# Run the application
root.mainloop()
