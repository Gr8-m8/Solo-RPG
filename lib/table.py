from textefficiency import text
from saver import Saver
from table_items import *
import random as rng
import os
import json

class Table:
    def __init__(self, name, desc, items) -> None:
        self.name = name
        self.desc = desc
        self.items = items

    def Roll(self, amount):
        return [rng.choice(self.items) for i in range(amount)]

    def Display(self, name=True, desc=True, items=True):
        return f"{f"{self.name}" if name else ""}{f"'{self.desc}'\n" if desc else ""}{self.items}" #{f"{', '.join([item.Display(tags=False) for item in self.items])}" if items else ""}"

    def Load(self, name = None):
        Table.Load(self.name)
        
    def Save(self):
        Saver.Save(f"{Saver.PATH_TABLES}/{self.name}.json", self.toJSON())

    def toJSON(self):
        #print(self.items[0])
        return {self.name: [self.name, self.desc, [item.toJSON() for item in self.items]]}
    
    TABLES = []

    @staticmethod
    def Load(name):
        qimport = Saver.Load(f"{Saver.PATH_TABLES}/{name}.json")
        key = list(qimport.keys())[0]
        table = Table(name=qimport[key][0], desc=qimport[key][1], items=qimport[key][2])
        #print(f"{table.items[0]}")
        return table
        

    @staticmethod
    def LoadAll():
        tables = {}
        for table_name in os.listdir(Saver.PATH_TABLES):
            table = Table.Load(table_name.split('.')[0])
            tables[table_name.split('.')[0]] = table

        Table.TABLES = tables
        return tables


    @staticmethod
    def Template():
        name = "Table Name"
        desc = "Table Description"
        items = [
            Table_Item(name=f"Table Item {i} Name", desc=f"Table Item {i} Description", tags=[f"Table Item {i} tag 1", f"Table Item {i} tag 2", f"Table Item {i} tag 3"])
            for i in range(3)
            #Table_Item(name=f"Table Item {i} Name", desc=f"Table Item {i} Description", tags=[f"Table Item {i} tag 1", f"Table Item {i} tag 2", f"Table Item {i} tag 3"]),
            ]
        #print(items[0].name)
        return Table(name=name, desc=desc, items=items)
