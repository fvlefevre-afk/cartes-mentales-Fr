"""O8 à O12 : exercices « À toi ! » PROPRES À CHAQUE CLASSE (26/11/2026, demande de l'enseignante : « prépare les exercices pour O8 à O12 »).

Comme O1 à O6 (`o_niveaux.py`) : `NIV_ATOI[<ceinture>] = {2: [exercices du CM1 par écran], 3: [exercices du CM2 par écran]}`, 4 exercices par écran ;
CM1 = mots seuls (trou dans un mot), CM2 = phrases (trou dans une phrase) ou questions plus fines. Aucun mot ne sert deux fois dans une même ceinture
(ni dans les exercices déjà présents : « À toi ! », PLUS, CM2_PLUS), CM1 et CM2 n'ont jamais le même mot.
Jamais d'écriture fausse montrée : propositions = fins de mots (trou) ou phrases justes sur la règle.

Usage : python3 o8_o12_niveaux.py            → liste les exercices et fait les contrôles (dictionnaire, doublons, 4 par écran)
        python3 o8_o12_niveaux.py --integrer → les ajoute à `NIV_ATOI` de index.html (relançable : remplace O8 à O12)
"""
import json, os, re, sys
H = 'hl'
RECOMP = []
CHECK = []   # (ceinture, classe, mot complet à chercher dans le dictionnaire)
def Q(p, bon, autres, hint, ask, mot=None, cc=None):
    if mot:
        CHECK.append((cc[0], cc[1], mot)); RECOMP.append((cc[0], cc[1], mot, p, bon))
    return {'p': p, 'tasks': [{'choose': [bon] + autres, 'ok': 0, 'hint': hint, 'ask': ask, 'fill': H}]}
def C(ask, bon, a, b, hint):
    return {'p': '', 'tasks': [{'choose': [bon, a, b], 'ok': 0, 'hint': hint, 'ask': ask}]}
NIV = {}

# =============================== O8 : les noms en -é, -ée, -té, -tée, -tié ===============================
ASK8 = 'Complète avec la bonne fin.'
R_M, R_F = 'Parce que c’est un nom masculin.', 'Parce que c’est un nom féminin.'
R_Q, R_A = 'Parce que c’est une qualité ou un état.', 'Parce que c’est une action ou un contenu.'
R_T = 'Parce que c’est l’un des trois noms en -tié.'
def f8(c, k, p, bon, autres, hint, mot): return Q(p, bon, autres, hint, ASK8, mot, ('O8', c))
def P8(mot, fin, bon, a, b, hint):
    return C('Pourquoi %s dans « %s » ?' % (fin, mot), bon, a, b, hint)
