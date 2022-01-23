import xml.etree.ElementTree as ET
from tkinter import *
from PIL import ImageTk, Image

okno=Tk()
okno.title ("Biblioteka+")
okno.iconbitmap("Library-Books.ico")
okno.geometry("1000x800")


def creating():
    data = ET.Element('bilbioteka')
    try:
        w=int(input("ile książek chcesz dodać do zbioru? "))
    except:
        print ("PODAJ LICZBĘ!")
        creating()
    a=1
    while a<=w:
        autor=input("podaj imię i nazwisko autora ")
        tytul=input("Podaj tytuł książki ")
        s_element2 = ET.SubElement(data, 'AUTOR')
        s_element2.set ('ID', str(a))
        s_element2.text=autor
        
        s_element3 = ET.SubElement(data, 'TYTUL')
        s_element3.set ('ID', str(a))
        s_element3.text=tytul
        a+=1
    b_xml = ET.tostring(data, encoding="unicode")
 
    with open("biblioteka.xml", "w", encoding='utf-8') as f:
        f.write(b_xml)
    menu()
def reading():
    tree = ET.parse('biblioteka.xml')
    root = tree.getroot()
    q=0
    button_menu1 = Button(okno, text="ID",  bd=2, state=DISABLED, width=5, disabledforeground="black") 
    button_menu2 = Button(okno, text="Autor",  bd=2, state=DISABLED, width=40, disabledforeground="black")
    button_menu3 = Button(okno, text="Tytuł",  bd=2, state=DISABLED, width=40, disabledforeground="black")
    
    for child in root:
        value = child.get('ID')
        data= child.text
        if child.tag == "AUTOR":
            kolumna="autor"
            kolumna_nr=1
        elif child.tag == "TYTUL":
             kolumna="tytul"
             kolumna_nr=2
        if int(value)%2==0:
            kolorek="green"
        else:
            kolorek="brown"    
            
       
        ksiazka= Button (okno, text=value, bd=2, state=DISABLED,  width=5, disabledforeground=kolorek)
        dane_ksiązki= Button(okno, text=data, bd=2, state=DISABLED, width=40, disabledforeground=kolorek)
       
        ksiazka.grid( row=int(value)+2, column=0)
        dane_ksiązki.grid( row=int(value)+2, column=kolumna_nr)
    
    button_menu1.grid( row=2, column=0)
    button_menu2.grid( row=2, column=1)
    button_menu3.grid( row=2, column=2)
    okno.mainloop()
def editing():
    reading(2)
    try:
        nr=int(input("Podaj ID książki której autora chcesz wyedytować: "))
    except:
        print ("PODAJ LICZBĘ!")
        editing()
    tree = ET.parse('biblioteka.xml')
    for b in tree.iter('AUTOR'):
        if b.attrib['ID']==str(nr):
            autor=input("podaj imię i nazwisko autora ")
        
            b.text=autor
    tree.write("biblioteka.xml")
    menu()
def czytelnicy():
    tree = ET.parse('czytelnicy.xml')
    root = tree.getroot()
    q=0
    button_menu1 = Button(okno, text="ID",  bd=2, state=DISABLED, width=5, disabledforeground="black") 
    button_menu2 = Button(okno, text="Imię i nazwisko",  bd=2, state=DISABLED, width=40, disabledforeground="black")
    button_menu3 = Button(okno, text="Dokument Tożsamości",  bd=2, state=DISABLED, width=40, disabledforeground="black")
    
    for child in root:
        value = child.get('ID')
        data= child.text
        if child.tag == "NAZWA":
            kolumna="autor"
            kolumna_nr=1
        elif child.tag == "DOKUMENT":
             kolumna="tytul"
             kolumna_nr=2
        if int(value)%2==0:
            kolorek="green"
        else:
            kolorek="brown"    
            
       
        ksiazka= Button (okno, text=value, bd=2, state=DISABLED,  width=5, disabledforeground=kolorek)
        dane_ksiązki= Button(okno, text=data, bd=2, state=DISABLED, width=40, disabledforeground=kolorek)
       
        ksiazka.grid( row=int(value)+2, column=0)
        dane_ksiązki.grid( row=int(value)+2, column=kolumna_nr)
    
    button_menu1.grid( row=2, column=0)
    button_menu2.grid( row=2, column=1)
    button_menu3.grid( row=2, column=2)
    okno.mainloop()
    return

def menu():
    button1 = Button(okno, text="Utwórz księgozbiór",  bd=2, command=creating)
    button2 = Button(okno, text="wyświetl księgozbór",  bd=2, command=reading)
    button3 = Button(okno, text="wyświetl czytelników",  bd=2, command=czytelnicy)
  


    button1.grid( row=0, column=0, pady=3)
    button2.grid (row=0, column=1, pady=3)
    button3.grid (row=0, column=2, pady=3)
   
    okno.mainloop()


menu()

