#!/usr/bin/env python3
"""G2 enrichie (08/11/2026, demande de l'enseignante) : plus d'écrans par rubrique (cartes de rubrique plus fournies)
et des phrases d'exercice différentes selon la classe : CE2 = phrases courtes (exercices de base), CM1 = NIV_ATOI['G2'][2],
CM2 = NIV_ATOI['G2'][3].  Le script remplace, dans index.html, le bloc G2 de LESSONS, PLUS['G2'], NIV_ATOI['G2'] et la liste
« retirer » de CE2_PLUS['G2'].  À lancer une seule fois sur un index.html d'origine (il refuse si G2 est déjà enrichie)."""
import json, os, re, subprocess, sys

RACINE = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..')
CHEMIN = os.path.join(RACINE, 'index.html')
s = open(CHEMIN, encoding='utf-8').read()
if 'Majuscule et point' in s:
    sys.exit('G2 est déjà enrichie.')

# ---------- 1. lire le bloc G2 d'origine (JavaScript) et le convertir en JSON ----------
a = s.index('\nG2:{sections:[') + 1
b = s.index('\nG3:{', a) + 1
bloc = s[a:b].rstrip().rstrip(',')
js = 'const o={' + bloc + '};process.stdout.write(JSON.stringify(o.G2));'
G2 = json.loads(subprocess.run(['node', '-e', js], capture_output=True, text=True, check=True).stdout)
anc = G2['ecrans']
assert len(anc) == 7, len(anc)
m = re.search(r'const PLUS=(\{.*\});\n', s)
PLUS = json.loads(m.group(1))
plus_anc = PLUS['G2']

# ---------- 2. outils pour fabriquer les exercices ----------
TYPES = ['déclarative', 'interrogative', 'impérative']


def ch(p, ask, bon, mauvais, hint, fill=None):
    t = {'ask': ask, 'choose': [bon] + list(mauvais), 'ok': 0, 'hint': hint}
    if fill:
        t['fill'] = fill
    return {'p': p, 'tasks': [t]}


def clic(p, ask, hint, n=None):
    t = {'click': 'x', 'ask': ask, 'hint': hint}
    if n:
        t['n'] = n
    return {'p': p, 'tasks': [t]}


# phrases par type et par niveau (1 = CE2, 2 = CM1, 3 = CM2)
DECL = {
    1: ['Le chat dort sur le canapé.', 'Nous mangeons des pommes.', 'Papa lit le journal.', 'Il fait beau aujourd’hui.', 'La maîtresse corrige les cahiers.', 'Les enfants jouent dehors.'],
    2: ['Ce matin, ma sœur a préparé un gâteau pour toute la famille.', 'Les élèves de CM1 visitent le musée de la ville.', 'Mon grand-père cultive des tomates dans son jardin.', 'Le train de Lyon arrive à quinze heures.', 'Pendant les vacances, nous irons chez nos cousins.', 'La boulangère vend du pain frais tous les matins.'],
    3: ['Quand la cloche a sonné, les élèves se sont rangés calmement devant la porte de la classe.', 'Mon voisin, qui est jardinier, taille ses rosiers chaque printemps avec beaucoup de soin.', 'Parce qu’il pleuvait, nous avons annulé la sortie au parc et nous sommes restés à l’école.', 'Le vieux phare, construit il y a deux siècles, guide encore les bateaux dans la nuit.', 'Si le temps le permet, nous pique-niquerons au bord de la rivière dimanche prochain.', 'Les randonneurs, fatigués mais heureux, ont atteint le sommet avant la tombée de la nuit.'],
}
INTER = {
    1: ['Où vas-tu ?', 'Tu as faim ?', 'Est-ce que tu viens ?', 'Qui a pris mon crayon ?', 'Quelle heure est-il ?', 'Aimes-tu le chocolat ?'],
    2: ['Pourquoi les oiseaux migrent-ils en automne ?', 'Est-ce que tu as terminé ton exercice de mathématiques ?', 'À quelle heure ta sœur rentre-t-elle de l’école ?', 'Combien de pages as-tu déjà lues dans ce livre ?', 'Tes cousins viennent-ils chez nous pendant les vacances ?', 'Qui a laissé la fenêtre ouverte dans la salle de classe ?'],
    3: ['Pourquoi le maître a-t-il décidé de reporter la sortie scolaire à la semaine prochaine ?', 'Est-ce que vous savez comment les abeilles fabriquent le miel dans la ruche ?', 'Quand les élèves de la classe de CM2 présenteront-ils leur exposé devant les parents ?', 'Comment ton frère a-t-il réussi à réparer le vélo sans aucun outil ?', 'Combien de temps faut-il à la lumière du Soleil pour atteindre la Terre ?', 'Ne trouves-tu pas que ce paysage ressemble à un tableau de peintre ?'],
}
IMP = {
    1: ['Ferme la porte.', 'Range ta chambre.', 'Écoutez bien.', 'Viens ici.', 'Lave-toi les mains.', 'Prenez vos cahiers.'],
    2: ['Rangez vos affaires avant de sortir dans la cour.', 'Prends ton manteau, il fait très froid dehors.', 'Écoute bien les consignes avant de commencer l’exercice.', 'Lisez le texte à voix basse puis répondez aux questions.', 'Apporte ton cahier de textes demain matin, s’il te plaît.', 'Lavez-vous les mains avant de passer à table.'],
    3: ['Avant de quitter la classe, rangez vos livres et poussez soigneusement vos chaises sous les tables.', 'Si tu as un doute sur l’orthographe, cherche le mot dans le dictionnaire avant de continuer.', 'Relisez attentivement votre texte, puis corrigez les fautes que vous aurez repérées.', 'Prenez une feuille, tracez un grand carré et coloriez l’intérieur en bleu.', 'Ne touchez à rien tant que la maîtresse n’a pas donné le signal du départ.', 'Soyez attentifs, regardez le tableau et recopiez la leçon sans faire de fautes.'],
}
BANQUE = {'déclarative': DECL, 'interrogative': INTER, 'impérative': IMP}
INDICE = {'déclarative': 'Elle raconte ou elle informe.', 'interrogative': 'Elle pose une question.', 'impérative': 'C’est un ordre ou un conseil, sans sujet écrit.'}
ADJ = {'déclarative': 'déclarative', 'interrogative': 'interrogative', 'impérative': 'impérative'}


def type_ex(niv, kind, i):
    ph = BANQUE[kind][niv][i % 6]
    autres = [t for t in TYPES if t != kind]
    return ch(ph, 'Quel est le type de cette phrase ?', kind, autres, INDICE[kind])


def pick_ex(niv, kind, i):
    bons = BANQUE[kind][niv][i % 6]
    autres = [BANQUE[k][niv][(i + 1) % 6] for k in TYPES if k != kind]
    return ch('', f'Quelle phrase est {kind} ?', bons, autres, INDICE[kind])


