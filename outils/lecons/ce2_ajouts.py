"""Leçons CE2 : la leçon CM1 du même numéro, sans les écrans trop difficiles (« retirer » : numéros des écrans CM1),
avec des écrans propres au CE2 (étiquette « CE2 », placés après le dernier écran de leur section)
et un encadré « Au CE2, je retiens » sous la carte.
Lancer :  python3 lecons/ce2_ajouts.py   puis   python3 inserer_cm2.py CE2"""
import os, sys, json
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from lhelp import E, Q, C, SV, V

OUT = {}
H = 'hl'


def lecon(lid, points, retirer=(), *ecrans, titre=None):
    ec = []
    for e in ecrans:
        e = dict(e); e['plus'] = e.pop('_plus'); e['ce2'] = True; ec.append(e)
    html = ('<div class="cm2-box ce2"><h3>Au CE2, je retiens</h3><ul>'
            + ''.join(f'<li>{p}</li>' for p in points) + '</ul></div>')
    OUT[lid] = {'html': html, 'retirer': list(retirer), 'ecrans': ec}
    if titre: OUT[lid]['titre'] = titre


# =============================================================== GRAMMAIRE
lecon('G1', ['Une phrase a un <b>sujet</b> et un <b>verbe</b>.', 'Je trouve le sujet avec <b>« qui est-ce qui ? »</b>.',
             'Je peux remplacer le sujet par <b>il, elle, ils, elles</b>.'], [3, 7, 8])

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
             'Certains mots changent (variables), d’autres jamais (invariables) : très, bien, demain, doucement.'], [2, 3, 5, 7, 9, 10],
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

# =============================================================== HOMOPHONES (un seul mot par ceinture au CE2 ; jamais son jumeau)
lecon('H1', ['Les verbes <b>avoir</b> (ai, as, a, ont) ; les verbes <b>être</b> (es, est, sont), au présent.', 'Je prouve avec « hier » : avait, était.'], [5])

lecon('H2', ['<b>on</b> désigne quelqu’un, comme <b>il</b>. Je prouve : je remplace par « il ».'], [2, 3, 4, 5],
 E('on', 'coche', 'Je prouve : on → il', 'girl', 'Pour prouver « on », je le remplace par « il ».',
   [('|On| joue dans la cour.', ''), ('|Il| joue dans la cour.', 'Je prouve : je remplace par « il ».')],
   Q('', ['Je remplace par « il ».', 'Je remplace par « avec ».'], 'on désigne quelqu’un, comme il.', 'Comment je prouve « on » dans « On chante » ?'),
   [Q('', ['On joue.', 'On jouent.'], 'on, comme il : le verbe au singulier.', 'Quelle phrase est bien écrite ?'),
    Q('', ['On part demain.', 'On partent demain.'], 'on, comme il : le verbe au singulier.', 'Quelle phrase est bien écrite ?')]),
 E('on', 'loupe', 'Je repère on', 'boy', 'on désigne quelqu’un : une ou plusieurs personnes.',
   [('|On| frappe à la porte.', 'on : quelqu’un frappe.'), ('Quelqu’un frappe à la porte.', 'on désigne une ou plusieurs personnes.')],
   C('Le matin, <on> se lève tôt.', 'Clique sur « on ».', 'Il désigne quelqu’un.'),
   [C('Ce soir, <on> mange des crêpes.', 'Clique sur « on ».', 'Il désigne quelqu’un.'),
    C('Dans la cour, <on> joue au ballon.', 'Clique sur « on ».', 'Il désigne quelqu’un.')]), titre='on')

