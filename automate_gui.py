import tkinter
from tkinter import Entry, filedialog,messagebox
from tkinter.constants import CENTER
import os,shutil

# global variables
working_dir = ""
target_dir = ""
extension = ""

root = tkinter.Tk()
# app size
root.geometry("400x300")
# creatimg frame container
frame = tkinter.Frame(root,pady=40)
frame.pack()


def working_path():
    global working_dir
    # directory path for the working dir -> /Users/andrej/Downloads for examples

    # working dir path -->
    working_dir = filedialog.askdirectory()


# Label and Button for target dir path 
label_chooser = tkinter.Label(frame,text="Choose Working Directory:")

label_chooser.grid(column=0,row=0)
ask_dir_path_btn = tkinter.Button(frame,text="Choose",command=working_path,activeforeground="blue",padx=30)
ask_dir_path_btn.grid(column=1,row=0)



# middle Frame, and entry for extensions

entry_frame = tkinter.Frame(root,pady=20)
entry_frame.pack()
entry_label = tkinter.Label(entry_frame,text="Enter name of extension e.g: '.mp3'")
entry_label.grid(column=1,row=0)
entry = Entry(entry_frame)
entry.grid(column=1,row=1)


# this function gets input from entry and deletes it after
def target_path():
    global extension
    global target_dir
    extension = entry.get()
    extension_length = len(extension)
    extension = extension.split(",")
    entry.delete(0,extension_length)

    #file_dialog for target dir -->
    target_dir = filedialog.askdirectory()

# start everything, this function moves all files from working dir with extension to target dir
# e.g from Downloads dir with .mp4 extension move all files to Desktop/mp4_folder

def start():
    os.chdir(working_dir)
    files = os.listdir()
    specific_files = []
    print(extension)
    for i in range(len(extension)):
        for file in files:
            if(file.endswith(extension[i])):
                specific_files.append(file)

    # print(specific_files)

    os.chdir(target_dir)
    for i in range(len(specific_files)):
        shutil.move(working_dir + "/" + specific_files[i],os.getcwd())
        print(f"{extension}: {i+1}: {specific_files[i]} has been moved.")

    messagebox.showinfo("Proccess","Proccess has completed!")

    

# New Frame, Label and Button for new dir path where to put new files from target dir path

bottom_frame = tkinter.Frame(root,pady=30)
bottom_frame.pack()

label_chooser_bottom = tkinter.Label(bottom_frame,text="Choose Target Directory:")
label_chooser_bottom.grid(column=0,row=0)
ask_dir_path_btn_bottom = tkinter.Button(bottom_frame,text="Choose",command=target_path,activeforeground="blue",padx=30)
ask_dir_path_btn_bottom.grid(column=1,row=0)


start_btn = tkinter.Button(bottom_frame,text="Start",padx=80,command=start)
start_btn.place(x=125,y=40,anchor=CENTER)


# calling the app
root.mainloop()
