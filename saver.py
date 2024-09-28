import json
import os

#simplify json save/load
class Saver:
    def __init__(self):
        os.makedirs("data/save", exist_ok=True)

    PATH_ALARMS = f"data/save/alarms.json"
    
    def save(self, path, content):
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

    def load(self, path):
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