lecon('H3', ['<b>à</b> est un petit mot qui ne change jamais, devant un lieu ou un moment : à l’école, à midi.'], [0, 1, 2, 5, 6],
 E('a', 'point', 'à devant un lieu, un moment', 'boy', 'à se place devant un lieu ou un moment.',
   [('Je vais |à| l’école.', 'à devant un lieu.'), ('Je mange |à| midi.', 'à devant un moment.'), ('un moulin |à| vent', '')],
   Q('Le film commence ___ huit heures.', ['à', 'dans', 'sous'], 'Un moment précis.', 'Complète.', fill='circ'),
   [Q('Il habite ___ Marseille.', ['à', 'sur', 'sous'], 'Un lieu.', 'Complète.', fill='circ'),
    Q('Nous rentrons ___ midi.', ['à', 'sous', 'dans'], 'Un moment précis.', 'Complète.', fill='circ')]),
 E('a', 'loupe', 'Je repère à', 'girl', 'à est un petit mot devant un lieu, un moment ou un moyen.',
   [('Je vais |à| la piscine |à| vélo.', 'à : devant un lieu, devant un moyen.')],
   C('Nous allons <à> la plage.', 'Clique sur « à ».', 'Le petit mot devant un lieu.'),
   [C('Il rentre <à> midi.', 'Clique sur « à ».', 'Le petit mot devant un moment.'),
    C('Je mange une glace <à> la fraise.', 'Clique sur « à ».', 'Le petit mot devant « la fraise ».')]), titre='à')

lecon('H4', ['<b>et</b> relie deux mots ou deux idées. Je prouve : je peux dire <b>« et puis »</b>.'], [1, 2, 4, 5],
 E('et', 'wagon', 'Je prouve : et puis', 'girl', 'et ajoute : je peux le remplacer par « et puis ».',
   [('du pain |et| du fromage', 'et ajoute.'), ('du pain |et puis| du fromage', 'Je prouve : je peux dire « et puis ».')],
   Q('', ['et ajoute un mot ou une idée.', 'et montre un lieu.', 'et remplace le sujet.'], 'Pense à « et puis ».', 'À quoi sert « et » ?'),
   [Q('Il fait beau ___ chaud.', ['et', 'à'], 'J’ajoute une idée : et puis.', 'Complète.', fill='circ'),
    Q('J’ai un crayon ___ une gomme.', ['et', 'on'], 'J’ajoute un mot : et puis.', 'Complète.', fill='circ')]),
 E('et', 'loupe', 'Je repère et', 'boy', 'et relie deux mots ou deux idées.',
   [('Léa |et| Tom jouent.', 'et relie deux noms.'), ('Il rit |et| il chante.', 'et relie deux idées.')],
   C('Je prends un livre <et> un cahier.', 'Clique sur « et ».', 'Il relie deux mots.'),
   [C('Le chat dort <et> le chien joue.', 'Clique sur « et ».', 'Il relie deux idées.'),
    C('Il fait froid <et> il pleut.', 'Clique sur « et ».', 'Il relie deux idées.')]), titre='et')

lecon('H5', ['<b>c’est</b> = cela est ; il s’écrit avec une apostrophe. Je prouve : <b>c’était</b>.', 'À la forme négative : <b>ce n’est pas</b>.'], [0, 1, 4, 5],
 E('cest', 'etiquette', 'J’écris c’est', 'girl', 'c’est s’écrit avec une apostrophe : c’ + est.',
   [('|C’est| mon ami.', 'c’ + est : une apostrophe.'), ('|Cela est| mon ami.', 'c’est veut dire « cela est ».')],
   Q('', ['C’est un chat.', 'Cest un chat.', 'C est un chat.'], 'N’oublie pas l’apostrophe.', 'Quelle phrase est bien écrite ?'),
   [Q('', ['C’est l’heure.', 'Cest l’heure.', 'C est l’heure.'], 'N’oublie pas l’apostrophe.', 'Quelle phrase est bien écrite ?')]),
 E('mix', 'non', 'À la forme négative', 'boy', 'À l’écrit, la négation de « c’est » est « ce n’est pas ».',
   [('|C’est| mon livre.', ''), ('|Ce n’est pas| mon livre.', 'À l’écrit : ce n’est pas.')],
   Q('', ['Ce n’est pas ma trousse.', 'C’est pas ma trousse.'], 'À l’écrit, on garde « ne ».', 'Quelle phrase est bien écrite ?'),
   [Q('', ['Ce n’est pas grave.', 'C’est pas grave.'], 'À l’écrit, on garde « ne ».', 'Quelle phrase est bien écrite ?')]), titre='c’est')

