"""Leçons O7 (refaite : « e, é, è, ê : accent ou pas », CE2) et O8 à O12 (CM1 et CM2 : la formation des mots), 11/11/2026,
programmation d'orthographe sur 3 ans (idée 203 du tableau de bord, dépôt `ressources`). Même plan que o1_a_o6.py : 5 cadres, des écrans animés, un exercice « À toi ! » et deux en plus.
Usage : python3 lecons/o7_o12.py   puis   python3 inserer.py O7-CE2 O8 O9 O10 O11 O12"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
import re
from mapgen import build, TL, TC, TR
from lhelp import *
from hlib import A

BL = (18, 568, 560, 350)
BR = (612, 568, 770, 350)
COL = {'bleu': '#1f5fc4', 'vert': '#23845a', 'orange': '#e67e22', 'violet': '#7b3fa0', 'rouge': '#c62828'}


def M(t):
    t = re.sub(r'%([^%]+)%', r'<span style="background:#ffe066;border-radius:4px;padding:0 1px;font-weight:700">\1</span>', t)
    t = re.sub(r'\|([^|]+)\|', r'<span style="border:2.5px solid #c62828;border-radius:12px;padding:0 3px;font-weight:700">\1</span>', t)
    return t.replace('→', A)


def ex(*lines, size=21):
    return f'<div class="exl" style="font-size:{size+3}px;line-height:1.6;margin-top:12px">' + '<br>'.join(M(l) for l in lines) + '</div>'


def txt(t, pr=0):
    return f'<p class="txt" style="padding-right:{pr}px;font-size:22px">{M(t)}</p>'


LEG = '<span style="background:#ffe066;font-weight:700;padding:0 4px">lettres étudiées</span> · <span style="border:2.5px solid #c62828;border-radius:12px;padding:0 5px;font-weight:700">ce qui décide</span>'
H = 'hl'


def lesson(lid, belt, niveau, titre, sous, maptitle, boxes, ecrans, title_size=None, **trace):
    title_size = title_size or (32 if lid == 'O11' else 38)
    geoms = [TL, TC, TR, BL, BR]
    cols = ['bleu', 'vert', 'orange', 'violet', 'rouge']
    bx = []
    for k, (bid, btitle, html) in enumerate(boxes):
        b = dict(id=bid, col=cols[k], geom=geoms[k], title=btitle, html=html)
        if k == 0: b['avatar'] = ('girl', 322, 122)
        if k == 3: b['avatar'] = ('boy', 445, 610); b['style'] = 'padding-top:52px'
        if k == 4: b['style'] = 'padding-top:52px'
        bx.append(b)
    out, zones = build(lid, maptitle, f'Orthographe — {lid.split("-")[0]} — {niveau}', LEG, bx, title_size=title_size, legend_pos='left:470px;top:880px')
    sections = [{'id': b[0], 'nom': b[1], 'couleur': COL[cols[k]]} for k, b in enumerate(boxes)]
    t = {'id': lid, 'f': 'O', 'ceinture': belt, 'titre': titre, 'sous': sous, 'lesson': True}
    if '-' in lid: t = {'id': lid, 'code': lid.split('-')[0], 'niveau': niveau, **{k: v for k, v in t.items() if k != 'id'}}      # leçon d'un seul niveau (O7-CE2)
    t.update(trace)
    save(lid, t, sections, ecrans, zones)


def prouve(*qs):
    return qs


# ================================================================ O7 : e, é, è, ê (CE2)
lesson('O7-CE2', 'Violette', 'CE2', 'e, é, è, ê : accent ou pas', 'é, e sans accent, è, ê', 'e, é, è, ê<br><small>accent ou pas ?</small>', [
 ('eaigu', 'J’écris é', txt('Quand j’entends <b>[é]</b>, j’écris <b>é</b>.', 100) + ex('une %é%cole', 'la sant%é%', 'une id%é%e')),
 ('e', 'J’écris e', txt('<b>Deux consonnes</b> après, ou une consonne à la <b>fin</b> : <b>e</b> sans accent.') + ex('b%e%|ll|e · t%e%|rr|e', 'la m%e%|r| · le s%e%|l|', size=20)),
 ('egrave', 'J’écris è', txt('Une consonne, puis un <b>e muet</b> : <b>è</b>.') + ex('la m%è%|r|e', 'la rivi%è%|r|e', 'le progr%è%s · le succ%è%s', size=19)),
 ('ecirc', 'J’écris ê', txt('Le <b>ê</b> : je <b>mémorise</b> ces mots.', 110) + ex('la t%ê%te · la f%ê%te', 'la for%ê%t · la b%ê%te', size=20)),
 ('prouve', 'Je prouve', txt('Je regarde <b>ce qui suit</b>.') + ex('b%e%|ll|e : deux consonnes → e', 'm%è%|r|e : une consonne + e muet → è', 'une %é%cole : j’entends [é] → é', size=19)),
], [
 E('eaigu', 'point', 'J’écris é', 'girl', 'Quand j’entends [é], j’écris é.',
   ['une %é%cole', 'la sant%é%', ('une id%é%e', 'Le son [é], bouche presque fermée : é.')],
   Q('une ___cole', ['é', 'e', 'è'], 'J’entends [é].', 'Complète avec la bonne lettre.', fill=H),
   [Q('la sant___', ['é', 'e', 'è'], 'J’entends [é] à la fin.', 'Complète avec la bonne lettre.', fill=H),
    Q('un ___lève', ['é', 'e', 'è'], 'J’entends [é] au début.', 'Complète avec la bonne lettre.', fill=H)]),
 E('e', 'attention', 'J’écris e', 'boy', 'Deux consonnes après, ou une consonne finale : e sans accent.',
   ['b%e%|ll|e', 't%e%|rr|e', ('la m%e%|r|', 'Deux consonnes, ou une consonne à la fin : e, sans accent.')],
   Q('la t___rre', ['e', 'é', 'è'], 'Deux consonnes suivent : rr.', 'Complète avec la bonne lettre.', fill=H),
   [Q('une b___lle fleur', ['e', 'é', 'è'], 'Deux consonnes suivent : ll.', 'Complète avec la bonne lettre.', fill=H),
    Q('le s___l', ['e', 'é', 'è'], 'Une consonne à la fin du mot.', 'Complète avec la bonne lettre.', fill=H)]),
 E('egrave', 'mots', 'J’écris è', 'girl', 'Une consonne, puis un e muet : è.',
   ['la m%è%|r|e', 'la rivi%è%|r|e', ('un probl%è%|m|e', 'Une consonne, puis un e muet : è.')],
   Q('la derni___re', ['è', 'e', 'é'], 'Une consonne puis un e muet : r + e.', 'Complète avec la bonne lettre.', fill=H),
   [Q('la lumi___re', ['è', 'e', 'é'], 'Une consonne puis un e muet : r + e.', 'Complète avec la bonne lettre.', fill=H),
    Q('un syst___me', ['è', 'e', 'é'], 'Une consonne puis un e muet : m + e.', 'Complète avec la bonne lettre.', fill=H)]),
 E('egrave', 'liste', 'è avant s', 'boy', 'À la fin de quelques mots, è s’écrit devant s : à mémoriser.',
   ['le progr%è%s', 'le succ%è%s', ('l’acc%è%s', 'Je mémorise ces trois mots.')],
   Q('le succ___s', ['è', 'e', 'é'], 'Un mot à mémoriser.', 'Complète avec la bonne lettre.', fill=H),
   [Q('le progr___s', ['è', 'e', 'é'], 'Un mot à mémoriser.', 'Complète avec la bonne lettre.', fill=H),
    Q('l’acc___s', ['è', 'e', 'é'], 'Un mot à mémoriser.', 'Complète avec la bonne lettre.', fill=H)]),
 E('ecirc', 'etiquette', 'J’écris ê', 'girl', 'Le ê : je mémorise ces mots.',
   ['la t%ê%te', 'la f%ê%te', ('la for%ê%t', 'Ces mots, je les mémorise.')],
   Q('', ['la tête', 'la tete', 'la tète'], 'Un mot avec ê.', 'Quel mot est bien écrit ?'),
   [Q('', ['la fête', 'la fete', 'la fète'], 'Un mot avec ê.', 'Quel mot est bien écrit ?'),
    Q('', ['la forêt', 'la foret', 'la forèt'], 'Un mot avec ê.', 'Quel mot est bien écrit ?')]),
 E('prouve', 'coche', 'Je prouve', 'boy', 'Je regarde ce qui suit.',
   ['b%e%lle', ('b%e%|ll|e', 'Je prouve : deux consonnes (ll) → e, sans accent.'), ('m%è%|r|e', 'Je prouve : une consonne et un e muet → è.')],
   Q('', ['Parce qu’il y a deux consonnes après : ll.', 'Parce que c’est un adjectif.', 'Parce que le mot est court.'], 'Regarde ce qui suit.', 'Pourquoi e sans accent dans « belle » ?'),
   [Q('', ['Parce qu’il y a une consonne puis un e muet.', 'Parce que c’est un nom.', 'Parce que c’est un mot court.'], 'Regarde ce qui suit.', 'Pourquoi è dans « mère » ?'),
    Q('', ['Parce que j’entends [é].', 'Parce qu’il y a deux consonnes.', 'Parce que c’est un nom.'], 'Écoute le son.', 'Pourquoi é dans « école » ?')]),
])

# ================================================================ O8 : -é, -ée, -té, -tié
lesson('O8', 'Marron', 'CM1', 'Les noms en [é]', '-é, -ée, -té, -tié', 'Les noms en [é]<br><small>-é, -ée, -té, -tié</small>', [
 ('masc', 'Masculin : -é', txt('Un nom <b>masculin</b> : <b>-é</b>, sans e.', 100) + ex('un caf%é%', 'un bl%é%', 'un march%é%')),
 ('fem', 'Féminin : -ée', txt('Un nom <b>féminin</b> : <b>-ée</b>, avec e.') + ex('une id%ée%', 'une journ%ée%', 'une ann%ée%', size=20)),
 ('te', 'Une qualité : -té', txt('Une <b>qualité</b>, un <b>état</b> : <b>-té</b>, sans e.') + ex('la san%té%', 'la liber%té%', 'la beau%té%', size=20)),
 ('tie', 'Trois noms : -tié', txt('Je <b>mémorise</b> ces trois noms.', 110) + ex('la moi%tié%', 'l’ami%tié%', 'la pi%tié%', size=20)),
 ('prouve', 'Je prouve', txt('Je regarde <b>le genre</b> du nom.') + ex('un caf%é% : masculin → é', 'une id%ée% : féminin → ée', 'la san%té% : un état → té', size=19)),
], [
 E('masc', 'point', 'Masculin : -é', 'girl', 'Un nom masculin en [é] s’écrit -é, sans e.',
   ['un caf%é%', 'un bl%é%', ('un march%é%', 'Un, le : masculin → -é.')],
   Q('un foss___', ['é', 'ée', 'er'], 'Le nom est masculin : un fossé.', 'Complète avec la bonne fin.', fill=H),
   [Q('un canap___', ['é', 'ée', 'er'], 'Le nom est masculin : un canapé.', 'Complète avec la bonne fin.', fill=H),
    Q('le th___', ['é', 'ée', 'er'], 'Le nom est masculin : le thé.', 'Complète avec la bonne fin.', fill=H)]),
 E('fem', 'mots', 'Féminin : -ée', 'boy', 'Un nom féminin en [é] s’écrit -ée, avec e.',
   ['une id%ée%', 'une journ%ée%', ('une ann%ée%', 'Une, la : féminin → -ée.')],
   Q('une araign___', ['ée', 'é', 'er'], 'Le nom est féminin : une araignée.', 'Complète avec la bonne fin.', fill=H),
   [Q('une pens___', ['ée', 'é', 'er'], 'Le nom est féminin : une pensée.', 'Complète avec la bonne fin.', fill=H),
    Q('une soir___', ['ée', 'é', 'er'], 'Le nom est féminin : une soirée.', 'Complète avec la bonne fin.', fill=H)]),
 E('te', 'attention', 'Une qualité : -té', 'girl', 'Un nom féminin qui dit une qualité ou un état s’écrit -té, sans e.',
   ['la san%té%', 'la liber%té%', ('la beau%té%', 'Une qualité, un état : -té, sans e.')],
   Q('la fier___', ['té', 'tée', 'tié'], 'C’est une qualité : la fierté.', 'Complète avec la bonne fin.', fill=H),
   [Q('la bon___', ['té', 'tée', 'tié'], 'C’est une qualité : la bonté.', 'Complète avec la bonne fin.', fill=H),
    Q('la vérit___', ['é', 'ée', 'ier'], 'C’est une vérité : -té, sans e.', 'Complète avec la bonne fin.', fill=H)]),
 E('tie', 'etiquette', 'Trois noms : -tié', 'boy', 'Trois noms s’écrivent -tié : je les mémorise.',
   ['la moi%tié%', 'l’ami%tié%', ('la pi%tié%', 'Trois noms seulement : je les mémorise.')],
   Q('', ['la moitié', 'la moité', 'la moitiée'], 'Un nom à mémoriser.', 'Quel mot est bien écrit ?'),
   [Q('', ['l’amitié', 'l’amité', 'l’amitiée'], 'Un nom à mémoriser.', 'Quel mot est bien écrit ?'),
    Q('', ['la pitié', 'la pité', 'la pitiée'], 'Un nom à mémoriser.', 'Quel mot est bien écrit ?')]),
 E('prouve', 'coche', 'Je prouve', 'girl', 'Je regarde le genre du nom.',
   ['un caf%é%', ('un caf%é%', 'Je prouve : un café, masculin → -é.'), ('une id%ée%', 'Je prouve : une idée, féminin → -ée.')],
   Q('', ['Parce que c’est un nom masculin.', 'Parce que c’est un nom féminin.', 'Parce que le mot est court.'], 'Regarde le petit mot devant : un.', 'Pourquoi -é dans « café » ?'),
   [Q('', ['Parce que c’est un nom féminin.', 'Parce que c’est un nom masculin.', 'Parce que c’est un animal.'], 'Regarde le petit mot devant : une.', 'Pourquoi -ée dans « journée » ?'),
    Q('', ['Parce que c’est une qualité ou un état.', 'Parce que c’est un nom masculin.', 'Parce que le mot est long.'], 'Une qualité, un état.', 'Pourquoi -té dans « santé » ?')]),
])

# ================================================================ O9 : les consonnes doubles
lesson('O9', 'Noire', 'CM1', 'Les consonnes doubles', 'début de mot et famille', 'Les consonnes<br>doubles', [
 ('debut', 'Début du mot', txt('Après <b>a-, e-, o-</b> ou <b>com-</b>, la consonne <b>se double</b>.', 100) + ex('a%pp%eler · a%cc%ident', 'a%tt%endre · e%ff%ort', 'o%ff%rir · co%mm%e', size=20)),
 ('exceptions', 'Quelques exceptions', txt('Je les <b>mémorise</b>.') + ex('a%p%rès · a%p%ercevoir', 'l’a%t%elier · l’a%t%ome', size=20)),
 ('famille', 'La famille m’aide', txt('Un mot de la <b>même famille</b> montre la consonne doublée.') + ex('donner → un do%nn%eur', 'une po%mm%e → un po%mm%ier', 'la te%rr%e → la te%rr%asse', size=19)),
 ('verif', 'Je vérifie', txt('Je cherche : <b>a-, e-, o-, com-</b> au début ? Un mot de la <b>famille</b> ?', 110) + ex('a|p|peler : début en a-', 'ballon : balle', size=20)),
 ('prouve', 'Je prouve', txt('Je donne <b>ma preuve</b>.') + ex('a%pp%eler : début en a- → pp', 'do%nn%eur : donner', 'a%p%rès : une exception', size=19)),
], [
 E('debut', 'point', 'Début du mot', 'girl', 'Après a-, e-, o- ou com-, la consonne se double.',
   ['a%pp%eler', 'a%cc%ident', ('a%tt%endre', 'Au début du mot, après a- : la consonne se double.')],
   Q('a___endre', ['tt', 't'], 'Le mot commence par a-.', 'Complète : consonne simple ou double ?', fill=H),
   [Q('a___rocher', ['pp', 'p'], 'Le mot commence par a-.', 'Complète : consonne simple ou double ?', fill=H),
    Q('a___uyer', ['pp', 'p'], 'Le mot commence par a-.', 'Complète : consonne simple ou double ?', fill=H)]),
 E('debut', 'mots', 'e-, o-, com-', 'boy', 'Après e-, o- ou com-, la consonne se double aussi.',
   ['e%ff%ort', 'o%ff%rir', ('co%mm%e', 'e-, o-, com- : la consonne se double.')],
   Q('o___rir', ['ff', 'f'], 'Le mot commence par o-.', 'Complète : consonne simple ou double ?', fill=H),
   [Q('e___ort', ['ff', 'f'], 'Le mot commence par e-.', 'Complète : consonne simple ou double ?', fill=H),
    Q('co___encer', ['mm', 'm'], 'Le mot commence par com-.', 'Complète : consonne simple ou double ?', fill=H)]),
 E('exceptions', 'attention', 'Quelques exceptions', 'girl', 'Quelques mots ne doublent pas la consonne : je les mémorise.',
   ['a%p%rès', 'a%p%ercevoir', ('l’a%t%elier', 'Une seule consonne : je mémorise.')],
   Q('', ['après', 'appès', 'apprès'], 'Une exception.', 'Quel mot est bien écrit ?'),
   [Q('', ['un atelier', 'un attelier', 'un attellier'], 'Une exception.', 'Quel mot est bien écrit ?'),
    Q('', ['apercevoir', 'appercevoir', 'apperçevoir'], 'Une exception.', 'Quel mot est bien écrit ?')]),
 E('famille', 'famille', 'La famille m’aide', 'boy', 'Un mot de la même famille montre la consonne doublée.',
   ['un do%nn%eur → donner', 'une po%mm%e → un po%mm%ier', ('la te%rr%e → la te%rr%asse', 'Même famille : même consonne doublée.')],
   Q('un do___eur', ['nn', 'n'], 'Pense à donner.', 'Complète : consonne simple ou double ?', fill=H),
   [Q('la te___asse', ['rr', 'r'], 'Pense à terre.', 'Complète : consonne simple ou double ?', fill=H),
    Q('un ba___on', ['ll', 'l'], 'Pense à balle.', 'Complète : consonne simple ou double ?', fill=H)]),
 E('verif', 'liste', 'Je vérifie', 'girl', 'Je cherche le début du mot ou un mot de la famille.',
   ['a|pp|eler : le mot commence par a-', ('ba|ll|on : balle', 'Un mot de la famille m’aide.'), 'a|p|rès : une exception'],
   Q('', ['a-, e-, o- ou com- au début du mot.', 'La longueur du mot.', 'Le nombre de lettres.'], 'Regarde le début du mot.', 'Qu’est-ce qui annonce souvent une consonne doublée ?'),
   [Q('', ['Je cherche un mot de la même famille.', 'Je compte les lettres.', 'Je regarde la fin du mot.'], 'Pense à la famille.', 'Comment vérifier une consonne doublée à l’intérieur du mot ?')]),
 E('prouve', 'coche', 'Je prouve', 'boy', 'Je donne ma preuve.',
   ['a%pp%eler', ('a%pp%eler', 'Je prouve : le mot commence par a- → pp.'), ('un do%nn%eur', 'Je prouve : donner a deux n → donneur aussi.')],
   Q('', ['Parce que le mot commence par a-.', 'Parce que c’est un verbe.', 'Parce que le mot est long.'], 'Regarde le début du mot.', 'Pourquoi pp dans « appeler » ?'),
   [Q('', ['Parce que dans « donner » il y a deux n.', 'Parce que c’est un nom.', 'Parce que le mot est court.'], 'Pense à donner.', 'Pourquoi nn dans « donneur » ?'),
    Q('', ['Parce que c’est une exception.', 'Parce que le mot est court.', 'Parce que c’est un nom.'], 'Je mémorise.', 'Pourquoi une seule consonne dans « après » ?')]),
])

# ================================================================ O10 : les noms en -eur
lesson('O10', 'Or', 'CM1', 'Les noms en -eur', 'sans e', 'Les noms en -eur<br><small>sans e</small>', [
 ('eur', 'J’écris -eur', txt('Un nom en <b>[œr]</b> : <b>-eur</b>, sans e.', 100) + ex('le bonh%eur%', 'la coul%eur%', 'la p%eur%', size=20)),
 ('verbe', 'Le verbe m’aide', txt('Un nom d’<b>agent</b> : je pense au <b>verbe</b>.') + ex('chanter → un chant%eur%', 'voler → un vol%eur%', 'danser → un dans%eur%', size=19)),
 ('exc', 'Exceptions', txt('Je les <b>mémorise</b>.') + ex('l’h%eure% · la dem%eure%', 'le b%eurre% · le l%eurre%', size=20)),
 ('coeur', 'cœur, sœur, chœur', txt('<b>œur</b> : trois noms à <b>mémoriser</b>.', 110) + ex('le c%œur%', 'la s%œur%', 'le ch%œur%', size=20)),
 ('prouve', 'Je prouve', txt('Je cherche le <b>verbe</b>, sinon je <b>mémorise</b>.') + ex('un chant%eur% : chanter', 'la coul%eur% : sans e', 'l’h%eure% : une exception', size=19)),
], [
 E('eur', 'point', 'J’écris -eur', 'girl', 'Un nom en [œr] s’écrit -eur, sans e.',
   ['le bonh%eur%', 'la coul%eur%', ('la p%eur%', 'Un nom en [œr] : -eur, sans e.')],
   Q('la chal___', ['eur', 'eure', 'œur'], 'Un nom en [œr] : la chaleur.', 'Complète avec la bonne fin.', fill=H),
   [Q('le malh___', ['eur', 'eure', 'œur'], 'Un nom en [œr] : le malheur.', 'Complète avec la bonne fin.', fill=H),
    Q('une fl___', ['eur', 'eure', 'œur'], 'Un nom en [œr] : une fleur.', 'Complète avec la bonne fin.', fill=H)]),
 E('verbe', 'remplacer', 'Le verbe m’aide', 'boy', 'Pour un nom d’agent, je pense au verbe.',
   ['chanter → un chant%eur%', 'voler → un vol%eur%', ('danser → un dans%eur%', 'Le nom d’agent finit par -eur.')],
   Q('un nag___', ['eur', 'eure', 'œur'], 'Pense à nager.', 'Complète avec la bonne fin.', fill=H),
   [Q('un coiff___', ['eur', 'eure', 'œur'], 'Pense à coiffer.', 'Complète avec la bonne fin.', fill=H),
    Q('un jou___', ['eur', 'eure', 'œur'], 'Pense à jouer.', 'Complète avec la bonne fin.', fill=H)]),
 E('exc', 'attention', 'Exceptions', 'girl', 'Quelques noms ont un e : je les mémorise.',
   ['l’h%eure%', 'la dem%eure%', ('le b%eurre%', 'Des exceptions : je les mémorise.')],
   Q('l’h___', ['eure', 'eur', 'œur'], 'Une exception.', 'Complète avec la bonne fin.', fill=H),
   [Q('la dem___', ['eure', 'eur', 'œur'], 'Une exception.', 'Complète avec la bonne fin.', fill=H),
    Q('le b___', ['eurre', 'eur', 'eure'], 'Une exception.', 'Complète avec la bonne fin.', fill=H)]),
 E('coeur', 'etiquette', 'cœur, sœur, chœur', 'boy', 'Trois noms s’écrivent œur : je les mémorise.',
   ['le c%œur%', 'la s%œur%', ('le ch%œur%', 'Trois noms seulement.')],
   Q('', ['le cœur', 'le queur', 'le keur'], 'Un nom à mémoriser.', 'Quel mot est bien écrit ?'),
   [Q('', ['la sœur', 'la seur', 'la soeur'], 'Un nom à mémoriser.', 'Quel mot est bien écrit ?'),
    Q('', ['le chœur', 'le cheur', 'le koeur'], 'Un nom à mémoriser.', 'Quel mot est bien écrit ?')]),
 E('prouve', 'coche', 'Je prouve', 'girl', 'Je cherche le verbe, sinon je mémorise.',
   ['un chant%eur%', ('un chant%eur%', 'Je prouve : chanter → un chanteur, -eur sans e.'), ('l’h%eure%', 'Je prouve : c’est une exception, je la mémorise.')],
   Q('', ['Parce qu’un nom en [œr] s’écrit -eur.', 'Parce que le mot est court.', 'Parce que c’est un animal.'], 'Pense à chanter.', 'Pourquoi -eur dans « chanteur » ?'),
   [Q('', ['Parce que c’est une exception.', 'Parce que c’est un verbe.', 'Parce que le mot est long.'], 'Je mémorise.', 'Pourquoi un e dans « heure » ?'),
    Q('', ['Parce que c’est un des trois noms en œur.', 'Parce que c’est un verbe.', 'Parce que le mot est court.'], 'Je mémorise.', 'Pourquoi œur dans « sœur » ?')]),
])

# ================================================================ O11 : -tion, -sion, -ssion
lesson('O11', 'Argent', 'CM1', 'Les noms en [sjɔ̃]', '-tion, -sion, -ssion', 'Les noms en [sjɔ̃]<br><small>-tion, -sion, -ssion</small>', [
 ('tion', 'J’écris -tion', txt('L’écriture <b>la plus fréquente</b> : <b>-tion</b>.', 100) + ex('une na%tion%', 'une ac%tion%', 'une inven%tion%', size=20)),
 ('sion', 'J’écris -sion', txt('Après une <b>voyelle</b>, j’entends <b>[z]</b> ; après <b>n, r, l</b> aussi : <b>-sion</b>.') + ex('une déci%sion% · la vi%sion%', 'la ten%sion% · la ver%sion%', size=19)),
 ('ssion', 'J’écris -ssion', txt('Entre deux <b>voyelles</b>, pour le son [s] : <b>ss</b>.') + ex('une mi%ssion%', 'une pa%ssion%', 'une permi%ssion%', size=20)),
 ('famille', 'Le verbe m’aide', txt('Je pense au <b>verbe</b> de la famille.', 110) + ex('décider → une déci%sion%', 'permettre → une permi%ssion%', 'inventer → une inven%tion%', size=18)),
 ('prouve', 'Je prouve', txt('Je regarde <b>la lettre avant</b> et je pense au <b>verbe</b>.') + ex('une déci%sion% : après i, [z]', 'une mi%ssion% : entre deux voyelles, [s]', 'une na%tion% : le plus fréquent', size=18)),
], [
 E('tion', 'point', 'J’écris -tion', 'girl', 'Le son [sjɔ̃] s’écrit le plus souvent -tion.',
   ['une na%tion%', 'une ac%tion%', ('une inven%tion%', 'L’écriture la plus fréquente : -tion.')],
   Q('une sta___', ['tion', 'sion', 'ssion'], 'Le plus fréquent : -tion.', 'Complète avec la bonne fin.', fill=H),
   [Q('une solu___', ['tion', 'sion', 'ssion'], 'Le plus fréquent : -tion.', 'Complète avec la bonne fin.', fill=H),
    Q('une informa___', ['tion', 'sion', 'ssion'], 'Pense à informer.', 'Complète avec la bonne fin.', fill=H)]),
 E('sion', 'mots', 'J’écris -sion', 'boy', 'Après une voyelle, j’entends [z] : -sion. Après n, r, l : -sion aussi.',
   ['une déci%sion%', 'la télévi%sion%', ('la ten%sion%', 'Après n, r, l : -sion.')],
   Q('une divi___', ['sion', 'tion', 'ssion'], 'Après i, j’entends [z].', 'Complète avec la bonne fin.', fill=H),
   [Q('la ver___', ['sion', 'tion', 'ssion'], 'Après r : -sion.', 'Complète avec la bonne fin.', fill=H),
    Q('une explo___', ['sion', 'tion', 'ssion'], 'Après o, j’entends [z] : exploser.', 'Complète avec la bonne fin.', fill=H)]),
 E('ssion', 'attention', 'J’écris -ssion', 'girl', 'Entre deux voyelles, pour le son [s], j’écris ss.',
   ['une mi%ssion%', 'une pa%ssion%', ('une permi%ssion%', 'Un seul s entre deux voyelles ferait [z] : ss.')],
   Q('une discu___', ['ssion', 'sion', 'tion'], 'Entre deux voyelles : [s] → ss.', 'Complète avec la bonne fin.', fill=H),
   [Q('une profe___', ['ssion', 'sion', 'tion'], 'Entre deux voyelles : [s] → ss.', 'Complète avec la bonne fin.', fill=H),
    Q('une pre___', ['ssion', 'sion', 'tion'], 'Entre deux voyelles : [s] → ss.', 'Complète avec la bonne fin.', fill=H)]),
 E('famille', 'famille', 'Le verbe m’aide', 'boy', 'Je pense au verbe de la même famille.',
   ['décider → une déci%sion%', 'permettre → une permi%ssion%', ('inventer → une inven%tion%', 'Le verbe m’aide.')],
   Q('une admi___', ['ssion', 'sion', 'tion'], 'Pense à admettre.', 'Complète avec la bonne fin.', fill=H),
   [Q('une révi___', ['sion', 'tion', 'ssion'], 'Pense à réviser.', 'Complète avec la bonne fin.', fill=H),
    Q('une imita___', ['tion', 'sion', 'ssion'], 'Pense à imiter.', 'Complète avec la bonne fin.', fill=H)]),
 E('prouve', 'coche', 'Je prouve', 'girl', 'Je regarde la lettre avant et je pense au verbe.',
   ['une déci%sion%', ('une déci%sion%', 'Je prouve : après i, j’entends [z] → -sion.'), ('une mi%ssion%', 'Je prouve : entre deux voyelles, [s] → -ssion.')],
   Q('', ['Parce qu’après i, j’entends [z].', 'Parce que le mot est long.', 'Parce que c’est un verbe.'], 'Écoute le son avant -ion.', 'Pourquoi -sion dans « décision » ?'),
   [Q('', ['Parce qu’entre deux voyelles, [s] s’écrit ss.', 'Parce que le mot est court.', 'Parce que c’est un animal.'], 'Un seul s ferait [z].', 'Pourquoi -ssion dans « mission » ?'),
    Q('', ['Parce que c’est l’écriture la plus fréquente.', 'Parce que le mot est court.', 'Parce que c’est un verbe.'], 'Le plus fréquent.', 'Pourquoi -tion dans « nation » ?')]),
])

# ================================================================ O12 : les adverbes en -ment
lesson('O12', 'Rouge', 'CM1', 'Les adverbes en -ment', 'adjectif + -ment', 'Les adverbes<br>en -ment', [
 ('fem', 'Le féminin + -ment', txt('Je pars de l’<b>adjectif au féminin</b>, j’ajoute <b>-ment</b>.', 100) + ex('lente → lente%ment%', 'douce → douce%ment%', 'heureuse → heureuse%ment%', size=19)),
 ('voyelle', 'Une voyelle + -ment', txt('Si l’adjectif finit par une <b>voyelle</b> : j’ajoute <b>-ment</b>.') + ex('vrai → vrai%ment%', 'poli → poli%ment%', 'absolu → absolu%ment%', size=20)),
 ('adj', 'Je cherche l’adjectif', txt('Je cherche d’<b>où vient</b> l’adverbe.') + ex('rapide%ment% : rapide', 'simple%ment% : simple', 'facile%ment% : facile', size=20)),
 ('mem', 'À mémoriser', txt('Quelques adverbes très courants : je les <b>mémorise</b>.', 110) + ex('seule%ment% · telle%ment%', 'vrai%ment% · finale%ment%', size=20)),
 ('prouve', 'Je prouve', txt('Je donne l’<b>adjectif</b> d’où vient l’adverbe.') + ex('lente%ment% : lent, lente', 'vrai%ment% : vrai', 'seule%ment% : seul, seule', size=19)),
], [
 E('fem', 'point', 'Le féminin + -ment', 'girl', 'Je pars de l’adjectif au féminin et j’ajoute -ment.',
   ['lente → lente%ment%', 'douce → douce%ment%', ('heureuse → heureuse%ment%', 'Le féminin de l’adjectif + -ment.')],
   Q('sérieuse___', ['ment', 'ement', 'mant'], 'Le féminin « sérieuse » + -ment.', 'Complète avec la bonne fin.', fill=H),
   [Q('franche___', ['ment', 'ement', 'mant'], 'Le féminin « franche » + -ment.', 'Complète avec la bonne fin.', fill=H),
    Q('calme___', ['ment', 'ement', 'mant'], 'L’adjectif « calme » + -ment.', 'Complète avec la bonne fin.', fill=H)]),
 E('voyelle', 'mots', 'Une voyelle + -ment', 'boy', 'Si l’adjectif finit par une voyelle, j’ajoute -ment.',
   ['vrai → vrai%ment%', 'poli → poli%ment%', ('absolu → absolu%ment%', 'Une voyelle + -ment.')],
   Q('joli___', ['ment', 'ement', 'mant'], 'L’adjectif « joli » finit par i.', 'Complète avec la bonne fin.', fill=H),
   [Q('résolu___', ['ment', 'ement', 'mant'], 'L’adjectif « résolu » finit par u.', 'Complète avec la bonne fin.', fill=H),
    Q('vrai___', ['ment', 'ement', 'mant'], 'L’adjectif « vrai » finit par i.', 'Complète avec la bonne fin.', fill=H)]),
 E('adj', 'remplacer', 'Je cherche l’adjectif', 'girl', 'Je cherche d’où vient l’adverbe.',
   ['rapide → rapide%ment%', 'facile → facile%ment%', ('simple → simple%ment%', 'Je retrouve l’adjectif.')],
   Q('simple___', ['ment', 'ement', 'mant'], 'L’adjectif est « simple ».', 'Complète avec la bonne fin.', fill=H),
   [Q('triste___', ['ment', 'ement', 'mant'], 'L’adjectif est « triste ».', 'Complète avec la bonne fin.', fill=H),
    Q('vive___', ['ment', 'ement', 'mant'], 'Le féminin de « vif » est « vive ».', 'Complète avec la bonne fin.', fill=H)]),
 E('mem', 'etiquette', 'À mémoriser', 'boy', 'Quelques adverbes très courants : je les mémorise.',
   ['seule%ment%', 'telle%ment%', ('vrai%ment%', 'Des adverbes très fréquents.')],
   Q('', ['seulement', 'seulment', 'seulemant'], 'Un adverbe à mémoriser.', 'Quel mot est bien écrit ?'),
   [Q('', ['tellement', 'tellment', 'tellemant'], 'Un adverbe à mémoriser.', 'Quel mot est bien écrit ?'),
    Q('', ['vraiment', 'vraiement', 'vraimant'], 'Un adverbe à mémoriser.', 'Quel mot est bien écrit ?')]),
 E('prouve', 'coche', 'Je prouve', 'girl', 'Je donne l’adjectif d’où vient l’adverbe.',
   ['lente%ment%', ('lente%ment%', 'Je prouve : lent, lente + -ment.'), ('vrai%ment%', 'Je prouve : vrai finit par une voyelle, + -ment.')],
   Q('', ['Parce que c’est le féminin « lente » + -ment.', 'Parce que le mot est long.', 'Parce que c’est un nom.'], 'Cherche l’adjectif.', 'Pourquoi -ment dans « lentement » ?'),
   [Q('', ['Parce que « vrai » finit par une voyelle : + -ment.', 'Parce que le mot est court.', 'Parce que c’est un nom.'], 'Cherche l’adjectif.', 'Pourquoi -ment dans « vraiment » ?'),
    Q('', ['Parce que le féminin de « doux » est « douce ».', 'Parce que le mot est long.', 'Parce que c’est un verbe.'], 'Cherche l’adjectif.', 'Pourquoi douce dans « doucement » ?')]),
])
