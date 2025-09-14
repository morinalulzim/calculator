import tkinter

# Funktion zu Schaltfläche Ender
def ende():
    main.destroy()

# Hauptfenster
main = tkinter.Tk()
main.title("Taschenrechner")

# Schaltfläche Ende
b = tkinter.Button(main, text="Ende", command=ende)
b.pack()

# Endlosschleife
main.mainloop()