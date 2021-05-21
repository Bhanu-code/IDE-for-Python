from tkinter import *
import tkinter.ttk as ttk
from tkinter import filedialog
from PIL import Image, ImageTk
from tkinter.filedialog import asksaveasfilename, askopenfilename
from tkinter import  font
import  subprocess

compiler = Tk()
compiler.title("PyPad")
compiler.geometry("900x600")
compiler.minsize(500,350)
compiler.iconbitmap('Icons/python.ico')

file_path = ''
global selected
selected =  False

image=Image.open('Icons/new_file_icon.png')
image = image.resize((20,20), Image.ANTIALIAS)
new_file_icon = ImageTk.PhotoImage(image)

image=Image.open('Icons/bold_icon.png')
image = image.resize((15,15), Image.ANTIALIAS)
bold_icon = ImageTk.PhotoImage(image)

image=Image.open('Icons/italic_icon.png')
image = image.resize((23,23), Image.ANTIALIAS)
italic_icon = ImageTk.PhotoImage(image)

image=Image.open('Icons/undo_icon.png')
image = image.resize((18,18), Image.ANTIALIAS)
undo_icon = ImageTk.PhotoImage(image)

image=Image.open('Icons/redo_icon.png')
image = image.resize((18,18), Image.ANTIALIAS)
redo_icon = ImageTk.PhotoImage(image)

image=Image.open('Icons/run_icon.png')
image = image.resize((23,23), Image.ANTIALIAS)
run_icon = ImageTk.PhotoImage(image)

image=Image.open('Icons/save_icon.png')
image = image.resize((20,20), Image.ANTIALIAS)
save_icon = ImageTk.PhotoImage(image)

image=Image.open('Icons/cut_icon.png')
image = image.resize((20,20), Image.ANTIALIAS)
cut_icon = ImageTk.PhotoImage(image)

image=Image.open('Icons/paste_icon.png')
image = image.resize((23,23), Image.ANTIALIAS)
paste_icon = ImageTk.PhotoImage(image)






def new_file(e):
    editor.delete('1.0',END)
    compiler.title('New File - PyPad')
    status_bar.config(text="New File         ")

def run(e):
    if file_path == '':
        save_prompt = Toplevel()
        text = Label(save_prompt, text='Please Save your code!',fg = 'red')
        text.pack()
        return
    command = f'python {file_path}'
    process = subprocess.Popen(command, stdout= subprocess.PIPE, stderr=subprocess.PIPE, shell = True)
    output,error = process.communicate()
    code_output.insert('1.0', output)
    code_output.insert('1.0', error)

def save_as(e):
    if file_path == '':
        path = asksaveasfilename(filetypes=[('Python Files', '*.py')])
    else:
        path = file_path
    with open(path, 'w') as file:
        code = editor.get('1.0', END)
        file.write(code)
        set_file_path(path)

def open_file(e):
    path = askopenfilename(title = "Open File", filetypes=[('Python Files', '*.py')])
    with open(path, 'r') as file:
        code = file.read()
        editor.delete('1.0', END)
        editor.insert('1.0', code)
        set_file_path(path)
        status_bar1.config(text=path)

def set_file_path(path):
    global file_path
    file_path = path

def undo_text(e):
    editor.edit_undo()

def redo_text(e):
    editor.edit_redo()

def cut_text(e):
    global selected
    if editor.selection_get():
        selected = editor.selection_get()
        editor.delete("sel.first", "sel.last")
        compiler.clipboard_clear()         
        compiler.clipboard_append(selected)

def change_font(p):
    if p==1:
        editor.config(font=("comicsans", 12))
    elif p==2:
        editor.config(font=("Helvetica", 12))
    elif p==3:
        editor.config(font=("Arial", 12))
    elif p==4:
        editor.config(font=("Calibri", 12))
    elif p==5:
        editor.config(font=("Futura", 12))
    elif p==6:
        editor.config(font=("Garamond", 12))
    elif p==7:
        editor.config(font=("Times New Roman", 12))
    elif p==8:
        editor.config(font=("Cambria", 12))
    elif p==9:
        editor.config(font=("Veradana", 12))
    else:
        editor.config(font=("Helvetica", 12))