def O8(c):
    # c = 2 (CM1) ou 3 (CM2) ; renvoie les 6 écrans
    if c == 2:
        return [
         [f8(c, 0, 'un caf___', 'é', ['ée', 'er'], 'Le nom est masculin : un café.', 'café'), f8(c, 0, 'un march___', 'é', ['ée', 'er'], 'Le nom est masculin : un marché.', 'marché'),
          f8(c, 0, 'un th___', 'é', ['ée', 'er'], 'Le nom est masculin : un thé.', 'thé'), f8(c, 0, 'un bl___', 'é', ['ée', 'er'], 'Le nom est masculin : le blé.', 'blé')],
         [f8(c, 1, 'une ros___', 'ée', ['é', 'er'], 'Le nom est féminin : la rosée.', 'rosée'), f8(c, 1, 'une journ___', 'ée', ['é', 'er'], 'Le nom est féminin : une journée.', 'journée'),
          f8(c, 1, 'une ann___', 'ée', ['é', 'er'], 'Le nom est féminin : une année.', 'année'), f8(c, 1, 'une id___', 'ée', ['é', 'er'], 'Le nom est féminin : une idée.', 'idée')],
         [f8(c, 2, 'la véri___', 'té', ['tée', 'tié'], 'C’est une qualité : la vérité.', 'vérité'), f8(c, 2, 'la beau___', 'té', ['tée', 'tié'], 'C’est une qualité : la beauté.', 'beauté'),
          f8(c, 2, 'la san___', 'té', ['tée', 'tié'], 'C’est un état : la santé.', 'santé'), f8(c, 2, 'la liber___', 'té', ['tée', 'tié'], 'C’est un état : la liberté.', 'liberté')],
         [f8(c, 3, 'une dic___', 'tée', ['té', 'tié'], 'L’action de dicter : une dictée, avec e.', 'dictée'), f8(c, 3, 'la mon___', 'tée', ['té', 'tié'], 'L’action de monter : la montée, avec e.', 'montée'),
          C('Quel nom s’écrit -tée ?', 'la dictée', 'la vérité', 'la moitié', 'Un nom d’action : on dicte.'), C('Quel nom s’écrit -tée ?', 'la montée', 'la beauté', 'la pitié', 'Un nom d’action : on monte.')],
         [f8(c, 4, 'l’ami___', 'tié', ['té', 'tée'], 'Je mémorise : moitié, amitié, pitié.', 'amitié'), f8(c, 4, 'la pi___', 'tié', ['té', 'tée'], 'Je mémorise : moitié, amitié, pitié.', 'pitié'),
          C('Quel nom s’écrit -tié ?', 'l’amitié', 'la fierté', 'la dictée', 'Un des trois noms en -tié.'), C('Quel nom s’écrit -tié ?', 'la moitié', 'la clarté', 'la montée', 'Un des trois noms en -tié.')],
         [P8('canapé', '-é', R_M, R_F, R_Q, 'Regarde le petit mot devant : un.'), P8('journée', '-ée', R_F, R_M, R_Q, 'Regarde le petit mot devant : une.'),
          P8('beauté', '-té', R_Q, R_A, R_M, 'Une qualité.'), P8('amitié', '-tié', R_T, R_Q, R_A, 'Je mémorise : moitié, amitié, pitié.')]]
    return [
     [f8(c, 0, 'Mon père boit un caf___ chaud le matin.', 'é', ['ée', 'er'], 'Le nom est masculin : un café.', 'café'),
      f8(c, 0, 'Le samedi, nous allons au march___ du village.', 'é', ['ée', 'er'], 'Le nom est masculin : le marché.', 'marché'),
      f8(c, 0, 'Le chat dort sur le canap___ du salon.', 'é', ['ée', 'er'], 'Le nom est masculin : le canapé.', 'canapé'),
      f8(c, 0, 'Ma grand-mère prépare un th___ au citron.', 'é', ['ée', 'er'], 'Le nom est masculin : un thé.', 'thé')],
     [f8(c, 1, 'Nous avons passé une belle soir___ chez mamie.', 'ée', ['é', 'er'], 'Le nom est féminin : une soirée.', 'soirée'),
      f8(c, 1, 'Cette journ___ de printemps était très chaude.', 'ée', ['é', 'er'], 'Le nom est féminin : une journée.', 'journée'),
      f8(c, 1, 'L’ann___ scolaire commence en septembre.', 'ée', ['é', 'er'], 'Le nom est féminin : l’année.', 'année'),
      f8(c, 1, 'J’ai eu une bonne id___ pour le goûter.', 'ée', ['é', 'er'], 'Le nom est féminin : une idée.', 'idée')],
     [f8(c, 2, 'La bon___ de ce voisin nous touche beaucoup.', 'té', ['tée', 'tié'], 'C’est une qualité : la bonté.', 'bonté'),
      f8(c, 2, 'Cette ville est connue pour sa beau___ au coucher du soleil.', 'té', ['tée', 'tié'], 'C’est une qualité : la beauté.', 'beauté'),
      f8(c, 2, 'Il est en bonne san___ malgré sa fatigue.', 'té', ['tée', 'tié'], 'C’est un état : la santé.', 'santé'),
      f8(c, 2, 'Les élèves aiment la liber___ de choisir leur livre.', 'té', ['tée', 'tié'], 'C’est un état : la liberté.', 'liberté')],
     [f8(c, 3, 'La dic___ de ce matin comptait dix lignes.', 'tée', ['té', 'tié'], 'L’action de dicter : la dictée, avec e.', 'dictée'),
      f8(c, 3, 'La mon___ vers le col était longue et raide.', 'tée', ['té', 'tié'], 'L’action de monter : la montée, avec e.', 'montée'),
      C('Quel nom d’action s’écrit -tée ?', 'la dictée', 'la sécurité', 'l’amitié', 'On dicte : c’est une action.'),
      P8('dictée', '-tée', R_A, R_Q, R_M, 'L’action de dicter.')],
     [f8(c, 4, 'Mon ami___ avec Léa dure depuis le CP.', 'tié', ['té', 'tée'], 'Je mémorise : moitié, amitié, pitié.', 'amitié'),
      f8(c, 4, 'Le juge n’a eu aucune pi___ pour le voleur.', 'tié', ['té', 'tée'], 'Je mémorise : moitié, amitié, pitié.', 'pitié'),
      f8(c, 4, 'Il a mangé la moi___ du gâteau au chocolat.', 'tié', ['té', 'tée'], 'Je mémorise : moitié, amitié, pitié.', 'moitié'),
      C('Combien de noms s’écrivent avec -tié ?', 'trois : moitié, amitié, pitié', 'un seul : la moitié', 'beaucoup, comme les noms en -té', 'Je mémorise ces trois noms.')],
     [P8('marché', '-é', R_M, R_F, R_Q, 'Regarde le petit mot devant : un.'), P8('année', '-ée', R_F, R_M, R_Q, 'Regarde le petit mot devant : une.'),
      P8('santé', '-té', R_Q, R_A, R_F, 'Un état.'), P8('moitié', '-tié', R_T, R_Q, R_A, 'Je mémorise : moitié, amitié, pitié.')]]
NIV['O8'] = {2: O8(2), 3: O8(3)}

