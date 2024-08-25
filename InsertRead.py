from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the 
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # You must edit the connection variables below to reflect
        # your own instance of MongoDB!
        #
        # Connection Variables
        #
        USER = username # (BME 8/3/2024) Replaced static username with passed input from front end
        PASS = password # (BME 8/3/2024) Replaced static password with passed input from front end
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 30465
        DB = 'AAC'
        COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]
        
        try:
            client = MongoClient(f'mongodb://{USER}:{PASS}@{HOST}:{PORT}', serverSelectionTimeoutMS=5000)
            client.server_info()  # Trigger exception if cannot connect to server
            print("Connected to MongoDB server as " + str(USER))
        except Exception as e:
            print(f"An error occurred: {e}")
        
        

# Complete this create method to implement the C in CRUD. (BME 7/31/2024)
    def create(self, data):
        if data is not None:
            self.database.animals.insert_one(data)  # data should be dictionary
            createDone = True
        else:
            print("Nothing to save because data parameter is empty")
            createDone = False
        return createDone

# Create method to implement the R in CRUD. (BME 7/31/2024)
    def read(self, query):
        if query is not None:
            results = self.database.animals.find(query)
            return list(results)
        else:
            raise Exception("Nothing to read because data parameter is empty")
            
# Update method to implement the U in CRUD. (BME 7/31/2024)
    def update(self, query, updateVals):
        if query is not None:
            updateResult = self.collection.update_many(query, updateVals)
            numUpdates = updateResult.modified_count
            return numUpdates
        else:
            raise Exception("Nothing to update because data parameter is empty")
            
# Delete method to implement the D in CRUD. (BME 7/31/2024)
    def delete(self, query):
        if query is not None:
            deletion = self.collection.delete_many(query)
            numDeleted = deletion.deleted_count
            return numDeleted
        else:
            raise Exception("Nothing to delete because data parameter is empty")
