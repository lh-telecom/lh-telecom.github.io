from yattag import Doc
from markdown import markdown


html_generator = Doc()

#Option 1: Markdown en fichier
# article1 = open("PLANNING.md")
# HTML = markdown(article1.read())
#Fin option 1

# #Option 2: Markdown en doctstring
TEXTE_MARKDOWN='''# Planning

`Syntaxe: [Échéance pour le] tâche`

## Planning hebdomadaire

### Phase initiale préparatoire

- [28 Février] Api normale finie (obtention d'informations, ordres envoyés au serveur) (Équipe 1: Nicolas + Tom) + Premier algorithme "aléatoire" interagissant avec le jeu (Équipe 2: Tom + Jules) + Premières recherches (Équipe 3: Pierre) + Jeu pour tester (Jules + Martin)

- [6 Mars] Réflexions stratégiques par le jeu (Jules + Pierre) + Aboutissement des recherches sur de vrais algorithmes utilisé pour les IA de jeux (Pierre) + Début d'implémentation informatique de mesures pour apprécier l’état de la partie (Équipe 1) (Équipes en duo) + Algorithme pour que les péons récoltent l'or (pas de construction/attaquants)

### Phase de programmation et d'élaboration de stratégies

- [20 Mars] Construction des châteaux et production d'unité (Tom) + Amélioration des techniques pour les péons (Nicolas + Jules) + Gestion de chevaliers en attaque/défense (Martin + Pierre)

- [3 Avril] Construction des châteaux et production d'unité (Nicolas) + Amélioration des techniques pour les péons (Pierre + Martin) + Gestion de chevaliers en attaque/défense (Tom + Jules)

- [10 Avril] Création d'un algortihme de suivi: Permet de trouver ce dont on a besoin (pas assez de chateaux, manque des chevaliers, trop d'or par rapport au nombre de péons..., occupation de la map)

- [24 Avril] Adaptation des trois autres blocs (château, péon, chevalier) pour pouvoir répondre aux objectifs qui sont maintenant déterminés. 

- [8 Mai] travail sur les blocs afin de les liers entre eux (3 équipes : lien château-peon , lien château chevalier, lien chevalier-peon) pour pouvoir agir de concert.

- [15 Mai] raffinage du bloc d'objectifs

- [29 Mai] Construction des châteaux et production d'unité + Amélioration des techniques pour les péons  + Gestion de chevaliers en attaque/défense 

- [12 Mai] Construction des châteaux et production d'unité + Amélioration des techniques pour les péons + Gestion de chevaliers en attaque/défense 

- [28 juin] Rendu final, correction des erreurs nettoyage du code, debug, testing exhaustif


### Organisation régulière

- Réunions de travail toutes les semaines pour faire le point sur l'avancement du projet (tous les membres de l'équipe) (discord, ou présentiel) et attribuer les .

## Attribution des tâches

### Par cycle de 15 jours

- Pôle API: Tom + Nicolas : Amélioration de l'API tous les 15 jours, en fonction des besoins demandés sur le salon discord
- Pôle Recherche: Pierre + Jules : Recherche d'algorithmes plus efficaces (temps et résultats)
- Pôle tests/amélioration des algorithmes: Martin + Jules : Tests des stratégies implémentées, rendu fait au membre en question

### Tâches régulières

- Construction des châteaux et production d'unité
- Amélioration des techniques pour les péons : récolte d'or, exploration, fuite
- Gestion de chevaliers : attaque, défense, exploration
- Dertemination des objectifs : plus de chateaux, de chevalier, de peon, de prise du centre, de protection d'une région manque d'or, manque d'information...
''' #Remplir le markdown ici en ctrl+c ctrl+v

HTML=markdown(str(TEXTE_MARKDOWN))
# #Fin option 2

TEMPLATE_VERSION=1

TITRE="Test d'article sous format planning"

articles = [
    ("tricot", "article 1"),
    ("crochet", "article 2"),
    ("couture", "article 3"),
    ("tutos", "article 4"),
]


def header(html_generator, titre):
    doc, tag, text = html_generator.tagtext()
    with tag('head'):
        with tag('meta', charset="utf-8"):
            pass
        with tag('title', id='titre'):
            text(titre)
        with tag("link", rel="icon", type="image/x-icon", href="/static/favicon_dead.ico"):
            pass
        with tag("link", href="../../../static/styles/LH1/accueil.css", type="text/css", rel="stylesheet"):
            pass

def navbar(html_generator):
    doc, tag, text = html_generator.tagtext()
    with tag("nav"):
        with tag("ul"):
            with tag("li", klass="menu"):
                with tag("a"):
                    text("les articles de la semaine")
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
            with tag("div", klass="haut_de_page_grille_body"):
                with tag("a", href="home.html", id="logo"):
                    with tag("img", src="../../../static/Logo_LH_Necro.png"):
                        pass
                with tag("div", id="text_accueil_LH"):
                    text("La LH XXX")

        with tag("div", klass="large_element_hors_grille"):
            navbar(html_generator)

        with tag("div", klass="grille_page"):
            with tag("div", klass="corps_de_page grille_body"):
                with tag("h1"):
                    text(TITRE)
                with tag("div", klass="mot_de_la_redaction"):
                    pass
                doc.asis(markdown(str(TEXTE_MARKDOWN)))

html = doc.getvalue()

# genere le html dans "dist"
with open("lh.html", "w",encoding='UTF-8') as file:
    file.write(html)
