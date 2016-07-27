import urllib2, base64, sys, json

class CommandException(Exception):
    pass

class Mode:
    quick = 1
    detail = 2


class Argument:
    tickets = []
    baseUrl = ""
    user = ""
    token = ""
    mode = Mode.quick
    def __readConfig(self):        
        f = open('config.js', 'r');
        config = json.loads(f.read())
        if 'baseUrl' not in config or 'user' not in config\
            or 'token' not in config or 'projId' not in config:

            raise CommandException("Please provide the sufficient access info")
        self.user = config['user']
        self.token = config['token']
        self.baseUrl = config['baseUrl']
    def __readStr (self,args, i):
        args[i]
        return i+1
    def __readNums (self, args, i):
        nums = [];
        for index in range(i+1, len(args)):
            if(args[index][0] == '-'):
                break
            try:
                nums.append(int(args[index]))
            except Exception as e:
                raise CommandException("Please provide the number")
            i+=1
        return i,nums   
    def __init__(self, args):
        self.__readConfig()
        i = 1
        while i < len(args):
             if (args[i] == '-t'):
                 self.mode = Mode.detail
                 i, self.tickets = self.__readNums(args,i)
                 break;
             if (args[i] == '-l'):
                 self.mode = Mode.quick        
             i+=1
                 

try:
    x = Argument(sys.argv)
    if x.mode == Mode.t
except CommandException as e:
    print str(e)