# =============================== O9 : les consonnes doubles ===============================
ASK9, ASKX = 'Complète : consonne simple ou double ?', 'Complète avec la bonne lettre.'
def d9(c, p, bon, autre, hint, mot, ask=ASK9): return Q(p, bon, [autre], hint, ask, mot, ('O9', c))
A_, E_, O_, COM = 'Le mot commence par a-.', 'Le mot commence par e-.', 'Le mot commence par o-.', 'Le mot commence par com-.'
def x9(c, p, bon, autre, mot): return d9(c, p, bon, autre, 'Une exception : je mémorise « %s ».' % mot, mot, ASKX)
def f9(c, p, bon, autre, base, mot): return d9(c, p, bon, autre, 'Pense à %s.' % base, mot)
FAMQ = 'Quel mot de la même famille m’aide à écrire « %s » ?'
def O9(c):
    if c == 2:
        return [
         [d9(c, 'a___eler', 'pp', 'p', A_, 'appeler'), d9(c, 'a___acher', 'tt', 't', A_, 'attacher'), d9(c, 'a___irmer', 'ff', 'f', A_, 'affirmer'), d9(c, 'un a___ident', 'cc', 'c', A_, 'accident')],
         [d9(c, 'e___ectuer', 'ff', 'f', E_, 'effectuer'), d9(c, 'une o___rande', 'ff', 'f', O_, 'offrande'), d9(c, 'un co___andant', 'mm', 'm', COM, 'commandant'), d9(c, 'une co___ission', 'mm', 'm', COM, 'commission')],
         [x9(c, 'a___usant', 'm', 'mm', 'amusant'), x9(c, 'a___oureux', 'm', 'mm', 'amoureux'), x9(c, 'co___ique', 'm', 'mm', 'comique'), x9(c, 'une o___inion', 'p', 'pp', 'opinion')],
         [f9(c, 'une fo___ette', 'ss', 's', 'fosse', 'fossette'), f9(c, 'une ca___ette', 'ss', 's', 'casser', 'cassette'), f9(c, 'un to___eau', 'nn', 'n', 'tonne', 'tonneau'), f9(c, 'une chau___ette', 'ss', 's', 'chausser', 'chaussette')],
         [C(FAMQ % 'fossette', 'une fosse', 'un fossile', 'le fond', 'Il a deux s.'), C(FAMQ % 'tonneau', 'une tonne', 'un ton', 'le tonnerre', 'Il a deux n.'),
          C('Pour écrire « effectuer », où regarder d’abord ?', 'Le début du mot : e-.', 'La fin du mot.', 'Le milieu du mot.', 'Après e-, la consonne se double.'),
          C('« amusant » commence par a-, mais n’a qu’une consonne. Que fais-je ?', 'Je le mémorise : c’est une exception.', 'Je double la consonne.', 'Je cherche un mot en -er.', 'Quelques mots font exception.')],
         [C('Pourquoi pp dans « appeler » ?', 'Parce que le mot commence par a-.', 'Parce que c’est un verbe.', 'Parce que le mot est long.', 'Après a-, la consonne se double.'),
          C('Pourquoi mm dans « commission » ?', 'Parce que le mot commence par com-.', 'Parce que c’est un nom.', 'Parce que le mot est court.', 'Après com-, la consonne se double.'),
          C('Pourquoi une seule consonne dans « amoureux » ?', 'Parce que c’est une exception.', 'Parce que le mot est long.', 'Parce que c’est un adjectif.', 'Je mémorise cette exception.'),
          C('Pourquoi ss dans « cassette » ?', 'Parce que dans « casser » il y a deux s.', 'Parce que le mot finit par -ette.', 'Parce que c’est un nom.', 'La famille me montre la consonne doublée.')]]
    return [
     [d9(c, 'Nous allons a___récier la musique du concert.', 'pp', 'p', A_, 'apprécier'), d9(c, 'Le courageux pompier va a___ronter le feu.', 'ff', 'f', A_, 'affronter'),
      d9(c, 'Le randonneur veut a___eindre le sommet avant midi.', 'tt', 't', A_, 'atteindre'), d9(c, 'Les voisins vont a___ourir à notre aide.', 'cc', 'c', A_, 'accourir')],
     [d9(c, 'Le co___erçant ouvre sa boutique à huit heures.', 'mm', 'm', COM, 'commerçant'), d9(c, 'L’o___icier salue le drapeau avec respect.', 'ff', 'f', O_, 'officier'),
      d9(c, 'Léo écrit un co___entaire sur la page du cahier.', 'mm', 'm', COM, 'commentaire'), d9(c, 'Elle s’e___orce de bien travailler chaque jour.', 'ff', 'f', E_, 'efforce')],
     [x9(c, 'Le suspect a un a___ibi solide.', 'l', 'll', 'alibi'), x9(c, 'Le bruit va a___eurer le petit chat.', 'p', 'pp', 'apeurer'),
      x9(c, 'Le co___ité des fêtes organise le défilé.', 'm', 'mm', 'comité'), x9(c, 'L’a___iral commande toute la flotte.', 'm', 'mm', 'amiral')],
     [f9(c, 'La cai___ière rend la monnaie au client.', 'ss', 's', 'caisse', 'caissière'), f9(c, 'La ba___erie de ma tablette est vide.', 'tt', 't', 'battre', 'batterie'),
      f9(c, 'Mon petit frère ronge un o___elet de poulet.', 'ss', 's', 'os', 'osselet'), f9(c, 'La so___erie du réveil m’a réveillé.', 'nn', 'n', 'sonner', 'sonnerie')],
     [C(FAMQ % 'chaussette', 'une chaussure', 'un chat', 'la chair', 'Il a deux s.'), C(FAMQ % 'cassette', 'casser', 'une caisse', 'un cas', 'Il a deux s.'),
      C('« attacher » et « effectuer » commencent par a- et e-. Que fait la consonne qui suit ?', 'Elle se double.', 'Elle reste seule.', 'Elle disparaît.', 'Après a-, e-, o-, com-, la consonne se double.'),
      C('« alibi » commence par a- et n’a qu’un l. Que fais-je ?', 'Je le mémorise : c’est une exception.', 'Je double la consonne.', 'Je cherche un mot de la famille.', 'Quelques mots font exception.')],
     [C('Pourquoi tt dans « atteindre » ?', 'Parce que le mot commence par a-.', 'Parce que c’est un verbe.', 'Parce que le mot est long.', 'Après a-, la consonne se double.'),
      C('Pourquoi ff dans « officier » ?', 'Parce que le mot commence par o-.', 'Parce que c’est un nom.', 'Parce que le mot est court.', 'Après o-, la consonne se double.'),
      C('Pourquoi une seule consonne dans « comité » ?', 'Parce que c’est une exception.', 'Parce que le mot est long.', 'Parce que c’est un nom.', 'Je mémorise cette exception.'),
      C('Pourquoi ss dans « chaussette » ?', 'Parce que dans « chausser » il y a deux s.', 'Parce que le mot finit par -ette.', 'Parce que c’est un nom.', 'La famille me montre la consonne doublée.')]]
