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
    """même code que les écrans : %lettres étudiées% en jaune, |lettre qui décide| entourée"""
    t = re.sub(r'%([^%]+)%', r'<span style="background:#ffe066;border-radius:4px;padding:0 1px;font-weight:700">\1</span>', t)
    t = re.sub(r'\|([^|]+)\|', r'<span style="border:2.5px solid #c62828;border-radius:12px;padding:0 3px;font-weight:700">\1</span>', t)
    return t.replace('→', A)


def ex(*lines, size=21):
    return f'<div class="exl" style="font-size:{size+3}px;line-height:1.6;margin-top:12px">' + '<br>'.join(M(l) for l in lines) + '</div>'


def txt(t, pr=0):
    return f'<p class="txt" style="padding-right:{pr}px;font-size:22px">{M(t)}</p>'


LEG = '<span style="background:#ffe066;font-weight:700;padding:0 4px">lettres étudiées</span> · <span style="border:2.5px solid #c62828;border-radius:12px;padding:0 5px;font-weight:700">la lettre qui décide</span>'


def lesson(lid, belt, titre, sous, maptitle, boxes, ecrans, title_size=38):
    geoms = [TL, TC, TR, BL, BR]
    cols = ['bleu', 'vert', 'orange', 'violet', 'rouge']
    bx = []
    for k, (bid, btitle, html) in enumerate(boxes):
        b = dict(id=bid, col=cols[k], geom=geoms[k], title=btitle, html=html)
        if k == 0: b['avatar'] = ('girl', 322, 122)
        if k == 3: b['avatar'] = ('boy', 445, 610); b['style'] = 'padding-top:52px'
        if k == 4: b['style'] = 'padding-top:52px'
        bx.append(b)
    out, zones = build(lid, maptitle, f'Orthographe — {lid} — CM1', LEG, bx, title_size=title_size, legend_pos='left:470px;top:880px')
    sections = [{'id': b[0], 'nom': b[1], 'couleur': COL[cols[k]]} for k, b in enumerate(boxes)]
    save(lid, {'id': lid, 'f': 'O', 'ceinture': belt, 'titre': titre, 'sous': sous, 'lesson': True}, sections, ecrans, zones)


H = 'hl'  # le mot complété apparaît surligné en jaune

