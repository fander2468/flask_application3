from flask import render_template, request, flash
import requests
from .import bp as main
from flask_login import login_required


# used to display pokemon data
@main.route('/pokemon', methods=['GET', 'POST'])
@login_required
def pokemon():
    if request.method == 'POST':
        name = request.form.get('name')
        url = f'https://pokeapi.co/api/v2/pokemon/{name}'
        response = requests.get(url)
        if not response.ok:
            # return -1
            flash("Uh-oh something went wrong!", "danger")
            render_template("pokemon.html.j2")
        else:
            data = response.json()
            if not data:
                flash(f"There is no Pokemon info for {name}, check the spelling", "warning")
                return render_template("pokemon.html.j2")
                # name, atleast one ability's name, base_experience, and 
                # the URL for its sprite
            complete_pokemon = []
            char_dict = {
                    "Name":data['forms'][0]['name'],
                    "Ability":data['abilities'][0]['ability']['name'],
                    "Base Experience":data['base_experience'], 
                    "Sprite URL":data['sprites']['front_shiny']
                    }
            complete_pokemon.append(char_dict)
            return render_template('pokemon.html.j2', pokemon=complete_pokemon)    
    return render_template("pokemon.html.j2")