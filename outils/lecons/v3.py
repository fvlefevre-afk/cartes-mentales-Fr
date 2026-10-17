import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from mapgen import build, TL, TC, TR
from lhelp import *
from hlib import R, table, A

P = lambda t: f'<span class="e">{t}</span>'           # préfixe / suffixe surligné
B = lambda t: f'<b style="color:#1f5fc4">{t}</b>'      # mot de base
boxes = [
 dict(id='mot', col='bleu', geom=TL, title='Un mot en morceaux', avatar=('girl', 322, 122), html=f'''
  <p class="txt" style="padding-right:100px">Un mot peut être fait d’un <b style="color:#1f5fc4">mot de base</b> et de morceaux ajoutés.</p>
  <div class="exl" style="font-size:21px;line-height:1.6;margin-top:14px">{P("re")}{B("faire")} {A} faire à nouveau<br>{B("jardin")}{P("ier")} {A} un métier</div>
  <p class="small" style="margin:8px 0 0">Devant : un <b>préfixe</b>. Derrière : un <b>suffixe</b>.</p>'''),
 dict(id='pre', col='violet', geom=TC, title='Les préfixes', html=f'''
  <table class="tr" style="font-size:21px"><tr><td style="white-space:nowrap">{P("re-")}</td><td>à nouveau : {P("re")}lire</td></tr>
  <tr><td>{P("dé-")}</td><td>le contraire : {P("dé")}coller</td></tr>
  <tr><td style="white-space:nowrap">{P("in-")} {P("im-")}</td><td>pas : {P("in")}connu, {P("im")}possible</td></tr>
  <tr><td>{P("mal-")}</td><td>pas : {P("mal")}heureux</td></tr></table>'''),
 dict(id='suf', col='vert', geom=TR, title='Les suffixes', html=f'''
  <table class="tr" style="font-size:19px"><tr><td style="white-space:nowrap;width:120px">{P("-ier")}</td><td>un métier : jardin{P("ier")}</td></tr>
  <tr><td style="white-space:nowrap">{P("-eur")}, {P("-euse")}</td><td>qui fait : chant{P("eur")}</td></tr>
  <tr><td>{P("-ette")}</td><td>petit : fill{P("ette")}</td></tr>
  <tr><td>{P("-able")}</td><td>qu’on peut : lav{P("able")}</td></tr>
  <tr><td>{P("-ment")}</td><td>de quelle manière : douce{P("ment")}</td></tr></table>'''),
 dict(id='sens', col='orange', geom=(18, 568, 560, 350), title='Je comprends un mot', style='padding-top:52px', avatar=('boy', 445, 610), html=f'''
  <p class="txt" style="padding-right:110px">Les morceaux sont des <b>indices dans le mot</b>.</p>
  <div class="exl" style="font-size:21px;line-height:1.6;margin-right:110px">Ce vase est {P("in")}{B("cass")}{P("able")}.<br>{A} qu’on ne peut <b>pas</b> casser</div>
  <div class="exl" style="font-size:21px;line-height:1.6;margin-right:110px;margin-top:10px">Ce jouet est {P("dé")}{B("mont")}{P("able")}.<br>{A} qu’on peut démonter</div>'''),
 dict(id='att', col='rouge', geom=(612, 568, 770, 350), title='Attention !', style='padding-top:52px', html='''
  <ul style="font-size:22px;line-height:1.5">
   <li>Il faut un <b>mot de base</b> qui existe : <i>reine</i> n’est pas re + ine.</li>
   <li>On écrit <b>im-</b> devant <b>b</b>, <b>p</b> et <b>m</b> : <i>impossible, imbuvable</i>.</li>
   <li>Un même mot peut avoir un préfixe <b>et</b> un suffixe : <i>incassable</i>.</li></ul>'''),
]
out, zones = build('V3', 'Préfixes<br>et suffixes', 'Vocabulaire — V3 — CM1', None, boxes, title_size=36)

