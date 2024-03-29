from flask import Flask, render_template

app = Flask(__name__)

@app.route('/LH/<lh_number>')
def acceuil_lh(lh_number):
    '''Renvoie la page d'acceuil d'une lh, stockée dans templates/lh_number/'''
    return render_template(f'{lh_number}/home.html')

@app.route('/LH/<lh_number>/<article>')
def un_article(lh_number,article):
    '''Affiche un article stocké dans templates/lh_number/'''
    return render_template(f'{lh_number}/{article}.html')


# Pour accéder à l'acceuil d'une LH: ip/LH/"numéro de la LH genre LH1"
#Pour un article de ce numéro: ip/LH/"numéro de la LH genre LH1"/"nom du fichier d'un article genre article_test"

if __name__ == '__main__':
    app.run(debug=False,port=80,host="0.0.0.0") #Lance l'appli