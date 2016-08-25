from flask import Flask
from flask import render_template
import database.py as db

app = Flask(__name__)

@app.route('/')
@app.route('/recipes')
def main():
    return render_template('main.html',recipe={'name':'Spaghetti'})

@app.route('/recipes/<int:recipe_id>')
def recipe():
    return render_template('recipe.html',recipe=db.getRecipe(recipe_id))

if __name__ == '__main__':
    app.run()
