import tkinter as tk
import tkinter.filedialog as tfd
import tkinter.messagebox as tmb

window=tk.Tk()
window.geometry("400x400")
window.title("NoteBook")

File_name=""


##Functions:

#-open_file
def open_file():
    global File_name
    text.delete(1.0,"end")
    File_name=tfd.askopenfilename()
    with open (File_name) as File:
        text.insert(1.0,File.read())

        
#-save_as
def save_as():
    global File_name
    File_name=tfd.asksaveasfilename()
    content=text.get(1.0,"end")
    tmb.showinfo("Saving","Saving to : " + (File_name) + "...")
    with open (File_name,"w") as File:
        File.write(content)
        window.title(f"Note Book - {File_name} ") 
        
        
#-save
def save():
    global File_name
    if File_name == "":
        save_as()
    else:
        if tmb.showinfo("","Your File was succesfully saved!"):
            content=text.get(1.0,"end")
            with open (File_name,"w") as File:
                File.write(content)
                 
        
#-New_file
def New_file():
    global File_name
    if tmb.askokcancel("Creation of a new File","Are you sure? (Text that will not be saved will be deleted!)"):
        File_name=""
        text.delete(1.0,"end")
        window.title(f"New File - NoteBook")
        

#-delete_all_text
def delete_all_text():
    global File_name
    if File_name == " ":
        tk.messagebox.showinfo("Information","You don't have text!")
        
    if tmb.askokcancel("Delete all Text","Are you sure? (!All THE TEXT WILL BE DELETED!)"):
        text.delete(1.0,"end")

#-Delete_file
def delete_file():
   tmb.showerror("Error","The button is not working yet!")
                  
##Creation of text area
text=tk.Text(window,wrap="word")
text.place(x=0,y=0,relheight=1,relwidth=1)

##Creation of icons
new_file_icon=tk.PhotoImage(file="new_file.gif")
open_file_icon=tk.PhotoImage(file="open_file.gif")
save_file_icon=tk.PhotoImage(file="save_file.gif")
save_as_file_icon=tk.PhotoImage(file="save_file.gif")
delete_text_icon=tk.PhotoImage(file="delete.gif")

##Creation of menu
main_menu=tk.Menu(window)
window.configure(menu=main_menu)
file_menu=tk.Menu(main_menu)
main_menu.add_cascade(label="File",menu=file_menu)
file_menu.add_command(label="New File",image=new_file_icon,compound="left",command=New_file)
file_menu.add_command(label="Open File",image=open_file_icon,compound="left",command=open_file)
file_menu.add_command(label="Save File",image=save_file_icon,compound="left",command=save)
file_menu.add_command(label="Save as",image=save_as_file_icon,compound="left",command=save_as)
file_menu.add_command(label="Delete all the text",image=delete_text_icon,compound="left",command=delete_all_text)
file_menu.add_command(label="Delete File",image=delete_text_icon,compound="left",command=delete_file)







window.mainloop()