# -- phrases du type « est-ce que » / inversion (I1, I3) --
# (déclarative, avec est-ce que, avec inversion, inversion mal écrite 1, inversion mal écrite 2)
FORMES = {
    1: [('Tu aimes les pâtes.', 'Est-ce que tu aimes les pâtes ?', 'Aimes-tu les pâtes ?', 'Aimes tu les pâtes ?', 'Tu aimes-tu les pâtes ?'),
        ('Il vient demain.', 'Est-ce qu’il vient demain ?', 'Vient-il demain ?', 'Vient il demain ?', 'Il vient-il demain ?'),
        ('Vous mangez ici.', 'Est-ce que vous mangez ici ?', 'Mangez-vous ici ?', 'Mangez vous ici ?', 'Vous mangez-vous ici ?'),
        ('Elle chante bien.', 'Est-ce qu’elle chante bien ?', 'Chante-t-elle bien ?', 'Chante elle bien ?', 'Elle chante-t-elle bien ?'),
        ('Tu as faim.', 'Est-ce que tu as faim ?', 'As-tu faim ?', 'As tu faim ?', 'Tu as-tu faim ?'),
        ('Ils jouent dehors.', 'Est-ce qu’ils jouent dehors ?', 'Jouent-ils dehors ?', 'Jouent ils dehors ?', 'Ils jouent-ils dehors ?')],
    2: [('Ton frère joue au football le mercredi.', 'Est-ce que ton frère joue au football le mercredi ?', 'Ton frère joue-t-il au football le mercredi ?', 'Ton frère joue il au football le mercredi ?', 'Joue ton frère au football le mercredi ?'),
        ('Tes amis viennent à la fête.', 'Est-ce que tes amis viennent à la fête ?', 'Tes amis viennent-ils à la fête ?', 'Tes amis viennent ils à la fête ?', 'Viennent tes amis à la fête ?'),
        ('Tu as terminé ton devoir.', 'Est-ce que tu as terminé ton devoir ?', 'As-tu terminé ton devoir ?', 'As tu terminé ton devoir ?', 'Tu as-tu terminé ton devoir ?'),
        ('Elle prend le bus le matin.', 'Est-ce qu’elle prend le bus le matin ?', 'Prend-elle le bus le matin ?', 'Prend elle le bus le matin ?', 'Elle prend-elle le bus le matin ?'),
        ('Nous partons en vacances demain.', 'Est-ce que nous partons en vacances demain ?', 'Partons-nous en vacances demain ?', 'Partons nous en vacances demain ?', 'Nous partons-nous en vacances demain ?'),
        ('Le train arrive à midi.', 'Est-ce que le train arrive à midi ?', 'Le train arrive-t-il à midi ?', 'Le train arrive il à midi ?', 'Arrive le train à midi ?')],
    3: [('Le maître a expliqué la règle aux élèves.', 'Est-ce que le maître a expliqué la règle aux élèves ?', 'Le maître a-t-il expliqué la règle aux élèves ?', 'Le maître a il expliqué la règle aux élèves ?', 'A le maître expliqué la règle aux élèves ?'),
        ('Vous avez compris la consigne de l’exercice.', 'Est-ce que vous avez compris la consigne de l’exercice ?', 'Avez-vous compris la consigne de l’exercice ?', 'Avez vous compris la consigne de l’exercice ?', 'Vous avez-vous compris la consigne de l’exercice ?'),
        ('Ta cousine habite près de la gare depuis un an.', 'Est-ce que ta cousine habite près de la gare depuis un an ?', 'Ta cousine habite-t-elle près de la gare depuis un an ?', 'Ta cousine habite elle près de la gare depuis un an ?', 'Habite ta cousine près de la gare depuis un an ?'),
        ('Les élèves présenteront leur exposé la semaine prochaine.', 'Est-ce que les élèves présenteront leur exposé la semaine prochaine ?', 'Les élèves présenteront-ils leur exposé la semaine prochaine ?', 'Les élèves présenteront ils leur exposé la semaine prochaine ?', 'Présenteront les élèves leur exposé la semaine prochaine ?'),
        ('Il a plu toute la nuit sur la région.', 'Est-ce qu’il a plu toute la nuit sur la région ?', 'A-t-il plu toute la nuit sur la région ?', 'A il plu toute la nuit sur la région ?', 'Il a-t-il plu toute la nuit sur la région ?'),
        ('Tu connais l’histoire de ce vieux château.', 'Est-ce que tu connais l’histoire de ce vieux château ?', 'Connais-tu l’histoire de ce vieux château ?', 'Connais tu l’histoire de ce vieux château ?', 'Tu connais-tu l’histoire de ce vieux château ?')],
}


def estce_ex(niv, i):
    d, e, inv, b1, b2 = FORMES[niv][i % 6]
    return ch('', 'Quelle question utilise « est-ce que » ?', e, [inv, d.rstrip('.') + ' ?'], 'Cherche les mots « est-ce que ».')


def inv_ex(niv, i):
    d, e, inv, b1, b2 = FORMES[niv][i % 6]
    return ch(d, 'Quelle question est bien écrite ?', inv, [b1, b2], 'Le sujet passe après le verbe, avec un tiret.')


def transf_ex(niv, i):
    d, e, inv, b1, b2 = FORMES[niv][i % 6]
    return ch(d, 'Je pose la question avec « est-ce que » :', e, [inv, b1.replace(' ?', '.')], 'Je commence par « est-ce que » et je garde la phrase telle quelle.')


# -- mots interrogatifs (I2) --
MOTS_Q = ['Où', 'Quand', 'Qui', 'Comment', 'Pourquoi', 'Combien']
QUESTIONS = {
    1: [('___ habites-tu ?', 'À Paris.', 'Où'), ('___ arrive le train ?', 'À midi.', 'Quand'), ('___ a cassé le verre ?', 'C’est Tom.', 'Qui'),
        ('___ vas-tu à l’école ?', 'À pied.', 'Comment'), ('___ pleures-tu ?', 'Parce que je suis triste.', 'Pourquoi'), ('___ de frères as-tu ?', 'Deux.', 'Combien')],
    2: [('___ les élèves partent-ils en classe de neige ?', 'En février.', 'Quand'), ('___ a gagné le concours de dessin ?', 'Ma voisine.', 'Qui'),
        ('___ de billes ton frère possède-t-il ?', 'Une trentaine.', 'Combien'), ('___ vas-tu fêter ton anniversaire ?', 'Chez mes grands-parents.', 'Où'),
        ('___ ranges-tu tes affaires aussi vite ?', 'Parce que je suis pressé.', 'Pourquoi'), ('___ fait-on pour construire une cabane ?', 'Avec des planches et des clous.', 'Comment')],
    3: [('___ ton frère a-t-il réparé la roue de son vélo ?', 'Avec une clé et beaucoup de patience.', 'Comment'), ('___ le maître a-t-il reporté la sortie à la semaine prochaine ?', 'À cause de la pluie.', 'Pourquoi'),
        ('___ les abeilles passent-elles l’hiver ?', 'Dans la ruche, serrées les unes contre les autres.', 'Où'), ('___ de kilomètres séparent la maison de l’école ?', 'Environ trois.', 'Combien'),
        ('___ a inventé l’imprimerie au quinzième siècle ?', 'Gutenberg.', 'Qui'), ('___ commencent les vacances d’été cette année ?', 'Le premier samedi de juillet.', 'Quand')],
}


def mot_ex(niv, i):
    ph, rep, bon = QUESTIONS[niv][i % 6]
    autres = [m for m in MOTS_Q if m != bon][(i % 2)::2][:2]
    return ch(ph, f'Quel mot interrogatif complète la question ? Réponse : « {rep} »', bon, autres, 'Regarde la réponse : un lieu, un moment, une personne, une manière, une cause, une quantité ?', 'pr')


