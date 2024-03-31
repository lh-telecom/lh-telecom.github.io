from markdown import markdown

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

AFTER_TITRE='''<div class="mot_de_la_redaction">'''

with open(f'./templates/V{TEMPLATE_VERSION}/header.txt','r',encoding='UTF-8') as header:
    HEADER=header.read()
with open(f'./templates/V{TEMPLATE_VERSION}/footer.txt','r',encoding='UTF-8') as footer:
    FOOTER=footer.read()

# genere le html dans "dist"
with open("article1.html", "w",encoding='UTF-8') as file:
    file.write(HEADER)
    file.write(f'''<h1>{TITRE}</h1>
               {AFTER_TITRE}''')
    file.write(HTML)
    file.write(FOOTER)
