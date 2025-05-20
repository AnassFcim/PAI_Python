# API
🌐 Mais en général
Cette application Flask fournit un guide de voyage simplifié : l'utilisateur entre le nom d'une ville, et l'application affiche :

📍 ses coordonnées géographiques,

☁️ la météo actuelle,

🖼️ quelques photos représentatives.

🔧 Fonctionnalités principales
Chargement des clés API avec dotenvcontient les clés pour :
Le fichier .envcontient les clés pour :

Unsplash (images),

OpenWeather (météo),

OpenCage (géolocalisation).

Fonctions API externes :

get_city_info(city_name)→ récupère la latitude, la longitude et le nom complet de la ville.

get_weather(city_name)→obtenir la température et la description météo actuelle.

get_photos(city_name)→ récupère jusqu'à 3 images de la ville depuis Unsplash.

Itinéraires Flask :

/→ afficher le formulaire d'accueil ( index.html).

./travel(POST) → traite la ville soumise, récupère les infos, et affiche le tout dans page2.html.

Sécurité minimale :

Gestion des erreurs d'API via try/except.

Vérification si le champ de formulaire est vide.

✅ Technologies utilisées
Python, Flask

API externes : OpenCage, OpenWeather, Unsplash

)HTML via Jinja2 ( render_template)
