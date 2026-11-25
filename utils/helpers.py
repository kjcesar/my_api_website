# utils/helpers.py
import requests

cache = {}


def get_pokemon(name):
    name = name.lower()
    if name in cache:
        return cache[name]

    url = f"https://pokeapi.co/api/v2/pokemon/{name}"
    r = requests.get(url, timeout=10)
    r.raise_for_status()
    data = r.json()

    cache[name] = data
    return data


def greet(name):
    return f"Hola, {name}!"
