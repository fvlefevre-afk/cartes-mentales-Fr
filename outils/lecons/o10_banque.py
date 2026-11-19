"""O10 (« Les noms en -eur ») : BANQUE d'exercices écrite à la main (19/11/2026). Intégration : `python3 o10_banque.py --integrer` (relançable : repart
des exercices d'origine) ; `python3 o10_banque.py` : liste et contrôles (banque_o.py : dictionnaire, doublons, signes phonétiques).

Sources : docs/dispositif-orthographe-ce2-cm1-cm2.md (O10 au CM1 : noms en -eur et leur féminin -euse, -rice, mots des dictées : bonheur, chaleur, moteur, couleur,
chanteur, nageur, vendeur ; CM2 : consolidée), programme du cycle 3 (morphologie : laid, laideur ; métiers en -eur / -rice : agriculteur, agricultrice),
règle de la leçon (-eur sans e ; le verbe aide pour un nom d'agent ; exceptions heure, demeure, beurre, leurre ; trois noms en œur).
Les écrans « Exceptions » et « cœur, sœur, chœur » n'ont que quelques mots : phrases et questions avec de vrais mots, aucune exception inventée.
Aucun signe phonétique (l'audit du 19/11/2026 les a retirés des ajouts)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from banque_o import Q, C, main
EUR = ['eur', 'eure', 'œur']
def N(p, mot): return Q(p, 'eur', ['eure', 'œur'], 'J’entends « eur » à la fin : %s, sans e.' % mot)
ECRAN_EUR = [N('la larg___', 'la largeur'), N('la longu___', 'la longueur'), N('la haut___', 'la hauteur'), N('la douc___', 'la douceur'),
             N('la lent___', 'la lenteur'), N('la grand___', 'la grandeur'), N('la fray___', 'la frayeur'), N('la sav___', 'la saveur'),
             N('la vap___', 'la vapeur'), N('une od___', 'une odeur'), N('la val___', 'la valeur'), N('un mot___', 'un moteur')]
def V(p, verbe): return Q(p, 'eur', ['eure', 'œur'], 'Pense à %s.' % verbe)
ECRAN_VERBE = [V('un vend___', 'vendre'), V('un promen___', 'se promener'), V('un pêch___', 'pêcher'), V('un saut___', 'sauter'),
               V('un cour___', 'courir'), V('un plong___', 'plonger'), V('un patin___', 'patiner'), V('un ment___', 'mentir'),
               V('un voyag___', 'voyager'), V('un dorm___', 'dormir'), V('un rêv___', 'rêver'), V('un travaill___', 'travailler')]
def FE(p, masc, fem): return Q(p, 'euse', ['eur', 'euze'], 'Un %s → une %s.' % (masc, fem))
def FT(p, masc, fem): return Q(p, 'trice', ['teuse', 'tresse'], 'Un %s → une %s.' % (masc, fem))
ECRAN_FEMININ = [FE('une nag___', 'nageur', 'nageuse'), FE('une jou___', 'joueur', 'joueuse'), FE('une patin___', 'patineur', 'patineuse'),
                 FE('une voyag___', 'voyageur', 'voyageuse'), FE('une plong___', 'plongeur', 'plongeuse'), FE('une promen___', 'promeneur', 'promeneuse'),
                 FT('une agricul___', 'agriculteur', 'agricultrice'), FT('une conduc___', 'conducteur', 'conductrice'), FT('une lec___', 'lecteur', 'lectrice'),
                 FT('une anima___', 'animateur', 'animatrice'), FT('une dessina___', 'dessinateur', 'dessinatrice'), FT('une moni___', 'moniteur', 'monitrice')]
QE = 'Quel nom s’écrit avec un e à la fin ?'
ECRAN_EXC = [Q('le l___', 'eurre', ['eur', 'eure'], 'Une exception : le leurre.'), Q('de bonne h___', 'eure', ['eur', 'œur'], 'Une exception : l’heure.'),
             Q('tout à l’h___', 'eure', ['eur', 'œur'], 'Une exception : l’heure.'), Q('une tartine de b___', 'eurre', ['eur', 'eure'], 'Une exception : le beurre.'),
             Q('une belle dem___', 'eure', ['eur', 'œur'], 'Une exception : la demeure.'),
             C(QE, 'l’heure', 'la peur', 'la fleur', 'Une exception à mémoriser.'), C(QE, 'la demeure', 'la couleur', 'la chaleur', 'Une exception à mémoriser.'),
             C(QE, 'le beurre', 'le bonheur', 'le moteur', 'Une exception à mémoriser.'),
             C('Quel nom s’écrit -eur, sans e ?', 'la largeur', 'l’heure', 'la demeure', 'L’heure et la demeure sont des exceptions.'),
             C('Quel nom s’écrit -eur, sans e ?', 'la douceur', 'le beurre', 'l’heure', 'Le beurre et l’heure sont des exceptions.')]
QO = 'Quel nom s’écrit avec œur ?'
ECRAN_COEUR = [Q('J’ai mal au c___r.', 'œu', ['eu'], 'Un des trois noms en œur : le cœur.', 'Complète avec les bonnes lettres.'),
               Q('Ma s___r a huit ans.', 'œu', ['eu'], 'Un des trois noms en œur : la sœur.', 'Complète avec les bonnes lettres.'),
               Q('Le ch___r chante à l’église.', 'œu', ['eu'], 'Un des trois noms en œur : le chœur.', 'Complète avec les bonnes lettres.'),
               Q('Je connais ma poésie par c___r.', 'œu', ['eu'], 'Un des trois noms en œur : le cœur.', 'Complète avec les bonnes lettres.'),
               Q('Mon frère et ma s___r jouent dehors.', 'œu', ['eu'], 'Un des trois noms en œur : la sœur.', 'Complète avec les bonnes lettres.'),
               C(QO, 'la sœur', 'la peur', 'la fleur', 'Je mémorise : cœur, sœur, chœur.'), C(QO, 'le cœur', 'le moteur', 'le bonheur', 'Je mémorise : cœur, sœur, chœur.'),
               C(QO, 'le chœur', 'le chanteur', 'le malheur', 'Je mémorise : cœur, sœur, chœur.'),
               C('Combien de noms s’écrivent avec œur ?', 'trois : cœur, sœur, chœur', 'un seul : cœur', 'beaucoup', 'Je les mémorise.')]
R_EUR = 'Parce qu’un nom en « eur » s’écrit -eur, sans e.'
R_X, R_O, R_C, R_L = 'Parce que c’est une exception.', 'Parce que c’est un des trois noms en œur.', 'Parce que le mot est court.', 'Parce que le mot est long.'
def P(mot, fin, bon, a, b, hint): return C('Pourquoi %s dans « %s » ?' % (fin, mot), bon, a, b, hint)
ECRAN_PROUVE = [P('largeur', '-eur', R_EUR, R_X, R_C, 'Pas une exception.'), P('douceur', '-eur', R_EUR, R_X, R_L, 'Pas une exception.'),
                P('moteur', '-eur', R_EUR, R_O, R_C, 'Pas une exception.'),
                P('vendeur', '-eur', 'Parce que je pense au verbe « vendre » : un nom en -eur.', R_X, R_C, 'Pense à vendre.'),
                P('nageuse', '-euse', 'Parce que c’est le féminin de « nageur ».', R_X, R_L, 'Un nageur → une nageuse.'),
                P('agricultrice', '-trice', 'Parce que « agriculteur » finit par -teur : au féminin, -trice.', R_X, R_C, 'Un agriculteur → une agricultrice.'),
                P('conductrice', '-trice', 'Parce que « conducteur » finit par -teur : au féminin, -trice.', R_X, R_C, 'Un conducteur → une conductrice.'),
                P('demeure', 'un e', R_X, R_EUR, R_C, 'Je mémorise.'), P('beurre', '-eurre', R_X, R_EUR, R_O, 'Je mémorise.'),
                P('cœur', 'œur', R_O, R_EUR, R_C, 'Je mémorise : cœur, sœur, chœur.'), P('chœur', 'œur', R_O, R_EUR, R_L, 'Je mémorise : cœur, sœur, chœur.'),
                P('plongeur', '-eur', 'Parce que je pense au verbe « plonger » : un nom en -eur.', R_X, R_L, 'Pense à plonger.')]
BANQUE = {'eur': ECRAN_EUR, 'verbe': ECRAN_VERBE, 'feminin': ECRAN_FEMININ, 'exc': ECRAN_EXC, 'coeur': ECRAN_COEUR, 'prouve': ECRAN_PROUVE}
ORDRE = ['eur', 'verbe', 'feminin', 'exc', 'coeur', 'prouve']
ORIGINE = [2, 2, 2, 2, 2, 2]
if __name__ == '__main__':
    main('O10', BANQUE, ORDRE, ORIGINE)
