import tkinter as tk
import sys
sys.path.insert(0,'/Users/ricks/Desktop/Projects')
from api_keys import apivalues as av
import requests

class Platform():
    def __init__(self):
        window = tk.Tk()
        window.title("Exchange Rates")
        CurrencyList = ["USD", "CAD", "INR", "EUR", "GBP"]

        #set the frame
        frame = tk.Frame(master=window)
        frame.grid(row=0,column=0)

        #base label
        l1 = tk.Label(master=frame,text="Amount:")
        l1.pack()

        #base amount entry box
        frame.grid(row=0, column=1)
        amountEntry = tk.Entry(master=frame)
        amountEntry.pack()

        #base currency listbox
        frame.grid(row=0, column=2)
        baseList = tk.Listbox(master=frame)
        baseList.pack()
        #populate baseList
        for currency in CurrencyList:
            baseList.insert(tk.END, currency)
        
        frame.grid(row=0,column=3)
        l2 = tk.Label(master=frame, text=" to ")
        l2.pack()

        #destination currency part
        frame.grid(row=0, column=4)
        l3 = tk.Label(master=frame, text="0.00")
        l3.pack()

        frame.grid(row=0, column=5)
        dstList = tk.Listbox(master=frame)
        dstList.pack()
        #populate dstList
        for currency in CurrencyList:
            dstList.insert(tk.END, currency)

        frame.grid(row=0, column=6)
        calculate = tk.Button(text="Convert")
        calculate.pack()

        window.mainloop()

    def getExchange(self, amount, base, dst):
         result = requests.get("https://v6.exchangerate-api.com/v6/{}/latest/{}".format(av.getExchangeRateKey(),"USD")).json()
         x = result["conversion_rates"]
         self.resultL.set(x["INR"]*5)
        

Platform()