from flask import Flask, render_template, request, jsonify
import os
import requests
from dotenv import load_dotenv

# Charger les variables d'environnement
load_dotenv()

app = Flask(__name__)

# Clés API
#Récupère les clés API à partir des variables d'environnement.

#Unsplash pour les photos, OpenWeather pour la météo et OpenCage pour la géolocalisation.
UNSPLASH_API_KEY = os.getenv("UNSPLASH_API_KEY")
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")
OPENCAGE_API_KEY = os.getenv("OPENCAGE_API_KEY")

#Fonction pour obtenir les informations de la Ville

def get_city_info(city_name):
    try:
        url = f"https://api.opencagedata.com/geocode/v1/json?q={city_name}&key={OPENCAGE_API_KEY}"
        response = requests.get(url)
        data = response.json()
        if 'results' in data and len(data['results']) > 0:
            city_info = data['results'][0]['formatted']
            latitude = data['results'][0]['geometry']['lat']
            longitude = data['results'][0]['geometry']['lng']
            return {"name": city_info, "latitude": latitude, "longitude": longitude}
        else:
            return {"error": f"Aucune donnée trouvée pour la ville '{city_name}'."}
    except Exception as e:
        return {"error": f"Erreur lors de la récupération des informations sur la ville: {str(e)}"}


#Fonction pour obtenir la météo
def get_weather(city_name):
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={OPENWEATHER_API_KEY}&units=metric"
        response = requests.get(url)
        data = response.json()
        if data.get("cod") != 200:
            return {"error": f"Erreur météo : {data.get('message', 'Ville non trouvée')}"}
        return {"temperature": data["main"]["temp"], "description": data["weather"][0]["description"]}
    except Exception as e:
        return {"error": f"Erreur lors de la récupération des données météo : {str(e)}"}


#Fonction pour obtenir des photos
def get_photos(city_name):
    try:
        url = f"https://api.unsplash.com/search/photos?query={city_name}&client_id={UNSPLASH_API_KEY}"
        response = requests.get(url)
        data = response.json()
        if data.get("results"):
            return [photo["urls"]["regular"] for photo in data["results"][:3]]
        return ["Aucune photo trouvée"]
    except Exception as e:
        return {"error": f"Erreur lors de la récupération des photos : {str(e)}"}

#Itinéraire pour afficher la page d'accueil ( index.html).
@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/travel', methods=['POST'])
def travel_guide():
    city_name = request.form.get("city")
    if not city_name:
        return jsonify({"error": "Veuillez fournir un nom de ville"}), 400
    city_info = get_city_info(city_name)
    weather = get_weather(city_name)
    photos = get_photos(city_name)
    return render_template('page2.html', city_info=city_info, weather=weather, photos=photos)


if __name__ == '__main__':
    app.run(debug=True)