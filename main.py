import tkinter as tk
import sys
sys.path.insert(0,'/Users/ricks/Desktop/Projects')
from api_keys import apivalues as av
import requests

class Platform():
    def __init__(self):
        window = tk.Tk()
        window.title("Exchange Rates")

        # l1 = tk.Label(text="Amount:").pack()

        # e1 = tk.Entry().pack()


        baseLstBox = tk.Listbox(height=5, width=8)
        baseScroll = tk.Scrollbar(baseLstBox, command= baseLstBox.yview)
        baseLstBox.configure(yscrollcommand = baseScroll.set)
        baseLstBox.pack(side="left")
        baseScroll.pack(side="right", fill="y")
        
        
        baseLstBox.insert(1,"USD")
        baseLstBox.insert(2,"CAD")
        baseLstBox.insert(3,"INR")
        baseLstBox.insert(4,"EUR")
        baseLstBox.insert(5,"GBP")
        baseLstBox.insert(6,"AMD")
        baseLstBox.insert(7,"XCD")
        baseLstBox.insert(8,"AOA")
        baseLstBox.pack()

        
        
        

        # l2 = tk.Label(text=" to ").grid(row=0, column=3)

        # dstLstBox = tk.Listbox()
        # dstLstBox.grid(row=0, column=4)
        # dstLstBox.insert(1,"USD")
        # dstLstBox.insert(2,"CAD")
        # dstLstBox.insert(3,"INR")
        # dstLstBox.insert(4,"EUR")
        # dstLstBox.insert(5,"GBP")

        # dstScroll = tk.Scrollbar(dstLstBox, orient="vertical")
        # dstScroll.pack()

        # resultL = tk.Label(text="0.0")
        # resultL.grid(row=0,column=5)

        # calculate = tk.Button(text="Convert")
        # calculate.grid(row=1, column=3)

        window.mainloop()

    def getExchange(self, amount, base, dst):
         result = requests.get("https://v6.exchangerate-api.com/v6/{}/latest/{}".format(av.getExchangeRateKey(),"USD")).json()
         x = result["conversion_rates"]
         self.resultL.set(x["INR"]*5)
        

Platform()