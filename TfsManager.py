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
        f = open('config.js', 'r')
        config = json.loads(f.read())
        if 'baseUrl' not in config or 'user' not in config\
            or 'token' not in config or 'projId' not in config:
            raise CommandException("Please provide the sufficient access info")
        self.assignedTo = "Tuyue Chen"
        self.sort = 'id'
        self.user = config['user']
        self.token = config['token']
        self.baseUrl = config['baseUrl']
        self.projId = config['projId']
        self.iteration = config['iteration']
    def __readStr (self,args, i):
        return i+1, args[i+1]
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
             if (args[i] == '-a'):
                 i, self.assignedTo = self.__readStr(args,i)
             if (args[i] == '-s'):
                 i, self.sort = self.__readStr(args,i)
             i+=1
                 

try:
    x = Argument(sys.argv)
    if x.mode == Mode.quick:
        ##Step1: get the query result
        url = "https://%s/DefaultCollection/%s/_apis/wit/wiql?api-version=1.0"%(x.baseUrl,x.projId)
        query  = "SELECT [System.Id], [System.Title],[System.State]   FROM WorkItems    WHERE [System.AssignedTo] = '%s' AND [System.IterationPath] Under '%s'"%(x.assignedTo, x.iteration)
        data = json.dumps({'query':query})
        request = urllib2.Request(url,data);
        request.add_header("Content-type","application/json")
        base64string = base64.encodestring('%s:%s'%(x.user,x.token)).replace('\n','')
        request.add_header("Authorization","Basic %s" % base64string)
        httpResult = urllib2.urlopen(request)
        responseData = json.loads(httpResult.read())
        ##Step2: get the item detail from the query result
        id_list = []
        for item in responseData["workItems"]:
            id_list.append(str(item["id"]))
        idStr = 'ids='+','.join(id_list)
        fieldStr = 'fields=System.Id,System.Title,System.State'
        apiStr = 'api-version=1.0'
        url2 = "https://%s/DefaultCollection/_apis/wit/WorkItems?%s&%s&%s"%(x.baseUrl,idStr,fieldStr,apiStr)
        request2 = urllib2.Request(url2);
        request2.add_header("Authorization", "Basic %s" % base64string)
        result = urllib2.urlopen(request2)
        responseData = json.loads(result.read())
        list = []
        for item in responseData["value"]:
        	list.append({'id':item["fields"]["System.Id"], 'state': item["fields"]["System.State"], 'title':item["fields"]["System.Title"]})
        from operator import itemgetter
        newlist = sorted(list, key=itemgetter(x.sort)) 
        for item in newlist:
        	print '%s\t %s\t%s' % (item["id"], item["state"].encode('utf-8').ljust(12), item["title"].encode('utf-8'))
except CommandException as e:
    print str(e)
