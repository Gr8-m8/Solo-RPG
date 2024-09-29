class Table_Item:
    def __init__(self, name, desc, tags, func = None) -> None:
        self.name = name
        self.desc = desc
        self.tags = tags
        self.func = func

    def Display(self, name=True, desc=True, tags=True):
        return f"{f"{self.name}" if name else ""}{f"{f"'{self.desc}'"}" if desc else ""}{f"{self.tags}" if tags else ""}"
    
    def toJSON(self):
        return [self.name, self.desc, self.tags]
