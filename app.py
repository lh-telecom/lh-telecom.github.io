import os
from flask import Flask, send_from_directory, abort

app = Flask(__name__)

@app.errorhandler(404)
def gerer_erreur(e):
    '''Quelle page renvoyer pour un message d'erreur'''
    return app.send_static_file('404.html'), 404

@app.route('/')
@app.route('/index.html')
def accueil():
    return app.send_static_file('index.html')

@app.route('/LH/<lh_number>')
def accueil_lh(lh_number):
    '''Renvoie la page d'accueil d'une lh, stockée dans templates/lh_number/'''
    # on décompose le chemin d'accès en deux : le chemin du HTML à renvoyer, et le chemin complet pour savoir si le fichier existe.
    path = f'{lh_number}/index.html'
    return app.send_static_file(path)

@app.route('/LH/<lh_number>/<article>.html')
def un_article_htmlless(lh_number,article):
    '''Affiche un article stocké dans templates/lh_number/'''
    path = f'{lh_number}/articles/{article}.html'
    return app.send_static_file(path)

# Pour accéder à l'accueil d'une LH: ip/LH/"numéro de la LH genre LH1"
# Pour un article de ce numéro: ip/LH/"numéro de la LH genre LH1"/"nom du fichier d'un article genre article_test"

if __name__ == '__main__':
    app.run(debug=False,port=80,host="0.0.0.0") # Lance l'appli