# -- ordres (M2, M3) --
VERBES = {
    1: [('fermer', 'la porte', 'Ferme', 'Fermes', 'Fermons', 'Fermez'), ('ranger', 'ta chambre', 'Range', 'Ranges', 'Rangeons', 'Rangez'), ('écouter', 'la maîtresse', 'Écoute', 'Écoutes', 'Écoutons', 'Écoutez'),
        ('lire', 'ce livre', 'Lis', 'Lit', 'Lisons', 'Lisez'), ('finir', 'ton assiette', 'Finis', 'Fini', 'Finissons', 'Finissez'), ('prendre', 'ton cahier', 'Prends', 'Prend', 'Prenons', 'Prenez')],
    2: [('fermer', 'toutes les fenêtres avant de partir', 'Ferme', 'Fermes', 'Fermons', 'Fermez'), ('ranger', 'les crayons dans la trousse', 'Range', 'Ranges', 'Rangeons', 'Rangez'),
        ('écouter', 'attentivement la consigne', 'Écoute', 'Écoutes', 'Écoutons', 'Écoutez'), ('lire', 'le texte à voix haute', 'Lis', 'Lit', 'Lisons', 'Lisez'),
        ('finir', 'l’exercice avant la récréation', 'Finis', 'Fini', 'Finissons', 'Finissez'), ('prendre', 'une feuille et un crayon', 'Prends', 'Prend', 'Prenons', 'Prenez')],
    3: [('fermer', 'soigneusement la porte de la salle avant de quitter l’école', 'Ferme', 'Fermes', 'Fermons', 'Fermez'), ('ranger', 'ton bureau avant que la cloche ne sonne', 'Range', 'Ranges', 'Rangeons', 'Rangez'),
        ('écouter', 'sans interrompre les explications du conférencier', 'Écoute', 'Écoutes', 'Écoutons', 'Écoutez'), ('lire', 'lentement le paragraphe qui décrit la forêt', 'Lis', 'Lit', 'Lisons', 'Lisez'),
        ('finir', 'tes devoirs avant de jouer dehors avec tes amis', 'Finis', 'Fini', 'Finissons', 'Finissez'), ('prendre', 'ton manteau avant de sortir dans le froid', 'Prends', 'Prend', 'Prenons', 'Prenez')],
}


def pers_ex(niv, i, pers=None):
    v = VERBES[niv][i % 6]
    pers = pers or ['tu', 'nous', 'vous'][i % 3]
    bon = {'tu': v[2], 'nous': v[4], 'vous': v[5]}[pers]
    mauv = {'tu': [v[3], v[5]], 'nous': [v[5], v[2]], 'vous': [v[4], v[3]]}[pers]
    return ch(f'___ {v[1]}.', f'Je donne un ordre à « {pers} » :', bon, mauv, {'tu': 'Avec « tu », le verbe est écrit sans sujet : Ferme, Prends…', 'nous': 'Avec « nous » : la terminaison -ons.', 'vous': 'Avec « vous » : la terminaison -ez.'}[pers], 'v')


ORDRES = {
    1: [('Tu fermes la porte.', 'Ferme la porte.', 'Fermes la porte.'), ('Tu prends ton sac.', 'Prends ton sac.', 'Tu prends ton sac.'), ('Vous écoutez la leçon.', 'Écoutez la leçon.', 'Vous écoutez la leçon.'),
        ('Tu finis ton assiette.', 'Finis ton assiette.', 'Tu finis ton assiette.'), ('Nous lisons ensemble.', 'Lisons ensemble.', 'Nous lisons ensemble.'), ('Tu ouvres ton cahier.', 'Ouvre ton cahier.', 'Ouvres ton cahier.')],
    2: [('Tu ranges tes affaires dans le casier.', 'Range tes affaires dans le casier.', 'Ranges tes affaires dans le casier.'), ('Vous prenez vos cahiers de mathématiques.', 'Prenez vos cahiers de mathématiques.', 'Vous prenez vos cahiers de mathématiques.'),
        ('Tu écoutes bien la consigne.', 'Écoute bien la consigne.', 'Écoutes bien la consigne.'), ('Nous partons à neuf heures.', 'Partons à neuf heures.', 'Nous partons à neuf heures.'),
        ('Tu finis ton travail avant la récréation.', 'Finis ton travail avant la récréation.', 'Tu finis ton travail avant la récréation.'), ('Vous lisez ce texte à voix basse.', 'Lisez ce texte à voix basse.', 'Vous lisez ce texte à voix basse.')],
    3: [('Tu relis ton texte avant de le rendre à la maîtresse.', 'Relis ton texte avant de le rendre à la maîtresse.', 'Relit ton texte avant de le rendre à la maîtresse.'),
        ('Vous rangez soigneusement les livres sur l’étagère du fond.', 'Rangez soigneusement les livres sur l’étagère du fond.', 'Vous rangez soigneusement les livres sur l’étagère du fond.'),
        ('Tu cherches le mot dans le dictionnaire.', 'Cherche le mot dans le dictionnaire.', 'Cherches le mot dans le dictionnaire.'), ('Nous finissons le travail avant la fin de la matinée.', 'Finissons le travail avant la fin de la matinée.', 'Nous finissons le travail avant la fin de la matinée.'),
        ('Tu fermes la fenêtre quand il fait froid dans la classe.', 'Ferme la fenêtre quand il fait froid dans la classe.', 'Fermes la fenêtre quand il fait froid dans la classe.'), ('Vous écoutez attentivement les explications du guide.', 'Écoutez attentivement les explications du guide.', 'Vous écoutez attentivement les explications du guide.')],
}


def ordre_ex(niv, i):
    d, imp, mal = ORDRES[niv][i % 6]
    return ch(d, 'Je la transforme en ordre :', imp, [mal, d.replace('.', ' !') if False else d.split(' ', 1)[1].capitalize() if False else mal.lower().capitalize() + ('' if mal.endswith('.') else '.')], 'Pas de sujet écrit : le verbe commence la phrase.') if False else \
        ch(d, 'Je la transforme en ordre :', imp, [mal] + ([d] if d != mal else []), 'Pas de sujet écrit : le verbe commence la phrase.')