# ---------------------------------------------------------------- O1
lesson('O1', 'Blanche', 'm devant m, b, p', 'devant m, b, p, j’écris m', 'm devant<br>m, b, p', [
 ('regle', 'La règle', txt('Devant <b>m</b>, <b>b</b>, <b>p</b>, j’écris <b>m</b>.', 100) + ex('une ja%m%|b|e', 'un ta%m%|b|our', 'un po%m%|p|ier', 'e%m%|m|ener')),
 ('ailleurs', 'Ailleurs : n', txt('Devant les <b>autres lettres</b>, j’écris <b>n</b>.') + ex('le ve%n%|t|re · le mo%n%|d|e', 'cha%n%|t|er · da%n%|s|er')),
 ('sons', 'Tous ces sons', txt('C’est vrai pour <b>an, en, in, on</b>.') + ex('une ch%am%|b|re', 'le t%em%|p|s', '%im%|p|ossible', 'un n%om%|b|re', size=20)),
 ('prouve', 'Je prouve', txt('Je regarde <b>la lettre qui suit</b> : m, b ou p ? Alors j’écris m.', 110) + ex('une la%m%|p|e : après, il y a p.', 'to%m%|b|er : après, il y a b.', size=20)),
 ('attention', 'Attention !', txt('Quelques mots ne suivent pas la règle : je les <b>mémorise</b>.') + ex('un bo%n%|b|on', 'une bo%n%|b|onne', 'néa%n%|m|oins', size=22)),
], [
 E('regle', 'point', 'La règle', 'girl', 'Devant m, b, p, j’écris m.',
   ['une ja%m%|b|e', 'un ta%m%|b|our', ('un po%m%|p|ier', 'Après, il y a b ou p : j’écris m.')],
   Q('une ja___be', ['m', 'n'], 'Après, il y a un b.', 'Complète : m ou n ?', fill=H),
   [Q('une o___bre', ['m', 'n'], 'Après, il y a un b.', 'Complète : m ou n ?', fill=H),
    Q('une ca___pagne', ['m', 'n'], 'Après, il y a un p.', 'Complète : m ou n ?', fill=H),
    Q('si___ple', ['m', 'n'], 'Après, il y a un p.', 'Complète : m ou n ?', fill=H)]),
 E('regle', 'attention', 'Devant m aussi', 'boy', 'Devant un autre m, j’écris m aussi.',
   ['e%m%|m|ener', 'e%m%|m|êler', ('e%m%|m|ener', 'm devant m : deux m qui se suivent.')],
   Q('e___mener', ['m', 'n'], 'Après, il y a un m.', 'Complète : m ou n ?', fill=H),
   [Q('il s’e___mêle', ['m', 'n'], 'Après, il y a un m.', 'Complète : m ou n ?', fill=H),
    Q('un ta___bour', ['m', 'n'], 'Après, il y a un b.', 'Complète : m ou n ?', fill=H)]),
 E('ailleurs', 'mots', 'Ailleurs : n', 'girl', 'Devant les autres lettres, j’écris n.',
   ['le ve%n%|t|re', 'le mo%n%|d|e', ('cha%n%|t|er', 'Après, il y a t ou d : j’écris n.')],
   Q('il cha___te', ['n', 'm'], 'Après, il y a un t : ce n’est ni m, ni b, ni p.', 'Complète : m ou n ?', fill=H),
   [Q('un e___fant', ['n', 'm'], 'Après, il y a un f.', 'Complète : m ou n ?', fill=H),
    Q('une ba___que', ['n', 'm'], 'Après, il y a un q.', 'Complète : m ou n ?', fill=H),
    Q('da___ser', ['n', 'm'], 'Après, il y a un s.', 'Complète : m ou n ?', fill=H)]),
 E('sons', 'liste', 'Tous ces sons', 'boy', 'La règle marche pour an, en, in et on.',
   ['une ch%am%|b|re', 'le t%em%|p|s', '%im%|p|ossible', ('un n%om%|b|re', 'am, em, im, om devant m, b, p.')],
   Q('co___pter', ['m', 'n'], 'Après, il y a un p.', 'Complète : m ou n ?', fill=H),
   [Q('le pri___temps', ['n', 'm'], 'Après, il y a un t.', 'Complète : m ou n ?', fill=H),
    Q('une tro___pette', ['m', 'n'], 'Après, il y a un p.', 'Complète : m ou n ?', fill=H),
    Q('un ma___teau', ['n', 'm'], 'Après, il y a un t.', 'Complète : m ou n ?', fill=H)]),
 E('prouve', 'loupe', 'Je prouve', 'boy', 'Je regarde la lettre qui suit.',
   ['une la%m%pe', ('une la%m%|p|e', 'Je prouve : après, il y a p, donc j’écris m.'), ('to%m%|b|er', 'Je prouve : après, il y a b, donc j’écris m.')],
   Q('', ['Parce qu’après, il y a un b.', 'Parce que le mot est court.', 'Parce que c’est un verbe.'], 'Regarde la lettre qui suit.', 'Pourquoi « tomber » s’écrit-il avec m ?'),
   [Q('', ['Après, il y a un s : ce n’est ni m, ni b, ni p.', 'Parce que c’est un verbe.', 'Parce que le mot finit par r.'], 'Regarde la lettre qui suit.', 'Pourquoi « danser » s’écrit-il avec n ?'),
    Q('', ['Parce qu’après, il y a un p.', 'Parce que c’est un nom.', 'Parce qu’il y a deux a.'], 'Regarde la lettre qui suit.', 'Pourquoi « campagne » s’écrit-il avec m ?')]),
 E('attention', 'attention', 'Attention !', 'girl', 'Quelques mots ne suivent pas la règle : je les mémorise.',
   ['un bo%n%|b|on', 'une bo%n%|b|onne', ('néa%n%|m|oins', 'Ces mots sont des exceptions : je les mémorise.')],
   Q('', ['un bonbon', 'un bombon'], 'C’est une exception : je l’ai mémorisée.', 'Quel mot est bien écrit ?'),
   [Q('', ['un tambour', 'un tanbour'], 'Après, il y a un b.', 'Quel mot est bien écrit ?'),
    Q('', ['emmener', 'enmener'], 'Après, il y a un m.', 'Quel mot est bien écrit ?'),
    Q('', ['un pompier', 'un ponpier'], 'Après, il y a un p.', 'Quel mot est bien écrit ?')]),
])

