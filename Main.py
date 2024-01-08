import tkinter
import openpyxl
import Menu

excelFile = openpyxl.load_workbook("quiz.xlsx")  # Loading a excel file to python
sh = excelFile.active

root = tkinter.Tk()
root.title("QUIZGAME")
root.geometry("300x250")

Menu.Menu(root, sh)

root.mainloop()
