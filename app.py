import os
from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route('/')
def acceuil():
    return render_template('home.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/LH/<lh_number>')
def accueil_lh(lh_number):
    '''Renvoie la page d'accueil d'une lh, stockée dans templates/lh_number/'''
    return render_template(f'{lh_number}/articles/home.html')

@app.route('/LH/<lh_number>/<article>')
def un_article(lh_number,article):
    '''Affiche un article stocké dans templates/lh_number/'''
    return render_template(f'{lh_number}/articles/{article}.html')

# Pour accéder à l'accueil d'une LH: ip/LH/"numéro de la LH genre LH1"
# Pour un article de ce numéro: ip/LH/"numéro de la LH genre LH1"/"nom du fichier d'un article genre article_test"

if __name__ == '__main__':
    app.run(debug=False,port=80,host="0.0.0.0") # Lance l'appli
