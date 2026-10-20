"""Leçons CE2 : la leçon CM1 du même numéro, sans les écrans trop difficiles (« retirer » : numéros des écrans CM1 au 17/10/2026, ou titres),
avec des écrans propres au CE2 (étiquette « CE2 », placés après le dernier écran de leur section)
et un encadré « Au CE2, je retiens » sous la carte.
Lancer :  python3 lecons/ce2_ajouts.py   puis   python3 inserer_cm2.py CE2"""
import os, sys, json
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from lhelp import E, Q, C, SV, V

OUT = {}
H = 'hl'
REF = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'titres_cm1_ref.json')))


def lecon(lid, points, retirer=(), *ecrans, titre=None):
    ec = []
    for e in ecrans:
        e = dict(e); e['plus'] = e.pop('_plus'); e['ce2'] = True; ec.append(e)
    # les numéros d'écrans renvoient à la leçon CM1 telle qu'elle était le 17 octobre 2026 (titres_cm1_ref.json) :
    # on les change en titres, pour que l'ajout plus tard d'écrans au CM1 ne décale rien
    retirer = [REF[lid][i] if isinstance(i, int) else i for i in retirer]
    html = ('<div class="cm2-box ce2"><h3>Au CE2, je retiens</h3><ul>'
            + ''.join(f'<li>{p}</li>' for p in points) + '</ul></div>')
    OUT[lid] = {'html': html, 'retirer': list(retirer), 'ecrans': ec}
    if titre: OUT[lid]['titre'] = titre


# =============================================================== GRAMMAIRE
lecon('G1', ['Une phrase a un <b>sujet</b> et un <b>verbe</b>.', 'Je trouve le sujet avec <b>« qui est-ce qui ? »</b>.',
             'Je peux remplacer le sujet par <b>il, elle, ils, elles</b>.'], [3, 7, 8, 'J’encadre avec « c’est… qui »'])

lecon('G2', ['3 types de phrase : <b>déclarative</b> (.), <b>interrogative</b> (?), <b>impérative</b>.',
             'Les formes <b>négative</b> (ne… pas) et <b>exclamative</b> (!).', 'Les <b>guillemets</b> montrent les paroles d’un personnage.'], [1, 5],
 E('inter', 'question', 'La phrase interrogative', 'girl', 'Une phrase qui pose une question se termine par un point d’interrogation.',
   [('Tu viens ?', 'Une question : un point d’interrogation.'),
    ('Est-ce que tu viens ?', '« Est-ce que » annonce aussi une question.')],
   Q('', ['Est-ce que tu as faim ?', 'Est-ce que tu as faim.', 'est-ce que tu as faim ?'], 'Une majuscule et un point d’interrogation.', 'Quelle question est bien écrite ?'),
   [Q('Où habites-tu', ['?', '.', '!'], 'C’est une question.', 'Quel point faut-il à la fin ?'),
    Q('Quelle heure est-il ?', ['interrogative', 'déclarative', 'impérative'], 'Elle pose une question.', 'Cette phrase est…')]),
 E('decl', 'bulle', 'Les guillemets du dialogue', 'boy', 'Les guillemets montrent les paroles d’un personnage.',
   [('Léa dit : « Je pars. »', 'Les deux-points annoncent les paroles.'),
    ('Tom demande : « Tu viens ? »', 'Les paroles sont entre guillemets.')],
   C('Maman crie : <« À table ! »>', 'Clique sur les paroles.', 'Elles sont entre guillemets.'),
   [Q('', ['Il dit : « Bonjour. »', 'Il dit « Bonjour. » :', 'Il dit : Bonjour.'], 'Deux-points, puis guillemets.', 'Quelle phrase est bien écrite ?')]))

lecon('G3', ['Le groupe nominal : <b>déterminant + nom</b>, parfois un <b>adjectif</b>.', 'Les accords : -e au féminin, -s au pluriel ; -x et -aux (un cheval → des chevaux).',
             'Les féminins qui s’entendent : lecteur → lectrice, joyeux → joyeuse.'])

