import tkinter as tk
import sys
sys.path.insert(0,'/Users/ricks/Desktop/Projects')
from api_keys import apivalues as av
import requests

class Platform():
    def __init__(self):
        window = tk.Tk()
        window.title("Exchange Rates")
        CurrencyList = ["USD", "CAD", "INR", "EUR", "GBP", "AUD","EGP", "BRL"]

        #base label
        l1 = tk.Label(text="Amount:").grid(row=0, column=0)

        #base amount entry box
        amountEntry = tk.Entry()
        amountEntry.insert(tk.END, "7.00")
        amountEntry.grid(row=0, column=1)

        #base currency listbox
        baseList = tk.Listbox(selectmode=tk.SINGLE, width=7, height=3, exportselection=False)
        baseList.grid(row=0, column=2, sticky=tk.W)
        baseScroll = tk.Scrollbar()
        baseScroll.grid(row=0, column=2, sticky=tk.E)
        #populate baseList
        for x in CurrencyList:
            baseList.insert(tk.END, x)
        
        #connect listbox with scroll
        baseList.config(yscrollcommand=baseScroll.set)
        baseScroll.config(command=baseList.yview)


        l2 = tk.Label(text=" to ").grid(row=0, column=3)

        #destination currency part
        l3 = tk.Label(text="0.00")
        l3.grid(row=0, column=4)

        dstList = tk.Listbox(selectmode=tk.SINGLE, width=7, height=3)
        dstList.grid(row=0, column=5, sticky=tk.W)
        dstScroll = tk.Scrollbar()
        dstScroll.grid(row=0, column=5, sticky=tk.E)
        #populate dstList
        for currency in CurrencyList:
             dstList.insert(tk.END, currency)

        #connect listbox with scroll
        dstList.config(yscrollcommand=dstScroll.set)
        dstScroll.config(command=dstList.yview)

        #function interacting with api to get exchange rates and calculate the transfer
        def getExchange():
            baseCurrency= baseList.get(baseList.curselection())
            dstCurrency = dstList.get(dstList.curselection())
            result = requests.get("https://v6.exchangerate-api.com/v6/{}/latest/{}".format(av.getExchangeRateKey(), baseCurrency)).json()
            x = result["conversion_rates"]
            value = round(x[dstCurrency]*float(amountEntry.get()),2)
            l3.config(text=value)

        #button to do the calculation
        calculate = tk.Button(text="Convert", command=lambda: getExchange())
        calculate.grid(row=0, column=6)

        window.mainloop()
        
Platform()