from tkinter import *
from PIL import Image, ImageTk # noqa: F401
import string



from random import randint, choice



def generate_password():
    password_min = 6
    password_maximum = 12
    all_chars = string.ascii_letters + string.punctuation + string.digits

    password = "".join (choice(all_chars) for x in range(randint(password_min, password_maximum)))
    password_entry.delete(0, END)
    password_entry.insert(0, password)
        



## création de la fenetre 
window = Tk()
window.title("Générateur de mot de passe")
window.geometry("720x480")
window.config(background='#4065A4')

## création de la frame principale 
main_fraim= Frame(window, bg='#4065A4')




#création d'image 
width = 300
height = 300
image_path = "canvas_image.png"
pil_image = Image.open(image_path)
image = ImageTk.PhotoImage(pil_image)

Canvas= Canvas(main_fraim, width=width, height=height, bg='#4065A4', bd=0, highlightthickness=0)
Canvas.create_image(width/2, height/2, image=image)
Canvas.grid(row=0, column=0, sticky=W)

## création d'une sous boîte 
right_frame = Frame(main_fraim, bg='#4065A4')


## création d'un titre
Label_title = Label(right_frame, text="Mot de passe", font=("helvetica", 20), bg='#4065A4', fg='white')
Label_title.pack()

## création d'un champs/input
password_entry= Entry(right_frame, font=("helvetica", 20), bg='burlywood4', fg='white')
password_entry.pack()


## création un bouton
genrate_password_button = Button(right_frame, text="Générer", font=("helvetica", 20), bg='#4065A4', fg='white', command = generate_password)
genrate_password_button.pack()



## placer la sous boite à droite de la frame princip
right_frame.grid(row=0, column=1, sticky=W)


## afficher la frame 
main_fraim.pack(expand=YES)

##création d'une barre de Menu
menu_bar = Menu(window)
# Premier Menu
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Nouveau", command = generate_password)
file_menu.add_command(label="Quitter", command = window.quit)
menu_bar.add_cascade(label="Fichier", menu = file_menu)

## Configuration de ma fenêtre pour add mon menu bar 
window.config(menu=menu_bar)

#affiche la fenetre
window.mainloop()