lecon('G4', ['Les classes de mots : <b>nom</b> (commun ou propre), <b>déterminant</b>, <b>adjectif</b>, <b>verbe</b>, <b>pronom sujet</b>, <b>adverbe</b>.',
             'Certains mots changent (variables), d’autres jamais (invariables) : très, bien, demain, doucement.'], [2, 3, 5, 7, 9, 10, 'Nature ou fonction ?'],
 E('gn', 'etiquette', 'Nom commun, nom propre', 'girl', 'Le nom propre désigne une personne ou un lieu précis ; il a une majuscule.',
   [('une |ville| · |Paris|', 'ville : nom commun ; Paris : nom propre.'),
    ('un |chien| · |Médor|', 'Le nom propre prend une majuscule.')],
   C('Mon chien s’appelle <Rex>.', 'Clique sur le nom propre.', 'Il commence par une majuscule.'),
   [C('Nous visitons <Lyon> en été.', 'Clique sur le nom propre.', 'Une majuscule : un lieu précis.'),
    Q('', ['un nom propre', 'un nom commun'], 'Une majuscule, une personne précise.', '« Léa » est…')]))

lecon('G5', ['Le sujet commande le verbe : <i>il chante, ils chantent</i>.', 'Je remplace le sujet par un pronom pour trouver la terminaison.'], [3, 4, 5, 6, 7, 8])

lecon('G6', ['La phrase : le <b>groupe sujet</b> et le <b>groupe verbal</b> (le verbe et ce qui le complète).',
             'Je peux <b>déplacer</b>, <b>supprimer</b>, <b>ajouter</b> ou <b>remplacer</b> des mots.'], [1, 2, 3, 4, 5, 7, 9],
 E('phrase', 'sv', 'Groupe sujet, groupe verbal', 'girl', 'La phrase a deux groupes : le groupe sujet et le groupe verbal.',
   [('[Le chat] mange sa pâtée.', 'Le groupe sujet : de qui on parle.'),
    ('Le chat %mange sa pâtée%.', 'Le groupe verbal : le verbe et ce qui le complète.')],
   Q('Les oiseaux construisent un nid.', ['construisent un nid', 'Les oiseaux', 'un nid'], 'Le verbe et ce qui le suit.', 'Quel est le groupe verbal ?'),
   [Q('Mon frère lit une bande dessinée.', ['Mon frère', 'lit', 'une bande dessinée'], 'De qui parle-t-on ?', 'Quel est le groupe sujet ?'),
    Q('La maîtresse écrit au tableau.', ['écrit au tableau', 'La maîtresse', 'au tableau'], 'Le verbe et ce qui le suit.', 'Quel est le groupe verbal ?')]),
 E('tests', 'ciseaux', 'Je supprime, j’ajoute', 'boy', 'Je peux enlever ou ajouter des mots : la phrase garde son sens.',
   ['Ce matin, les élèves chantent dans la cour.',
    ('Les élèves chantent.', 'Je supprime des mots : la phrase a encore du sens.'),
    ('Les petits élèves chantent joyeusement.', 'J’ajoute des mots : la phrase est plus précise.')],
   Q('Le chien dort sous la table.', ['sous la table', 'le chien', 'dort'], 'La phrase doit garder son sens.', 'Quel groupe peut-on supprimer ?'),
   [Q('', ['Le gros chat noir dort.', 'Le chat dort.'], 'On a ajouté des mots.', 'Quelle phrase est enrichie ?'),
    Q('Hier, Léa a lu un livre.', ['Hier', 'Léa', 'a lu'], 'La phrase doit garder son sens.', 'Quel mot peut-on supprimer ?')]),
 E('tests', 'remplacer', 'Je remplace', 'girl', 'Je remplace le groupe sujet par un pronom.',
   [('[Le chat] dort.', ''), ('[Il] dort.', 'le chat → il.'), ('[Les filles] jouent. → [Elles] jouent.', 'les filles → elles.')],
   Q('Les enfants courent.', ['Ils courent.', 'Il court.', 'Elles courent.'], 'les enfants → ils.', 'Je remplace le groupe sujet par un pronom :'),
   [Q('Ma sœur chante.', ['Elle chante.', 'Il chante.', 'Elles chantent.'], 'ma sœur → elle.', 'Je remplace le groupe sujet par un pronom :'),
    Q('Le vent souffle.', ['Il souffle.', 'Elle souffle.', 'Ils soufflent.'], 'le vent → il.', 'Je remplace le groupe sujet par un pronom :')]), titre='Groupe sujet, groupe verbal')

