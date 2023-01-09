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
    pokedex = Pokedex(request.form['nome'].lower(),"")
    try:
        res = json.loads(requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokedex.nome}").text)
        resposta = res['sprites']
        resposta = resposta['front_default']
        pokedex.foto = resposta
        
    except:
        return "pokemon não encontrado "

    return render_template('index.html',
    foto = pokedex.foto,
    nome = pokedex.nome 
    )
if __name__=='__name__':
    app.run(Debug=True)