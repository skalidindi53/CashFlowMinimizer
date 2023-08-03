import tkinter as tk
from tkinter import ttk



#functin to calculate the minimum index of an array
def minVal(arr):
    minVal = 0
    for i in range(len(arr)):
        if int(arr[i]) < int(arr[minVal]):
            minVal = i
    return minVal

#function to calculate the maximum index of an array
def maxVal(arr):
    maxVal = 0
    for i in range(len(arr)):
        if int(arr[i]) > int(arr[maxVal]):
            maxVal = i
    return maxVal

#function to return the minimum value of two numbers
def minof2(a, b):
    if a < b:
        return a
    else:
        return b
    
count = 0
#function to calculate the minimum cash flow
def minCashFlow(amount):
    global count
    
    mxCredit = maxVal(amount)
    mxDebit = minVal(amount)


    if (amount[mxCredit] == 0 and amount[mxDebit] == 0):
        return 0
    
    min = minof2(-amount[mxDebit], amount[mxCredit])
    amount[mxCredit] -= min
    amount[mxDebit] += min

    
    print("Person " + str(mxDebit) + " pays " + str(min) + " to " + "Person " + str(mxCredit))
    output = "Person " + str(mxDebit) + " pays " + str(min) + " to " + "Person " + str(mxCredit)
    output_label = tk.Label(root, text=output)
    #Place the widget in the bottom middle of the screen
    output_label.place(x = 260, y = 350 + count*20, width = 200)
    #output_label.grid(row=50+count, column=2)
    count+=1

    minCashFlow(amount)


root = tk.Tk()
root.geometry("700x500")

root.tk.call('source', 'forest-dark.tcl')
ttk.Style().theme_use('forest-dark')




def select_people():


    global num_people
    num_people = int(people_spinbox.get())
    
    global matrix
    matrix = []
    for i in range(num_people):
        global matrixRow
        matrixRow = []
        for j in range(num_people):
            matrixInput = tk.Entry(root, bg = "black", fg = "green")
            #use the place method to place the widgets as a grid
            matrixInput.place(x = 275 + j*50, y = 125 + i*30, width = 50)
            if(i == j):
                matrixInput.insert(0, 0)
            matrixRow.append(matrixInput)
        matrix.append(matrixRow)

    B2 = ttk.Button (root, text="Calculate", style= "Accent.TButton", command=storeMatrix)
    #Place the widget in the bottom middle of the screen
    B2.place(relx=0.5, rely=0.9, anchor="center")


#Read the input values from the matrix and store into a new matrix
def storeMatrix():
    global new_matrix
    new_matrix = []
    for i in range(num_people):
        global matrixRow
        matrixRow = []
        for j in range(num_people):
            matrixInput = matrix[i][j].get()
            matrixRow.append(matrixInput)
        new_matrix.append(matrixRow)
    print(new_matrix)
    print("Matrix stored")
    #Calculate the net amount for each person
    amount = [0 for i in range(num_people)]
    for i in range(num_people):
        for j in range(num_people):
            amount[i] += int(new_matrix[j][i]) - int(new_matrix[i][j])
    
    minCashFlow(amount)
    
    

# Creating a Label Widget
title = tk.Label(root, text="CashFlow Minimizer", font=("Helvetica", 16))
#Place the widget in the center of the screen
title.place(relx=0.5, rely=0.05, anchor="center")

people = tk.Label(root, text="How many people?")
#Place the widget below the title and slightly to the left
people.place(x= 150, y= 56)

# Creating a Spinbox Widget and padding it
people_spinbox = ttk.Spinbox(root, from_=2, to=10, width=2)
people_spinbox.place(x=280, y=53)


# Creating a Button Widget to save the number of people
people_button = ttk.Button(root, text="Submit",  command=select_people) 
people_button.place(x=370, y=53)



root.mainloop()

