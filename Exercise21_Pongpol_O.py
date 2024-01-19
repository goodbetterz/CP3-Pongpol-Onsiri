from tkinter import *

def leftClickButton(event):
    bmi = round(float(textBoxWeight.get()) / (float(textBoxHeight.get())/100)**2, 2)
    print(bmi)
    if bmi > 30:
        labelResult.configure(text = f"{bmi} อ้วนมาก")
    elif bmi >= 25:
        labelResult.configure(text = f"{bmi} อ้วน")
    elif bmi >= 23:
        labelResult.configure(text = f"{bmi} น้ำหนักเกิน")
    elif bmi >= 18.6:
        labelResult.configure(text = f"{bmi} น้ำหนักปกติ")
    elif bmi < 18.6:
        labelResult.configure(text = f"{bmi} ผอมเกินไป")
    

MainWindow = Tk()

labelHeight = Label(MainWindow, text = "ส่วนสูง (cm.)")
labelHeight.grid(row = 0, column = 0)
textBoxHeight = Entry(MainWindow)
textBoxHeight.grid(row = 0, column = 1)

labelWeight = Label(MainWindow, text = "น้ำหนัก (kg.)")
labelWeight.grid(row = 1, column = 0)
textBoxWeight = Entry(MainWindow)
textBoxWeight.grid(row = 1, column = 1)

calculateButton = Button(MainWindow, text = "คำนวน BMI")
calculateButton.grid(row = 2, column = 0)
calculateButton.bind("<Button-1>", leftClickButton)

labelResult = Label(MainWindow, text = "ผลลัพธ์")
labelResult.grid(row = 2, column = 1)

MainWindow.mainloop()