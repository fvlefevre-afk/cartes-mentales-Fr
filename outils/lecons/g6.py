import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from mapgen import build, TL, TC, TR
from lhelp import *

boxes = [
 dict(id='phrase', col='turquoise', geom=TL, title='Sujet, verbe… et plus', avatar=('girl', 322, 122), html='''
  <p class="txt" style="padding-right:100px">Une phrase a un <span class="s">sujet</span> et un <span class="v">verbe</span>.</p>
  <p class="txt" style="padding-right:100px">Elle peut avoir des <b>compléments</b>.</p>
  <div class="ex" style="font-size:21px;margin-top:14px;line-height:1.5"><span class="cc">Ce matin,</span> <span class="s">Léa</span> <span class="v">mange</span> <span class="co">une pomme</span> <span class="cc">dans la cuisine</span>.</div>'''),
 dict(id='cod', col='indigo', geom=TC, title='Le complément d’objet', hstyle='font-size:28px', html='''
  <ul style="font-size:19px;line-height:1.3">
   <li>Il complète le verbe : il se place <b>après lui</b>.</li>
   <li>On ne peut <b>pas le déplacer</b>.</li></ul>
  <div class="ex" style="font-size:19px;line-height:1.4;margin-top:6px"><span class="s">Tom</span> <span class="v">lance</span> <span class="co">le ballon</span>. <span class="arrow">→</span> <b>COD</b><br><span class="s">Il</span> <span class="v">parle</span> <span class="co">à sa mère</span>. <span class="arrow">→</span> <b>COI</b></div>
  <p style="margin:4px 0 0;font-size:16px">COI : avec un petit mot (<b>à</b>, <b>de</b>) après le verbe.</p>'''),
 dict(id='cc', col='marron', geom=TR, title='Compléments circonstanciels', hstyle='font-size:25px', avatar=('boy', 1250, 122), html='''
  <ul style="font-size:20px;padding-right:96px">
   <li>Ils donnent des <b>précisions</b> sur l’action.</li>
   <li>On peut les <b>supprimer</b> et les <b>déplacer</b>.</li></ul>
  <div class="ex" style="font-size:20px;line-height:1.5"><span class="cc">Hier,</span> <span class="s">Léa</span> <span class="v">a joué</span><br><span class="cc">dans le parc</span> <span class="cc">joyeusement</span>.</div>'''),
 dict(id='tests', col='violet', geom=(18, 568, 560, 350), title='Les tests', style='padding-top:52px', html='''
  <p class="txt"><b>1. Je supprime :</b></p>
  <div class="ex" style="font-size:20px;margin:0 0 6px"><span class="barre">Ce matin,</span> <span class="s">les élèves</span> <span class="v">chantent</span> <span class="barre">dans la cour</span>.</div>
  <p class="txt" style="font-size:18px">La phrase a encore du sens.</p>
  <p class="txt"><b>2. Je déplace :</b></p>
  <div class="ex" style="font-size:20px;margin:0"><span class="cc">Dans la cour,</span> <span class="s">les élèves</span> <span class="v">chantent</span>.</div>'''),
 dict(id='att', col='rouge', geom=(612, 568, 770, 350), title='Attention !', style='padding-top:52px', html='''
  <ul style="font-size:20px;line-height:1.45">
   <li>En début de phrase, le complément circonstanciel est suivi<br>d’une <span class="e">virgule</span> : <span class="cc">Le matin<span class="e">,</span></span> les oiseaux chantent.</li>
   <li>Une phrase peut avoir <b>plusieurs</b> compléments.</li>
   <li>Le test le plus sûr : <b>je déplace</b>.<br>Le complément d’objet ne bouge pas.</li></ul>'''),
]
legend = '<span class="s">sujet</span> · <span class="v">verbe</span> · <span class="co">compl. d’objet</span> · <span class="cc">compl. circonstanciel</span>'
out, zones = build('G6', 'Les<br>compléments', 'Grammaire — G6 — CM1', legend, boxes, title_size=38, legend_pos='right:18px;top:470px')