NIV['O9'] = {2: O9(2), 3: O9(3)}

# =============================== O10 : les noms en -eur, -euse, -trice, -eure, -œur ===============================
A10, AO = 'Complète avec la bonne fin.', 'Complète avec les bonnes lettres.'
def e10(c, p, bon, autres, hint, mot, ask=A10): return Q(p, bon, autres, hint, ask, mot, ('O10', c))
def N10(c, p, mot): return e10(c, p, 'eur', ['eure', 'œur'], 'J’entends « eur » à la fin : %s, sans e.' % mot, mot.split(' ', 1)[-1])
def V10(c, p, verbe, mot): return e10(c, p, 'eur', ['eure', 'œur'], 'Pense à %s.' % verbe, mot)
def FE10(c, p, m, f): return e10(c, p, 'euse', ['eur', 'euze'], 'Un %s → une %s.' % (m, f), f)
def FT10(c, p, m, f): return e10(c, p, 'trice', ['teuse', 'tresse'], 'Un %s → une %s.' % (m, f), f)
def X10(c, p, bon, autres, mot): return e10(c, p, bon, autres, 'Une exception : %s.' % mot, mot.split(' ', 1)[-1])
def O10(c):
    QE = 'Quel nom s’écrit avec un e à la fin ?'
    if c == 2:
        return [
         [N10(c, 'la coul___', 'la couleur'), N10(c, 'la p___', 'la peur'), N10(c, 'une err___', 'une erreur'), N10(c, 'le bonh___', 'le bonheur')],
         [V10(c, 'un chant___', 'chanter', 'chanteur'), V10(c, 'un ski___', 'skier', 'skieur'), V10(c, 'un buv___', 'boire', 'buveur'), V10(c, 'un box___', 'boxer', 'boxeur')],
         [FE10(c, 'une chant___', 'chanteur', 'chanteuse'), FE10(c, 'une vend___', 'vendeur', 'vendeuse'), FT10(c, 'une ac___', 'acteur', 'actrice'), FT10(c, 'une institu___', 'instituteur', 'institutrice')],
         [X10(c, 'Il est six h___.', 'eure', ['eur', 'œur'], 'l’heure'), X10(c, 'du b___ salé', 'eurre', ['eur', 'eure'], 'le beurre'),
          X10(c, 'une dem___ ancienne', 'eure', ['eur', 'œur'], 'la demeure'), X10(c, 'un l___ de pêche', 'eurre', ['eur', 'eure'], 'le leurre')],
         [e10(c, 'un c___r rouge', 'œu', ['eu'], 'Un des trois noms en œur : le cœur.', 'cœur', AO), e10(c, 'une petite s___r', 'œu', ['eu'], 'Un des trois noms en œur : la sœur.', 'sœur', AO),
          e10(c, 'un ch___r d’enfants', 'œu', ['eu'], 'Un des trois noms en œur : le chœur.', 'chœur', AO), C('Quel nom s’écrit avec œur ?', 'le cœur', 'la couleur', 'le skieur', 'Je mémorise : cœur, sœur, chœur.')],
         [C('Pourquoi -eur dans « couleur » ?', 'Parce qu’un nom en « eur » s’écrit -eur, sans e.', 'Parce que c’est une exception.', 'Parce que le mot est court.', 'Pas une exception.'),
          C('Pourquoi -eur dans « skieur » ?', 'Parce que je pense au verbe « skier » : un nom en -eur.', 'Parce que c’est une exception.', 'Parce que le mot est long.', 'Pense à skier.'),
          C('Pourquoi -trice dans « actrice » ?', 'Parce que « acteur » finit par -teur : au féminin, -trice.', 'Parce que c’est une exception.', 'Parce que le mot est court.', 'Un acteur → une actrice.'),
          C('Pourquoi œur dans « sœur » ?', 'Parce que c’est un des trois noms en œur.', 'Parce qu’un nom en « eur » s’écrit -eur, sans e.', 'Parce que le mot est court.', 'Je mémorise : cœur, sœur, chœur.')]]
    return [
     [N10(c, 'La profond___ du lac nous impressionne.', 'la profondeur'), N10(c, 'Le ciel prend une belle pâl___ rose.', 'la pâleur'),
      N10(c, 'L’épaiss___ de ce mur est de vingt centimètres.', 'l’épaisseur'), N10(c, 'Quelle fraîch___ dans cette forêt !', 'la fraîcheur')],
     [V10(c, 'Le chass___ suit la piste du sanglier.', 'chasser', 'chasseur'), V10(c, 'Le march___ s’arrête pour boire un peu d’eau.', 'marcher', 'marcheur'),
      V10(c, 'L’entraîn___ explique le jeu à l’équipe.', 'entraîner', 'entraîneur'), V10(c, 'Le balay___ nettoie la rue à l’aube.', 'balayer', 'balayeur')],
     [FE10(c, 'La ski___ prend le télésiège.', 'skieur', 'skieuse'), FE10(c, 'La rêv___ regarde les nuages passer.', 'rêveur', 'rêveuse'),
      FT10(c, 'La specta___ applaudit à la fin du film.', 'spectateur', 'spectatrice'), FT10(c, 'La présenta___ annonce le journal du soir.', 'présentateur', 'présentatrice')],
     [X10(c, 'Il est trois h___ de l’après-midi.', 'eure', ['eur', 'œur'], 'l’heure'), X10(c, 'Maman étale du b___ sur la tartine chaude.', 'eurre', ['eur', 'eure'], 'le beurre'),
      X10(c, 'Ce château est la dem___ du comte.', 'eure', ['eur', 'œur'], 'la demeure'), X10(c, 'Le pêcheur lance un l___ dans l’eau.', 'eurre', ['eur', 'eure'], 'le leurre')],
     [e10(c, 'Mon c___r bat très vite après la course.', 'œu', ['eu'], 'Un des trois noms en œur : le cœur.', 'cœur', AO), e10(c, 'Ma grande s___r prépare le goûter.', 'œu', ['eu'], 'Un des trois noms en œur : la sœur.', 'sœur', AO),
      e10(c, 'Le ch___r des enfants chante à l’école.', 'œu', ['eu'], 'Un des trois noms en œur : le chœur.', 'chœur', AO), C('Quel nom s’écrit avec œur ?', 'la sœur', 'la douceur', 'la chasseuse', 'Je mémorise : cœur, sœur, chœur.')],
     [C('Pourquoi -eur dans « profondeur » ?', 'Parce qu’un nom en « eur » s’écrit -eur, sans e.', 'Parce que c’est une exception.', 'Parce que le mot est court.', 'Pas une exception.'),
      C('Pourquoi -eur dans « marcheur » ?', 'Parce que je pense au verbe « marcher » : un nom en -eur.', 'Parce que c’est une exception.', 'Parce que le mot est long.', 'Pense à marcher.'),
      C('Pourquoi -trice dans « présentatrice » ?', 'Parce que « présentateur » finit par -teur : au féminin, -trice.', 'Parce que c’est une exception.', 'Parce que le mot est court.', 'Un présentateur → une présentatrice.'),
      C('Pourquoi un e dans « heure » ?', 'Parce que c’est une exception.', 'Parce que le mot est court.', 'Parce qu’un nom en « eur » s’écrit -eur, sans e.', 'Je mémorise.')]]
