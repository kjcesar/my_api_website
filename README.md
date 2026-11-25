# API Website

A small Flask web app that consumes public APIs and displays the results with Bootstrap/Bootswatch.

## What it does

- `/` — landing page with a short project description.
- `/nasa_apod` — shows NASA's Astronomy Picture of the Day using the current WordPress APOD endpoint. If APOD returns a video, the page shows the poster image and a link to the APOD article.
- `/pokemon` — search a Pokémon by name using the public PokéAPI and show its data.

The old `api.nasa.gov/planetary/apod` legacy endpoint is no longer used. The current APOD endpoint does not require an API key, so this project no longer needs `NASA_KEY`.

## Stack

- Python 3.12
- Flask
- requests
- Bootstrap 5 with the Bootswatch **Brite** theme
- Gunicorn for production

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

Then open:

```text
http://127.0.0.1:5000/
```

## Deploy on Render

- **Build Command:** `pip install -r requirements.txt`
- **Start Command:** `gunicorn app:app`
- **Python Version:** set by `.python-version` (`3.12`)

After a deploy, go to `/nasa_apod` to see the NASA picture or video poster of the day.

## Notes

- `.env` is ignored and not committed.
- `uv.lock` is kept for dependency reproducibility.
