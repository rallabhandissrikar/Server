from pymongo import MongoClient

client = MongoClient("mongodb://mongo:jUKxDHvBcGwJkP4fgXzJ@containers-us-west-45.railway.app:7677")

def add_Single_Data(database:str, collection:str, data:dict):
    tempDatabase = client[database]
    tempCollection = tempDatabase[collection]
    data_insert_ID = tempCollection.insert_one(data).inserted_id
    return data_insert_ID

def add_multiple_Data(database:str, collection:str, data:list):
    tempDatabase = client[database]
    tempCollection = tempDatabase[collection]
    data_insert_ID = tempCollection.insert_many(data).inserted_ids
    return data_insert_ID

def get_single_Data(database:str, collection:str, filter:dict):
    tempDatabase = client[database]
    tempCollection = tempDatabase[collection]
    tempData = tempCollection.find_one(filter=filter)
    if tempData != None:
        tempData.pop('_id')
    return tempData

def get_complete_Data_Collection(database:str, collection:str):
    tempDatabase = client[database]
    tempCollecion = tempDatabase[collection]
    rawData = tempCollecion.find({})
    tempData = []
    for x in rawData:
        x.pop("_id")
        tempData.append(x)
    if tempData == [] :
        return None
    else : 
        return 

def update_single_Doccument(database:str, collection:str, filter:dict, updateDict:dict):
    tempDatabase = client[database]
    tempCollection = tempDatabase[collection]
    updateStatus = tempCollection.update_one(filter=filter, update={"$set":updateDict})
    return updateStatus

    
def find_User(username:str):
    data = get_single_Data(database="Users", collection="Users Collection", filter={"name" : username})
    if data == None :
        return "no data"
    else : 
        return data
    
def create_User(name:str, password:str, head_user:bool):
    if name==password==0 or head_user == None:
        raise TypeError('empty objects given')
    else : 
        data = {
            "name" : name,
            "password" : password,
            "head_user" : head_user
        }
    
    tempData = get_single_Data("Users", "Users Collection", {"name" : data['name']})
    if tempData == None:
        postID = add_Single_Data(database="Users", collection="Users Collection", data=data)
        return True
    else : 
        return False

def update_User_data(username:str, password:str, change_password:str, change_headuser:bool):
    if len(username)!=0 and len(password)!=0 and len(change_password) != 0 and change_headuser!=None:
        dat = {
            "name" : username,
            "password" : password
        }
        tempData = get_single_Data("Users", "Users Collection", {"name" : username})
        if tempData == None:
            return False
        else :
            if tempData['name'] == username and tempData['password'] == password:
                update_single_Doccument("Users", "Users Collection", {"name" : username}, {"password" : change_password, "head_user" : change_headuser})
            else :
                return False
    else :
        return False