NIV['O10'] = {2: O10(2), 3: O10(3)}

# =============================== O11 : -tion, -sion, -ssion ===============================
A11 = 'Complète avec la bonne fin.'
def e11(c, p, bon, hint, mot):
    return Q(p, bon, [x for x in ('tion', 'sion', 'ssion') if x != bon], hint, A11, mot, ('O11', c))
def P11(mot, bon, a, b, hint, fin): return C('Pourquoi %s dans « %s » ?' % (fin, mot), bon, a, b, hint)
R_Z = 'Parce qu’après la voyelle, j’entends « z ».'
R_S = 'Parce qu’entre deux voyelles, « s » s’écrit ss.'
R_T = 'Parce que c’est l’écriture la plus fréquente.'
def verbe(v): return 'Parce que le verbe de la famille est « %s ».' % v
FREQ = 'Le plus fréquent : -tion.'
def O11(c):
    if c == 2:
        return [
         [e11(c, 'une nota___', 'tion', FREQ, 'notation'), e11(c, 'une ques___', 'tion', FREQ, 'question'), e11(c, 'la sta___', 'tion', FREQ, 'station'), e11(c, 'une na___', 'tion', FREQ, 'nation')],
         [e11(c, 'une inva___', 'sion', 'Après a, j’entends « z ».', 'invasion'), e11(c, 'une déci___', 'sion', 'Après i, j’entends « z ».', 'décision'),
          e11(c, 'une fu___', 'sion', 'Après u, j’entends « z ».', 'fusion'), e11(c, 'une diver___', 'sion', 'Après r : un mot en -sion à mémoriser.', 'diversion')],
         [e11(c, 'une mi___', 'ssion', 'Entre deux voyelles : « s » → ss.', 'mission'), e11(c, 'une conce___', 'ssion', 'Pense à concéder : -ssion.', 'concession'),
          e11(c, 'une admi___', 'ssion', 'Pense à admettre : -ssion.', 'admission'), e11(c, 'une soumi___', 'ssion', 'Pense à soumettre : -ssion.', 'soumission')],
         [Q('augmenter → une augmenta___', 'tion', ['sion', 'ssion'], 'Les verbes en -er donnent le plus souvent -tion.', A11, 'augmentation', ('O11', c)),
          Q('adopter → une adop___', 'tion', ['sion', 'ssion'], 'Les verbes en -er donnent le plus souvent -tion.', A11, 'adoption', ('O11', c)),
          Q('supprimer → une suppre___', 'ssion', ['tion', 'sion'], 'supprimer : -ssion.', A11, 'suppression', ('O11', c)),
          Q('étendre → une exten___', 'sion', ['tion', 'ssion'], 'étendre : -sion.', A11, 'extension', ('O11', c))],
         [P11('question', R_T, R_Z, R_S, 'Le plus fréquent.', '-tion'), P11('décision', R_Z, R_S, R_T, 'Écoute le son avant -ion.', '-sion'),
          P11('mission', R_S, R_Z, R_T, 'Un seul s ferait « z ».', '-ssion'), P11('admission', verbe('admettre'), R_Z, R_T, 'Cherche le verbe de la famille.', '-ssion')]]
    return [
     [e11(c, 'Nous préparons l’inaugura___ de la nouvelle école.', 'tion', FREQ, 'inauguration'), e11(c, 'Le médecin donne une prescrip___ très claire.', 'tion', FREQ, 'prescription'),
      e11(c, 'Notre classe visite l’exposi___ de peinture.', 'tion', FREQ, 'exposition'), e11(c, 'Le jury annonce la sélec___ des plus beaux dessins.', 'tion', FREQ, 'sélection')],
     [e11(c, 'L’excur___ en forêt était superbe.', 'sion', 'Après r : un mot en -sion à mémoriser.', 'excursion'), e11(c, 'La dimen___ de cette table est de deux mètres.', 'sion', 'Après n : un mot en -sion à mémoriser.', 'dimension'),
      e11(c, 'La compréhen___ du texte demande de la patience.', 'sion', 'Après n : un mot en -sion à mémoriser.', 'compréhension'), e11(c, 'L’expan___ de la ville est rapide.', 'sion', 'Après n : un mot en -sion à mémoriser.', 'expansion')],
     [e11(c, 'La proce___ avance lentement dans la rue.', 'ssion', 'Entre deux voyelles : « s » → ss.', 'procession'), e11(c, 'La confe___ du coupable surprend tout le monde.', 'ssion', 'Entre deux voyelles : « s » → ss.', 'confession'),
      e11(c, 'Le roi laisse la succe___ à son fils.', 'ssion', 'Entre deux voyelles : « s » → ss.', 'succession'), e11(c, 'La démi___ du ministre fait du bruit.', 'ssion', 'Pense à démettre : -ssion.', 'démission')],
     [Q('inventer → une inven___', 'tion', ['sion', 'ssion'], 'Les verbes en -er donnent le plus souvent -tion.', A11, 'invention', ('O11', c)),
      Q('exclure → une exclu___', 'sion', ['tion', 'ssion'], 'Les verbes en -clure donnent -sion.', A11, 'exclusion', ('O11', c)),
      Q('omettre → une omi___', 'ssion', ['tion', 'sion'], 'Les verbes en -mettre donnent -ssion.', A11, 'omission', ('O11', c)),
      Q('punir → une puni___', 'tion', ['sion', 'ssion'], 'Les verbes en -ir donnent -tion.', A11, 'punition', ('O11', c))],
     [P11('station', R_T, R_Z, R_S, 'Le plus fréquent.', '-tion'), P11('confusion', R_Z, R_S, R_T, 'Écoute le son avant -ion.', '-sion'),
      P11('commission', verbe('commettre'), R_Z, R_T, 'Cherche le verbe de la famille.', '-ssion'), P11('inauguration', R_T, R_Z, R_S, 'Le plus fréquent.', '-tion')]]
