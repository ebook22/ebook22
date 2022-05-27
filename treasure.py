from tkinter import Tk, Button, Label, StringVar, Frame
import random
from tkinter.ttk import Combobox


class Starter(Tk):

    def game(self, sizer):
        self.label.destroy()
        self.combo.destroy()
        self.button.destroy()
        self.title(f'Treasure Island {sizer}')
        siz = 130*int(sizer[0])
        self.geometry(f"{siz}x{siz}")
        self.resizable(False, False)

        self.frame1 = Frame(self, relief='sunken', width=3)
        self.frame1.grid(column=0, row=0, columnspan=int(sizer[0])-1)
        self.label1 = Label(self.frame1, text="Welcome to the Treasure Island!\n Your goal is to find treasure.\n Use metal detector\n"
                                              "Blue field - You are here. Pink field - You can go there\n"
                                              "Yellow field - You found a treasure!")
        self.label1.grid(column=0, row=0, columnspan=int(sizer[0])-2)

        self.info_button = Button(self, text="CLOSE", command=lambda: self.transfer(2))
        self.info_button.grid(column=int(sizer[0])-1, row=0)
        row = 0
        col = 0
        self.buttonx = []
        hidden = [int(sizer[0])-1, int(sizer[0])-1]
        while hidden == [int(sizer[0])-1, int(sizer[0])-1]:
            hidden = [random.randint(0, int(sizer[0])-1), random.randint(0, int(sizer[0])-1)]
        curr = [int(sizer[0]), int(sizer[0])]
        for q in range(int(sizer[0])**2):
            if q != 0 and q % int(sizer[0]) == 0:
                row += 1
            if col == int(sizer[0]):
                col = 0

            self.buttonx.append(Button(self, bg="gray", text=f'AREA {q+1}', width=14,
                                  height=5, state="disabled"))
            if row == curr[0]-2 and col == curr[1]-1:
                self.buttonx[q].configure(state="active", bg="#FFDDEE", activebackground="#FFDDEE", command=lambda: self.move
                (row-1, col-1, hidden, sizer[0]))
            elif col == curr[1]-2 and row == curr[0]-1:
                self.buttonx[q].configure(state="active", bg="#FFDDEE", activebackground="#FFDDEE", command=lambda: self.move
                (col-1, row-1, hidden, sizer[0]))
            if row == curr[1]-1 and col == curr[0]-1:
                self.buttonx[q].configure(bg="blue", foreground="black", text="You're here")
            self.buttonx[q].grid(row=row+1, column=col)
            col += 1

    def move(self, row, col, hidden, rozmiar):

        if row == hidden[0] and col == hidden[1]:
            self.label1.configure(text="CONGRATULATIONS!\n You found the treasure!!!")
            self.buttonx[int(row*int(rozmiar)+col)].configure(bg="yellow", activebackground="yellow")
        else:
            if hidden[0]-row < 0:
                if hidden[0]-row > -2:
                    self.label1.configure(text="Metal detector points strongly to the north...\n")
                else:
                    self.label1.configure(text="Metal detector points faintly to the north...\n")
            else:
                if hidden[0]-row == 0:
                    self.label1.configure(text="Metal detector points in line N-S\n")
                elif hidden[0]-row > 1:
                    self.label1.configure(text="Metal detector points faintly to the south...\n")
                else:
                    self.label1.configure(text="Metal detector points strongly to the south...\n")
            if hidden[1]-col < 0:
                if hidden[1]-col > -2:
                    self.label1['text'] += "Metal detector points strongly to the west...\n"
                else:
                    self.label1['text'] += "Metal detector points faintly to the west...\n"
            else:
                if hidden[1] - col == 0:
                    self.label1['text'] += "Metal detector points in line W-E\n"
                elif hidden[1]-col > 1:
                    self.label1['text'] += "Metal detector points faintly to the east...\n"
                else:
                    self.label1['text'] += "Metal detector points strongly to the east...\n"
            active_areas = [[row-1, col], [row+1, col], [row, col-1], [row, col+1]]
            new_row = 0
            new_col = 0
            for q in range(int(rozmiar)**2):
                if q != 0 and q % int(rozmiar) == 0:
                    new_row += 1
                if new_col == int(rozmiar):
                    new_col = 0
                if [new_row, new_col] in active_areas:
                    self.buttonx[q].configure(state="active", text=f'AREA {q}', bg="#FFDDEE", activebackground="#FFDDEE", command=lambda new_col=new_col, new_row=new_row: self.move
                (new_row, new_col, hidden, rozmiar))
                else:
                    self.buttonx[q].configure(bg="gray", text=f'AREA {q}', state='disabled')
                new_col += 1
            self.buttonx[int(row * int(rozmiar) + col)].configure(bg="blue", activebackground="blue", text="You're here", state='disabled')

    def transfer(self, cout):
        if cout == 2:
            app.destroy()

        else:
            self.app2 = self.game(self.combo.get())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title('Treasure Island')
        self.geometry("300x100")
        self.resizable(False, False)
        # The Label widget
        self.label = Label(self, text='Please select the size of the Treasure Island')
        self.label.pack(fill='x', padx=10)
        # scroll-up menu
        self.sizes = StringVar(self)
        self.combo = Combobox(self, width=10, textvariable=self.sizes)
        self.combo['values'] = ('3 x 3', '4 x 4', '5 x 5', '6 x 6', '7 x 7', '8 x 8', '9 x 9')
        self.combo.current(0)
        self.combo.pack()

        # The button widget
        # self.button = Button(self, text='Submit', command=lambda: Game(self.combo.get()))
        self.button = Button(self, text='Submit', command=lambda: Starter.transfer(self, 1))
        self.button.pack(padx=10, pady=3)


if __name__ == '__main__':
    app = Starter()
    app.mainloop()
