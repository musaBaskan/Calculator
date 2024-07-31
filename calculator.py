

from tkinter import *

def yaz(x):
    s = len(giris.get())
    giris.insert(s, str(x))

hesap = None  # İlk değer olarak None
s1 = 0

def islemler(x):
    global hesap
    global s1
    if hesap is not None:
        hesapla()
    s1 = float(giris.get())
    hesap = x
    giris.delete(0, 'end')

def sifirla():
    global s1, s2, hesap
    s1 = 0
    s2 = 0
    hesap = None
    giris.delete(0, 'end')

def hesapla():
    global s1, s2, hesap
    s2 = float(giris.get())
    sonuc = 0
    if hesap == 0:
        sonuc = s1 + s2
    elif hesap == 1:
        sonuc = s1 - s2
    elif hesap == 2:
        sonuc = s1 * s2
    elif hesap == 3:
        sonuc = s1 / s2
    giris.delete(0, 'end')
    giris.insert(0, str(sonuc))
    s1 = sonuc  # Sonuç yeni s1 olur;
    hesap = None  # Hesap sıfırlanır

pencere = Tk()
pencere.title("Hesap Makinesi")
pencere.attributes('-fullscreen', True)
pencere.bind("<Escape>", lambda e: pencere.attributes("-fullscreen", False))
pencere.configure(bg="black")

giris = Entry(pencere, font="Verdana 20 bold", width=10, justify=RIGHT, bd=11, insertwidth=2, bg="black", fg="White")
giris.grid(row=0, column=0, columnspan=3)

b = []

for i in range(1, 10):
    b.append(Button(pencere, text=str(i), font="Verdana 14 bold", command=lambda x=i: yaz(x), height=2, width=5, bd=5, bg="black",fg="white"))

sayac = 0

for i in range(1, 4):
    for j in range(3):
        b[sayac].grid(row=i, column=j)
        sayac += 1

islem = []

for i in range(4):
    islem.append(Button(pencere, font="Verdana 14 bold", width=5, height=2, bd=5, bg="orange", command=lambda x=i: islemler(x)))

islem[0]['text'] = "+"
islem[1]['text'] = "-"
islem[2]['text'] = "*"
islem[3]['text'] = "/"

for i in range(4):
    islem[i].grid(row=i+1, column=3)

sb = Button(pencere, text="0", font="Verdana 14 bold", command=lambda x=0: yaz(x), height=2, width=5, bd=5, bg="black",fg="white")
sb.grid(row=4, column=0)

nb = Button(pencere, text=".", font="Verdana 14 bold", width=5, height=2, bd=5, bg="black", fg="white", command=lambda x=".": yaz(x))
nb.grid(row=4, column=1)

eb = Button(pencere, text="=", fg="WHITE", font="Verdana 14 bold", command=hesapla, height=2, width=5, bd=5, bg="#00BFFF")
eb.grid(row=4, column=2)

reset_button = Button(pencere, text="C", fg="WHITE", font="Verdana 14 bold", command=sifirla, height=2, width=5, bd=5, bg="red")
reset_button.grid(row=0, column=3)

pencere.mainloop()