NIV['O11'] = {2: O11(2), 3: O11(3)}

# =============================== O12 : les adverbes en -ment (-emment, -amment au CM2 : écran propre, hors de cette liste) ===============================
A12 = 'Complète avec la bonne fin.'
def e12(c, p, bon, autres, hint, mot): return Q(p, bon, autres, hint, A12, mot, ('O12', c))
def M12(c, p, hint, mot): return e12(c, p, 'ment', ['ement', 'mant'], hint, mot)
def X12(c, p, hint, mot): return e12(c, p, 'ément', ['ement', 'ment'], hint, mot)
def P12(mot, fin, bon, a, b, hint): return C('Pourquoi %s dans « %s » ?' % (fin, mot), bon, a, b, hint)
def FEM12(c, p, f, mot): return M12(c, p, 'Le féminin « %s » + -ment.' % f, mot)
def VOY12(c, p, a, fin, mot): return M12(c, p, 'L’adjectif « %s » finit par %s.' % (a, fin), mot)
def ADJ12(c, p, a, mot): return M12(c, p, 'L’adjectif est « %s ».' % a, mot)
def O12(c):
    if c == 2:
        return [
         [FEM12(c, 'heureuse___', 'heureuse', 'heureusement'), FEM12(c, 'lente___', 'lente', 'lentement'), FEM12(c, 'douce___', 'douce', 'doucement'), FEM12(c, 'folle___', 'folle', 'follement')],
         [VOY12(c, 'hardi___', 'hardi', 'i', 'hardiment'), VOY12(c, 'étourdi___', 'étourdi', 'i', 'étourdiment'), VOY12(c, 'exagéré___', 'exagéré', 'é', 'exagérément'), VOY12(c, 'désespéré___', 'désespéré', 'é', 'désespérément')],
         [ADJ12(c, 'calme___', 'calme', 'calmement'), ADJ12(c, 'brave___', 'brave', 'bravement'), ADJ12(c, 'pauvre___', 'pauvre', 'pauvrement'), ADJ12(c, 'honnête___', 'honnête', 'honnêtement')],
         [X12(c, 'commod___', 'commode → commodément.', 'commodément'), X12(c, 'aveugl___', 'aveugle → aveuglément.', 'aveuglément'),
          X12(c, 'uniform___', 'uniforme → uniformément.', 'uniformément'), X12(c, 'obscur___', 'obscur → obscurément.', 'obscurément')],
         [P12('heureusement', '-ment', 'Parce que c’est le féminin « heureuse » + -ment.', 'Parce que c’est un nom.', 'Parce que le mot est court.', 'Le féminin + -ment.'),
          P12('hardiment', '-ment', 'Parce que « hardi » finit par une voyelle : + -ment.', 'Parce que c’est un nom.', 'Parce que le mot est court.', 'L’adjectif finit par i.'),
          P12('calmement', '-ment', 'Parce que « calme » finit par e : + -ment.', 'Parce que c’est un nom.', 'Parce que le mot est court.', 'Je cherche l’adjectif.'),
          P12('commodément', '-ément', 'Parce que c’est une exception à mémoriser.', 'Parce que c’est le féminin + -ment.', 'Parce que « commode » finit par une voyelle.', 'Je mémorise cette exception.')]]
    return [
     [FEM12(c, 'La petite fille avoue honteuse___ sa bêtise.', 'honteuse', 'honteusement'), FEM12(c, 'Le chat entre secrète___ dans la cuisine.', 'secrète', 'secrètement'),
      FEM12(c, 'Notre équipe joue active___ pendant tout le match.', 'active', 'activement'), FEM12(c, 'Elle quitte discrète___ la salle de classe.', 'discrète', 'discrètement')],
     [VOY12(c, 'Elle court éperdu___ vers la maison.', 'éperdu', 'u', 'éperdument'), VOY12(c, 'Le garçon répond effronté___ au maître.', 'effronté', 'é', 'effrontément'),
      VOY12(c, 'Le garçon répète obstiné___ la même question.', 'obstiné', 'é', 'obstinément'), VOY12(c, 'Il dépense son argent inconsidéré___ chaque semaine.', 'inconsidéré', 'é', 'inconsidérément')],
     [ADJ12(c, 'Le chat saute agile___ sur le mur.', 'agile', 'agilement'), ADJ12(c, 'L’élève répond modeste___ à la question.', 'modeste', 'modestement'),
      ADJ12(c, 'Le garçon sourit aimable___ à la voisine.', 'aimable', 'aimablement'), ADJ12(c, 'Il fait terrible___ froid ce matin.', 'terrible', 'terriblement')],
     [X12(c, 'Ce fruit est commun___ appelé « cerise ».', 'commun → communément.', 'communément'), X12(c, 'La lumière entre diffus___ dans la pièce.', 'diffus → diffusément.', 'diffusément'),
      X12(c, 'Le maître a express___ demandé le silence.', 'exprès → expressément.', 'expressément'), X12(c, 'Le facteur est arrivé inopin___ ce matin.', 'inopiné → inopinément.', 'inopinément')],
     [P12('honteusement', '-ment', 'Parce que c’est le féminin « honteuse » + -ment.', 'Parce que c’est un nom.', 'Parce que le mot est court.', 'Le féminin + -ment.'),
      P12('éperdument', '-ment', 'Parce que « éperdu » finit par une voyelle : + -ment.', 'Parce que c’est un nom.', 'Parce que le mot est court.', 'L’adjectif finit par u.'),
      P12('modestement', '-ment', 'Parce que « modeste » finit par e : + -ment.', 'Parce que c’est un nom.', 'Parce que le mot est court.', 'Je cherche l’adjectif.'),
      P12('communément', '-ément', 'Parce que c’est une exception à mémoriser.', 'Parce que c’est le féminin + -ment.', 'Parce que « commun » finit par une voyelle.', 'Je mémorise cette exception.')]]
