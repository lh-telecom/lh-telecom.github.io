import os
from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.errorhandler(404)
def gerer_erreur(e):
    '''Quelle page renvoyer pour un message d'erreur'''
    return render_template('/404.html'), 404

@app.route('/')
def accueil():
    return render_template('home.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/LH/<lh_number>')
def accueil_lh(lh_number):
    '''Renvoie la page d'accueil d'une lh, stockée dans templates/lh_number/'''
    # on décompose le chemin d'accès en deux : le chemin du HTML à renvoyer, et le chemin complet pour savoir si le fichier existe.
    template_path = f'{lh_number}/articles/home.html'
    full_path = os.path.join(app.root_path, 'templates', template_path)
    if os.path.exists(full_path):
        return render_template(template_path)
    else: # techniquement c'est pas nécessaire de mettre else mais bon
        return render_template('/404.html'), 404

@app.route('/LH/<lh_number>/<article>')
def un_article(lh_number,article):
    '''Affiche un article stocké dans templates/lh_number/'''
    template_path = f'{lh_number}/articles/{article}.html'
    full_path = os.path.join(app.root_path, 'templates', template_path)
    if os.path.exists(full_path):
        return render_template(template_path)
    else: # techniquement c'est pas nécessaire de mettre else mais bon
        return render_template('/404.html'), 404

# Pour accéder à l'accueil d'une LH: ip/LH/"numéro de la LH genre LH1"
# Pour un article de ce numéro: ip/LH/"numéro de la LH genre LH1"/"nom du fichier d'un article genre article_test"

if __name__ == '__main__':
    app.run(debug=False,port=80,host="0.0.0.0") # Lance l'appli