lecon('G7', ['La chaîne des accords : le <b>groupe nominal</b> s’accorde, puis le <b>verbe</b> s’accorde avec le sujet.'], [2, 3, 4, 5, 6, 7],
 E('chaine', 'liste', 'Toute la chaîne', 'boy', 'Au pluriel, tout change : déterminant, adjectif, nom et verbe.',
   [('^Le^ petit chat (joue).', 'Au singulier.'),
    ('^Les^ petit*s* chat*s* (jouent).', 'Au pluriel : toute la chaîne change.')],
   Q('', ['Les petits chiens aboient.', 'Les petit chiens aboient.', 'Les petits chiens aboie.'], 'Tout s’accorde.', 'Quelle phrase est bien accordée ?'),
   [Q('Les grandes filles ___.', ['dansent', 'danse', 'danses'], 'Les grandes filles = elles.', 'Complète avec le verbe.', fill='v'),
    Q('', ['Mes jolies fleurs poussent.', 'Mes jolie fleurs poussent.', 'Mes jolies fleurs pousse.'], 'Tout s’accorde.', 'Quelle phrase est bien accordée ?')]),
 E('methode', 'coche', 'Je vérifie une phrase', 'girl', 'J’accorde le groupe nominal, puis le verbe.',
   [('Les vieille maison brille.', 'Il y a des erreurs !'),
    ('Les vieilles maisons brille.', '1. J’accorde le groupe nominal.'),
    ('Les vieilles maisons brillent.', '2. J’accorde le verbe.')],
   Q('Mes cousin joue.', ['Mes cousins jouent.', 'Mes cousins joue.', 'Mes cousin jouent.'], 'Le groupe nominal, puis le verbe.', 'Quelle est la bonne correction ?'),
   [Q('Les petite souris mange.', ['Les petites souris mangent.', 'Les petites souris mange.', 'Les petite souris mangent.'], 'Le groupe nominal, puis le verbe.', 'Quelle est la bonne correction ?')]))

# Pas de ceintures d'homophones au CE2 : le programme du cycle 2 ne les prévoit pas (décision d'octobre 2026).

# =============================================================== CONJUGAISON (les verbes irréguliers sont en C6 et C7 au CE2)
lecon('C1', ['Le présent d’<b>être</b>, d’<b>avoir</b> et des verbes du <b>1er groupe</b> (-er).', 'Le verbe a un <b>radical</b> et une <b>terminaison</b> ; je retrouve son <b>infinitif</b>.',
             'Les verbes irréguliers (aller, faire, dire…) : ceinture C6.'], [3, 4, 5, 7, 8, 9, 10],
 E('rad', 'loupe', 'Je trouve l’infinitif', 'girl', 'L’infinitif est le nom du verbe : radical + er.',
   [('il chant§e§ → chanter', 'Je retrouve l’infinitif.'), ('nous jou§ons§ → jouer', ''), ('vous parl§ez§ → parler', '')],
   Q('', ['danser', 'dansent', 'dansez'], 'L’infinitif se termine par -er.', 'Quel est l’infinitif de « ils dansent » ?'),
   [Q('', ['marcher', 'marchons', 'marche'], 'L’infinitif se termine par -er.', 'Quel est l’infinitif de « nous marchons » ?'),
    Q('', ['être', 'est', 'étais'], 'C’est le verbe être.', 'Quel est l’infinitif de « il est » ?')]))