NIV['O12'] = {2: O12(2), 3: O12(3)}

# =============================== contrôles et intégration ===============================
RACINE = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..')
INDEX = os.environ.get('INDEX_FICHIER') or os.path.join(RACINE, 'index.html')
def lire_json(s, nom):
    i = s.index('const ' + nom + '=') + len('const ' + nom + '=')
    j = s.index('\n', i)
    return json.loads(s[i:j].rstrip(';')), i, j
def controles(s):
    pb = []
    niv_ex, _, _ = lire_json(s, 'NIV_ATOI')
    plus, _, _ = lire_json(s, 'PLUS')
    cm2, _, _ = lire_json(s, 'CM2_PLUS')
    mots = set(w.strip() for w in open('/usr/share/dict/french', encoding='utf-8'))
    deja = {}
    for c in ('O8', 'O9', 'O10', 'O11', 'O12'):
        base = {json.dumps(e, ensure_ascii=False) for l in plus[c] for e in l}
        if c in cm2:
            for e in cm2[c]['ecrans']:
                for x in e.get('plus', []) + ([e['atoi']] if e.get('atoi') else []): base.add(json.dumps(x, ensure_ascii=False))
        L1 = []
        for cl in (2, 3):
            ec = NIV[c][cl]
            if len(ec) != len(plus[c]): pb.append('%s %d : %d écrans au lieu de %d' % (c, cl, len(ec), len(plus[c])))
            for k, l in enumerate(ec):
                if len(l) != 4: pb.append('%s classe %d écran %d : %d exercices au lieu de 4' % (c, cl, k, len(l)))
                for e in l:
                    j = json.dumps(e, ensure_ascii=False)
                    if j in base: pb.append('%s classe %d écran %d : exercice déjà présent : %s' % (c, cl, k, e['p'] or e['tasks'][0]['ask']))
                    L1.append((cl, k, e))
        vus = {}
        for cl, k, e in L1:
            cle = e['p'] or (e['tasks'][0]['ask'] + '→' + e['tasks'][0]['choose'][0])
            if cle in vus: pb.append('%s : exercice répété (classes %d et %d) : %s' % (c, vus[cle], cl, cle))
            vus[cle] = cl
    for c, cl, m, p, b in RECOMP:
        w = m.split(' ')[-1].replace('l’', '')
        if w not in p.replace('___', b).lower().replace('l’', ' ').split() and w not in p.replace('___', b).lower(): pb.append('%s classe %d : le trou ne redonne pas « %s » : %s' % (c, cl, m, p))
    OK_SANS_DICO = {'cœur', 'sœur', 'chœur'}
    for c, cl, m in CHECK:
        w = m.split(' ')[-1].lower().replace('l’', '')
        if w not in OK_SANS_DICO and w not in mots: pb.append('%s classe %d : mot absent du dictionnaire : %s' % (c, cl, m))
    # même mot dans les deux classes d'une ceinture
    par = {}
    for c, cl, m in CHECK: par.setdefault((c, m), set()).add(cl)
    FERMES = {'heure', 'beurre', 'demeure', 'leurre', 'cœur', 'sœur', 'chœur'}
    for (c, m), cls in par.items():
        if c != 'O8' and m.split(' ')[-1].replace('l’', '') not in FERMES and len(cls) > 1: pb.append('%s : le mot « %s » sert au CM1 et au CM2' % (c, m))
    return pb
