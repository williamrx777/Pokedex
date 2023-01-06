from flask import Flask,render_template,request,redirect,url_for
import requests

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        nome = request.form['nome']
        return redirect(url_for('pokedex', nome=nome))
    else:    
        return render_template('index.html')
@app.route('/pokedex/<nome>')
def pokedex(nome=None):        
    p = nome
    pokedex = requests.get(f'https://pokeapi.co/api/v2/pokemon/{p}')
    pokedex_view = pokedex.json()
    forms = pokedex_view['forms'][0]['name']
    sprites = pokedex_view['sprites']['front_default']
    abilities = pokedex_view['abilities'][0]['ability']['name']
    return render_template('pokedex.html', forms=forms,sprites=sprites, abilities=abilities )
if __name__=='__name__':
    app.run(Debug=True)