def copy_text(e):
    global selected
    if e:
        selected = complier.clipboard_get()
    if editor.selection_get():
        selected = editor.selection_get()
        compiler.clipboard_clear()
        compiler.clipboard_append(selected)

def paste_text(e):
    if e:
        selected = complier.clipboard_get()
    else:
        if selected:
            pos = editor.index(INSERT)
            editor.insert(pos, selected)

def night_mode():
    main_color = "blue4"
    first_color = "midnight blue"
    second_color = "grey30"
    text_color = "white"

    compiler.config(bg=first_color)
    status_bar.config(bg=main_color, fg=text_color)
    status_bar1.config(bg=main_color, fg=text_color)
    editor.config(bg=second_color,fg=text_color)
    code_output.config(bg=second_color,fg=text_color)

def light_mode():
    main_color = "white"
    first_color = "light green"
    second_color = "light yellow"
    text_color = "black"

    compiler.config(bg=second_color)
    status_bar.config(bg=first_color, fg=text_color)
    status_bar1.config(bg=first_color, fg=text_color)
    editor.config(bg=main_color,fg=text_color)
    code_output.config(bg=main_color,fg=text_color)

def bold_it():
    bold_font=font.Font(editor,editor.cget("font"))
    bold_font.config(weight="bold")

    editor.tag_configure("bold", font=bold_font)

    current_tags=editor.tag_names("sel.first")

    if "bold" in current_tags:
        editor.tag_remove("bold","sel.first","sel.last")
    else:
        editor.tag_add("bold","sel.first","sel.last")

def italic_it():
    italics_font = font.Font(editor, editor.cget("font"))
    italics_font.config(slant="italic")

    editor.tag_configure("italic", font=italics_font)

    current_tags = editor.tag_names("sel.first")

    if "italic" in current_tags:
        editor.tag_remove("italic", "sel.first", "sel.last")
    else:
        editor.tag_add("italic", "sel.first", "sel.last")

menu_bar = Menu(compiler)

file_bar = Menu(menu_bar, tearoff=0)
file_bar.add_command(label="New File", command=lambda:new_file(1),accelerator="(Ctrl+N)")
file_bar.add_command(label="Open", command=lambda:open_file(1),accelerator="(Ctrl+O)")
file_bar.add_command(label="Save", command=lambda:save_as(False),accelerator="(Ctrl+S)")
file_bar.add_command(label="Save as", command=lambda:save_as(False),accelerator="(Ctrl+Shift+S)")
file_bar.add_separator()
file_bar.add_command(label="Exit", command=lambda:exit(False),accelerator="(Alt+X)")
menu_bar.add_cascade(label='File', menu =file_bar)

edit_bar = Menu(menu_bar, tearoff=0)
edit_bar.add_command(label="Copy", command=lambda:copy_text(False),accelerator="(Ctrl+C)")
edit_bar.add_command(label="Cut", command=lambda:cut_text(False),accelerator="(Ctrl+X)")
edit_bar.add_command(label="Paste", command=lambda:paste_text(False),accelerator="(Ctrl+V)")
menu_bar.add_cascade(label='Edit', menu =edit_bar)

user_bar = Menu(menu_bar, tearoff=0)
user_bar.add_command(label="Undo", command=lambda:undo_text(False),accelerator="(Ctrl+z)")
user_bar.add_command(label="Redo", command=lambda:redo_text(False),accelerator="(Ctrl+y)")
menu_bar.add_cascade(label='User', menu =user_bar)

theme_bar = Menu(menu_bar, tearoff=0)
theme_bar.add_command(label="Light Mode", command=light_mode)
theme_bar.add_command(label="Night Mode", command=night_mode)
menu_bar.add_cascade(label='Themes', menu =theme_bar)

font_bar = Menu(menu_bar, tearoff=0)
font_bar.add_command(label="Comicsans", command=lambda:change_font(1))
font_bar.add_command(label="Helvetica", command=lambda:change_font(2))
font_bar.add_command(label="Arial", command=lambda:change_font(3))
font_bar.add_command(label="Calibri", command=lambda:change_font(4))
font_bar.add_command(label="Futura", command=lambda:change_font(5))
font_bar.add_command(label="Garamond", command=lambda:change_font(6))
font_bar.add_command(label="Times New Roman", command=lambda:change_font(7))
font_bar.add_command(label="Cambria", command=lambda:change_font(8))
font_bar.add_command(label="Verdana", command=lambda:change_font(9))
menu_bar.add_cascade(label='Font', menu =font_bar)

