from tkinter import *
from tkinter.messagebox import *

fenetre = Tk()
fenetre.title('Ma fenetre')
fenetre.geometry("400x300")

"""
label = Label(fenetre, text="Hello World", fg='red', font=("Courier", 30))
label.pack()

bout = Button(fenetre, text='Quitter', command = fenetre.destroy)
bout.pack()

l = Label( fenetre, text = "Entrez votre age" )
l.pack(side = LEFT)
e = Entry(fenetre, bd = 10, width=30)
e.pack(side = RIGHT)

check1 = Checkbutton(fenetre, text="Masculin")
check1.pack()
check2 = Checkbutton(fenetre, text="Feminin")
check2.pack()

val = StringVar()
radio1 = Radiobutton(fenetre, text="Oui", variable=val, value=1)
radio2 = Radiobutton(fenetre, text="Non", variable=val, value=2)
radio3 = Radiobutton(fenetre, text="Peut-être", variable=val, value=3)
radio1.pack()
radio2.pack()
radio3.pack()

canvas = Canvas(fenetre, width=400, height=300, background='yellow')

ligne1 = canvas.create_line(75, 0, 75, 120)
ligne2 = canvas.create_line(0, 60, 150, 60)
txt = canvas.create_text(75, 60, text="Cible", font="Arial 16 italic", fill="blue")

canvas.create_rectangle(150,150,250,250)
canvas.create_oval(150,150,250,250,fill="orange",width=4)
canvas.pack()

value = DoubleVar()
scale = Scale(fenetre, variable=value)
scale.pack()

"""
def somme():
    som = int(nbre1.get()) + int(nbre2.get())
    return som
    
def affiche():
    showinfo("Alerte La somme est ", somme())
    
value1 = StringVar()
value2 = StringVar()
value1.set("10")
value2.set("15")
nbre1 = Entry(fenetre, textvariable=value1, width=30)
nbre2 = Entry(fenetre, textvariable=value2, width=30)
nbre1.pack()
nbre2.pack()

bouton = Button(fenetre, text="Valider", command=affiche)
bouton.pack()



"""
p = PanedWindow(fenetre, orient=HORIZONTAL)
p.pack(side=TOP, expand=Y, fill=BOTH, pady=2, padx=2)
p.add(Label(p, text='Volet 1', background='blue', anchor=CENTER))
p.add(Label(p, text='Volet 2', background='white', anchor=CENTER) )
p.add(Label(p, text='Volet 3', background='red', anchor=CENTER) )
p.pack()

s = Spinbox(fenetre, from_=0, to=10)
s.pack()

l = LabelFrame(fenetre, text="Titre de la frame", padx=20, pady=20)
l.pack(fill="both", expand="yes")
 
Label(l, text="A l'intérieure de la frame").pack()

"""


def alert():
    showinfo("alerte", "Bravo!")

menubar = Menu(fenetre)
menu1 = Menu(menubar)
menu1.add_command(label="Créer")
menu1.add_command(label="Editer")
menu1.add_separator()
menu1.add_command(label="Quitter")

menubar.add_cascade(label="Fichier", menu=menu1)

menu2 = Menu(menubar)
menu2.add_command(label="Couper")
menu2.add_command(label="Copier")
menu2.add_command(label="Coller")

menubar.add_cascade(label="Editer", menu=menu2)

menu3 = Menu(menubar)
menu3.add_command(label="A propos")

menubar.add_cascade(label="Aide", menu=menu3)

fenetre.config(menu=menubar)


"""
filepath = askopenfilename(title="Ouvrir une image",filetypes=[('png files','.png'),('all files','.*')])
photo = PhotoImage(file=filepath)
canvas = Canvas(fenetre, width=photo.width(), height=photo.height(), bg="yellow")
canvas.create_image(0, 0, anchor=NW, image=photo)
canvas.pack()
"""

l=[4,0,4,8,3,2,0]
l.sort()
print(l)
fenetre.mainloop()