# ---------------------------------------------------------------- O2
lesson('O2', 'Rose', 'Les lettres finales muettes', 'un mot de la même famille m’aide', 'Les lettres<br>finales<br>muettes', [
 ('muette', 'Une lettre muette', txt('À la fin de beaucoup de mots, une lettre <b>ne s’entend pas</b>.', 100) + ex('le lai%t%', 'un galo%p%', 'gran%d%', 'un ri%z%')),
 ('famille', 'La famille m’aide', txt('Dans un mot de <b>la même famille</b>, je l’entends.') + ex('lai%t% → lai|t|ier', 'galo%p% → galo|p|er', 'spor%t% → spor|t|if', size=20)),
 ('feminin', 'Le féminin m’aide', txt('Au <b>féminin</b>, j’entends souvent la lettre.') + ex('gran%d% → gran|d|e', 'peti%t% → peti|t|e', 'gri%s% → gri|s|e', size=20)),
 ('prouve', 'Je prouve', txt('« J’écris un <b>t</b> à la fin de <i>chat</i>, car j’entends t dans <i>chaton</i>. »', 110) + ex('cha%t% → cha|t|on', 'dra%p% → dra|p|eau', size=20)),
 ('memo', 'Je mémorise', txt('Quand <b>aucun mot</b> ne m’aide, je mémorise le mot.') + ex('le ne%z% · un pui%ts%', 'toujour%s% · un pie%d%', size=22)),
], [
 E('muette', 'bulle', 'Une lettre muette', 'girl', 'À la fin d’un mot, une lettre ne s’entend pas toujours.',
   [('le lai%t%', 'Je n’entends pas le t.'), 'un galo%p%', ('il est gran%d%', 'Ces lettres sont muettes : on ne les entend pas.')],
   Q('', ['t', 'c', 'h'], 'Elle est à la fin du mot.', 'Quelle lettre est muette dans « chat » ?'),
   [Q('', ['d', 'r', 'b'], 'Elle est à la fin du mot.', 'Quelle lettre est muette dans « bord » ?'),
    Q('', ['s', 'p', 'i'], 'Elle est à la fin du mot.', 'Quelle lettre est muette dans « tapis » ?')]),
 E('famille', 'loupe', 'La famille m’aide', 'girl', 'Je cherche un mot de la même famille : j’entends la lettre.',
   ['le lai%t%', ('le lai%t% → le lai|t|ier', 'Dans « laitier », j’entends le t.'), ('un galo%p% → galo|p|er', 'Dans « galoper », j’entends le p.')],
   Q('un cam___', ['p', 't', 'd'], 'Pense à « camper ».', 'Quelle lettre muette faut-il écrire ?', fill=H),
   [Q('le spor___', ['t', 'd', 's'], 'Pense à « sportif ».', 'Quelle lettre muette faut-il écrire ?', fill=H),
    Q('un renar___', ['d', 't', 's'], 'Pense à « renarde ».', 'Quelle lettre muette faut-il écrire ?', fill=H),
    Q('un bavar___', ['d', 't', 's'], 'Pense à « bavarder ».', 'Quelle lettre muette faut-il écrire ?', fill=H)]),
 E('famille', 'mots', 'Des familles de mots', 'boy', 'Le mot de la même famille garde la lettre, et je l’entends.',
   ['le tro%t% → tro|t|ter', 'le cham%p% → cham|p|être', ('le ri%z% → la ri|z|ière', 'Même famille : même lettre.')],
   Q('le blan___', ['c', 'k', 't'], 'Pense à « blanchir ».', 'Quelle lettre muette faut-il écrire ?', fill=H),
   [Q('un regar___', ['d', 't', 's'], 'Pense à « regarder ».', 'Quelle lettre muette faut-il écrire ?', fill=H),
    Q('le ven___', ['t', 'd', 's'], 'Pense à « venteux ».', 'Quelle lettre muette faut-il écrire ?', fill=H)]),
 E('feminin', 'remplacer', 'Le féminin m’aide', 'boy', 'Pour un adjectif, je pense au féminin.',
   ['gran%d% → gran|d|e', 'peti%t% → peti|t|e', ('gri%s% → gri|s|e', 'Au féminin, j’entends la lettre.')],
   Q('un garçon for___', ['t', 'd', 's'], 'Pense à « forte ».', 'Quelle lettre muette faut-il écrire ?', fill=H),
   [Q('un pantalon gri___', ['s', 't', 'x'], 'Pense à « grise ».', 'Quelle lettre muette faut-il écrire ?', fill=H),
    Q('un chemin lon___', ['g', 'c', 't'], 'Pense à « longue ».', 'Quelle lettre muette faut-il écrire ?', fill=H),
    Q('un ballon ron___', ['d', 't', 's'], 'Pense à « ronde ».', 'Quelle lettre muette faut-il écrire ?', fill=H)]),
 E('prouve', 'coche', 'Je prouve', 'boy', 'Je prouve avec un mot de la même famille.',
   ['un cha%t%', ('un cha%t% → un cha|t|on', 'Je prouve : j’entends t dans « chaton ».'), ('le dra%p% → le dra|p|eau', 'Je prouve : j’entends p dans « drapeau ».')],
   Q('', ['Parce que j’entends t dans « chaton ».', 'Parce que tous les mots finissent par t.', 'Parce que c’est un animal.'], 'Cherche un mot de la même famille.', 'Pourquoi « chat » finit-il par t ?'),
   [Q('', ['Parce que j’entends g dans « longue ».', 'Parce que c’est un adjectif.', 'Parce que le mot est court.'], 'Pense au féminin.', 'Pourquoi « long » finit-il par g ?'),
    Q('', ['Parce que j’entends d dans « bavarder ».', 'Parce que c’est un nom.', 'Parce qu’il y a un r avant.'], 'Cherche un mot de la même famille.', 'Pourquoi « bavard » finit-il par d ?')]),
 E('memo', 'attention', 'Je mémorise', 'girl', 'Quand aucun mot ne m’aide, je mémorise.',
   [('le ne%z%', 'Aucun mot de la famille ne m’aide.'), ('un pui%ts%', 'Je le mémorise.'), ('toujour%s%', 'Je l’écris dans mon carnet de mots.')],
   Q('', ['Je le mémorise.', 'Je cherche le féminin.', 'J’ajoute toujours un e.'], 'Aucun mot de la famille ne m’aide.', 'Pour écrire « nez », que fais-je ?'),
   [Q('', ['Je cherche un mot de la même famille.', 'J’écris toujours un s.', 'Je n’écris rien.'], 'Pense à « galoper ».', 'Pour trouver la fin de « galop », que fais-je ?'),
    Q('', ['Je pense au féminin : petite.', 'J’écris toujours un s.', 'Je le mémorise sans réfléchir.'], 'C’est un adjectif.', 'Pour trouver la fin de « petit », que fais-je ?')]),
])