sections = [
 {'id': 'mot', 'nom': 'Un mot en morceaux', 'couleur': '#1f5fc4'},
 {'id': 'pre', 'nom': 'Les préfixes', 'couleur': '#7b3fa0'},
 {'id': 'suf', 'nom': 'Les suffixes', 'couleur': '#23845a'},
 {'id': 'sens', 'nom': 'Je comprends un mot', 'couleur': '#e67e22'},
 {'id': 'att', 'nom': 'Attention !', 'couleur': '#c62828'},
]
ecrans = [
 E('mot', 'ciseaux', 'Un mot en morceaux', 'girl', 'Je découpe le mot : je cherche le mot de base.',
   ['refaire · jardinier',
    ('%re%|faire|', 'refaire = re + faire : faire à nouveau.'),
    ('|jardin|%ier%', 'jardinier = jardin + ier : la personne qui s’occupe du jardin.'),
    ('%re%|faire| · |jardin|%ier%', 'Devant : un préfixe. Derrière : un suffixe.')],
   Q('démonter', ['dé + monter', 'dém + onter', 'démon + ter'], 'Cherche un mot que tu connais.', 'Comment se découpe ce mot ?'),
   [Q('chanteur', ['chant + eur', 'cha + nteur', 'chante + ur'], 'Cherche le mot de base : chant.', 'Comment se découpe ce mot ?'),
    Q('replanter', ['re + planter', 'rep + lanter', 'replan + ter'], 'Cherche un mot que tu connais.', 'Comment se découpe ce mot ?'),
    Q('fillette', ['un suffixe', 'un préfixe'], 'Le morceau ajouté est à la fin.', 'Dans « fillette », le morceau ajouté est…')]),
 E('pre', 'remplacer', 're- : à nouveau', 'boy', 'Le préfixe re- veut dire : à nouveau.',
   ['lire · partir · écrire',
    ('%re%|lire| · %re%|partir| · %ré%|écrire|', 're-, ré- : faire à nouveau.')],
   Q('Relire, c’est…', ['lire encore une fois', 'ne pas lire', 'lire avant'], 're- : à nouveau.', 'Choisis le bon sens.'),
   [Q('Repeindre, c’est…', ['peindre à nouveau', 'ne pas peindre', 'peindre un peu'], 're- : à nouveau.', 'Choisis le bon sens.'),
    Q('Fermer à nouveau, c’est…', ['refermer', 'défermer', 'fermeur'], 're- : à nouveau.', 'Choisis le bon mot.')]),
 E('pre', 'non', 'dé-, in-, im-, mal- : le contraire', 'boy', 'Certains préfixes fabriquent le contraire.',
   [('%dé%|coller| · %dés%|obéir|', 'dé-, dés- : le contraire.'),
    ('%in%|connu| · %im%|possible|', 'in-, im- : pas.'),
    ('%mal%|heureux| · %mal%|propre|', 'mal- : pas.')],
   Q('Le contraire de « faire », avec un préfixe :', ['défaire', 'refaire', 'faiseur'], 'dé- fabrique le contraire.', 'Choisis le bon mot.'),
   [Q('Le contraire de « visible » :', ['invisible', 'revisible', 'visiblement'], 'in- : pas.', 'Choisis le bon mot.'),
    Q('« impossible » veut dire…', ['pas possible', 'possible à nouveau', 'très possible'], 'im- : pas.', 'Choisis le bon sens.'),
    Q('Le contraire de « adroit » :', ['maladroit', 'readroit', 'adroitement'], 'mal- : pas.', 'Choisis le bon mot.')]),
 E('suf', 'etiquette', 'Les personnes et les métiers', 'girl', 'Certains suffixes désignent une personne.',
   [('|jardin|%ier% · |pâtiss|%ier%', '-ier : un métier.'),
    ('|chant|%eur% · |dans|%euse%', '-eur, -euse : la personne qui fait l’action.')],
   Q('Une personne qui nage :', ['un nageur', 'une nageoire', 'un nageage'], '-eur : la personne qui fait l’action.', 'Choisis le bon mot.'),
   [Q('Une personne qui joue :', ['un joueur', 'un jouet', 'un jouable'], '-eur : la personne qui fait l’action.', 'Choisis le bon mot.'),
    Q('La personne qui vend du lait :', ['la laitière', 'la laiterie', 'le laitage'], '-ière : un métier.', 'Choisis le bon mot.')]),
 E('suf', 'mots', 'Petit, possible, manière', 'girl', 'D’autres suffixes changent aussi le sens.',
   [('|fill|%ette% · |maison|%nette%', '-ette : petit.'),
    ('|lav|%able% · |mange|%able%', '-able : qu’on peut.'),
    ('|douce|%ment% · |rapide|%ment%', '-ment : de quelle manière.')],
   Q('Une eau qu’on peut boire est…', ['buvable', 'buveuse', 'reboire'], '-able : qu’on peut.', 'Choisis le bon mot.'),
   [Q('Un petit garçon :', ['un garçonnet', 'un garçonnier', 'un garçonnable'], '-et, -ette : petit.', 'Choisis le bon mot.'),
    Q('Marcher d’une manière lente :', ['lentement', 'lenteur', 'ralentir'], '-ment : de quelle manière.', 'Choisis le bon mot.')]),
 E('sens', 'loupe', 'Je comprends un mot inconnu', 'boy', 'J’utilise les indices dans le mot.',
   ['Ce vase est #incassable#.',
    ('%in%|cass|%able%', 'Je découpe : in + cass(er) + able.'),
    ('incassable = *qu’on ne peut pas casser*', 'in- : pas · -able : qu’on peut.')],
   Q('Cette tache est ineffaçable.', ['qu’on ne peut pas effacer', 'qu’on efface souvent', 'très effacée'], 'in- : pas · -able : qu’on peut.', '« ineffaçable » veut dire…'),
   [Q('Ce jouet est démontable.', ['qu’on peut démonter', 'qu’on ne peut pas monter', 'déjà monté'], 'dé- : le contraire de monter · -able : qu’on peut.', '« démontable » veut dire…'),
    Q('Ce chien est infatigable.', ['qui ne se fatigue pas', 'très fatigué', 'qui fatigue les autres'], 'in- : pas.', '« infatigable » veut dire…')]),
 E('att', 'attention', 'Les pièges', 'girl', 'Un préfixe, c’est seulement s’il reste un vrai mot de base.',
   [('reine · renard', 'Si j’enlève re-, il ne reste pas un mot : pas de préfixe.'),
    ('%im%|possible| · %im%|buvable| · %in%|connu|', 'im- devant p, b, m ; in- ailleurs.')],
   Q('', ['refaire', 'renard', 'reine'], 'Enlève re- : reste-t-il un mot ?', 'Lequel contient vraiment un préfixe ?'),
   [Q('', ['imbattable', 'inbattable'], 'Devant b, on écrit im-.', 'Quel mot est bien écrit ?')]),
]
save('V3', {'id': 'V3', 'f': 'V', 'ceinture': 'Jaune', 'titre': 'Les préfixes et les suffixes', 'sous': 'des indices dans le mot', 'lesson': True}, sections, ecrans, zones)
