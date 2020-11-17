import os
import tkinter as tk
import tkinter.filedialog

r = tk.Tk()
r.withdraw()
photo_path= tkinter.filediaglog.askdirectory(title='what folder would you like to copy the contents from?', initialdir='/')


#Get list of filenames in current directory
file_list=[]

for filename in os.listdir(photo_path):
    if os.path.splitext(filename)[1]=='.JPG':
        file_list.append(os.path.splitext(filename)[0])
    else: pass

file_search='code:('+' OR '.join(file_list)+')'

r.clipboard_clear()
r.clipboard_append(file_search)
r.destroy()
