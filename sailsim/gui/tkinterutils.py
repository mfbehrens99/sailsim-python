from tkinter import Tk, Label, Button, N, E, S, W


def exitMsg(save, dest):
    def saveFunc():
        save()
        exitFunc()

    def exitFunc():
        dest.destroy()
        window.destroy()

    window = Tk()
    Label(window, text="Do you really want to close this window without saving?").grid(row=0, column=0, columnspan=3)
    Button(window, text="Save and Close", command=saveFunc).grid(row=1, column=0)
    Button(window, text="Close without saving", command=exit).grid(row=1, column=1)
    Button(window, text="Cancel", command=window.destroy).grid(row=1, column=2)
    window.mainloop()


def drawCompass(canvas, cpX, cpY, r1, r2, r3, fill1, fill2):
    font = ("Broadway", 16)
    canvas.create_oval(cpX - r3, cpY - r3, cpX + r3, cpY + r3)
    canvas.create_polygon(cpX, cpY - r2, cpX + r1, cpY - r1, cpX, cpY, fill=fill1)
    canvas.create_polygon(cpX + r2, cpY, cpX + r1, cpY - r1, cpX, cpY, fill=fill2)
    canvas.create_polygon(cpX + r2, cpY, cpX + r1, cpY + r1, cpX, cpY, fill=fill1)
    canvas.create_polygon(cpX, cpY + r2, cpX + r1, cpY + r1, cpX, cpY, fill=fill2)
    canvas.create_polygon(cpX, cpY + r2, cpX - r1, cpY + r1, cpX, cpY, fill=fill1)
    canvas.create_polygon(cpX - r2, cpY, cpX - r1, cpY + r1, cpX, cpY, fill=fill2)
    canvas.create_polygon(cpX - r2, cpY, cpX - r1, cpY - r1, cpX, cpY, fill=fill1)
    canvas.create_polygon(cpX, cpY - r2, cpX - r1, cpY - r1, cpX, cpY, fill=fill2)
    canvas.create_text(cpX, cpY - r2, anchor=S, font=font, text="N")
    canvas.create_text(cpX + r2, cpY, anchor=W, font=font, text=" E")
    canvas.create_text(cpX, cpY + r2, anchor=N, font=font, text="S")
    canvas.create_text(cpX - r2, cpY, anchor=E, font=font, text="W")