# -- formes affirmative / négative (A1, A2, N1, N4) --
# (affirmative, négative bien écrite, négative mal écrite 1, mal écrite 2)
NEGS = {
    1: [('Tom joue.', 'Tom ne joue pas.', 'Tom joue pas.', 'Tom ne pas joue.'), ('Léa chante.', 'Léa ne chante pas.', 'Léa chante pas.', 'Léa ne pas chante.'),
        ('Il pleut.', 'Il ne pleut pas.', 'Il pleut pas.', 'Il ne pas pleut.'), ('Nous mangeons.', 'Nous ne mangeons pas.', 'Nous mangeons pas.', 'Nous ne pas mangeons.'),
        ('Elle dort.', 'Elle ne dort pas.', 'Elle dort pas.', 'Elle ne pas dort.'), ('Je parle.', 'Je ne parle pas.', 'Je parle pas.', 'Je ne pas parle.')],
    2: [('Mon frère aime les épinards.', 'Mon frère n’aime pas les épinards.', 'Mon frère ne aime pas les épinards.', 'Mon frère aime pas les épinards.'),
        ('Les élèves jouent dans la cour.', 'Les élèves ne jouent pas dans la cour.', 'Les élèves jouent pas dans la cour.', 'Les élèves ne pas jouent dans la cour.'),
        ('Elle écoute la radio le soir.', 'Elle n’écoute pas la radio le soir.', 'Elle ne écoute pas la radio le soir.', 'Elle écoute pas la radio le soir.'),
        ('Nous allons à la piscine.', 'Nous n’allons pas à la piscine.', 'Nous ne allons pas à la piscine.', 'Nous allons pas à la piscine.'),
        ('Le chat monte sur la table.', 'Le chat ne monte pas sur la table.', 'Le chat monte pas sur la table.', 'Le chat ne pas monte sur la table.'),
        ('Tu ouvres la fenêtre en hiver.', 'Tu n’ouvres pas la fenêtre en hiver.', 'Tu ne ouvres pas la fenêtre en hiver.', 'Tu ouvres pas la fenêtre en hiver.')],
    3: [('Le facteur apporte le courrier avant midi.', 'Le facteur n’apporte pas le courrier avant midi.', 'Le facteur ne apporte pas le courrier avant midi.', 'Le facteur apporte pas le courrier avant midi.'),
        ('Les enfants regardent la télévision pendant le repas.', 'Les enfants ne regardent pas la télévision pendant le repas.', 'Les enfants regardent pas la télévision pendant le repas.', 'Les enfants ne pas regardent la télévision pendant le repas.'),
        ('Ma voisine arrose ses fleurs quand il pleut.', 'Ma voisine n’arrose pas ses fleurs quand il pleut.', 'Ma voisine ne arrose pas ses fleurs quand il pleut.', 'Ma voisine arrose pas ses fleurs quand il pleut.'),
        ('Nous visitons ce musée tous les ans.', 'Nous ne visitons pas ce musée tous les ans.', 'Nous visitons pas ce musée tous les ans.', 'Nous ne pas visitons ce musée tous les ans.'),
        ('Le cycliste respecte les feux rouges de la ville.', 'Le cycliste ne respecte pas les feux rouges de la ville.', 'Le cycliste respecte pas les feux rouges de la ville.', 'Le cycliste ne pas respecte les feux rouges de la ville.'),
        ('Mes parents utilisent la voiture pour aller travailler.', 'Mes parents n’utilisent pas la voiture pour aller travailler.', 'Mes parents ne utilisent pas la voiture pour aller travailler.', 'Mes parents utilisent pas la voiture pour aller travailler.')],
}


def forme_ex(niv, i):
    aff, neg, b1, b2 = NEGS[niv][i % 6]
    if i % 2 == 0:
        return ch(aff, 'Quelle est sa forme ?', 'affirmative', ['négative'], 'Y a-t-il ne… pas autour du verbe ?')
    return ch(neg, 'Quelle est sa forme ?', 'négative', ['affirmative'], 'Y a-t-il ne… pas autour du verbe ?')


def neg_ex(niv, i):
    aff, neg, b1, b2 = NEGS[niv][i % 6]
    return ch(aff, 'Je mets cette phrase à la forme négative :', neg, [b1, b2], 'Ne… pas encadre le verbe ; devant une voyelle : n’.')


def neg_pick_ex(niv, i):
    aff, neg, b1, b2 = NEGS[niv][i % 6]
    autre = NEGS[niv][(i + 2) % 6][0]
    autre2 = NEGS[niv][(i + 3) % 6][0]
    return ch('', 'Quelle phrase est négative ?', neg, [autre, autre2], 'Cherche les deux mots qui encadrent le verbe.')


# -- négation : cliquer les deux mots --
CLIC = {
    1: ['Léa <ne> (boit) <jamais> de café.', 'Le bébé <ne> (dort) <pas> encore.', 'Tom <ne> (mange) <plus> de bonbons.', 'Je <ne> (vois) <rien> dans le noir.', 'Nous <n’>(avons) <pas> peur.', 'Ils <ne> (parlent) <jamais> en classe.'],
    2: ['Mon petit frère <ne> (veut) <plus> manger de soupe.', 'Les voisins <ne> (partent) <jamais> en vacances en été.', 'Je <n’>(ai) <rien> entendu pendant la nuit.', 'Nous <ne> (voyons) <personne> dans la rue.', 'Elle <ne> (parle) <plus> à son voisin depuis hier.', 'Ils <n’>(oublient) <jamais> leurs affaires de sport.'],
    3: ['Depuis l’accident, mon grand-père <ne> (conduit) <plus> sa voiture dans le centre-ville.', 'Les enfants <n’>(ont) <jamais> vu un spectacle aussi impressionnant.', 'Malgré tous nos efforts, nous <n’>(avons) <rien> trouvé dans la vieille malle.', 'Le chat <ne> (sort) <pas> quand il pleut à verse sur le jardin.', 'Dans cette salle, il <ne> (reste) <plus> une seule place pour le spectacle.', 'Ces randonneurs <ne> (craignent) <pas> la montagne, même en plein hiver.'],
}


def clic_ex(niv, i):
    return clic(CLIC[niv][i % 6], 'Clique sur les deux mots de la négation.', 'Ils sont autour du verbe.', 2)


# -- ne / n’ (N2) --
NEN = {
    1: [('Elle ___ écoute personne.', 'n’', 'ne'), ('Tu ___ parles plus.', 'ne', 'n’'), ('Il ___ aime pas la soupe.', 'n’', 'ne'), ('Je ___ vois rien.', 'ne', 'n’'), ('Nous ___ avons plus faim.', 'n’', 'ne'), ('Ils ___ jouent jamais ici.', 'ne', 'n’')],
    2: [('Mon frère ___ ouvre jamais la fenêtre en hiver.', 'n’', 'ne'), ('Les élèves ___ rangent pas leurs affaires.', 'ne', 'n’'), ('Je ___ ai rien compris à la leçon.', 'n’', 'ne'), ('Nous ___ mangeons plus de bonbons.', 'ne', 'n’'), ('Tu ___ écoutes personne dans la classe.', 'n’', 'ne'), ('Elle ___ regarde jamais la télévision le soir.', 'ne', 'n’')],
    3: [('Depuis son déménagement, ma cousine ___ écrit plus à ses anciennes voisines.', 'n’', 'ne'), ('Ces enfants ___ jouent jamais dehors quand il fait aussi froid.', 'ne', 'n’'), ('Malgré la fatigue, le coureur ___ abandonne pas la course.', 'n’', 'ne'), ('Dans ce village, on ___ entend plus aucun bruit après minuit.', 'n’', 'ne'), ('Nos voisins ___ utilisent jamais leur voiture pour aller au marché.', 'ne', 'n’'), ('Le professeur ___ oublie jamais de corriger les cahiers.', 'n’', 'ne')],
}


def nen_ex(niv, i):
    ph, bon, mal = NEN[niv][i % 6]
    return ch(ph, 'Quel mot faut-il écrire ?', bon, [mal], f'Le mot suivant commence par {"une voyelle" if bon == "n’" else "une consonne"}.', 'neg')