# ---------------------------------------------------------------- O3
lesson('O3', 'Jaune', 'Le son « s »', 's, ss, c, ç', 'Le son « s »<br><small>s, ss, c, ç</small>', [
 ('s', 'J’écris s', txt('Au <b>début</b> du mot, ou à côté d’une <b>consonne</b>.', 100) + ex('%s%ac · le %s%oleil', 'une per%s%onne', 'pen%s%er')),
 ('ss', 'J’écris ss', txt('<b>Entre deux voyelles</b>, j’écris <b>ss</b>.') + ex('un poi%ss%on', 'une cai%ss%e', 'Attention : poi%s%on → z !', size=20)),
 ('c', 'J’écris c', txt('<b>c</b> devant <b>e, i, y</b> fait « s ».') + ex('%c%|e|rise · %c%|i|néma', 'une bi%c%|y|clette', size=20)),
 ('cedille', 'J’écris ç', txt('Devant <b>a, o, u</b>, j’ajoute une cédille.', 110) + ex('un gar%ç%|o|n · re%ç%|u|', 'une fa%ç%|a|de', 'nous commen%ç%|o|ns', size=20)),
 ('prouve', 'Je prouve', txt('Je regarde <b>la lettre qui suit</b>, puis je choisis.') + ex('gar%ç%|o|n : après, il y a o → ç', 'gla%c%|e| : après, il y a e → c', 'poi%ss%on : entre deux voyelles → ss', size=19)),
], [
 E('s', 'point', 'J’écris s', 'girl', 'Au début du mot ou à côté d’une consonne : s.',
   ['un %s%ac', 'le %s%oleil', ('une per%s%onne', 'Au début du mot ou à côté d’une consonne : s.')],
   Q('un ___erpent', ['s', 'ss', 'ç'], 'C’est le début du mot.', 'Complète avec la bonne lettre.', fill=H),
   [Q('la ___alade', ['s', 'ss', 'c'], 'C’est le début du mot, devant a.', 'Complète avec la bonne lettre.', fill=H),
    Q('pen___er', ['s', 'ss', 'ç'], 'À côté d’une consonne : n.', 'Complète avec la bonne lettre.', fill=H)]),
 E('ss', 'attention', 'J’écris ss', 'girl', 'Entre deux voyelles, j’écris ss.',
   ['un poi%ss%on', ('un poi%s%on', 'Avec un seul s entre deux voyelles, j’entends z !'), ('une cai%ss%e', 'Pour entendre « s » entre deux voyelles : ss.')],
   Q('une tro___e', ['ss', 's', 'c'], 'Entre deux voyelles, pour entendre « s ».', 'Complète avec la bonne lettre.', fill=H),
   [Q('il gli___e', ['ss', 's', 'ç'], 'Entre deux voyelles, pour entendre « s ».', 'Complète avec la bonne lettre.', fill=H),
    Q('une ro___e', ['s', 'ss'], 'Ici, on entend z : rose.', 'Complète avec la bonne lettre.', fill=H),
    Q('la pre___e', ['ss', 's', 'c'], 'Entre deux voyelles, pour entendre « s ».', 'Complète avec la bonne lettre.', fill=H)]),
 E('c', 'mots', 'J’écris c', 'boy', 'Devant e, i, y, la lettre c fait « s ».',
   ['une %c%|e|rise', 'le %c%|i|néma', ('une bi%c%|y|clette', 'c devant e, i, y fait « s ».')],
   Q('une ___itrouille', ['c', 'ç', 'ss'], 'Après, il y a un i.', 'Complète avec la bonne lettre.', fill=H),
   [Q('un ___erf', ['c', 'ç', 'ss'], 'Après, il y a un e.', 'Complète avec la bonne lettre.', fill=H),
    Q('une gla___e', ['c', 'ç', 's'], 'Après, il y a un e.', 'Complète avec la bonne lettre.', fill=H)]),
 E('cedille', 'remplacer', 'J’écris ç', 'boy', 'Devant a, o, u, j’ajoute une cédille sous le c.',
   ['un gar%ç%|o|n', 'un ma%ç%|o|n', ('j’ai re%ç%|u|', 'Devant a, o, u : ç.')],
   Q('une le___on', ['ç', 'c', 'ss'], 'Après, il y a un o.', 'Complète avec la bonne lettre.', fill=H),
   [Q('un gla___on', ['ç', 'c', 's'], 'Après, il y a un o.', 'Complète avec la bonne lettre.', fill=H),
    Q('nous avan___ons', ['ç', 'c', 'ss'], 'Après, il y a un o.', 'Complète avec la bonne lettre.', fill=H)]),
 E('cedille', 'liste', 'La cédille dans les verbes', 'girl', 'Avec nous, les verbes en -cer prennent une cédille.',
   ['commen%c%|e|r', ('nous commen%ç%|o|ns', 'Après, il y a o : je mets une cédille.'), ('il lan%ç%|a|it', 'Après, il y a a : cédille.')],
   Q('nous pla___ons', ['ç', 'c', 'ss'], 'Après, il y a un o.', 'Complète avec la bonne lettre.', fill=H),
   [Q('il effa___ait', ['ç', 'c', 'ss'], 'Après, il y a un a.', 'Complète avec la bonne lettre.', fill=H),
    Q('vous avan___ez', ['c', 'ç', 'ss'], 'Après, il y a un e : pas de cédille.', 'Complète avec la bonne lettre.', fill=H)]),
 E('prouve', 'coche', 'Je prouve', 'boy', 'Je regarde la lettre qui suit, puis je choisis.',
   ['un gar%ç%on', ('un gar%ç%|o|n', 'Je prouve : après, il y a o. Sans cédille, je lirais « k ».'), ('une gla%c%|e|', 'Après, il y a e : pas besoin de cédille.')],
   Q('', ['Parce qu’après le c, il y a un a.', 'Parce que c’est la fin du mot.', 'Parce que c’est un nom.'], 'Regarde la lettre qui suit.', 'Pourquoi une cédille dans « façade » ?'),
   [Q('', ['Le s est entre deux voyelles : avec un seul s, j’entendrais z.', 'Parce que c’est un animal.', 'Parce que le mot est long.'], 'Regarde les lettres autour.', 'Pourquoi deux s dans « poisson » ?'),
    Q('', ['Parce qu’après le c, il y a un i.', 'Parce que c’est le début du mot.', 'Parce que c’est un fruit.'], 'Regarde la lettre qui suit.', 'Pourquoi pas de cédille dans « citron » ?')]),
])

