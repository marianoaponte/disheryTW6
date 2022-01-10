from pymongo import MongoClient
import certifi

# connection to cluster
connection_string = "mongodb+srv://admin:12345@disherydb.3ufhz.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
cluster = MongoClient(connection_string, tlsCAFile=certifi.where())

# connection to dbs
recipes_db = cluster["recipesDB"]
users_db = cluster["usersDB"]

# connection to collections
recipes_col = recipes_db["recipesCOL"]
users_col = users_db["usersCOL"]