lecon('C2', ['Le futur d’<b>être</b>, d’<b>avoir</b> et du <b>1er groupe</b> : je chanterai, nous chanterons.', 'Les verbes irréguliers au futur : ceinture C7.'], [3, 5, 6, 7, 8])
lecon('C3', ['L’imparfait d’<b>être</b>, d’<b>avoir</b> et du <b>1er groupe</b> : je chantais, nous chantions.', 'Les verbes irréguliers à l’imparfait : ceinture C7.'], [3, 5, 6])
lecon('C4', ['Le passé composé avec <b>avoir</b> : avoir au présent + participe passé (j’ai chanté).'], [4])
lecon('C5', ['Le passé composé avec <b>être</b> pour les verbes de déplacement : je suis parti, il est arrivé.'], [2, 4])

# =============================================================== VOCABULAIRE
lecon('V1', ['Le <b>mot générique</b> (le mot-étiquette) regroupe des <b>mots précis</b>.'])

lecon('V2', ['Pour comprendre un mot inconnu : les indices de la phrase et du mot, puis je vérifie dans un <b>dictionnaire adapté</b>.'], [2],
 E('methode', 'liste', 'Je vérifie dans le dictionnaire', 'girl', 'Je propose un sens, puis je vérifie dans le dictionnaire.',
   [('Le boulanger cuit le pain dans le #fournil#.', 'Je propose un sens avec les indices.'),
    ('fournil, n. m. : pièce où le boulanger cuit le pain.', 'Je vérifie dans le dictionnaire.'),
    ('Les mots sont rangés dans l’ordre alphabétique.', '')],
   Q('', ['ami, bateau, chat', 'chat, ami, bateau', 'bateau, chat, ami'], 'a, b, c…', 'Quel est l’ordre alphabétique ?'),
   [Q('', ['Je regarde la deuxième lettre.', 'Je prends le premier mot de la page.', 'Je saute la page.'], 'abeille, avion…', 'Deux mots commencent par la même lettre : que fais-je ?')]))

lecon('V3', ['Les <b>préfixes</b> dé-, mal-, in- (le contraire) et re- (à nouveau).', 'Les <b>suffixes</b> -eur, -ier (une personne, un métier) et -ette (petit).'], [6])

lecon('V4', ['Une <b>famille de mots</b> : une partie commune et un même sens (port, portuaire, aéroport).', 'Dans une famille, il y a des noms, des verbes, des adjectifs.'], [],
 E('fam', 'mots', 'Nom, verbe, adjectif', 'boy', 'Dans une famille, il y a des mots de classes différentes.',
   [('|observ|ation · |observ|er · |observ|able', 'un nom · un verbe · un adjectif'),
    ('|port| · |port|uaire · aéro|port|', 'La partie commune donne le sens.')],
   Q('', ['un verbe', 'un nom', 'un adjectif'], 'On peut le conjuguer.', 'Dans la famille de « danse », « danser » est…'),
   [Q('', ['un nom', 'un verbe', 'un adjectif'], 'On peut dire « le lavage ».', 'Dans la famille de « laver », « lavage » est…')]))

