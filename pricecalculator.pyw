import tkinter as tk

class GUI:

    def __init__(self):
        # Window Creation
        self.window = tk.Tk() 
        self.window.geometry("600x400") 
        self.window.title("New Parts Price Tool") 
        self.window.bind("<Return>", self.calculate) 
        
        # Title Header
        self.header = tk.Label(self.window, text="Enter Purchase Price", font=('Arial', 18))
        self.header.pack(pady=50)

        # User Entry Box
        self.entrybox = tk.Entry(self.window, font=('Arial', 18))
        self.entrybox.pack()

        # Error Message Label
        self.errormessage = tk.Label(self.window, text="", font=('Arial', 12))
        self.errormessage.pack()

        # Button Grid
        self.buttonframe = tk.Frame(self.window)
        self.buttonframe.columnconfigure(0, weight=1)
        self.submitbutton = tk.Button(self.buttonframe, text="Submit", width=7, font=('Arial', 18), command=self.calculate)
        self.submitbutton.grid(row=0, column=0)
        self.clearbutton = tk.Button(self.buttonframe, text="Clear", width=7, font=('Arial', 18), command=self.clearall)
        self.clearbutton.grid(row=0, column=1)
        self.buttonframe.pack()

        # Information Header
        self.header2 = tk.Label(self.window, pady=20, text="Recommended Price", font=('Arial', 18))
        self.header2.pack()

        # Output label
        self.answer = tk.Label(self.window, text="---", font=('Arial', 18))
        self.answer.pack()

        # Main Loop
        self.window.mainloop()

    def calculate(self, event=None):

        def round_to_nearest(num, base=5):
            # Format of ###.95
            return (base * round(num / base)) - 0.05
        
        self.userstr = self.entrybox.get()
        
        try:
            self.convert = float(self.userstr)
            self.errormessage["text"] = ""
        except ValueError:
            self.errormessage["text"] = "Error: Only Integers And Decimals Allowed" # Handles invalid user input
            self.answer["text"] = "---" # Reset answer label
            return

        self.calculation = self.convert + 0.3 # 30 cent transaction fee

        if self.convert < 75: # $7 shipping cost added if below $75
            self.calculation += 7

        # The following conditions check price points and apply profit and final value fees
        # Example: If price to purchase is under $50, the first if statement will trigger
        # The profit margin is a static $10, and final value fee is 12% (/ 0.88)
        if self.calculation <= 50:
            self.calculation = (self.calculation + 10) / 0.88 # $50 or less
        elif self.calculation > 50 and self.calculation <= 100: # $51 - $100
            self.calculation = (self.calculation + 20) / 0.88
        elif self.calculation > 100 and self.calculation <= 200: # $101 - $200
            self.calculation = (self.calculation * 1.25) / 0.88
        elif self.calculation > 200 and self.calculation <= 500: # $201 - $500
            self.calculation = (self.calculation * 1.2) / 0.88
        else:
            self.calculation = (self.calculation * 1.2) / 0.88 # More than $500
        
        self.calculation = round_to_nearest(self.calculation) # Calls Helper Function

        self.answer["text"] = self.calculation

    def clearall(self):
        '''Deletes Text From User Entry Box'''
        self.entrybox.delete(0, 'end') # Deletion from index 0 to end
        self.answer["text"] = "---" # Reset
        self.errormessage["text"] = "" # Reset

GUI() #Creates GUI Object