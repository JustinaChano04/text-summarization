from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import pdb
from dotenv import load_dotenv
import os


load_dotenv()
url= os.getenv("MONGO_URL")
print(url)
# Create a new client and connect to the server
client = MongoClient(url, server_api=ServerApi('1'))
my_db = client['financial_terms']

# accessing a collection
vocab_table = my_db['vocab_table']
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)


# inserting new vocabulary into the database
def db_insert(word):    
    rec = vocab_table.replace_one(word, word, upsert=True)

# retrieve all vocabulary from the database  
def db_retrieve_all():
    all_cursors = vocab_table.find()
    entries = []
    for d in all_cursors:
        term_dict = {}
        term_dict['word'] = d['word']
        term_dict['definition'] = d['definition']
        entries.append(term_dict)
    return entries
 
if __name__ == "__main__":
    # db_insert('word')
    a = db_retrieve_all()
    
