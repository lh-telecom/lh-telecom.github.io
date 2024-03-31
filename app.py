import os
from flask import Flask, send_from_directory

app = Flask(__name__)

@app.errorhandler(404)
def gerer_erreur(e):
    '''Quelle page renvoyer pour un message d'erreur'''
    return app.send_static_file('404.html'), 404

@app.route('/')
@app.route('/home.html')
def accueil():
    return app.send_static_file('home.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/LH/<lh_number>')
def accueil_lh(lh_number):
    '''Renvoie la page d'accueil d'une lh, stockée dans templates/lh_number/'''
    # on décompose le chemin d'accès en deux : le chemin du HTML à renvoyer, et le chemin complet pour savoir si le fichier existe.
    path = f'{lh_number}/home.html'
    full_path = os.path.join(app.root_path, 'static', path)
    if os.path.exists(full_path):
        return app.send_static_file(path)
    else: # techniquement c'est pas nécessaire de mettre else mais bon
        return app.send_static_file('/404.html'), 404

@app.route('/LH/<lh_number>/<article>.html')
def un_article(lh_number,article):
    '''Affiche un article stocké dans templates/lh_number/'''
    path = f'{lh_number}/articles/{article}.html'
    full_path = os.path.join(app.root_path, 'static', path)
    if os.path.exists(full_path):
        return app.send_static_file(path)
    else: # techniquement c'est pas nécessaire de mettre else mais bon
        return app.send_static_file('/404.html'), 404

@app.route('/LH/<lh_number>/<article>/')
def un_article_htmlless(lh_number,article):
    '''Affiche un article stocké dans templates/lh_number/'''
    path = f'{lh_number}/articles/{article}.html'
    full_path = os.path.join(app.root_path, 'static', path)
    if os.path.exists(full_path):
        return app.send_static_file(path)
    else: # techniquement c'est pas nécessaire de mettre else mais bon
        return app.send_static_file('/404.html'), 404

# Pour accéder à l'accueil d'une LH: ip/LH/"numéro de la LH genre LH1"
# Pour un article de ce numéro: ip/LH/"numéro de la LH genre LH1"/"nom du fichier d'un article genre article_test"

if __name__ == '__main__':
    app.run(debug=False,port=8080,host="0.0.0.0") # Lance l'appli
