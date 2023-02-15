from flask import Flask
from random import randint

app = Flask(__name__)


@app.route("/")
def start_page():
    return "<h1 style='max-width: 60ch; margin: auto; " \
           "margin-top: 25px; font-family: Georgia, serif; " \
           "text-align: center;'>Guess a number between 1 and 9!</h1>" \
           "<p style='text-align: center'>Enter /guess/your_number in the URL above</p>" \
           "<img style='display: block;margin-top: 25px; margin-left: auto; margin-right: auto; width: 50%;'" \
           " src='https://media.giphy.com/media/l378khQxt68syiWJy/giphy.gif'>"


number = randint(1, 9)
print(f"The number is: {number}")


@app.route(f"/guess/{number}")
def correct_guess():
    return f"<h1 style='color: green; max-width: 60ch; margin: auto; " \
           "margin-top: 25px; font-family: Georgia, serif; " \
           "text-align: center;'>You found me!<br>" \
           f"{number} was the number.</h1>" \
           f"<img style='display: block;margin-top: 25px; margin-left: auto; margin-right: auto; width: 50%;'" \
           f"src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>" \



@app.route("/guess/<incorrect_number>")
def incorrect_guess(incorrect_number):
    if int(incorrect_number) < number:
        return f"<h1 style='color: red; max-width: 60ch; margin: auto; " \
           "margin-top: 25px; font-family: Georgia, serif; " \
           "text-align: center;'>Too low, try again!</h1>" \
           f"<img style='display: block;margin-top: 25px; margin-left: auto; margin-right: auto; width: 50%;'" \
           f"src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>"
    else:
        return f"<h1 style='color: brown; max-width: 60ch; margin: auto; " \
           "margin-top: 25px; font-family: Georgia, serif; " \
           "text-align: center;'>Too high, try again!</h1>" \
           f"<img style='display: block;margin-top: 25px; margin-left: auto; margin-right: auto; width: 50%;'" \
           f"src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>"


if __name__ == "__main__":
    app.run(debug=True)