# -- mots de la négation (N3) --
MOTS_N = ['pas', 'jamais', 'plus', 'rien', 'personne']
NEGMOTS = {
    1: [('Il n’y a ___ dans la boîte.', 'Elle est vide.', 'rien'), ('Il n’y a ___ dans la rue.', 'Elle est déserte.', 'personne'), ('Léa ne pleure ___.', 'Avant elle pleurait, maintenant c’est fini.', 'plus'),
        ('Tom ne ment ___.', 'À aucun moment.', 'jamais'), ('Je ne mange ___ de viande aujourd’hui.', 'Simple négation.', 'pas'), ('Nous ne voyons ___ à la fenêtre.', 'Aucune personne.', 'personne')],
    2: [('Depuis hier, mon frère ne mange ___ de chocolat.', 'Il en mangeait avant, c’est terminé.', 'plus'), ('Ce garçon ne dit ___ la vérité.', 'À aucun moment.', 'jamais'), ('Dans la cave, il n’y a ___ d’intéressant.', 'Aucune chose.', 'rien'),
        ('Au parc, il n’y avait ___ ce matin.', 'Aucune personne.', 'personne'), ('Je ne comprends ___ cette consigne.', 'Simple négation.', 'pas'), ('Le magasin ne vend ___ de bonbons le dimanche.', 'Simple négation.', 'pas')],
    3: [('Malgré nos recherches, nous ne trouvons ___ dans cette vieille malle poussiéreuse.', 'Aucune chose.', 'rien'), ('Depuis la tempête, le phare ne brille ___ la nuit.', 'Avant il brillait, c’est terminé.', 'plus'),
        ('Elle ne se plaint ___ , même quand le chemin devient très difficile.', 'À aucun moment.', 'jamais'), ('Dans toute la maison, il n’y avait ___ pour nous accueillir.', 'Aucune personne.', 'personne'),
        ('Cette année, nous n’irons ___ en classe de mer.', 'Simple négation.', 'pas'), ('Il n’y a ___ à ajouter : le texte est parfait.', 'Aucune chose.', 'rien')],
}


def negmot_ex(niv, i):
    ph, sens, bon = NEGMOTS[niv][i % 6]
    autres = [m for m in MOTS_N if m != bon][(i % 2)::2][:2]
    return ch(ph, f'Quel mot de la négation complète la phrase ? ({sens})', bon, autres, 'Pense à ce que la phrase veut dire.', 'neg')


# -- négation au passé composé (N4) --
PASSE = {
    1: [('Léa a mangé.', 'Léa n’a pas mangé.', 'Léa a pas mangé.', 'Léa ne a pas mangé.'), ('Tom a fini.', 'Tom n’a pas fini.', 'Tom a pas fini.', 'Tom ne a pas fini.'),
        ('J’ai gagné.', 'Je n’ai pas gagné.', 'J’ai pas gagné.', 'Je ne ai pas gagné.'), ('Elle a chanté.', 'Elle n’a pas chanté.', 'Elle a pas chanté.', 'Elle ne a pas chanté.'),
        ('Il a dormi.', 'Il n’a pas dormi.', 'Il a pas dormi.', 'Il ne a pas dormi.'), ('Nous avons joué.', 'Nous n’avons pas joué.', 'Nous avons pas joué.', 'Nous ne avons pas joué.')],
    2: [('Mon frère a terminé son travail.', 'Mon frère n’a pas terminé son travail.', 'Mon frère a pas terminé son travail.', 'Mon frère ne a pas terminé son travail.'),
        ('Nous avons visité le musée.', 'Nous n’avons pas visité le musée.', 'Nous avons pas visité le musée.', 'Nous ne avons pas visité le musée.'),
        ('Elle a oublié son cartable ce matin.', 'Elle n’a pas oublié son cartable ce matin.', 'Elle a pas oublié son cartable ce matin.', 'Elle ne a pas oublié son cartable ce matin.'),
        ('Les élèves ont rangé la classe.', 'Les élèves n’ont pas rangé la classe.', 'Les élèves ont pas rangé la classe.', 'Les élèves ne ont pas rangé la classe.'),
        ('Tu as écouté la consigne.', 'Tu n’as pas écouté la consigne.', 'Tu as pas écouté la consigne.', 'Tu ne as pas écouté la consigne.'),
        ('Ils ont gagné le match de hier.', 'Ils n’ont pas gagné le match de hier.', 'Ils ont pas gagné le match de hier.', 'Ils ne ont pas gagné le match de hier.')],
    3: [('Le maître a corrigé tous les cahiers pendant la récréation.', 'Le maître n’a pas corrigé tous les cahiers pendant la récréation.', 'Le maître a pas corrigé tous les cahiers pendant la récréation.', 'Le maître ne a pas corrigé tous les cahiers pendant la récréation.'),
        ('Les randonneurs ont atteint le sommet avant la nuit.', 'Les randonneurs n’ont pas atteint le sommet avant la nuit.', 'Les randonneurs ont pas atteint le sommet avant la nuit.', 'Les randonneurs ne ont pas atteint le sommet avant la nuit.'),
        ('Ma sœur a réussi son examen malgré le stress.', 'Ma sœur n’a pas réussi son examen malgré le stress.', 'Ma sœur a pas réussi son examen malgré le stress.', 'Ma sœur ne a pas réussi son examen malgré le stress.'),
        ('Nous avons trouvé la solution du problème difficile.', 'Nous n’avons pas trouvé la solution du problème difficile.', 'Nous avons pas trouvé la solution du problème difficile.', 'Nous ne avons pas trouvé la solution du problème difficile.'),
        ('Tu as bien compris les explications de la maîtresse.', 'Tu n’as pas bien compris les explications de la maîtresse.', 'Tu as pas bien compris les explications de la maîtresse.', 'Tu ne as pas bien compris les explications de la maîtresse.'),
        ('Les voisins ont entendu le bruit cette nuit.', 'Les voisins n’ont pas entendu le bruit cette nuit.', 'Les voisins ont pas entendu le bruit cette nuit.', 'Les voisins ne ont pas entendu le bruit cette nuit.')],
}


def passe_ex(niv, i):
    aff, neg, b1, b2 = PASSE[niv][i % 6]
    return ch(aff, 'Je mets cette phrase à la forme négative :', neg, [b1, b2], 'Ne… pas encadre le verbe avoir : n’a pas, n’ont pas…')


