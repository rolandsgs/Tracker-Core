import pymongo
import datetime

class User(object):

    def __init__(self, name, operation, computername, date, time):
        self.name = name
        self.created_at = datetime.datetime.utcnow()
        self.event = {'date':date,'computername':computername,'operation':operation,'time':time}
        if date == datetime.datetime.now().strftime('%d/%m/%Y') and operation == 'logon':
            self.active = 1
        else:
            self.active = 0

    def insert(self):
        user_returned = mydb['users'].find_one({"name": self.name})
        if not user_returned:
            mydb['users'].insert_one(self.insert_json())
        else:
            mydb['users'].update_one({"name": self.name},self.update_json())

    def insert_json(self):
        return {
            'name': self.name,
            'created_at': self.created_at,
            'active':self.active,
            'event':[{
                    'date': self.event['date'],
                    'time': self.event['time'],
                    'computername': self.event['computername'],
                    'operation':self.event['operation']
                    }  
            ]    
        }

    def update_json(self):
       return {
            "$set":{
                "active":self.active
            },
            "$push":{
                    'event':{
                            'date': self.event['date'],
                            'time': self.event['time'],
                            'computername': self.event['computername'],
                            'operation':self.event['operation']
                            }
                    }
        }  

# Inicia a insercao no banco com todos os dados ate a data atual
def create_file():
    print("Creating Database...")
    print("Inserting Users")
    with open('/mnt/tracker/logon.log') as file:
        a = file.readlines()
        mydb['register'].insert_one({'id':'linhas', 'number_lines':len(a)})
        for i in a:
            line = i.split(' ')
            if line[4] == '':
                user = User(line[1], line[0], line[2], line[3], line[5])
            else:
                user = User(line[1], line[0], line[2], line[3], line[4])
            user.insert()
    print("done!")

def update_file():
    print("Updating Registers")
    with open('/mnt/tracker/logon.log') as file:
        last_line = mydb['register'].find_one({'id':'linhas'})
        for _ in range(last_line['number_lines']):
            next(file)
        a = file.readlines()
        mydb['register'].update_one({'id':'linhas'}, {'$set':{'number_lines':len(a)+last_line['number_lines']}})
        for i in a:
            line = i.split(' ')
            if line[4] == '':
                user = User(line[1], line[0], line[2], line[3], line[5])
            else:
                user = User(line[1], line[0], line[2], line[3], line[4])
            user.insert()
    print("done!")


if __name__ == "__main__":
    print("Starting BD")
    myclient = pymongo.MongoClient("mongodb://db-tracker:27017/")
    mydb = myclient['trackerdb-dev']

    print("Initializing update")
    if mydb['users'].count_documents({}) == 0:
        create_file()
    else:
        update_file()

    with open('/mnt/tracker/logon.log') as f:
        s = len(f.readlines())
        print("Usuarios no arquivo de log: ", s)

    ll = mydb['register'].find_one({'id':'linhas'})
    print("Usuarios no banco tracker_db: ", ll['number_lines'])