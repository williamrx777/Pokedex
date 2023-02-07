from flask import Flask,render_template
from flask.globals import request
from models.pokedex import Pokedex
import requests
import json
app = Flask(__name__)

@app.route('/')
def index(): 
    return render_template('index.html')
@app.route('/buscar', methods=['GET','POST'])
def pokedex():        
    pokedex = Pokedex(request.form['nome'],['foto'],['moves'],['habilidade1'],['habilidade2'])
    try:
        res = json.loads(requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokedex.nome}").text)
        resposta = res['sprites']['front_default']
        moves = res['moves'][0]['move']['name']
        habilidade1 = res['abilities'][0]['ability']['name']
        habilidade2 = res['abilities'][1]['ability']['name']
        pokedex.foto = resposta
        pokedex.moves = moves
        pokedex.habilidade1 = habilidade1
        pokedex.habilidade2 = habilidade2
    except:
        return "pokemon não encontrado "

    return render_template('index.html',
    foto = pokedex.foto,
    nome = pokedex.nome,
    moves = pokedex.moves,
    habilidade1 = pokedex.habilidade1,
    habilidade2 = pokedex.habilidade2,
    )
if __name__=='__main__':
    app.run(debug=True)