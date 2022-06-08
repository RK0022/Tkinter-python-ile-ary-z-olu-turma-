import tkinter as tk

pencere=tk.Tk()

#tasarım ve çalışacaak kodlar
pencere.title("MERZ")
pencere.geometry("700x400+600+100")

etiket = tk.Label(text="SESLİ ASİSTAN", font="Times 22 bold")
etiket.pack()
#pack()komponentleri paketliyor
#grid() arayüzün  parçalara bölünüyor
#place() x,y kordinantlarıyla yerleştirliyor


pencere.mainloop()