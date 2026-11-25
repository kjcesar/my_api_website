import requests
from flask import Flask, render_template, request

from utils.helpers import get_pokemon

# from datetime import datetime

# NASA = "https://api.nasa.gov/planetary/apod" ## legacy
NASA = "https://science.nasa.gov/wp-json/wp/v2/apod-basic"


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/nasa_apod")
def example():
    # api_key = os.getenv("NASA_KEY") legacy
    # start_date = "2025-10-01"  # YYYY-MM-DD
    # end_date = datetime.today().date()
    parameter = {
        "per_page": 1,
        "_fields": "date,title,media_type,url,hdurl,explanation,credit,alt",
    }
    # parameter = {"api_key": api_key, "count": 1} # legacy
    print("before requests")
    response = requests.get(url=NASA, params=parameter)
    response.raise_for_status()

    data = response.json()[0]
    print(data)
    print(type(data))

    # message = {
    #     "message": "esta es una página que mostrara la imagen del dia de la nasa"
    # }
    # nasa devuelve una lista con un objeto dentro
    return render_template("nasa.html", apod=data)
    # return jsonify(data)


@app.route("/pokemon", methods=["GET", "POST"])
def pokemon():
    pokemon_data = None
    error = None

    if request.method == "POST":
        name = request.form.get("pokemon_name")
        if name:
            try:
                pokemon_data = get_pokemon(name)
            except (requests.RequestException, ValueError) as exc:
                error = f"could not find pokemon '{name}': {exc}"

    return render_template("pokemon.html", pokemon=pokemon_data, error=error)


if __name__ == "__main__":
    app.run(debug=True)
