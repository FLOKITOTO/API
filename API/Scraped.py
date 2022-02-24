# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import requests
import json


class Scraped:
    def __init__(self):
        self.headers = {'Content-Type': 'application/json'}
        self.urlConnectStr = "http://localhost:5001/mongodb"
        self.source = requests.get('https://pythonprogramming.net/parsememcparseface/')
        self.payload = json.dumps({
        "database":"local",
        "collection":"mozilla",
        "Document": self.read_dict()
        })

    def extract_brute(self):
        soup = bs(self.source.content, 'html.parser')
        table = soup.table
        print(table)
        #--------- Brut code ⇈ ------------
        return table

    def iterate_table(self):
        table = self.extract_brute()
        tableRows = table.find_all('tr')
        for tr in tableRows:
            print(tr.get_text())
            th = tr.find_all('th')
            row = [i.get_text() for i in th]
            print(row)
            #--------⇈ Parcours du tableau⇈----------------

    def read_dict(self):
        dfs = pd.read_html("https://pythonprogramming.net/parsememcparseface/",header=0)[0]
        data = dfs.to_dict()
        print(data)
        # -------⇈ ⇈ Insertion dans un dictionnaire pour pouvoir traiter la data ⇈ ⇈----------
        return data
    
    
    def response_payload(self):
        print(self.payload,'payload')
        response = requests.request("POST", self.urlConnectStr, headers=self.headers, data=self.payload)
        print(response.text)
    

execute = Scraped()
execute.extract_brute()
execute.iterate_table()
execute.read_dict()
execute.response_payload()