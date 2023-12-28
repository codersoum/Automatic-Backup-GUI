import tkinter as tk
from tkinter import *    
from tkinter import filedialog as fd
from tkinter import messagebox as m
from tkinter.messagebox import showinfo
import shutil 
import time
import os 
def Browse_Source():
    res= m.askyesno("Choose option","Click at 'Yes'to open a file or 'No' to open a folder?")
    if res :
     Source_dir = fd.askopenfilename()
     Source_entry.delete(0,tk.END)
     Source_entry.insert(0,Source_dir)
    else:
     Source_dir = fd.askdirectory()
     Source_entry.delete(0,tk.END)
     Source_entry.insert(0,Source_dir)
def Browse_Dest():
    Dest_dir= fd.askdirectory()
    Dest_Entry.delete(0,tk.END)
    Dest_Entry.insert(0,Dest_dir)
def backup():
    Source_dir=Source_entry.get()
    Dest_dir=Dest_Entry.get()
    #backup_folder = os.path.join(Dest_dir, date_format)
    #shutil.copytree(Source_dir,Dest_dir)
    if not Source_dir and not Dest_dir:
       status_label=tk.label(text="Please select source and destination directories.")
       status_label.place(relx=0.4 ,rely=0.7,anchor='center')
       status_label.configure(fg="Blue",bg="cyan")
    try:
       status_label=tk.Label(root,text="Backup in progress...")
       status_label.place(relx=0.4 ,rely=0.7,anchor='center')
       #base_name, extension = os.path.splitext(os.path.basename(Source_dir))
       if os.path.isdir(Source_dir):
        backup_path = os.path.join(Dest_dir, "backup_" + time.strftime("%Y%m%d_%H%M%S"))
        shutil.copytree(Source_dir, backup_path)
       else:
          base_name, extension = os.path.splitext(os.path.basename(Source_dir))
          shutil.copy2(Source_dir, os.path.join(Dest_dir, "backup_" + time.strftime("%Y%m%d_%H%M%S")+base_name+extension))
       status_label=tk.Label(text="Status:Backup completed successfully!")
       status_label.place(relx=0.4 ,rely=0.7,anchor='center')
       status_label.configure(fg="Blue",bg="cyan")
    except Exception as e:
       status_label=tk.Label(text=f"An unexpexcted Error occured: {str(e)}")
       print(f"An unexpexcted Error occured: {str(e)}")
       status_label.configure(fg="Red",bg="cyan")
       status_label.place(relx=0.4 ,rely=0.7,anchor='center')
#Create the interface window
root = tk.Tk()
root.title('Automatic Backup')            
root.resizable(False, False)
root.geometry('500x200')
root.configure(bg='cyan')
Source= tk.Label(text="Source :")
Source_entry = tk.Entry()
Destination=tk.Label(text="Destination :")
Dest_Entry=tk.Entry()
Source.grid(row=0, column=0,padx=10, pady=5,sticky=tk.W)
Source.configure(fg='blue',bg='cyan')
Source_entry.grid(row=0,column=1,ipadx=30,ipady=0,padx=0, pady=15,sticky=tk.W)
Destination.grid(row=1, column=0, padx=10, pady=5,sticky=tk.W)
Destination.configure(fg='blue',bg='cyan')
Dest_Entry.grid(row=1,column=1,ipadx=30,ipady=0,padx=0, pady=5,sticky=tk.W)
browse_button = tk.Button(
    text="Click to Browse Source File/Folder!",
    fg="green",
    height=0, 
    width=27,
    command=Browse_Source
)
select_button = tk.Button(
    text="Click to Browse Backup Folder!",
    fg="green",
    height=0, 
    width=27,
    command=Browse_Dest
)
submit_button = tk.Button(
    text="Click to Create Backup",
    fg="green",
    command=backup
)
browse_button.grid(row=0,column=2,padx=15,sticky=tk.E)
select_button.grid(row=1,column=2,padx=15,sticky=tk.E)
submit_button.place(relx=0.4,rely=0.6,anchor='center')
root.mainloop()

