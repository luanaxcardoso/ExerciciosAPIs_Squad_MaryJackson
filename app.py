from flask import Flask, render_template
import urllib.request
import json
import ssl

ssl._create_default_https_context = ssl._create_unverified_context()  # Para evitar erros de certificado SSL

app = Flask(__name__)

@app.route('/')
def get_list_elements_page():
    url = "https://rickandmortyapi.com/api/character/"
    context = ssl._create_unverified_context()
    response = urllib.request.urlopen(url, context=context)
    data = response.read()
    characters_dict = json.loads(data)
    
    return render_template("characters.html", characters=characters_dict['results'])

@app.route('/profile/<id>')
def get_profile(id):
    url = "https://rickandmortyapi.com/api/character/" + id
    context = ssl._create_unverified_context()
    response = urllib.request.urlopen(url, context=context)
    data = response.read()
    character_dict = json.loads(data)
    
    return render_template("profile.html", profile=character_dict)

@app.route('/locations')
def get_location_list():
    url = "https://rickandmortyapi.com/api/location"
    context = ssl._create_unverified_context()
    response = urllib.request.urlopen(url, context=context)
    data = response.read().decode('utf-8')
    locations_dict = json.loads(data)
    
    return render_template("locations.html", locations=locations_dict['results'])

@app.route('/location/<id>')
def get_location(id):
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

    return render_template("location.html", location=location_dict, characters=characters_data)

@app.route('/episodes')
def get_episode_list():
    url = "https://rickandmortyapi.com/api/episode"
    context = ssl._create_unverified_context()
    response = urllib.request.urlopen(url, context=context)
    data = response.read().decode('utf-8')
    episodes_dict = json.loads(data)
    
    return render_template("episodes.html", episodes=episodes_dict['results'])

@app.route('/episode/<id>')
def get_episode(id):
    url = "https://rickandmortyapi.com/api/episode/" + id
    context = ssl._create_unverified_context()
    response = urllib.request.urlopen(url, context=context)
    data = response.read().decode('utf-8')
    episode_dict = json.loads(data)

    characters_data = []
    for character_url in episode_dict['characters']:
        with urllib.request.urlopen(character_url, context=context) as response:
            character_data = json.loads(response.read())
            characters_data.append(character_data)

    return render_template("episode.html", episode=episode_dict, characters=characters_data)


if __name__ == '__main__':
    app.run(debug=True)