# -- exclamation (E1, E2, E3) --
EXCL = {
    1: [('Le chien a cassé le vase !', 'déclarative'), ('Range ta chambre !', 'impérative'), ('Il fait très chaud !', 'déclarative'), ('Ferme la fenêtre !', 'impérative'), ('Tu as encore oublié ton cahier !', 'déclarative'), ('Viens vite !', 'impérative')],
    2: [('Quel beau cadeau ma tante m’a offert !', 'déclarative'), ('Fais attention en traversant la rue !', 'impérative'), ('Mon équipe a enfin gagné le match !', 'déclarative'),
        ('Ne touchez pas à ce fil électrique !', 'impérative'), ('Comme ce paysage est magnifique !', 'déclarative'), ('Soyez prudents sur le chemin du retour !', 'impérative')],
    3: [('Comme le temps passe vite quand on s’amuse avec ses amis !', 'déclarative'), ('Rentrez tout de suite avant que l’orage n’éclate au-dessus du village !', 'impérative'),
        ('Que ce château est impressionnant avec ses hautes tours de pierre !', 'déclarative'), ('Surtout, ne dis rien à personne avant que je te l’autorise !', 'impérative'),
        ('Quelle belle journée nous avons passée au bord de la mer !', 'déclarative'), ('Arrêtez de courir dans les couloirs, vous allez tomber !', 'impérative')],
}
EMO = {
    1: [('Quel beau dessin !', 'Il fait un dessin.', 'Fait-il un dessin ?'), ('Comme il est grand !', 'Il est grand.', 'Est-il grand ?'), ('Que ce gâteau est bon !', 'Ce gâteau est bon.', 'Ce gâteau est-il bon ?'),
        ('Bravo, tu as gagné !', 'Tu as gagné.', 'As-tu gagné ?'), ('Quelle chaleur !', 'Il fait chaud.', 'Fait-il chaud ?'), ('Quel bruit !', 'Il y a du bruit.', 'Y a-t-il du bruit ?')],
    2: [('Quelle belle surprise ma sœur m’a faite !', 'Ma sœur m’a fait une surprise.', 'Ma sœur m’a-t-elle fait une surprise ?'), ('Comme ce film est drôle !', 'Ce film est drôle.', 'Ce film est-il drôle ?'),
        ('Que ces fleurs sentent bon !', 'Ces fleurs sentent bon.', 'Ces fleurs sentent-elles bon ?'), ('Bravo, vous avez réussi le défi !', 'Vous avez réussi le défi.', 'Avez-vous réussi le défi ?'),
        ('Comme il fait froid ce matin !', 'Il fait froid ce matin.', 'Fait-il froid ce matin ?'), ('Quel orage nous avons eu cette nuit !', 'Nous avons eu un orage cette nuit.', 'Avons-nous eu un orage cette nuit ?')],
    3: [('Comme les vacances passent vite quand on se promène en forêt !', 'Les vacances passent vite quand on se promène en forêt.', 'Les vacances passent-elles vite quand on se promène en forêt ?'),
        ('Que ce vieux livre est précieux pour toute notre famille !', 'Ce vieux livre est précieux pour toute notre famille.', 'Ce vieux livre est-il précieux pour toute notre famille ?'),
        ('Quelle émotion nous avons ressentie en voyant la mer pour la première fois !', 'Nous avons ressenti de l’émotion en voyant la mer pour la première fois.', 'Avons-nous ressenti de l’émotion en voyant la mer pour la première fois ?'),
        ('Comme ton petit frère a grandi depuis l’été dernier !', 'Ton petit frère a grandi depuis l’été dernier.', 'Ton petit frère a-t-il grandi depuis l’été dernier ?'),
        ('Que ces montagnes sont majestueuses au lever du soleil !', 'Ces montagnes sont majestueuses au lever du soleil.', 'Ces montagnes sont-elles majestueuses au lever du soleil ?'),
        ('Quel courage ces pompiers ont montré pendant l’incendie !', 'Ces pompiers ont montré du courage pendant l’incendie.', 'Ces pompiers ont-ils montré du courage pendant l’incendie ?')],
}
EMOTIONS = {
    1: [('Hourra, j’ai gagné !', 'la joie'), ('Aïe, ça fait mal !', 'la douleur'), ('Au secours, un loup !', 'la peur'), ('Quelle belle surprise !', 'la surprise'), ('Tu m’énerves !', 'la colère'), ('Que c’est beau !', 'l’admiration')],
    2: [('Hourra, nous partons enfin en vacances !', 'la joie'), ('Au secours, le chien du voisin court vers nous !', 'la peur'), ('Oh, tu es déjà là, quelle surprise !', 'la surprise'),
        ('Ça suffit, je ne supporte plus ce bruit !', 'la colère'), ('Aïe, je me suis coincé le doigt dans la porte !', 'la douleur'), ('Quel magnifique coucher de soleil !', 'l’admiration')],
    3: [('Youpi, nous avons gagné la finale du tournoi contre l’école voisine !', 'la joie'), ('Au secours, l’eau monte très vite dans la cave de la maison !', 'la peur'),
        ('Comment, tu as déjà terminé tout ton travail, quelle surprise !', 'la surprise'), ('Assez, je ne veux plus entendre vos disputes dans la cour !', 'la colère'),
        ('Aïe, la douleur est si forte que je ne peux plus marcher !', 'la douleur'), ('Quel talent, ce pianiste joue avec tant de finesse !', 'l’admiration')],
}
TOUTES_EMO = ['la joie', 'la douleur', 'la peur', 'la surprise', 'la colère', 'l’admiration']


def exclt_ex(niv, i):
    ph, t = EXCL[niv][i % 6]
    return ch(ph, 'Quel est son type ?', t, [x for x in TYPES if x != t][:2], 'Le point d’exclamation s’ajoute à un autre type de phrase.')


def exclmarque_ex(niv, i):
    e, neutre, inter = EMO[niv][i % 6]
    return ch('', 'Quelle phrase exprime une émotion ?', e, [neutre, inter], 'Cherche le point d’exclamation.')


def emo_ex(niv, i):
    ph, bon = EMOTIONS[niv][i % 6]
    autres = [m for m in TOUTES_EMO if m != bon][(i % 3)::3][:2]
    return ch(ph, 'Quelle émotion montre cette phrase ?', bon, autres, 'Lis la phrase avec la voix : que ressent la personne ?')


# -- majuscule et point (D2) --
MAJ = {
    1: [('Le chat dort.', 'le chat dort.', 'Le chat dort'), ('Papa lit un livre.', 'papa lit un livre.', 'Papa lit un livre'), ('Nous jouons dehors.', 'nous jouons dehors.', 'Nous jouons dehors'),
        ('Léa mange une pomme.', 'léa mange une pomme.', 'Léa mange une pomme'), ('Il pleut ce matin.', 'il pleut ce matin.', 'Il pleut ce matin'), ('Les oiseaux chantent.', 'les oiseaux chantent.', 'Les oiseaux chantent')],
    2: [('Ce matin, ma sœur a préparé un gâteau.', 'ce matin, ma sœur a préparé un gâteau.', 'Ce matin, ma sœur a préparé un gâteau'), ('Mon grand-père cultive des tomates dans son jardin.', 'mon grand-père cultive des tomates dans son jardin.', 'Mon grand-père cultive des tomates dans son jardin'),
        ('Pendant les vacances, nous irons chez nos cousins.', 'pendant les vacances, nous irons chez nos cousins.', 'Pendant les vacances, nous irons chez nos cousins'), ('Le train de Lyon arrive à quinze heures.', 'le train de Lyon arrive à quinze heures.', 'Le train de Lyon arrive à quinze heures'),
        ('La boulangère vend du pain frais tous les matins.', 'la boulangère vend du pain frais tous les matins.', 'La boulangère vend du pain frais tous les matins'), ('Les élèves visitent le musée de la ville.', 'les élèves visitent le musée de la ville.', 'Les élèves visitent le musée de la ville')],
    3: [('Quand la cloche a sonné, les élèves se sont rangés calmement.', 'quand la cloche a sonné, les élèves se sont rangés calmement.', 'Quand la cloche a sonné, les élèves se sont rangés calmement'),
        ('Mon voisin, qui est jardinier, taille ses rosiers au printemps.', 'mon voisin, qui est jardinier, taille ses rosiers au printemps.', 'Mon voisin, qui est jardinier, taille ses rosiers au printemps'),
        ('Si le temps le permet, nous pique-niquerons au bord de la rivière.', 'si le temps le permet, nous pique-niquerons au bord de la rivière.', 'Si le temps le permet, nous pique-niquerons au bord de la rivière'),
        ('Le vieux phare guide encore les bateaux dans la nuit noire.', 'le vieux phare guide encore les bateaux dans la nuit noire.', 'Le vieux phare guide encore les bateaux dans la nuit noire'),
        ('Les randonneurs, fatigués mais heureux, ont atteint le sommet.', 'les randonneurs, fatigués mais heureux, ont atteint le sommet.', 'Les randonneurs, fatigués mais heureux, ont atteint le sommet'),
        ('Parce qu’il pleuvait, nous sommes restés à l’école.', 'parce qu’il pleuvait, nous sommes restés à l’école.', 'Parce qu’il pleuvait, nous sommes restés à l’école')],
}


