class Command:
    def __init__(self, command) -> None:
        self.command = command

    def Func(args = None):
        return args

    def isCommand(self, command):
        if command in self.command:
            return True
        else:
            return False

    
    COMMANDS = []

    @staticmethod 
    def Read():
        qinput = input("> ").split(' ')
        for command in Command.COMMANDS:
            if command.isCommand(qinput[0]):
                return command.Func(qinput[1:] if len(qinput)>1 else None)
            
        return None
                


