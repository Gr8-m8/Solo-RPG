from textefficiency import text
from saver import Saver
from table_items import *
import random as rng

class Table:
    def __init__(self, name, desc, items) -> None:
        self.name = name
        self.desc = desc
        self.items = items

    def Roll(self, amount):
        return [rng.choice(self.items) for i in range(amount)]

    def Display(self, name=True, desc=True, items=True):
        return f"{f"{self.name}" if name else ""}{f"'{self.desc}'\n" if desc else ""}{f"{', '.join([item.Display(tags=False) for item in self.items])}" if items else ""}"

    def Load(self):
        qimport = Saver.Load(f"{Saver.PATH}/{self.name}.json")
        print(qimport)
        
    def Save(self):
        Saver.Save(f"{Saver.PATH}/{self.name}.json", self.toJSON())

    def toJSON(self):
        return {self.name: [self.name, self.desc, [item.toJSON() for item in self.items]]}
    
    @staticmethod
    def Template():
        name = "Test Template"
        desc = "This table has items"
        items = [Table_Item(name="Item1", desc="This in an item", tags=['Item', 'Empty', 'Template'], func=print),
                 Table_Item(name="Item2", desc="This in an item", tags=["Item", "Empty", "Template"], func=print),
                 Table_Item(name="Item3", desc="This in an item", tags=["Item", "Empty", "Template"], func=print)]
        return Table(name=name, desc=desc, items=items)
