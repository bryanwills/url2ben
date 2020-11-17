from tkinter import *
import pyperclip

def updateClipboard():
    cliptext = pyperclip.paste()
    processClipping(cliptext=cliptext)
    root.after(ms=100, func=updateClipboard)

def processClipping(cliptext):
    cliptextCleaned = cleanClipText(cliptext=cliptext)
    label["text"] = cliptextCleaned

def cleanClipText(cliptext):
    #removing all characters > 65535 
    cliptext = "".join([c for c in cliptext if ord(c) <= 65535])
    return cliptext

def onClick(labelElem):
    labelText = labelElem["text"]
    print(labelText)
    pyperclip.copy(labelText)


if __name__ == '__main__':
    root = Tk()
    label = Label(root, text="", cursor="plus", relief=RAISED, pady=5, wraplength=500)
    label.bind("<Button-1>", lambda event, labelElem=label: onClick(labelElem))
    label.pack()
    updateClipboard()
    root.mainloop()