from flask import Flask, render_template
import urllib.request
import json 
import ssl 

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
    url = "https://rickandmortyapi.com/api/character/"+id #+id
    context = ssl._create_unverified_context()
    response = urllib.request.urlopen(url, context=context)
    data = response.read()
    dict = json.loads(data)
    
    return render_template("profile.html", profile=dict)

@app.route('/lista')
def get_list_elements():
    url = "https://rickandmortyapi.com/api/character/"
    context = ssl._create_unverified_context()

    try:
        response = urllib.request.urlopen(url, context=context)
        characters = response.read()
        dict = json.loads(characters)

        characters_list = []

        for character in dict['results']:
            character_data = {
                "name": character['name'],
                "status": character['status'],
                "species": character['species'],
            }
            characters_list.append(character_data)
        
        return {"characters": characters_list}
    except Exception as e:
        return {"error": str(e)}


@app.route('/locations')
def get_location_list():
    url = "https://rickandmortyapi.com/api/location"
    context = ssl._create_unverified_context()
    response = urllib.request.urlopen(url, context=context)
    data = response.read()
    dict = json.loads(data)
    
    return render_template("locations.html", locations=dict['results'])


@app.route('/episodes')
def get_episode_list():
    url = "https://rickandmortyapi.com/api/episode"
    context = ssl._create_unverified_context()
    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)
    
    return render_template("episodes.html", episodes=dict['results'])


if __name__ == '__main__':
    app.run(debug=True)


