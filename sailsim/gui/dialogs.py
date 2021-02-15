from tkinter import Tk, Label, Button


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
