import tkinter
import random


class Quiz:
    def __init__(self, root, sh):
        entry = tkinter.Entry(root, width=15, font=("Arial", 11))
        entry.place(x=150, y=90, anchor="center")

        buttonNext = tkinter.Button(
            root,
            text="Next",
            padx=30,
            command=lambda: Quiz.change_word(self, sh, labelWordPl, labelresult, entry),
        )
        buttonBack = tkinter.Button(root, text="Back", padx=30)
        buttonCheck = tkinter.Button(
            root,
            text="Check",
            padx=10,
            command=lambda: Quiz.read_Eword_typed(self, entry, labelresult),
        )

        buttonNext.place(x=250, y=190, anchor="center")
        buttonBack.place(x=50, y=190, anchor="center")
        buttonCheck.place(x=250, y=90, anchor="center")

        labelWordPl = tkinter.Label(root)
        labelWordEng = tkinter.Label(root, text="Po angielsku:")
        labelresult = tkinter.Label(root)

        labelWordPl.place(x=150, y=60, anchor="center")
        labelWordEng.place(x=50, y=90, anchor="center")
        labelresult.place(x=150, y=110, anchor="center")

        Quiz.change_word(self, sh, labelWordPl, labelresult, entry)

    def change_word(self, sh, label, label2, entry):
        i = random.randint(2, 7)
        Pword = sh.cell(row=i, column=1)
        self.Eword = sh.cell(row=i, column=2)
        label.config(text=Pword.value)
        label2.config(text=" ")
        entry.delete(0, tkinter.END)

    def read_Eword_typed(self, entry, label):
        Ewordtyped = entry.get().lower()
        if self.Eword.value.lower() == Ewordtyped:
            label.config(text="Git!")
        else:
            label.config(text=self.Eword.value.lower())
        print(Ewordtyped)
