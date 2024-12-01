from currency_converter import CurrencyConverter,RateNotFoundError
from tkinter import *
from tkinter import PhotoImage
from tkinter.ttk import Combobox
from PIL import Image, ImageTk

p = CurrencyConverter()

# print(p.currencies)
def convert():
    try:
        amount = float(entry1.get())
        p1 = combo1.get()
        p2 = combo2.get()
        data = p.convert(amount,p1,p2)
        label0.config(text=f'Converted Amount: {data:.2f} {p2}')
    except:
        label0.config(text='Converted Amount: Invalid input')

root = Tk()
root.title("Currency Converter")
root.geometry('400x472')             # width and height

img = Image.open(r"C:\Users\Hp\Downloads\WhatsApp Image 2024-11-29 at 9.42.32 PM.jpeg")

resize_img = img.resize((404,400))
image = ImageTk.PhotoImage(resize_img)
labelll = Label(root,image=image).place(y=70)


currency = Label(root,text = 'Currency',fg = 'white',font=('Times New Roman', 20, 'bold'),bg = "#219ebc").pack(fill='x')
converter = Label(root,text = 'Converter',fg = 'white',font=('Times New Roman', 20, 'bold'),bg = "#219ebc").pack(fill='x')
label0= Label(root,text = 'Converted Amount:',font=('arial',10,'bold'),fg = 'dark green',bg = 'white')
label0.place( x = 100,y=430)

From = Label(root,text = 'From',font=('Helvetica', 11, 'bold')).place(x=38,y = 91)
To = Label(root,text = 'To',font=('Helvetica', 11, 'bold')).place(x=218,y=91)

bt = Button(root,text = 'Convert',bg = '#219ebc',command=convert,fg = 'white',font=('Helvetica', 12, 'bold'),width=20).place(x=100,y=380)

entry1 = Entry(root)
entry1.place(x=145,y=345)

combo1 = Combobox(root,state='readonly')
combo1['value'] = ('SGD', 'CYP', 'JPY', 'SEK', 'INR', 'CZK', 'ISK', 'TRY', 'RUB', 'MXN', 'SKK', 'PHP', 'PLN', 'BGN', 'CNY', 'EEK', 'DKK', 'EUR', 'HRK', 'MTL', 'ILS', 'SIT', 'NOK', 'HKD', 'LVL', 'ROL', 'USD', 'THB', 'GBP', 'HUF', 'RON', 'CAD', 'CHF', 'LTL', 'AUD', 'KRW', 'NZD', 'TRL', 'MYR', 'BRL', 'IDR', 'ZAR')
combo1.current(4)
combo1.place(y=120,x=40)

combo2 = Combobox(root,state='readonly')
combo2['value'] = ('SGD', 'CYP', 'JPY', 'SEK', 'INR', 'CZK', 'ISK', 'TRY', 'RUB', 'MXN', 'SKK', 'PHP', 'PLN', 'BGN', 'CNY', 'EEK', 'DKK', 'EUR', 'HRK', 'MTL', 'ILS', 'SIT', 'NOK', 'HKD', 'LVL', 'ROL', 'USD', 'THB', 'GBP', 'HUF', 'RON', 'CAD', 'CHF', 'LTL', 'AUD', 'KRW', 'NZD', 'TRL', 'MYR', 'BRL', 'IDR', 'ZAR')
combo2.current(26)
combo2.place(x=220,y=120)



root.mainloop()