lecon('V5', ['Les <b>synonymes</b> (même sens) et les <b>contraires</b>.', 'Des mots de plus en plus forts : la crainte, la peur, l’épouvante.',
             'Les <b>niveaux de langue</b> : une bagnole (familier), une voiture (courant), une automobile (soutenu).'], [3, 4, 5],
 E('syn', 'liste', 'Du plus faible au plus fort', 'girl', 'Des mots proches peuvent être de plus en plus forts.',
   [('la crainte → la peur → l’épouvante', 'De plus en plus fort.'), ('tiède → chaud → brûlant', '')],
   Q('', ['brûlant', 'tiède', 'chaud'], 'Le plus fort.', 'Lequel est le plus chaud ?'),
   [Q('', ['hurler', 'parler', 'chuchoter'], 'Le plus fort.', 'Lequel est le plus fort ?')]),
 E('choix', 'bulle', 'Les niveaux de langue', 'boy', 'On ne parle pas pareil entre copains et dans un livre.',
   [('une |bagnole|', 'familier : entre copains.'), ('une |voiture|', 'courant : tous les jours.'), ('une |automobile|', 'soutenu : dans les livres, les discours.')],
   Q('', ['courant', 'familier', 'soutenu'], 'On le dit tous les jours.', '« une chaussure » est du langage…'),
   [Q('', ['familier', 'courant', 'soutenu'], 'Entre copains.', '« un bouquin » est du langage…'),
    Q('', ['soutenu', 'courant', 'familier'], 'Dans un livre, un discours.', '« un ouvrage », pour un livre, est du langage…')]))

lecon('V6', ['Un mot peut avoir un <b>sens propre</b> (le sens de base) et un <b>sens figuré</b> (une image).', 'Un même mot peut avoir plusieurs sens : la phrase m’aide.'], [0, 1, 2, 4, 'Un mot, plusieurs sens'],
 E('def', 'bulle', 'Sens propre, sens figuré', 'girl', 'Un mot peut avoir un sens de base et un sens imagé.',
   [('Je |souffle| mes bougies.', 'sens propre : le sens de base.'), ('Je |souffle| la réponse à mon voisin.', 'sens figuré : une image.'),
    ('La pluie |inonde| la cave. · Le soleil |inonde| la pièce.', '')],
   Q('Le soleil inonde la pièce.', ['le sens figuré', 'le sens propre'], 'Le soleil ne met pas d’eau partout.', 'Ici, « inonde » est au…'),
   [Q('La rivière inonde le champ.', ['le sens propre', 'le sens figuré'], 'L’eau couvre vraiment le champ.', 'Ici, « inonde » est au…'),
    Q('Il a un cœur de pierre.', ['le sens figuré', 'le sens propre'], 'Son cœur n’est pas vraiment en pierre.', 'Ici, « de pierre » est au…')]),
 E('pareil', 'etiquette', 'Un mot, plusieurs sens', 'boy', 'Le même mot peut avoir plusieurs sens : la phrase m’aide.',
   [('une |souris| grise', 'un petit animal'), ('la |souris| de l’ordinateur', 'un objet')],
   Q('Je clique avec la souris.', ['un objet pour l’ordinateur', 'un petit animal'], 'Lis toute la phrase.', 'Ici, « souris » veut dire…'),
   [Q('Le chat chasse une souris.', ['un petit animal', 'un objet pour l’ordinateur'], 'Lis toute la phrase.', 'Ici, « souris » veut dire…')]), titre='Sens propre, sens figuré')

# =============================================================== ORTHOGRAPHE
lecon('O1', ['Devant <b>m, b, p</b>, j’écris <b>m</b> : une jambe, un pompier.'])
lecon('O2', ['Pour trouver la lettre muette, je cherche un mot de la même famille : un chat → un chaton, beau → beauté.'])
lecon('O3', ['Le son « s » : s, ss entre deux voyelles, c devant e, i, y, ç devant a, o, u.'])
lecon('O4', ['Le son « k » : c devant a, o, u ; qu devant e, i ; k dans quelques mots.'])
lecon('O5', ['Le son « g » : g devant a, o, u ; gu devant e, i.'])
lecon('O6', ['<b>ill</b> après une voyelle (la paille) ; le son « oi » s’écrit <b>oi</b> (le roi).'], [3, 5, 6], titre='ill ; oi')

D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'sortie')
os.makedirs(D, exist_ok=True)
json.dump(OUT, open(os.path.join(D, 'CE2_PLUS.json'), 'w'), ensure_ascii=False, indent=1)
print(len(OUT), 'leçons,', sum(len(v['ecrans']) for v in OUT.values()), 'écrans CE2,',
      sum(len(v['retirer']) for v in OUT.values()), 'écrans CM1 retirés')
