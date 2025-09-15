import tkinter

# Funktion zu Schaltfläche Exit
def close_app():
    main.destroy()

# Funktion zu Schaltfläche Resize
def resize():
    main.geometry("800x600")

# Hauptfenster
main = tkinter.Tk()
main.title("Taschenrechner")
main.geometry("600x400")
main.configure(background="lightblue")

# Schaltfläche Ende
exitButton = tkinter.Button(main, text="Exit", command=close_app)
exitButton["bg"] = "red"
exitButton.pack()

# Test Button
resizeButton = tkinter.Button(main, text="Resize", command=resize)
resizeButton["bg"] = "blue"
resizeButton.pack()

# Test Button für Reihen


# Endlosschleife
main.mainloop()