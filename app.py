import os
from flask import Flask, send_from_directory, abort

app = Flask(__name__, static_url_path="")

@app.errorhandler(404)
def gerer_erreur(e):
    '''Quelle page renvoyer pour un message d'erreur'''
    return app.send_static_file('404.html'), 404

@app.route('/')
def accueil():
    return app.send_static_file('index.html')

@app.route('/LH<int:lh_number>/')
def accueil_lh(lh_number):
    return app.send_static_file(f"LH{lh_number}/index.html")


if __name__ == '__main__':
    app.run(debug=False,port=80,host="0.0.0.0") # Lance l'appli