# ---------------------------------------------------------------- O4
lesson('O4', 'Orange', 'Le son « k »', 'c, qu, k', 'Le son « k »<br><small>c, qu, k</small>', [
 ('c', 'J’écris c', txt('Devant <b>a, o, u</b>, j’écris <b>c</b>.', 100) + ex('une %c%|a|bane', 'une %c%|o|rde', 'un %c%|u|be')),
 ('consonne', 'Devant une consonne', txt('Devant une <b>consonne</b> ou à la <b>fin</b> du mot : <b>c</b>.') + ex('un %c%|r|abe · un %c%|l|ou', 'un sa%c%', size=20)),
 ('qu', 'J’écris qu', txt('Devant <b>e, i</b>, j’écris <b>qu</b>.') + ex('une %qu%|i|lle', 'un ban%qu%|e|t', 'Je mémorise : %qu%and, %qu%atre', size=19)),
 ('k', 'J’écris k', txt('Le <b>k</b> est rare : je <b>mémorise</b> ces mots.', 110) + ex('un %k%angourou · un %k%ilo', 'un %k%iwi · un %k%ayak', size=20)),
 ('prouve', 'Je prouve', txt('Je regarde <b>la lettre qui suit</b>.') + ex('%c%|u|be : après, il y a u → c', '%qu%|i|lle : après, il y a i → qu', 'c devant i ferait « s » : cil', size=19)),
], [
 E('c', 'point', 'J’écris c', 'girl', 'Devant a, o, u, j’écris c.',
   ['une %c%|a|bane', 'une %c%|o|rde', ('un %c%|u|be', 'Devant a, o, u : c.')],
   Q('un ___orbeau', ['c', 'qu', 'k'], 'Après, il y a un o.', 'Complète avec la bonne lettre.', fill=H),
   [Q('une ___ulotte', ['c', 'qu', 'k'], 'Après, il y a un u.', 'Complète avec la bonne lettre.', fill=H),
    Q('un ___anard', ['c', 'qu', 'k'], 'Après, il y a un a.', 'Complète avec la bonne lettre.', fill=H)]),
 E('consonne', 'mots', 'Devant une consonne', 'girl', 'Devant une consonne ou à la fin du mot : c.',
   ['un %c%|r|abe', 'un %c%|l|ou', ('un sa%c%', 'Devant une consonne ou à la fin du mot : c.')],
   Q('un ___rayon', ['c', 'qu', 'k'], 'Après, il y a un r.', 'Complète avec la bonne lettre.', fill=H),
   [Q('la ___lasse', ['c', 'qu', 'k'], 'Après, il y a un l.', 'Complète avec la bonne lettre.', fill=H),
    Q('un ar___', ['c', 'qu', 'k'], 'C’est la fin du mot.', 'Complète avec la bonne lettre.', fill=H)]),
 E('qu', 'attention', 'J’écris qu', 'boy', 'Devant e, i, j’écris qu.',
   ['une %qu%|i|lle', 'un ban%qu%|e|t', ('la %qu%|e|ue', 'Devant e, i : qu.')],
   Q('une ___ille', ['qu', 'c', 'k'], 'Après, il y a un i.', 'Complète avec la bonne lettre.', fill=H),
   [Q('un ban___et', ['qu', 'c', 'k'], 'Après, il y a un e.', 'Complète avec la bonne lettre.', fill=H),
    Q('une mo___ette', ['qu', 'c', 'k'], 'Après, il y a un e.', 'Complète avec la bonne lettre.', fill=H)]),
 E('qu', 'liste', 'Des mots à mémoriser', 'girl', 'Quelques mots très courants s’écrivent avec qu devant a ou o.',
   ['%qu%and', '%qu%atre', ('%qu%oi', 'Ces mots fréquents, je les mémorise.')],
   Q('', ['quand', 'cand', 'kand'], 'Un mot à mémoriser.', 'Quel mot est bien écrit ?'),
   [Q('', ['quatre', 'catre', 'katre'], 'Un mot à mémoriser.', 'Quel mot est bien écrit ?'),
    Q('', ['pourquoi', 'pourcoi', 'pourkoi'], 'Un mot à mémoriser.', 'Quel mot est bien écrit ?')]),
 E('k', 'etiquette', 'J’écris k', 'boy', 'Le k est rare : je mémorise ces mots.',
   ['un %k%angourou', 'un %k%ilo', ('un %k%iwi', 'Ces mots viennent souvent d’autres langues.')],
   Q('', ['un kayak', 'un cayak', 'un quayak'], 'Un mot avec k.', 'Quel mot est bien écrit ?'),
   [Q('', ['un koala', 'un coala', 'un quoala'], 'Un mot avec k.', 'Quel mot est bien écrit ?'),
    Q('', ['un kimono', 'un quimono', 'un cimono'], 'Un mot avec k.', 'Quel mot est bien écrit ?')]),
 E('prouve', 'coche', 'Je prouve', 'girl', 'Je regarde la lettre qui suit.',
   ['une %qu%ille', ('une %qu%|i|lle', 'Je prouve : après, il y a i. Avec c, je lirais « s ».'), ('un %c%|u|be', 'Je prouve : après, il y a u, donc c.')],
   Q('', ['Parce qu’après, il y a un i : c devant i ferait « s ».', 'Parce que c’est le début du mot.', 'Parce que c’est un jeu.'], 'Regarde la lettre qui suit.', 'Pourquoi qu dans « quille » ?'),
   [Q('', ['Parce qu’après, il y a un u.', 'Parce que le mot est court.', 'Parce que c’est un nom.'], 'Regarde la lettre qui suit.', 'Pourquoi c dans « cube » ?'),
    Q('', ['Parce qu’après, il y a un e.', 'Parce qu’il y a un n avant.', 'Parce que c’est un repas.'], 'Regarde la lettre qui suit.', 'Pourquoi qu dans « banquet » ?')]),
])

