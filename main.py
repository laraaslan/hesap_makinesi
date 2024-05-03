from tkinter import *

window = Tk()
window.title("Hesap Makinesi")
window.geometry("300x250")

entry_1 = Entry(window)
entry_1.pack()
entry_2 = Entry(window)
entry_2.pack()


def toplama():
  try:
    sayi_1 = float(entry_1.get())
    sayi_2 = float(entry_2.get())
    sonuc = sayi_1 + sayi_2
    sonuc_label.config(
        text=str(sonuc))  # Sonucu görüntülemek için Label widget'ını güncelle
  except ValueError:
    sonuc_label.config(text="Geçersiz giriş!")


def cikarma():
  try:
    sayi_1 = float(entry_1.get())
    sayi_2 = float(entry_2.get())
    sonuc = sayi_1 - sayi_2
    sonuc_label.config(
        text=str(sonuc))  # Sonucu görüntülemek için Label widget'ını güncelle
  except ValueError:
    sonuc_label.config(text="Geçersiz giriş!")


def carpma():
  try:
    sayi_1 = float(entry_1.get())
    sayi_2 = float(entry_2.get())
    sonuc = sayi_1 * sayi_2
    sonuc_label.config(
        text=str(sonuc))  # Sonucu görüntülemek için Label widget'ını güncelle
  except ValueError:
    sonuc_label.config(text="Geçersiz giriş!")


def bolme():
  try:
    sayi_1 = float(entry_1.get())
    sayi_2 = float(entry_2.get())
    if sayi_2 == 0:
      sonuc_label.config(text="Sayı, sıfıra bölünemez!")
    else:
      sonuc = sayi_1 / sayi_2
      sonuc_label.config(text=str(
          sonuc))  # Sonucu görüntülemek için Label widget'ını güncelle
  except ValueError:
    sonuc_label.config(text="Geçersiz giriş!")


def temizle():
  entry_1.delete(0, END)
  entry_2.delete(0, END)
  sonuc_label.config(text="")


toplama_button = Button(window, text="+", command=toplama)
toplama_button.pack()
cikarma_button = Button(window, text="-", command=cikarma)
cikarma_button.pack()
carpma_button = Button(window, text="*", command=carpma)
carpma_button.pack()
bolme_button = Button(window, text="/", command=bolme)
bolme_button.pack()

# Sonucu görüntülemek için bir Label widget'ı oluştur
sonuc_label = Label(window, text="")
sonuc_label.pack()

temizle_button = Button(window, text="Temizle", command=temizle)
temizle_button.pack()

window.mainloop()
