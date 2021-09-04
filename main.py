import requests
import json

from logging import debug
from flask import Flask
texto = 'Random Quote'
url = 'https://thesimpsonsquoteapi.glitch.me/quotes'

app = Flask(__name__)

@app.route("/")
def index():
    response = requests.get(url).json()
    quote = (response[0]["quote"])
    char = (response[0]["character"])
    image = (response[0]["image"])
    return f'''
<html>
<body>
  <div class="container-fluid">
    <img class="img-responsive center-block" src="https://cdn.glitch.com/3c3ffadc-3406-4440-bb95-d40ec8fcde72%2Fsimpsons.PNG?1497481539770" />
    <h1 class="center">{texto}</h1>
    <h1 class="center">{quote}</h1>
    <h1 class="center">{char}</h1>
    <img class="img-responsive center-block" src={image} />
  </div>
</body>
</html>    '''


if __name__ == "__main__":
    app.run(debug=True)