run_bar = Menu(menu_bar, tearoff=0)
run_bar.add_command(label="Run", command=lambda:run(False), accelerator = "(Alt+F5)")
menu_bar.add_cascade(label='Run', menu =run_bar)

help_bar = Menu(menu_bar, tearoff=0)
help_bar.add_command(label="About",command=run)
menu_bar.add_cascade(label='Help', menu = help_bar)

#Creating Toolbar
toolbar = Frame(compiler)
toolbar.pack(fill=X)

#Adding a Frame
f1 = Frame(compiler)
f2 = Frame(compiler)
f1.pack()
f2.pack()

#Creating a scrollbar
text_scroll = Scrollbar(f1)
text_scroll.pack(side=RIGHT, fill=Y)
text_scroll1 = Scrollbar(f2)
text_scroll1.pack(side=RIGHT, fill=Y)

#Creating Textbox
status_bar1 = Label(f1, text=file_path, bg="light green",font=("comicsans", 12))
status_bar1.pack(fill = X,side = TOP)


#Creating Textbox
editor = Text(f1,width=160,height=17, bg="white",font = ("calibri", 14), borderwidth=3, relief="sunken", selectbackground = "yellow", selectforeground = "black" , undo=True,yscrollcommand=text_scroll.set)
editor.pack(pady=5,padx=5)

#Configuring Scrollbar
text_scroll.config(command = editor.yview)

#Creating Buttons
new_file_button=Button(toolbar,image=new_file_icon,command=lambda:new_file(False), borderwidth=0)
new_file_button.grid(row=0, sticky = W, column=0,padx=10)

save_button=Button(toolbar,image=save_icon,command=lambda:save_as(False), borderwidth=0)
save_button.grid(row=0,column=1, padx=10)

cut_button=Button(toolbar,image=cut_icon,command=lambda:cut_text(False), borderwidth=0)
cut_button.grid(row=0,column=2, padx=10)

paste_button=Button(toolbar,image=paste_icon,command=lambda:paste_text(False), borderwidth=0)
paste_button.grid(row=0,column=3, padx=10)

bold_button=Button(toolbar,image=bold_icon,command=bold_it, borderwidth=0)
bold_button.grid(row=0,column=4, padx=10)

italics_button=Button(toolbar,image=italic_icon,command=italic_it, borderwidth=0)
italics_button.grid(row=0, column=5,padx=10)

undo_button=Button(toolbar,image=undo_icon,command=lambda:undo_text(False),borderwidth=0)
undo_button.grid(row=0, column=6,padx=10)

redo_button=Button(toolbar,image=redo_icon,command=lambda:redo_text(False), borderwidth=0)
redo_button.grid(row=0, column=7, padx=10)

run_button=Button(toolbar,image=run_icon,command=lambda:run(False), borderwidth=0)
run_button.grid(row=0, column=8, padx=10)


code_output = Text(f2,width=160,height=15,bg = "white",font = ("Helvetica", 14),borderwidth=3, relief="sunken")
code_output.pack(padx=5)



#Bindking with Keyboard Shortcuts
compiler.bind('<Control-Key-x>', cut_text)
compiler.bind('<Control-Key-c>', copy_text)
compiler.bind('<Control-Key-v>', paste_text)
compiler.bind('<Control-Key-z>', undo_text)
compiler.bind('<Control-Key-y>', redo_text)
compiler.bind('<Control-Key-o>', open_file)
compiler.bind('<Control-Key-S>', save_as)
compiler.bind('<Alt-Key-F5>', run)
compiler.bind('<Alt-Key-x>',compiler.quit())

#Status Bar
status_bar = Label(f1, text="Output",bg = "light green",fg="black",font=("comicsans", 12))
status_bar.pack(fill = X,side = BOTTOM)


compiler.config(menu=menu_bar, borderwidth=3, bg="light yellow", relief="sunken")


compiler.mainloop()
