import json

def getRecipe()


def makeRecipe(name,ingredients,steps,notes):
    data = {
        'name':name,
        'ingredients':ingredients,
        'steps':steps,
        'notes':notes
    }
    return json.dumps(data)

def openRecipe(recipe):
    return json.load(data)

def main():
    example = makeRecipe('Spaghetti',['Pack of Spaghetti','Sauce','Coriander'],'Cook Spaghetti','Remember the Spaghetti')
    print(example)

if __name__ == '__main__':
    main()