sections = [
 {'id': 'phrase', 'nom': 'Sujet, verbe… et plus', 'couleur': '#00838f'},
 {'id': 'cod', 'nom': 'Le complément d’objet', 'couleur': '#5e35b1'},
 {'id': 'cc', 'nom': 'Les compléments circonstanciels', 'couleur': '#8d5524'},
 {'id': 'tests', 'nom': 'Les tests', 'couleur': '#7b3fa0'},
 {'id': 'att', 'nom': 'Attention !', 'couleur': '#c62828'},
]
ecrans = [
 E('phrase', 'sv', 'Plus que sujet + verbe', 'girl', 'Les compléments ajoutent des informations à la phrase.',
   ['[Léa] (mange).',
    ('[Léa] (mange) ~*une pomme*~.', 'Qu’est-ce qu’elle mange ?'),
    ('^*Ce matin,*^ [Léa] (mange) ~une pomme~ ^*dans la cuisine*^.', 'Quand ? Où ? D’autres compléments.')],
   SV('[Tom] (lit) un livre dans son lit.'),
   [SV('Le soir, [mon père] (prépare) le repas.'), SV('[Les élèves] (écoutent) une histoire en classe.'),
    SV('Dans la forêt, [le renard] (chasse) un lapin.')]),
 E('cod', 'loupe', 'Le complément d’objet', 'boy', 'Il complète le verbe et se place après lui : « qu’est-ce que… ? », « à qui… ? ».',
   ['[Léa] (mange) une pomme.',
    ('[Léa] (mange) ~*une pomme*~.', 'Il complète le verbe.'),
    ('[Tom] (parle) ~*à sa mère*~.', 'Il parle à qui ? À sa mère.')],
   C('Le chat attrape <une souris>.', 'Clique sur le complément d’objet.', 'Le chat attrape quoi ?'),
   [C('Ma sœur dessine <un cheval>.', 'Clique sur le complément d’objet.', 'Elle dessine quoi ?'),
    C('Tom écrit <à son cousin>.', 'Clique sur le complément d’objet.', 'Il écrit à qui ?'),
    C('Nous regardons <un film>.', 'Clique sur le complément d’objet.', 'Nous regardons quoi ?')]),
 E('cod', 'attention', 'Il est collé au verbe', 'boy', 'Le complément d’objet ne se déplace pas : il reste après le verbe.',
   ['[Tom] (lance) ~le ballon~.',
    ('[Tom] (lance) ~le ballon~.', 'Je cherche s’il peut changer de place.'),
    ('{{Le ballon}} [Tom] (lance).', 'Je déplace : impossible !')],
   Q('Tom construit une cabane.', ['une cabane', 'Tom', 'construit'], 'Tom construit quoi ?', 'Quel est le complément d’objet ?'),
   [Q('Léa offre des fleurs.', ['des fleurs', 'Léa', 'offre'], 'Léa offre quoi ?', 'Quel est le complément d’objet ?'),
    Q('Le soir, le chat mange sa pâtée.', ['« sa pâtée »', '« Le soir »'], 'Le complément d’objet reste après le verbe.', 'Quel groupe ne peut pas changer de place ?')]),
 E('cod', 'loupe', 'COD ou COI ?', 'boy', 'Avec ou sans petit mot entre le verbe et le complément ?',
   [('[Léa] (mange) ~une pomme~.', 'Sans petit mot : complément d’objet direct (COD).'),
    ('[Tom] (parle) ~*à* sa mère~.', 'Avec un petit mot (à, de) : complément d’objet indirect (COI).'),
    ('[Léa] (mange) quoi ? → COD · [Tom] (parle) à qui ? → COI', 'Je pose la question juste après le verbe.')],
   Q('Le chien obéit à son maître.', ['un COI', 'un COD'], 'Il y a le petit mot « à » : objet indirect.', '« à son maître » est…'),
   [Q('Léa lit un livre.', ['un COD', 'un COI'], 'Pas de petit mot : objet direct.', '« un livre » est…'),
    Q('Tom pense à ses vacances.', ['un COI', 'un COD'], 'Il y a le petit mot « à ».', '« à ses vacances » est…'),
    Q('Nous parlons de notre voyage.', ['un COI', 'un COD'], 'Il y a le petit mot « de ».', '« de notre voyage » est…')]),
 E('cc', 'horloge', 'Des précisions en plus', 'girl', 'Les compléments circonstanciels donnent des précisions sur l’action.',
   [('^*Hier,*^ [Léa] (a joué).', 'Une précision : je peux la supprimer.'),
    ('[Léa] (a joué) ^*dans le parc*^.', 'Une autre précision : je peux la déplacer.'),
    ('[Léa] (a joué) ^*joyeusement*^.', 'Encore une précision. Je les repère, sans les classer.')],
   Q('Le soir, Tom lit.', ['Le soir', 'Tom', 'lit'], 'Je peux le déplacer ou le supprimer : la phrase garde son sens.', 'Quel groupe est un complément circonstanciel ?'),
   [Q('Les poissons nagent dans la rivière.', ['dans la rivière', 'Les poissons', 'nagent'], 'Je peux le déplacer ou le supprimer : la phrase garde son sens.', 'Quel groupe est un complément circonstanciel ?'),
    Q('Le chat marche doucement.', ['doucement', 'Le chat', 'marche'], 'Je peux le déplacer ou le supprimer : la phrase garde son sens.', 'Quel groupe est un complément circonstanciel ?'),
    Q('En été, nous allons à la mer.', ['En été', 'nous', 'allons'], 'Je peux le déplacer ou le supprimer : la phrase garde son sens.', 'Quel groupe est un complément circonstanciel ?')]),
 E('tests', 'ciseaux', 'Je supprime', 'boy', 'Un complément circonstanciel peut être supprimé : la phrase garde son sens.',
   ['^Ce matin,^ [les élèves] (chantent) ^dans la cour^.',
    '{Ce matin,} [les élèves] (chantent) {dans la cour}.',
    ('[Les élèves] (chantent).', 'La phrase a encore du sens : ce sont des compléments circonstanciels.')],
   Q('Le chien dort sous la table.', ['sous la table', 'le chien', 'dort'], 'La phrase doit garder du sens.', 'Quel groupe peut-on supprimer ?'),
   [Q('Demain, nous irons au cinéma.', ['Demain', 'nous', 'irons'], 'Un complément circonstanciel peut se supprimer.', 'Quel mot peut-on supprimer ?'),
    Q('Les oiseaux chantent dans les arbres.', ['dans les arbres', 'Les oiseaux', 'chantent'], 'La phrase doit garder du sens.', 'Quel groupe peut-on supprimer ?')]),
 E('tests', 'deplacer', 'Je déplace', 'boy', 'Un complément circonstanciel peut changer de place.',
   ['[Les élèves] (chantent) ^dans la cour^.',
    ('^*Dans la cour,*^ [les élèves] (chantent).', 'Je peux le mettre en début de phrase.'),
    ('[Les élèves] (chantent) ^dans la cour^.', 'ou le laisser à la fin.')],
   Q('Le chat dort sur le canapé.', ['Sur le canapé, le chat dort.', 'Le canapé dort sur le chat.', 'Dort le chat sur le canapé.'], 'Je déplace seulement le complément circonstanciel.', 'Quelle phrase déplace bien le complément ?'),
   [Q('Nous partons demain.', ['Demain, nous partons.', 'Partons demain nous.', 'Nous demain, partons.'], 'Je déplace « demain » au début.', 'Quelle phrase déplace bien le complément ?'),
    Q('Tom joue au foot dans le jardin.', ['Dans le jardin, Tom joue au foot.', 'Au foot, Tom joue dans le jardin.'], '« au foot » est collé au verbe.', 'Quelle phrase déplace bien le complément circonstanciel ?')]),
 E('tests', 'loupe', 'Complément d’objet ou circonstanciel ?', 'boy', 'Le test le plus sûr : je déplace.',
   ['[Léa] (cueille) des fleurs dans le jardin.',
    ('[Léa] (cueille) des fleurs ^*dans le jardin*^.', 'Je peux le déplacer : complément circonstanciel.'),
    ('[Léa] (cueille) ~*des fleurs*~ ^dans le jardin^.', 'Je ne peux pas le déplacer : complément d’objet.')],
   Q2('Léa cueille des fleurs dans le jardin.',
      ('Quel est le complément d’objet ?', ['des fleurs', 'dans le jardin'], 'Léa cueille quoi ?'),
      ('Quel est le complément circonstanciel ?', ['dans le jardin', 'des fleurs'], 'Où ? Je peux le supprimer.')),
   [Q2('Le soir, Papa lit un livre.',
      ('Quel est le complément d’objet ?', ['un livre', 'Le soir'], 'Papa lit quoi ?'),
      ('Quel est le complément circonstanciel ?', ['Le soir', 'un livre'], 'Quand ? Je peux le déplacer.')),
    Q2('Le chien mange sa pâtée dans la cuisine.',
      ('Quel est le complément d’objet ?', ['sa pâtée', 'dans la cuisine'], 'Le chien mange quoi ?'),
      ('Quel est le complément circonstanciel ?', ['dans la cuisine', 'sa pâtée'], 'Où ? Je peux le supprimer.'))]),
 E('att', 'point', 'La virgule', 'girl', 'En début de phrase, le complément circonstanciel est suivi d’une virgule.',
   ['[Les oiseaux] (chantent) ^le matin^.',
    ('^Le matin*,*^ [les oiseaux] (chantent).', 'Je le déplace au début : j’ajoute une virgule.')],
   Q('', ['Le matin, les oiseaux chantent.', 'Le matin les oiseaux, chantent.', 'Le, matin les oiseaux chantent.'], 'La virgule se place juste après le complément.', 'Quelle phrase est bien écrite ?'),
   [Q('', ['Dans la cour, les enfants jouent.', 'Dans la cour les enfants, jouent.', 'Dans, la cour les enfants jouent.'], 'La virgule se place juste après « Dans la cour ».', 'Quelle phrase est bien écrite ?'),
    Q('', ['Hier soir, il a neigé.', 'Hier, soir il a neigé.', 'Hier soir il, a neigé.'], 'Le complément, c’est « Hier soir ».', 'Quelle phrase est bien écrite ?')]),
 E('att', 'liste', 'Plusieurs compléments', 'girl', 'Une phrase peut avoir plusieurs compléments.',
   [('^Samedi,^ [nous] (avons mangé) ~une glace~ ^au bord de la mer^.', 'Trois compléments !'),
    ('^Samedi^ → quand ? · ^au bord de la mer^ → où ?', 'Deux compléments circonstanciels.'),
    ('~une glace~ → nous avons mangé quoi ?', 'Un complément d’objet.')],
   Q('Demain matin, Léa promènera son chien dans le parc.', ['2', '1', '3'], 'Quand ? Où ?', 'Combien de compléments circonstanciels ?'),
   [Q('Le soir, Tom range sa chambre.', ['1', '2', '0'], 'Seul « Le soir » peut se supprimer.', 'Combien de compléments circonstanciels ?')]),
]
# écrans dont les étapes restent affichées (14/11/2026, comme G2 et G3)
for _e in ecrans:
    if _e['titre'] in ['Des précisions en plus']: _e['cumul'] = True
save('G6', {'id': 'G6', 'f': 'G', 'ceinture': 'Bleue', 'titre': 'Les compléments', 'sous': 'd’objet et circonstanciels', 'lesson': True}, sections, ecrans, zones)
