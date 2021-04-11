import tkinter as tk
import add_pretext

root = tk.Tk()
root.geometry("600x100")
root.resizable(0,0)
root.title("Breeam In-Use Pdf rename")

BIU_code_label = tk.Label(root, text="BIU Code")
BIU_code = tk.Entry(root, width=75)
src_code = BIU_code.get()

directory_label = tk.Label(root, text="Path to project")
directory = tk.Entry(root, width=75)


def button_function(dir_path, project_code):
    add_pretext.add_pretext(dir_path, project_code)


transl_button = tk.Button(root, text="Add Text", command=lambda: button_function(directory.get(),BIU_code.get()))


BIU_code_label.grid(row=0, column=0, pady=5, padx = 5)
BIU_code.grid(row=0, column=1, pady=5)
directory_label.grid(row=1, column=0, pady=5)
directory.grid(row=1, column=1, pady=5)
transl_button.grid(row=2, column=0, pady=5, padx=5)


root.mainloop()