# ---------------------------------------------------------------- O5
lesson('O5', 'Verte', 'Le son « g »', 'g, gu (et ge)', 'Le son « g »<br><small>g, gu, ge</small>', [
 ('g', 'J’écris g', txt('Devant <b>a, o, u</b> ou une <b>consonne</b> : <b>g</b>.', 100) + ex('une %g%|a|re', 'une %g%|o|mme', 'une fi%g%|u|re', '%g%|r|and')),
 ('gu', 'J’écris gu', txt('Devant <b>e, i</b>, j’écris <b>gu</b>.') + ex('une %gu%|i|tare', 'une ba%gu%|e|', 'une %gu%|i|rlande', size=20)),
 ('gj', 'g fait « j »', txt('Devant <b>e, i, y</b>, la lettre <b>g</b> fait « j ».') + ex('une %g%|i|rafe', 'un %g%|e|nou', 'le %g%|y|mnase', size=20)),
 ('ge', 'J’écris ge', txt('Pour garder « j » devant <b>a, o, u</b> : <b>ge</b>.', 110) + ex('nous man%ge%|o|ns', 'un pi%ge%|o|n', 'il na%ge%|a|it', size=20)),
 ('prouve', 'Je prouve', txt('Je regarde <b>la lettre qui suit</b>.') + ex('%gu%|i|tare : sans u → « gitare »', '%g%|o|mme : après, il y a o → g', 'pi%ge%|o|n : pour garder « j » → ge', size=19)),
], [
 E('g', 'point', 'J’écris g', 'girl', 'Devant a, o, u ou une consonne : g.',
   ['une %g%|a|re', 'une %g%|o|mme', ('une fi%g%|u|re', 'Devant a, o, u : g.')],
   Q('une ___omme', ['g', 'gu', 'ge'], 'Après, il y a un o.', 'Complète avec la bonne lettre.', fill=H),
   [Q('un ___âteau', ['g', 'gu', 'ge'], 'Après, il y a un a.', 'Complète avec la bonne lettre.', fill=H),
    Q('une ___renouille', ['g', 'gu', 'ge'], 'Après, il y a un r.', 'Complète avec la bonne lettre.', fill=H),
    Q('un lé___ume', ['g', 'gu', 'ge'], 'Après, il y a un u.', 'Complète avec la bonne lettre.', fill=H)]),
 E('gu', 'attention', 'J’écris gu', 'girl', 'Devant e, i, j’écris gu.',
   ['une %gu%|i|tare', 'une ba%gu%|e|', ('une %gu%|i|rlande', 'Devant e, i : gu. Le u ne s’entend pas.')],
   Q('une ba___e', ['gu', 'g', 'ge'], 'Après, il y a un e : g seul ferait « j ».', 'Complète avec la bonne lettre.', fill=H),
   [Q('une ___êpe', ['gu', 'g', 'ge'], 'Après, il y a un ê.', 'Complète avec la bonne lettre.', fill=H),
    Q('un ___ide', ['gu', 'g', 'ge'], 'Après, il y a un i.', 'Complète avec la bonne lettre.', fill=H)]),
 E('gj', 'bulle', 'g fait « j »', 'boy', 'Devant e, i, y, la lettre g fait « j ».',
   ['une %g%|i|rafe', 'un %g%|e|nou', ('le %g%|y|mnase', 'Devant e, i, y : g fait « j ».')],
   Q('', ['« j » comme dans « jardin »', '« g » comme dans « gare »'], 'Après le g, il y a un i.', 'Dans « girafe », le g se prononce…'),
   [Q('', ['« g » comme dans « gare »', '« j » comme dans « jardin »'], 'Après le g, il y a un o.', 'Dans « gorille », le g se prononce…'),
    Q('', ['« j » comme dans « jardin »', '« g » comme dans « gare »'], 'Après le g, il y a un e.', 'Dans « genou », le g se prononce…')]),
 E('ge', 'remplacer', 'J’écris ge', 'boy', 'Pour garder « j » devant a, o, u, j’écris ge.',
   ['man%g%|e|r', ('nous man%ge%|o|ns', 'Après, il y a o : j’ajoute un e pour garder « j ».'), ('un pi%ge%|o|n', 'Le e ne s’entend pas.')],
   Q('nous plon___ons', ['ge', 'g', 'gu'], 'Après, il y a un o : pour entendre « j », j’écris ge.', 'Complète avec la bonne lettre.', fill=H),
   [Q('il na___ait', ['ge', 'g', 'gu'], 'Après, il y a un a : pour entendre « j », j’écris ge.', 'Complète avec la bonne lettre.', fill=H),
    Q('nous ran___ons', ['ge', 'g', 'gu'], 'Après, il y a un o : pour entendre « j », j’écris ge.', 'Complète avec la bonne lettre.', fill=H)]),
 E('prouve', 'coche', 'Je prouve', 'girl', 'Je regarde la lettre qui suit.',
   ['une %gu%itare', ('une %gu%|i|tare', 'Je prouve : sans u, g devant i ferait « j ».'), ('nous man%ge%|o|ns', 'Je prouve : après, il y a o ; sans e, je lirais « g ».')],
   Q('', ['Sans u, g devant i ferait « j ».', 'Parce que c’est un instrument.', 'Parce que le u s’entend.'], 'Regarde la lettre qui suit le g.', 'Pourquoi un u dans « guitare » ?'),
   [Q('', ['Après, il y a o : sans e, je lirais « g ».', 'Parce que c’est un oiseau.', 'Parce que le mot est long.'], 'Regarde la lettre qui suit le g.', 'Pourquoi ge dans « pigeon » ?'),
    Q('', ['Parce qu’après, il y a un a.', 'Parce que c’est le début du mot.', 'Parce que c’est un nom.'], 'Regarde la lettre qui suit.', 'Pourquoi g seul dans « gare » ?')]),
])

