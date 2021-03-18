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

        #base label
        l1 = tk.Label(text="Amount:").grid(row=0, column=0)

        #base amount entry box
        amountEntry = tk.Entry()
        amountEntry.insert(tk.END, "7.00")
        amountEntry.grid(row=0, column=1)

        #base currency listbox
        baseList = tk.Listbox()
        baseList.grid(row=0, column=2)
        #populate baseList
        for x in CurrencyList:
            baseList.insert(tk.END, x)
        
        l2 = tk.Label(text=" to ").grid(row=0, column=3)

        #destination currency part
        l3 = tk.Label(text="0.00")
        l3.grid(row=0, column=4)

        dstList = tk.Listbox()
        dstList.grid(row=0, column=5)
        #populate dstList
        for currency in CurrencyList:
             dstList.insert(tk.END, currency)

        def getExchange():
            result = requests.get("https://v6.exchangerate-api.com/v6/{}/latest/{}".format(av.getExchangeRateKey(),"USD")).json()
            x = result["conversion_rates"]
            value = round(x["INR"]*float(amountEntry.get()),2)
            l3.config(text=value)

        calculate = tk.Button(text="Convert", command=lambda: getExchange())
        calculate.grid(row=0, column=6)

        window.mainloop()
        
Platform()