import xml.etree.ElementTree as ET
from tkinter import *
from PIL import ImageTk, Image

okno=Tk()
okno.title ("Biblioteka+")
okno.iconbitmap("Library-Books.ico")
okno.geometry("1000x800")

def all_children (okno) :
    _list = okno.winfo_children()

    for item in _list :
        if item.winfo_children() :
            _list.extend(item.winfo_children())

    return _list

def activate(event,  b, tab):
    szukane_1=event.widget.get()
    szukane_2=b
   #przetwarzamy wyszukiwanie i wyświetlamy listę książek
    if tab==1:
        plik="biblioteka.xml"
        reading (szukane_1, szukane_2, plik)
    else:
        plik="czytelnicy.xml"
        reading (szukane_1, szukane_2, plik)

    return

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


def reading(szukane_1, szukane_2, plik):
    #usuwamy wszysktie elementy
    widget_list = all_children(okno)
    for item in widget_list:
        item.destroy()
        #poniżej nagłówek tabeli głównej wyników wyszukiwania oraz zmienne definiujące wyświetlane tabele i jej kolumny   
    if plik=="biblioteka.xml":
        tree = ET.parse('biblioteka.xml')
        button_menu1 = Button(okno, text="ID",  bd=2, state=DISABLED, width=5, disabledforeground="black") 
        button_menu2 = Button(okno, text="Autor",  bd=2, state=DISABLED, width=40, disabledforeground="black")
        button_menu3 = Button(okno, text="Tytuł ksiązki",  bd=2, state=DISABLED, width=40, disabledforeground="black")
        binder1="AUTOR"
        binder2="TYTUL"
        tab=1
        
    else:
        tree= ET.parse("czytelnicy.xml")
        button_menu1 = Button(okno, text="ID",  bd=2, state=DISABLED, width=5, disabledforeground="black") 
        button_menu2 = Button(okno, text="Imię i nazwisko",  bd=2, state=DISABLED, width=40, disabledforeground="black")
        button_menu3 = Button(okno, text="Dokument",  bd=2, state=DISABLED, width=40, disabledforeground="black")
        binder1="NAZWA"
        binder2="DOKUMENT"
        tab=2
    button_menu4 = Button(okno,  bd=2, state=DISABLED, width=10)     
    search_1=Entry(okno, width=45)
    search_2=Entry(okno, width=45)
    root = tree.getroot()
    q=0
    #q to zmienna do kontroli ilości kolumn (ID)

    # i drukujemy wniki
    for child in root:

        value = child.get('ID')
        data= child.text
        kolorek="green"
      
        if child.text.rfind(str(szukane_1))!=-1 and child.tag==str(szukane_2):
            q=int(value)

            for szukany in root:
                ksiazka= Button (okno, text=szukany.get("ID"), bd=2, state=DISABLED,  width=5, disabledforeground=kolorek)
                dane_ksiązki= Button(okno, text=szukany.text, bd=2, state=DISABLED, width=40, disabledforeground=kolorek)
                edycja=Button (okno, text="Edytuj", bd=2, command=lambda i=szukany.get("ID"): editing(plik, i))
                
                if szukany.tag == "AUTOR" or szukany.tag == "NAZWA":
                    
                    kolumna_nr=1
                elif szukany.tag == "TYTUL" or szukany.tag == "DOKUMENT":
                   
                    kolumna_nr=2
                if int(szukany.get("ID")) == q:
                    
                    ksiazka.grid( row=int(szukany.get("ID"))+3, column=0)
                    dane_ksiązki.grid( row=int(szukany.get("ID"))+3, column=kolumna_nr)
                    edycja.grid(row=int(szukany.get("ID"))+3, column=3)
    
    button_menu1.grid( row=2, column=0)
    button_menu2.grid( row=2, column=1)
    button_menu3.grid( row=2, column=2)
    button_menu4 .grid(row=2, column=3)
    search_1.grid( row=3, column=1)
    search_2.grid( row=3, column=2)

    search_1.bind("<Return>", lambda event, b=binder1: activate(event, b, tab))
    search_2.bind("<Return>", lambda event, b=binder2: activate(event, b, tab))

    menu()
    
def editing(plik, wiersz):
    widget_list = all_children(okno)
    for item in widget_list:
        item.destroy()

    if plik=="biblioteka.xml":
        tree = ET.parse('biblioteka.xml')
        button_menu1 = Button(okno, text="ID",  bd=2, state=DISABLED, width=5, disabledforeground="black") 
        button_menu2 = Button(okno, text="Autor",  bd=2, state=DISABLED, width=40, disabledforeground="black")
        button_menu3 = Button(okno, text="Tytuł ksiązki",  bd=2, state=DISABLED, width=40, disabledforeground="black")
        binder1="AUTOR"
        binder2="TYTUL"
        tab=1
        
    else:
        tree= ET.parse("czytelnicy.xml")
        button_menu1 = Button(okno, text="ID",  bd=2, state=DISABLED, width=5, disabledforeground="black") 
        button_menu2 = Button(okno, text="Imię i nazwisko",  bd=2, state=DISABLED, width=40, disabledforeground="black")
        button_menu3 = Button(okno, text="Dokument",  bd=2, state=DISABLED, width=40, disabledforeground="black")
        binder1="NAZWA"
        binder2="DOKUMENT"
        tab=2
    button_menu4 = Button(okno,  bd=2, state=DISABLED, width=10)   
    root = tree.getroot()
    for child in root:
        value = child.get('ID')
        data= child.text
        kolorek="black"
        search_1=Entry(okno, width=45)
        search_2=Entry(okno, width=45)
      
        if child.get('ID')==wiersz:
            q=int(value)

            for szukany in root:
                zapis=Button (okno, text="Zapisz", bd=2, command=lambda i=szukany.get("ID"): zapisz(plik, i))
                if szukany.tag == "AUTOR" or szukany.tag == "NAZWA":
                    
                    kolumna_nr=1
                elif szukany.tag == "TYTUL" or szukany.tag == "DOKUMENT":
                   
                    kolumna_nr=2
                if int(szukany.get("ID")) == q:
                    print (str(szukany.text))
                    search_1.grid( row=3, column=1)
                    search_2.grid( row=3, column=2)
                    if kolumna_nr==1:
                        search_1.insert(0,str(szukany.text))
                        zapis.grid(row=3, column=3)
                    else:
                         search_2.insert(0,str(szukany.text))
                         zapis.grid(row=3, column=3)
    
    button_menu1.grid( row=2, column=0)
    button_menu2.grid( row=2, column=1)
    button_menu3.grid( row=2, column=2)
    button_menu4 .grid(row=2, column=3)

    
    menu()
    
def zapisz(plik, i):
    print("Udałlo się")
    print (str(plik) + str(i))

def menu():
    #button1 = Button(okno, text="Utwórz księgozbiór",  bd=2, command=creating)
    button2 = Button(okno, text="Wyświetl księgozbiór",  bd=2, command=lambda:reading("","AUTOR","biblioteka.xml"))
    button3 = Button(okno, text="wyświetl czytelników",  bd=2, command=lambda:reading("","NAZWA", "czytelnicy.xml"))
  


    #button1.grid( row=0, column=0, pady=3)
    button2.grid (row=0, column=1, pady=3)
    button3.grid (row=0, column=2, pady=3)
   
    


menu()

okno.mainloop()