lecon('H6', ['<b>son</b> est un déterminant : à lui, à elle. Je prouve : <b>mon</b> ; au pluriel, <b>ses</b>.'], [1, 2, 3, 4, 5],
 E('son', 'remplacer', 'Je prouve : mon, ses', 'girl', 'son est devant un nom : je peux dire « mon », ou « ses » au pluriel.',
   [('|son| vélo', 'son, devant un nom : à lui, à elle.'), ('|mon| vélo', 'Je prouve : je remplace par « mon ».'), ('|ses| vélos', 'Au pluriel : ses.')],
   Q('Léo range ___ cartable.', ['son', 'ses'], 'Un seul cartable.', 'Complète.', fill='circ'),
   [Q('Léa promène ___ chien.', ['son', 'ses'], 'Un seul chien.', 'Complète.', fill='circ'),
    Q('Il range ___ jouets.', ['ses', 'son'], 'Plusieurs jouets.', 'Complète.', fill='circ')]),
 E('acc', 'loupe', 'Je repère son', 'boy', 'son est un déterminant : il est devant un nom.',
   [('Tom range |son| sac.', 'son : devant un nom, à lui.'), ('Léa range |son| sac.', 'À elle aussi : son.')],
   C('Le chien mange <son> os.', 'Clique sur « son ».', 'Le déterminant devant « os ».'),
   [C('Ma voisine arrose <son> jardin.', 'Clique sur « son ».', 'Le déterminant devant « jardin ».'),
    C('Le roi pose <son> épée.', 'Clique sur « son ».', 'Le déterminant devant « épée ».')]), titre='son')

lecon('H8', ['Les paires du CE2 : <b>a / à</b>, <b>ont / on</b>, <b>est / et</b>, <b>sont / son</b>. Pour chaque mot, je fais la preuve.'], [0, 1, 2, 3, 5],
 E('verbes', 'liste', 'Les quatre paires du CE2', 'boy', 'Pour chaque mot, je fais la preuve.',
   [('|a| ou |à|', 'a → avait ; à ne change pas.'), ('|ont| ou |on|', 'ont → avaient ; on → il.'),
    ('|est| ou |et|', 'est → était ; et → et puis.'), ('|sont| ou |son|', 'sont → étaient ; son → mon.')],
   Q('Léa ___ un chat.', ['a', 'à'], 'Je prouve : « avait ».', 'Complète.', fill='circ'),
   [Q('___ joue dehors.', ['On', 'Ont'], 'Je prouve : « il ».', 'Complète.', fill='circ'),
    Q('Le ciel est bleu ___ le soleil brille.', ['et', 'est'], 'Je prouve : « et puis ».', 'Complète.', fill='circ'),
    Q('Mes amis ___ contents.', ['sont', 'son'], 'Je prouve : « étaient ».', 'Complète.', fill='circ')]),
 E('relire', 'coche', 'Je corrige une phrase', 'girl', 'Je repère les mots qui se prononcent pareil, puis je fais la preuve.',
   [('Léo à faim et il et fatigué.', 'Il y a des erreurs !'), ('Léo |a| faim et il |est| fatigué.', 'avait faim · était fatigué.')],
   Q('Les enfants on fini leur goûter.', ['Les enfants ont fini leur goûter.', 'Les enfants on fini leur goûter.'], 'Je prouve : avaient fini.', 'Quelle est la bonne correction ?'),
   [Q('Il va a l’école.', ['Il va à l’école.', 'Il va a l’école.'], 'à ne change pas : il allait à l’école.', 'Quelle est la bonne correction ?')]))

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
lecon('C8', ['Je révise les temps du CE2 : présent, futur, imparfait, passé composé, verbes irréguliers compris.'], [2, 4], titre='Révision')

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

lecon('V6', ['Un mot peut avoir un <b>sens propre</b> (le sens de base) et un <b>sens figuré</b> (une image).', 'Un même mot peut avoir plusieurs sens : la phrase m’aide.'], [0, 1, 2, 4],
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
