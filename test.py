import os
import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("597529bd5007460aa53a5f5d1f7d60c4")

location = "Paris"
url = f"https://api.opencagedata.com/geocode/v1/json?q=roma&key=597529bd5007460aa53a5f5d1f7d60c4"

response = requests.get(url)
data = response.json()

if data['results']:
    print("Latitude :", data['results'][0]['geometry']['lat'])
    print("Longitude :", data['results'][0]['geometry']['lng'])
else:
    print("Aucune donnée trouvée.")
