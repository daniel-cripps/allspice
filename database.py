from pymongo import MongoClient
from bson.objectid import ObjectId
import datetime
import sys

client = MongoClient()
db = client.allspice
recipes = db.recipes

# recipe = {
#     'name':'Spaghetti',
#     'description':'A wonderful spaghetti recipe',
#     'ingredients':['spaghetti','sauce','basil'],
#     'steps':['cook spaghetti','add sauce','add basil'],
#     'tags':['pasta','quick','easy'],
#     'notes':'Remember the spaghetti',
#     'date': datetime.datetime.utcnow()
# }
# recipes.insert_one(recipe)
# print(recipes.find_one())

def getRecipe(rid):
    recipe = recipes.find_one({'_id': ObjectId(rid)})
    return recipe

def AddRecipe(name, description, ingredients, steps, tags, notes):
    r = {
        'name':name,
        'description':description,
        'ingredients':ingredients,
        'steps':steps,
        'tags':tags,
        'notes':notes
    }
    recipes.insert_one(r)
