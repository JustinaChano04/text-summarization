from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import pdb



# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
my_db = client['financial_terms']

# accessing a collection
vocab_table = my_db['vocab_table']
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)


def db_insert(word):
    record={
        'word': 'turn',
        'definition': "f;lasdjfsdakl;fjdas;fsad"
    }
    rec = vocab_table.insert_one(record)

    
if __name__ == "__main__":
    # db_create()
    db_insert('word')