def maj_ex(niv, i):
    bon, sans_maj, sans_point = MAJ[niv][i % 6]
    return ch('', 'Quelle phrase déclarative est bien écrite ?', bon, [sans_maj, sans_point], 'Une majuscule au début et un point à la fin.')


def serie(niv, fabriques):
    """4 exercices pour un niveau : une liste de (fonction, indice)."""
    return [f(niv, i) for f, i in fabriques]


# ---------- 3. les 18 écrans ----------
def ecran(sec, picto, titre, guide, bulle, steps, atoi, plus, f2, f3, **kw):
    e = {'sec': sec, 'picto': picto, 'titre': titre, 'guide': guide, 'bulle': bulle, 'steps': steps, 'atoi': atoi, 'plus': plus}
    return e, f2, f3


ECR = []   # (écran, 4 exercices CM1, 4 exercices CM2)


def anc_ecran(k, f2, f3):
    e = dict(anc[k])
    e['plus'] = plus_anc[k]
    ECR.append((e, [f(2, i) for f, i in f2], [f(3, i) for f, i in f3]))


def nouv(sec, picto, titre, guide, bulle, steps, base, f1, f2, f3):
    """base : 3 exercices de niveau CE2 (À toi + 2 autres) = [f(1,i)…] ; f2, f3 : listes (fonction, indice) pour CM1 et CM2."""
    ex = [f(1, i) for f, i in base]
    e = {'sec': sec, 'picto': picto, 'titre': titre, 'guide': guide, 'bulle': bulle, 'steps': steps, 'atoi': ex[0], 'plus': ex[1:]}
    ECR.append((e, [f(2, i) for f, i in f2], [f(3, i) for f, i in f3]))


# --- Déclarative ---
anc_ecran(0, [(type_ex, 0), (type_ex, 3), (pick_ex, 1), (type_ex, 5)] if False else [(lambda n, i: type_ex(n, 'déclarative', i), 0), (lambda n, i: pick_ex(n, 'déclarative', i), 1), (lambda n, i: type_ex(n, 'déclarative', i), 3), (lambda n, i: maj_ex(n, i), 5)],
          [(lambda n, i: type_ex(n, 'déclarative', i), 0), (lambda n, i: pick_ex(n, 'déclarative', i), 1), (lambda n, i: type_ex(n, 'déclarative', i), 3), (lambda n, i: maj_ex(n, i), 5)])
D = lambda n, i: type_ex(n, 'déclarative', i)
I = lambda n, i: type_ex(n, 'interrogative', i)
M = lambda n, i: type_ex(n, 'impérative', i)
PD = lambda n, i: pick_ex(n, 'déclarative', i)
PI = lambda n, i: pick_ex(n, 'interrogative', i)
PM = lambda n, i: pick_ex(n, 'impérative', i)
nouv('decl', 'majuscule' if False else 'point', 'Majuscule et point', 'boy', 'Je commence par une majuscule et je finis par un point.',
     [{'p': 'le chat dort'}, {'p': '*L*e chat dort', 'c': 'Au début : une majuscule.'}, {'p': 'Le chat dort*.*', 'c': 'À la fin : un point.'}],
     [(maj_ex, 0), (maj_ex, 1), (maj_ex, 2)], None,
     [(maj_ex, 0), (maj_ex, 1), (maj_ex, 2), (maj_ex, 3)], [(maj_ex, 0), (maj_ex, 1), (maj_ex, 2), (maj_ex, 3)])
nouv('decl', 'loupe', 'Je reconnais une déclarative', 'girl', 'Elle raconte : je la distingue d’une question et d’un ordre.',
     [{'p': 'Léa range sa chambre.', 'c': 'Elle raconte : déclarative.'}, {'p': 'Léa range-t-elle sa chambre ?', 'c': 'Elle pose une question : interrogative.'}, {'p': 'Range ta chambre.', 'c': 'C’est un ordre : impérative.'}],
     [(D, 1), (PD, 2), (D, 4)], None,
     [(D, 2), (PD, 3), (D, 4), (PD, 5)], [(D, 4), (PD, 5), (D, 0), (PD, 1)])

# --- Interrogative ---
anc_ecran(1, [(estce_ex, 0), (inv_ex, 1), (lambda n, i: type_ex(n, 'interrogative', i), 0), (lambda n, i: pick_ex(n, 'interrogative', i), 2)],
          [(estce_ex, 0), (inv_ex, 1), (lambda n, i: type_ex(n, 'interrogative', i), 0), (lambda n, i: pick_ex(n, 'interrogative', i), 2)])
nouv('inter', 'question', 'Les mots qui questionnent', 'girl', 'Où ? Quand ? Qui ? Comment ? Pourquoi ? Combien ?',
     [{'p': '*Où* habites-tu ?', 'c': 'Où : pour un lieu.'}, {'p': '*Quand* arrive le train ?', 'c': 'Quand : pour un moment.'}, {'p': '*Qui* a pris mon crayon ?', 'c': 'Qui : pour une personne.'},
      {'p': '*Comment* vas-tu à l’école ?', 'c': 'Comment : pour une manière. Pourquoi : pour une cause. Combien : pour une quantité.'}],
     [(mot_ex, 0), (mot_ex, 1), (mot_ex, 2)], None,
     [(mot_ex, 0), (mot_ex, 1), (mot_ex, 2), (mot_ex, 3)], [(mot_ex, 0), (mot_ex, 1), (mot_ex, 2), (mot_ex, 3)])
nouv('inter', 'remplacer', 'Je transforme en question', 'boy', 'Je peux changer une phrase qui raconte en question.',
     [{'p': 'Tu viens.'}, {'p': 'Tu viens*?*', 'c': 'Avec la voix : j’ajoute le point d’interrogation.'}, {'p': '*Est-ce que* tu viens ?', 'c': 'Avec « est-ce que » au début.'}, {'p': '(*Viens*)-[*tu*] ?', 'c': 'Avec l’inversion : le sujet après le verbe, relié par un tiret.'}],
     [(transf_ex, 0), (transf_ex, 1), (transf_ex, 2)], None,
     [(transf_ex, 2), (inv_ex, 3), (transf_ex, 4), (inv_ex, 5)], [(transf_ex, 0), (inv_ex, 1), (transf_ex, 2), (inv_ex, 3)])

# --- Impérative ---
anc_ecran(2, [(M, 0), (PM, 1), (M, 3), (M, 4)], [(M, 0), (PM, 1), (M, 3), (M, 4)])
nouv('imp', 'doigt', 'Tu, nous, vous', 'boy', 'À l’impératif, je donne un ordre à tu, à nous ou à vous.',
     [{'p': '(*Ferme*) la porte.', 'c': 'À « tu » : pas de s pour les verbes en -er.'}, {'p': '(*Fermons*) la porte.', 'c': 'À « nous » : on propose de le faire ensemble.'}, {'p': '(*Fermez*) la porte.', 'c': 'À « vous » : terminaison -ez.'}],
     [(pers_ex, 0), (pers_ex, 1), (pers_ex, 2)], None,
     [(pers_ex, 0), (pers_ex, 1), (pers_ex, 2), (pers_ex, 3)], [(pers_ex, 0), (pers_ex, 1), (pers_ex, 2), (pers_ex, 3)])
