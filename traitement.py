from yattag import Doc
from markdown import markdown
import os
#dossier où seront les md
directory = 'articles/LH1/'
#liste des articles avec les liens pour y accéder
articles = [ ("/LH/LH1/"+a.split(".")[0]+".html", a.split(".")[0]) for a in os.listdir(directory) ]


for art in os.listdir(directory):

    html_generator = Doc()

#Option 1: Markdown en fichier
# article1 = open("PLANNING.md")
# HTML = markdown(article1.read())
#Fin option 1

# #Option 2: Markdown en doctstring
    article= open(directory+"/"+art, encoding="utf-8")
    TEXTE_MARKDOWN= markdown(article.read())

    HTML=markdown(str(TEXTE_MARKDOWN))
    # #Fin option 2

    TEMPLATE_VERSION=1

    TITRE=art.split(".")[0] #art=filename.md



    def header(html_generator, titre):
        doc, tag, text = html_generator.tagtext()
        with tag('head'):
            with tag('meta', charset="utf-8"):
                pass
            with tag('title', id='titre'):
                text(titre)
            with tag("link", rel="icon", type="image/x-icon", href="favicon_dead.ico"):
                pass
            with tag("link", href="/static/styles/LH1/accueil.css", type="text/css", rel="stylesheet"):
                pass

    def navbar(html_generator):
        doc, tag, text = html_generator.tagtext()
        with tag("nav"):
            with tag("ul"):
                with tag("li", klass="menu"):
                    with tag("a"):
                        text("les articles de la semaine")
                    with tag('ul', klass="sous"):
                        for (url, nom) in articles:
                            with tag("li"):
                                with tag("a", href=url):
                                    text(nom)
                with tag("li"):
                    with tag("a", href="evenements.html"):
                        text("Les derniers numéros")
                with tag("li"):
                    with tag("a", href="club.html"):
                        text("Find your LH !")


    doc, tag, text = html_generator.tagtext()

    with tag('html'):
        header(html_generator, "LH1 - LH d'outre-tombe")
        with tag("body"):
            with tag("div", klass="grille_page"):
                with tag("div", klass="haut_de_page grille_body"):
                    with tag("a", href="/home.html", id="logo"):
                        with tag("img", src="/static/Logo_LH_Necro.png"):
                            pass
                    with tag("div", id="text_accueil_LH"):
                        text("LH1 - LH d'outre-tombe")

            with tag("div", klass="large_element_hors_grille"):
                navbar(html_generator)

            with tag("div", klass="grille_page"):
                with tag("div", klass="corps_de_page grille_body"):
                    with tag("h1"):
                        text(TITRE)
                    with tag("div", klass="mot_de_la_redaction"):
                        doc.asis(markdown(str(TEXTE_MARKDOWN)))

    html = doc.getvalue()

    # genere le html dans "dist"
    with open("static/LH1/articles/"+art.split(".")[0]+".html", "w",encoding='utf-8') as file:
        file.write(html)


html_generator = Doc()

#Option 1: Markdown en fichier
# article1 = open("PLANNING.md")
# HTML = markdown(article1.read())
#Fin option 1

# #Option 2: Markdown en doctstring
article= open("articles/mot.md", encoding="utf-8")
TEXTE_MARKDOWN= markdown(article.read())

HTML=str(TEXTE_MARKDOWN)
# #Fin option 2

TEMPLATE_VERSION=1

TITRE="Le mot de la rédaction :" #art=filename.md



def header(html_generator, titre):
    doc, tag, text = html_generator.tagtext()
    with tag('head'):
        with tag('meta', charset="utf-8"):
            pass
        with tag('title', id='titre'):
            text(titre)
        with tag("link", rel="icon", type="image/x-icon", href="favicon_dead.ico"):
            pass
        with tag("link", href="/static/styles/LH1/accueil.css", type="text/css", rel="stylesheet"):
            pass

def navbar(html_generator):
    doc, tag, text = html_generator.tagtext()
    with tag("nav"):
        with tag("ul"):
            with tag("li", klass="menu"):
                with tag("a"):
                    text("les articles de la semaine")
                with tag('ul', klass="sous"):
                    for (url, nom) in articles:
                        with tag("li"):
                            with tag("a", href=url):
                                text(nom)
            with tag("li"):
                with tag("a", href="evenements.html"):
                    text("Les derniers numéros")
            with tag("li"):
                with tag("a", href="club.html"):
                    text("Find your LH !")


doc, tag, text = html_generator.tagtext()

with tag('html'):
    header(html_generator, "LH1 - LH d'outre-tombe")
    with tag("body"):
        with tag("div", klass="grille_page"):
            with tag("div", klass="haut_de_page grille_body"):
                with tag("a", href="/home.html", id="logo"):
                    with tag("img", src="/static/Logo_LH_Necro.png"):
                        pass
                with tag("div", id="text_accueil_LH"):
                    text("LH1 - LH d'outre-tombe")

        with tag("div", klass="large_element_hors_grille"):
            navbar(html_generator)

        with tag("div", klass="grille_page"):
            with tag("div", klass="corps_de_page grille_body"):
                with tag("h1"):
                    text(TITRE)
                with tag("div", klass="mot_de_la_redaction"):
                    doc.asis(markdown(str(TEXTE_MARKDOWN)))

html = doc.getvalue()

# genere le html dans "dist"
with open("static/LH1/home.html", "w",encoding='utf-8') as file:
    file.write(html)
