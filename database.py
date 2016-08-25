from pymongo import MongoClient
import datetime

client = MongoClient()
db = client.allspice
recipes = db.recipes

recipe = {
    'name':'Spaghetti',
    'description':'A wonderful spaghetti recipe',
    'ingredients':['spaghetti','sauce','basil'],
    'steps':['cook spaghetti','add sauce','add basil'],
    'tags':['pasta','quick','easy'],
    'notes':'Remember the spaghetti',
    'date': datetime.datetime.utcnow()
}

recipes.insert_one(recipe)

print(recipes.find_one())

def getRecipe():
    pass