# ---------------------------------------------------------------- O6
lesson('O6', 'Bleue', 'ill, y ; oi, oy', 'les sons « ill » et « oi »', 'ill, y<br>oi, oy', [
 ('ill', 'ill après une voyelle', txt('Après une <b>voyelle</b>, j’écris <b>ill</b>.', 100) + ex('la pa%ill%e', 'une feu%ill%e', 'une abe%ill%e', 'le solei%l% · un révei%l%', size=20)),
 ('ille', 'ille', txt('Après une <b>consonne</b>, j’écris souvent <b>ille</b>.') + ex('une f%ille%', 'une b%ille%', 'une qu%ille%', size=21)),
 ('y', 'y = deux i', txt('<b>y</b> entre deux voyelles vaut <b>deux i</b>.') + ex('un cra%y%on → crai-ion', 'un no%y%au → noi-iau', size=19)),
 ('oi', 'oi', txt('Le son « oi » s’écrit souvent <b>oi</b>.', 110) + ex('le r%oi% · un %oi%seau', 'une v%oi%ture', size=21)),
 ('oy', 'oy', txt('Devant une <b>voyelle</b>, j’écris <b>oy</b>.') + ex('un v%oy%|a|ge · le r%oy%|a|ume', 'oy = oi + i : roi-iaume', size=20)),
], [
 E('ill', 'point', 'ill après une voyelle', 'girl', 'Après une voyelle, j’écris ill.',
   ['la pa%ill%e', 'une feu%ill%e', ('une abe%ill%e', 'Après a, eu, e : ill.')],
   Q('une grenou___e', ['ill', 'y', 'oy'], 'Après une voyelle : ill.', 'Complète avec les bonnes lettres.', fill=H),
   [Q('une méda___e', ['ill', 'y', 'oy'], 'Après une voyelle : ill.', 'Complète avec les bonnes lettres.', fill=H),
    Q('une citrou___e', ['ill', 'y', 'oy'], 'Après une voyelle : ill.', 'Complète avec les bonnes lettres.', fill=H)]),
 E('ill', 'attention', 'À la fin : il', 'boy', 'À la fin d’un nom masculin, j’écris souvent il.',
   ['le solei%l%', 'un révei%l%', ('un éventa%il%', 'Masculin : -il. Féminin : -ille.')],
   Q('un trava___', ['il', 'ille', 'y'], 'Un nom masculin : -il.', 'Complète avec les bonnes lettres.', fill=H),
   [Q('une vola___e', ['ill', 'il', 'y'], 'Un nom féminin : -ille.', 'Complète avec les bonnes lettres.', fill=H),
    Q('un orte___', ['il', 'ille', 'y'], 'Un nom masculin : -il.', 'Complète avec les bonnes lettres.', fill=H)]),
 E('ille', 'mots', 'ille', 'girl', 'Après une consonne, j’écris souvent ille.',
   ['une f%ille%', 'une b%ille%', ('une qu%ille%', 'Après une consonne : ille.')],
   Q('une fam___', ['ille', 'y', 'il'], 'Après une consonne : ille.', 'Complète avec les bonnes lettres.', fill=H),
   [Q('une gr___', ['ille', 'y', 'il'], 'Après une consonne : ille.', 'Complète avec les bonnes lettres.', fill=H),
    Q('une chen___e', ['ill', 'y', 'il'], 'Après une consonne : ille.', 'Complète avec les bonnes lettres.', fill=H)]),
 E('y', 'loupe', 'y = deux i', 'boy', 'Entre deux voyelles, y vaut deux i.',
   ['un cra%y%on', ('un cra%y%on', 'crai-ion : le y fait « ai » puis « ion ».'), ('un no%y%au', 'noi-iau : y = deux i.')],
   Q('un tu___au', ['y', 'ill', 'i'], 'Entre deux voyelles, deux i : tui-iau.', 'Complète avec la bonne lettre.', fill=H),
   [Q('un ra___on de soleil', ['y', 'ill', 'i'], 'Entre deux voyelles, deux i : rai-ion.', 'Complète avec la bonne lettre.', fill=H),
    Q('un pa___san', ['y', 'ill', 'i'], 'Entre deux voyelles, deux i : pai-isan.', 'Complète avec la bonne lettre.', fill=H)]),
 E('oi', 'bulle', 'oi', 'girl', 'Le son « oi » s’écrit souvent oi.',
   ['le r%oi%', 'un %oi%seau', ('une v%oi%ture', 'Le son « oi » : oi.')],
   Q('une ét___le', ['oi', 'oy', 'ill'], 'Le son « oi » devant une consonne.', 'Complète avec les bonnes lettres.', fill=H),
   [Q('le m___s de mai', ['oi', 'oy', 'y'], 'Le son « oi » à la fin.', 'Complète avec les bonnes lettres.', fill=H),
    Q('une p___re', ['oi', 'oy', 'ill'], 'Le son « oi » devant une consonne.', 'Complète avec les bonnes lettres.', fill=H)]),
 E('oy', 'remplacer', 'oy', 'boy', 'Devant une voyelle, j’écris oy : oy = oi + i.',
   ['un v%oy%|a|ge', ('le r%oy%|a|ume', 'roi-iaume : oy = oi + i.'), ('un n%oy%|a|u', 'Devant une voyelle : oy.')],
   Q('il v___age', ['oy', 'oi', 'ill'], 'Devant une voyelle : oy.', 'Complète avec les bonnes lettres.', fill=H),
   [Q('il se n___ait', ['oy', 'oi', 'ill'], 'Devant une voyelle : oy.', 'Complète avec les bonnes lettres.', fill=H),
    Q('il env___e une lettre', ['oi', 'oy', 'ill'], 'Le e final ne se prononce pas : envoie.', 'Complète avec les bonnes lettres.', fill=H)]),
 E('oy', 'coche', 'Je prouve', 'girl', 'J’écoute et je regarde la lettre qui suit.',
   ['un v%oy%age', ('un v%oy%|a|ge', 'Je prouve : après, il y a a, une voyelle → oy.'), ('la pa%ill%e', 'Je prouve : après a, une voyelle → ill.')],
   Q('', ['Parce qu’après, il y a une voyelle : oy = oi + i.', 'Parce que c’est un nom.', 'Parce que le mot est long.'], 'Regarde la lettre qui suit.', 'Pourquoi oy dans « royaume » ?'),
   [Q('', ['Parce que y entre deux voyelles vaut deux i.', 'Parce que c’est un objet.', 'Parce que le y ne s’entend pas.'], 'Dis le mot lentement : crai-ion.', 'Pourquoi un y dans « crayon » ?'),
    Q('', ['Parce qu’avant, il y a une voyelle : a.', 'Parce que c’est un mot court.', 'Parce que c’est un animal.'], 'Regarde la lettre avant.', 'Pourquoi ill dans « paille » ?')]),
])