def integrer():
    s = open(INDEX, encoding='utf-8').read()
    niv_ex, i, j = lire_json(s, 'NIV_ATOI')
    for c in ('O8', 'O9', 'O10', 'O11', 'O12'):
        niv_ex[c] = {'2': NIV[c][2], '3': NIV[c][3]}
    s = s[:i] + json.dumps(niv_ex, ensure_ascii=False) + s[j:]
    open(INDEX, 'w', encoding='utf-8').write(s)
    print('NIV_ATOI : O8 à O12 ajoutées (4 exercices par écran et par classe)')
if __name__ == '__main__':
    s = open(INDEX, encoding='utf-8').read()
    pb = controles(s)
    for c in ('O8', 'O9', 'O10', 'O11', 'O12'):
        print('==', c, [len(l) for l in NIV[c][2]], [len(l) for l in NIV[c][3]])
        if '--liste' in sys.argv:
            for cl in (2, 3):
                for k, l in enumerate(NIV[c][cl]):
                    for e in l: print('  CM%d é%d' % (cl - 1, k), e['p'] or e['tasks'][0]['ask'], '→', e['tasks'][0]['choose'][0])
    print('\n'.join(pb) if pb else 'contrôles : aucun problème')
    if '--integrer' in sys.argv:
        if pb: sys.exit('Corriger d’abord les problèmes ci-dessus.')
        integrer()
