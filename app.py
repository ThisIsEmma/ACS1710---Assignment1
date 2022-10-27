from random import randint
from flask import Flask

app = Flask(__name__)

@app.route('/')
def homepage():
    """Shows a greeting to the user."""
    return 'Are you there, world? It\'s me, Ducky!'

@app.route('/animal/<users_animal>')
def favorite_animal(users_animal):
    """Display a message to the user that changes based on their favorite animal."""
    return f'Wow, {users_animal} is my favorite animal, too!'

@app.route('/dessert/<users_dessert>')
def favorite_dessert(users_dessert):
    return f'How did you know I liked {users_dessert}'

@app.route('/madlibs/<adjective>/<noun>')
def madlibs(adjective,noun):
    return f'I went to the store to purchase a {adjective} {noun}'

@app.route('/multiply/<number1>/<number2>')
def multiply(number1, number2):
    if number1.isdigit() == True and number2.isdigit() == True:
        return f'{number1} times {number2} is {int(number1) * int(number2)}'
    else:
        return f'Invalid inputs. Please try again by entering 2 numbers!'

@app.route('/sayntimes/<word>/<n>')
def sayntimes(word, n):
    message = ''
    if n.isdigit() == True:
        for i in range(int(n)):
            message += word + ' ' 
    else:
        message = 'Invalid input.Please try again by entering a word and a number !'

    return message

@app.route('/dicegame')
def dicegame():
    dice_roll = randint(1,6)
    if dice_roll == 6:
        return f'You rolled a {dice_roll}. You won!'
    else:
        return f'You rolled a {dice_roll}. You lost!'

if __name__ == '__main__':
    app.run(debug=True)