nouv('imp', 'remplacer', 'Je transforme en ordre', 'girl', 'Pour donner un ordre, je supprime le sujet.',
     [{'p': '[Tu] (ranges) ta chambre.'}, {'p': '{[Tu]} (ranges) ta chambre.', 'c': 'Je supprime le sujet.'}, {'p': '(*Range*) ta chambre.', 'c': 'Et le verbe : pas de s avec « tu » pour un verbe en -er.'}],
     [(ordre_ex, 0), (ordre_ex, 1), (ordre_ex, 2)], None,
     [(ordre_ex, 0), (ordre_ex, 1), (ordre_ex, 2), (ordre_ex, 3)], [(ordre_ex, 0), (ordre_ex, 1), (ordre_ex, 2), (ordre_ex, 3)])

# --- Affirmative ---
anc_ecran(3, [(forme_ex, 0), (forme_ex, 1), (neg_pick_ex, 2), (forme_ex, 3)], [(forme_ex, 0), (forme_ex, 1), (neg_pick_ex, 2), (forme_ex, 3)])
nouv('aff', 'coche', 'Affirmative ou négative ?', 'boy', 'Je cherche s’il y a une négation autour du verbe.',
     [{'p': 'Léa aime les pâtes.', 'c': 'Pas de négation : affirmative.'}, {'p': 'Léa |*n’*|(aime) |*pas*| les pâtes.', 'c': 'Une négation autour du verbe : négative.'}],
     [(forme_ex, 0), (neg_ex, 1), (forme_ex, 2)], None,
     [(forme_ex, 1), (neg_ex, 2), (neg_pick_ex, 3), (neg_ex, 4)], [(forme_ex, 1), (neg_ex, 2), (neg_pick_ex, 3), (neg_ex, 4)])

# --- Négative ---
anc_ecran(4, [(clic_ex, 0), (clic_ex, 1), (clic_ex, 2), (neg_ex, 3)], [(clic_ex, 0), (clic_ex, 1), (clic_ex, 2), (neg_ex, 3)])
anc_ecran(5, [(nen_ex, 0), (nen_ex, 1), (nen_ex, 2), (nen_ex, 3)], [(nen_ex, 0), (nen_ex, 1), (nen_ex, 2), (nen_ex, 3)])
nouv('neg', 'non', 'Les mots de la négation', 'girl', 'pas, jamais, plus, rien, personne : chaque mot a son sens.',
     [{'p': 'Léa ne mange |*pas*| de pain.', 'c': 'pas : la négation simple.'}, {'p': 'Léa ne ment |*jamais*|.', 'c': 'jamais : à aucun moment.'}, {'p': 'Léa ne pleure |*plus*|.', 'c': 'plus : c’est terminé.'},
      {'p': 'Il n’y a |*rien*| · |*personne*|', 'c': 'rien : aucune chose. personne : aucune personne.'}],
     [(negmot_ex, 0), (negmot_ex, 1), (negmot_ex, 2)], None,
     [(negmot_ex, 0), (negmot_ex, 1), (negmot_ex, 2), (negmot_ex, 3)], [(negmot_ex, 0), (negmot_ex, 1), (negmot_ex, 2), (negmot_ex, 3)])
nouv('neg', 'horloge', 'La négation au passé', 'boy', 'Au passé composé, la négation encadre le verbe avoir.',
     [{'p': 'Léa (a) mangé.'}, {'p': 'Léa |*n’*|(a) |*pas*| mangé.', 'c': 'La négation encadre « a », pas le participe.'}, {'p': 'Nous |*n’*|(avons) |*pas*| joué.', 'c': 'Avec « avons » aussi.'}],
     [(passe_ex, 0), (passe_ex, 1), (passe_ex, 2)], None,
     [(passe_ex, 0), (passe_ex, 1), (passe_ex, 2), (passe_ex, 3)], [(passe_ex, 0), (passe_ex, 1), (passe_ex, 2), (passe_ex, 3)])

# --- Exclamative ---
anc_ecran(6, [(exclt_ex, 0), (exclt_ex, 1), (exclmarque_ex, 2), (emo_ex, 3)], [(exclt_ex, 0), (exclt_ex, 1), (exclmarque_ex, 2), (emo_ex, 3)])
nouv('excl', 'exclam', 'Le point d’exclamation', 'boy', 'Il montre une émotion : surprise, joie, colère…',
     [{'p': 'Il fait beau.', 'c': 'Une phrase déclarative.'}, {'p': 'Il fait beau*!*', 'c': 'Avec un point d’exclamation : j’exprime une émotion.'}, {'p': 'Quel beau temps*!*', 'c': 'Quel, comme, que… annoncent souvent une exclamation.'}],
     [(exclmarque_ex, 0), (exclmarque_ex, 1), (exclmarque_ex, 2)], None,
     [(exclmarque_ex, 0), (exclmarque_ex, 1), (exclmarque_ex, 2), (exclmarque_ex, 3)], [(exclmarque_ex, 0), (exclmarque_ex, 1), (exclmarque_ex, 2), (exclmarque_ex, 3)])
nouv('excl', 'ampoule', 'Je reconnais l’émotion', 'girl', 'Je lis la phrase avec la voix pour deviner l’émotion.',
     [{'p': 'Hourra, j’ai gagné !', 'c': 'La joie.'}, {'p': 'Au secours, un loup !', 'c': 'La peur.'}, {'p': 'Tu m’énerves !', 'c': 'La colère.'}, {'p': 'Quelle belle surprise !', 'c': 'La surprise.'}],
     [(emo_ex, 0), (emo_ex, 1), (emo_ex, 2)], None,
     [(emo_ex, 0), (emo_ex, 1), (emo_ex, 2), (emo_ex, 3)], [(emo_ex, 0), (emo_ex, 1), (emo_ex, 2), (emo_ex, 3)])

# ---------- 4. écrire le résultat dans index.html ----------
nouveaux = [e for e, _, _ in ECR]
G2n = {'sections': G2['sections'], 'ecrans': []}
for e in nouveaux:
    e2 = {k: v for k, v in e.items() if k != 'plus'}
    G2n['ecrans'].append(e2)
bloc_js = 'G2:' + json.dumps(G2n, ensure_ascii=False) + ',\n'
s = s[:a] + bloc_js + s[b:]

PLUS['G2'] = [e['plus'] for e in nouveaux]
niv = {'2': [x for _, x, _ in ECR], '3': [x for _, _, x in ECR]}
m = re.search(r'const PLUS=(\{.*\});\n', s)
s = s[:m.start(1)] + json.dumps(PLUS, ensure_ascii=False) + s[m.end(1):]
m = re.search(r'const NIV_ATOI=(\{.*\});\n', s)
NIV = json.loads(m.group(1))
NIV['G2'] = niv
s = s[:m.start(1)] + json.dumps(NIV, ensure_ascii=False) + s[m.end(1):]

# CE2 : écrans retirés en plus (trop difficiles pour le CE2)
m = re.search(r'const CE2_PLUS=(\{.*\});\n', s)
CE2 = json.loads(m.group(1))
for t in ('Je transforme en question', 'La négation au passé'):
    if t not in CE2['G2']['retirer']:
        CE2['G2']['retirer'].append(t)
s = s[:m.start(1)] + json.dumps(CE2, ensure_ascii=False) + s[m.end(1):]

open(CHEMIN, 'w', encoding='utf-8').write(s)
print('G2 enrichie :', len(nouveaux), 'écrans ;', sum(len(x) for x in niv['2']), 'exercices CM1,', sum(len(x) for x in niv['3']), 'exercices CM2')
