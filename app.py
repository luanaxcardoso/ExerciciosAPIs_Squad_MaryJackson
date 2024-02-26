from flask import Flask, render_template
import urllib.request
import json
import ssl

ssl._create_default_https_context = ssl._create_unverified_context  # Para evitar errores de certificado SSL

app = Flask(__name__)

@app.route('/')
def get_list_elements_page():
    url = "https://rickandmortyapi.com/api/character/"
    context = ssl._create_unverified_context()
    response = urllib.request.urlopen(url, context=context)
    data = response.read()
    dict = json.loads(data)
    
    return render_template("characters.html", characters=dict['results'])

@app.route('/profile/<id>')
def get_profile(id):
    url = "https://rickandmortyapi.com/api/character/" + id
    context = ssl._create_unverified_context()
    response = urllib.request.urlopen(url, context=context)
    data = response.read()
    dict = json.loads(data)
    
    return render_template("profile.html", profile=dict)

@app.route('/lista')
def get_list_elements():
    url_characters = "https://rickandmortyapi.com/api/character/"
    url_locations = "https://rickandmortyapi.com/api/location"
    context = ssl._create_unverified_context()

    try:
        with urllib.request.urlopen(url_characters, context=context) as response:
            characters_data = response.read()
            characters_dict = json.loads(characters_data)

        with urllib.request.urlopen(url_locations, context=context) as response:
            locations_data = response.read().decode('utf-8')
            locations_dict = json.loads(locations_data)

        characters_list = []

        for character in characters_dict['results']:
            character_data = {
                "name": character['name'],
                "status": character['status'],
                "species": character['species'],
                "gender": character['gender']['name'],
                "origin": character['origin']['name']
            }
            characters_list.append(character_data)
        
        return render_template("lista.html", characters=characters_list, locations=locations_dict)
    except Exception as e:
        return {"error": str(e)}

@app.route('/locations')
def get_location_list():
    url = "https://rickandmortyapi.com/api/location"
    context = ssl._create_unverified_context()
    response = urllib.request.urlopen(url, context=context)
    data = response.read().decode('utf-8')
    dict = json.loads(data)
    
    return render_template("locations.html", locations=dict['results'])

@app.route('/id_location/<id>')
def get_id_location(id):
    url = "https://rickandmortyapi.com/api/location/" + id
    context = ssl._create_unverified_context()
    response = urllib.request.urlopen(url, context=context)
    data = response.read().decode('utf-8')
    location_dict = json.loads(data)

    
    characters_data = []
    for resident_url in location_dict['residents']:
        with urllib.request.urlopen(resident_url, context=context) as response:
            character_data = json.loads(response.read().decode('utf-8'))
            characters_data.append(character_data)

    return render_template("id_location.html", id_location=location_dict, characters=characters_data)

@app.route('/episodes')
def get_episode_list():
    url = "https://rickandmortyapi.com/api/episode"
    context = ssl._create_unverified_context()
    response = urllib.request.urlopen(url, context=context)
    data = response.read().decode('utf-8')
    dict = json.loads(data)
    
    return render_template("episodes.html", episodes=dict['results'])

if __name__ == '__main__':
    app.run(debug=True)








