import json
import os

#simplify json save/load
class Saver:
    def __init__(self):
        os.makedirs(Saver.PATH_TABLES, exist_ok=True)

    PATH_TABLES = "Data/Tables/"
    
    @staticmethod
    def Save(path, content):
        #print(f"Saver {path}:{json.dumps(content)}")
        try:
            open(path, "x")
        except:
            pass

        try:
            save_file = open(path, "w")
            save_file.write(json.dumps(content))
            save_file.close()
        except:
            pass

    @staticmethod
    def Load(path):
        content = None
        try:
            save_file = open(path, "r")
            content = json.loads(save_file.read())
            save_file.close()
        except:
            try:
                open(path, "x")
            except:
                pass
            
        return content
    
Saver()