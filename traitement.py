from yattag import Doc
from markdown import markdown
import os

def header(html_generator, titre):
    doc, tag, text = html_generator.tagtext()
    with tag('head'):
        with tag('meta', charset="utf-8"):
            pass
        with tag('title', id='titre'):
            text(titre)
        with tag("link", rel="icon", type="image/x-icon", href="/static/favicon_dead.ico"):
            pass
        with tag("link", href="/static/styles/LH1/accueil.css", type="text/css", rel="stylesheet"):
            pass


def navbar(html_generator, articles):
    doc, tag, text = html_generator.tagtext()
    with tag("div", klass="large_element_hors_grille"):
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



def genere_debut_page(html_generator, titre_lh):
    doc, tag, text = html_generator.tagtext()
    with tag("div", klass="grille_page"):
        with tag("div", klass="haut_de_page grille_body"):
            with tag("a", href="/index.html", id="logo"):
                with tag("img", src="/static/Logo_LH_Necro.png"):
                    pass
            with tag("div", id="text_accueil_LH"):
                text(titre_lh)


def genere_article(n_lh, titre_lh, name, autres_articles):
    path = f'articles/{n_lh}/{name}.md'
    article= open(path, encoding="utf-8")
    TEXTE_MARKDOWN= markdown(article.read())
    article.close()


    HTML=markdown(str(TEXTE_MARKDOWN))

    # TODO: ne pas utiliser le nom de fichier comme titre
    TITRE=name

    html_generator = Doc()
    doc, tag, text = html_generator.tagtext()

    with tag('html'):
        header(html_generator, titre_lh)
        with tag("body"):
            genere_debut_page(html_generator, titre_lh)
            navbar(html_generator, autres_articles)

            with tag("div", klass="grille_page"):
                with tag("div", klass="corps_de_page grille_body"):
                    with tag("h1"):
                        text(TITRE)
                    with tag("div", klass="mot_de_la_redaction"):
                        doc.asis(markdown(str(TEXTE_MARKDOWN)))



    html = doc.getvalue()

    # genere le html dans "dist"
    with open(f"static/LH1/articles/{name}.html", "w",encoding='utf-8') as file:
        file.write(html)


MD_404 = """
Le contenu que vous recherchez n'existe pas! (encore)

[Revenir à la page d'accueil](/index.html)
"""

def genere_404():
    html_generator = Doc()
    doc, tag, text = html_generator.tagtext()

    with tag('html'):
        header(html_generator, "La LH")
        with tag("body"):
            genere_debut_page(html_generator, "La LH")

            with tag("div", klass="grille_page"):
                with tag("div", klass="corps_de_page grille_body"):
                    with tag("h1"):
                        text("Vous ")
                        with tag("del"):
                            text("avez")
                        text(" êtes perdu·e !")
                    with tag("div", klass="mot_de_la_redaction"):
                        doc.asis(markdown(MD_404))


    html = doc.getvalue()

    # genere le html dans "dist"
    with open(f"static/404.html", "w",encoding='utf-8') as file:
        file.write(html)

def genere_edition(n_lh, tire_lh, articles):
    fichier_mot_redaction = open(f"articles/{n_lh}/README.md", encoding="utf-8")
    mot_redaction = markdown(fichier_mot_redaction.read())
    fichier_mot_redaction.close()

    html_generator = Doc()
    doc, tag, text = html_generator.tagtext()

    with tag('html'):
        header(html_generator, titre_lh)
        with tag("body"):
            genere_debut_page(html_generator, titre_lh)
            navbar(html_generator, articles)

            with tag("div", klass="grille_page"):
                with tag("div", klass="corps_de_page grille_body"):
                    with tag("h1"):
                        text("Le mot de la rédaction")
                    with tag("div", klass="mot_de_la_redaction"):
                        doc.asis(mot_redaction)

    html = doc.getvalue()

    # genere le html dans "static"
    with open(f"static/{n_lh}/index.html", "w",encoding='utf-8') as file:
        file.write(html)


if __name__ == "__main__":
    genere_404()

    for (n_lh, titre_lh) in [("LH1", "LH1 - LH d'outre-tombe")]:

        directory = f"articles/{n_lh}"
        article_names = [a.split(".")[0] for a in os.listdir(directory) if a != "README.md"]

        # TODO: ne pas utiliser le nom de fichier comme titre
        articles = [ (f"/LH/{n_lh}/{name}.html", name) for name in article_names]

        genere_edition(n_lh, titre_lh, articles)

        for name in article_names:
            genere_article(n_lh, titre_lh, name, articles)

