import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from mapgen import build, TL, TC, TR
from lhelp import *

e = lambda t: f'<span class="e">{t}</span>'
boxes = [
 dict(id='gn', col='orange', geom=TL, title='Dans le GN', avatar=('girl', 322, 122), html=f'''
  <p class="txt" style="padding-right:100px">Le <span class="d">déterminant</span> et l’<span class="a">adjectif</span> s’accordent avec le <b style="color:#1f5fc4">nom noyau</b>.</p>
  <div class="ex big" style="margin-top:16px"><span class="d">les</span> <span class="a">petit{e('es')}</span> <span class="n">fille{e('s')}</span></div>
  <p class="small" style="margin:8px 0 0">féminin <span class="arrow">→</span> souvent <b>e</b> · pluriel <span class="arrow">→</span> souvent <b>s</b></p>'''),
 dict(id='sv', col='rouge', geom=TC, title='Sujet → verbe', html=f'''
  <p class="txt">Le <span class="v">verbe</span> s’accorde avec son <span class="s">sujet</span>.</p>
  <div class="ex" style="text-align:center;font-size:22px;line-height:1.6"><span class="s">La fille</span> <span class="v">chante</span>.<br><span class="s">Les filles</span> <span class="v">chant{e('ent')}</span>.</div>'''),
 dict(id='etre', col='violet', geom=TR, title='Le participe passé avec être', hstyle='font-size:25px', html=f'''
  <p class="txt" style="font-size:19px">Avec <b>être</b>, il s’accorde avec le <span class="s">sujet</span>, comme un adjectif.</p>
  <div class="ex" style="font-size:19px;line-height:1.45"><span class="s">Tom</span> <span class="v">est parti</span>. · <span class="s">Léa</span> <span class="v">est parti{e('e')}</span>.<br><span class="s">Ils</span> <span class="v">sont parti{e('s')}</span>. · <span class="s">Elles</span> <span class="v">sont parti{e('es')}</span>.</div>
  <p class="small" style="margin:6px 0 0">Avec <b>avoir</b> : pas d’accord avec le sujet.<br><span class="s">Léa</span> <span class="v">a mangé</span>.</p>'''),
 dict(id='chaine', col='bleu', geom=(18, 568, 700, 350), title='La chaîne complète', style='padding-top:52px', html=f'''
  <p class="txt">Le nom noyau du sujet commande toute la chaîne.</p>
  <div class="ex" style="text-align:center;font-size:25px;padding:12px 8px"><span class="d">Les</span> <span class="a">petit{e('es')}</span> <span class="n">fille{e('s')}</span> <span class="v">sont</span> <span class="v">arrivé{e('es')}</span>.</div>
  <p class="txt" style="text-align:center;margin-top:10px"><b style="color:#1f5fc4">filles</b> <span class="arrow">→</span> féminin pluriel</p>
  <p class="txt" style="text-align:center;margin:0 0 10px">les · petites · sont · arrivées : tout s’accorde !</p>
  <div class="ex" style="text-align:center;font-size:20px;line-height:1.5">Le petit chat est rentré.<br><span class="arrow">→</span> Les petit<span class="e">s</span> chat<span class="e">s</span> <span class="v">sont</span> rentré<span class="e">s</span>.</div>'''),
 dict(id='methode', col='vert', geom=(752, 568, 630, 350), title='Je vérifie', style='padding-top:52px', avatar=('boy', 1250, 610), html='''
  <ol style="margin:0;padding-left:26px;font-size:22px;line-height:1.5;padding-right:112px">
   <li>Je trouve le <b>nom noyau</b> du sujet : masculin ou féminin ? singulier ou pluriel ?</li>
   <li>J’accorde le <b>GN</b>.</li>
   <li>J’accorde le <span class="v">verbe</span>.</li>
   <li>Avec <b>être</b>, j’accorde le participe passé.</li></ol>'''),
]
legend = '<span class="d">dét.</span> · <span class="a">adj.</span> · <b style="color:#1f5fc4">nom</b> · <span class="s">sujet</span> · <span class="v">verbe</span>'
out, zones = build('G7', 'La chaîne<br>des accords', 'Grammaire — G7 — CM1', legend, boxes, title_size=38, legend_pos='right:18px;top:470px')

sections = [
 {'id': 'gn', 'nom': 'Dans le GN', 'couleur': '#e67e22'},
 {'id': 'sv', 'nom': 'Sujet → verbe', 'couleur': '#c62828'},
 {'id': 'etre', 'nom': 'Le participe passé avec être', 'couleur': '#7b3fa0'},
 {'id': 'chaine', 'nom': 'La chaîne complète', 'couleur': '#1f5fc4'},
 {'id': 'methode', 'nom': 'Je vérifie', 'couleur': '#23845a'},
]
ecrans = [
 E('gn', 'wagon', 'Le nom noyau commande', 'girl', 'Dans le GN, tout s’accorde avec le nom noyau.',
   ['un chat noir',
    ('^des^ |chat*s*| ~noir*s*~', 'Pluriel : le nom et l’adjectif prennent un s.'),
    ('^une^ |chatte| ~noir*e*~', 'Féminin : l’adjectif prend souvent un e.')],
   Q('les ___ voitures', ['petites', 'petite', 'petits'], 'Voitures : féminin pluriel.', fill='pr'),
   [Q('des ballons ___', ['ronds', 'rond', 'rondes'], 'Ballons : masculin pluriel.', fill='pr'),
    Q('une ___ maison', ['grande', 'grand', 'grandes'], 'Maison : féminin singulier.', fill='pr'),
    Q('', ['de jolies fleurs', 'de jolie fleurs', 'de jolies fleur'], 'Chaque mot prend la marque du pluriel.', 'Quel GN est bien accordé ?')]),
 E('sv', 'sv', 'Le sujet commande le verbe', 'boy', 'Le verbe s’accorde avec son sujet.',
   ['[La fille] (chante).',
    ('[Les filles] (chant*ent*).', 'Les filles = elles → -ent'),
    ('[Les filles du voisin] (chant*ent*).', 'Le sujet peut être long : je cherche le nom noyau.')],
   Q('Les chiens du voisin ___.', ['aboient', 'aboie'], 'Qui est-ce qui aboie ? Les chiens.', fill='v'),
   [Q('Le frère de mes amis ___ loin.', ['habite', 'habitent'], 'Qui est-ce qui habite ? Le frère.', fill='v'),
    Q('Tes cousines ___ en vacances.', ['partent', 'part'], 'Tes cousines = elles.', fill='v')]),
 E('etre', 'tableau', 'Avec être, le participe s’accorde', 'girl', 'Avec être, le participe passé s’accorde avec le sujet.',
   ['[Tom] (est parti).',
    ('[Léa] (est parti*e*).', 'Léa : féminin → e'),
    ('[Les garçons] (sont parti*s*).', 'pluriel → s'),
    ('[Les filles] (sont parti*es*).', 'féminin pluriel → es')],
   Q('Ma sœur est ___.', ['tombée', 'tombé', 'tombés'], 'Ma sœur : féminin singulier.', fill='v'),
   [Q('Mes amis sont ___.', ['venus', 'venu', 'venues'], 'Mes amis : masculin pluriel.', fill='v'),
    Q('Les filles sont ___ au parc.', ['allées', 'allé', 'allés'], 'Les filles : féminin pluriel.', fill='v'),
    Q('Mon père est ___ tard.', ['rentré', 'rentrée', 'rentrés'], 'Mon père : masculin singulier.', fill='v')]),
 E('etre', 'ampoule', 'Comme un adjectif', 'girl', 'Le participe passé avec être s’accorde comme un adjectif.',
   [('[Léa] (est) ~content*e*~.', 'L’adjectif s’accorde avec Léa.'),
    ('[Léa] (est arrivé*e*).', 'Le participe passé aussi !'),
    ('[Mes amies] (sont arrivé*es*).', 'Mes amies = elles : féminin pluriel.')],
   Q('Les enfants sont ___ à l’école.', ['allés', 'allé', 'allée'], 'Les enfants : masculin pluriel.', fill='v'),
   [Q('La neige est ___.', ['tombée', 'tombé', 'tombées'], 'La neige : féminin singulier.', fill='v'),
    Q('Nos voisines sont ___.', ['parties', 'partie', 'partis'], 'Nos voisines : féminin pluriel.', fill='v')]),
 E('etre', 'attention', 'Avec avoir, c’est différent', 'girl', 'Avec avoir, le participe passé ne s’accorde pas avec le sujet.',
   [('[Léa] (a mangé).', 'avec avoir : pas d’accord avec le sujet.'),
    ('[Léa] (est tombé*e*).', 'avec être : j’accorde.')],
   Q('Mes sœurs ont ___ une glace.', ['mangé', 'mangées', 'mangés'], 'Avec avoir, je n’accorde pas avec le sujet.', fill='v'),
   [Q('Mes sœurs sont ___.', ['tombées', 'tombé', 'tombés'], 'Avec être, j’accorde : féminin pluriel.', fill='v'),
    Q('Les filles ont ___ une chanson.', ['chanté', 'chantées', 'chantés'], 'Avec avoir, pas d’accord avec le sujet.', fill='v')]),
 E('chaine', 'wagon', 'Toute la chaîne', 'boy', 'Le nom noyau du sujet commande toute la chaîne.',
   ['Les petites filles sont arrivées.',
    ('^Les^ ~petites~ |filles| sont arrivées.', '1. Le GN sujet : féminin pluriel.'),
    ('[Les petites filles] (*sont*) arrivées.', '2. Le verbe : elles → sont.'),
    ('[Les petites filles] (sont arrivé*es*).', '3. Le participe passé : féminin pluriel → es.')],
   Q('', ['Les grandes sœurs sont venues.', 'Les grande sœurs sont venues.', 'Les grandes sœurs est venues.'], 'Vérifie chaque mot : GN, verbe, participe.', 'Quelle phrase est bien accordée ?'),
   [Q('', ['Les vieux chats sont rentrés.', 'Les vieux chats est rentrés.', 'Les vieux chat sont rentré.'], 'Chats : masculin pluriel.', 'Quelle phrase est bien accordée ?'),
    Q('', ['Ma petite cousine est arrivée.', 'Ma petit cousine est arrivé.', 'Ma petite cousine sont arrivée.'], 'Cousine : féminin singulier.', 'Quelle phrase est bien accordée ?')]),
 E('chaine', 'remplacer', 'Je change le sujet', 'boy', 'Si le sujet change, toute la chaîne change !',
   ['[Le petit chat] (est rentré).',
    ('[Les petit*s* chat*s*] (sont rentré*s*).', 'Pluriel : tout change.'),
    ('[La petit*e* chatt*e*] (est rentré*e*).', 'Féminin : tout change aussi.')],
   Q('La petite chatte est ___.', ['rentrée', 'rentré', 'rentrés'], 'Chatte : féminin singulier.', fill='v'),
   [Q('Les petites chattes ___ rentrées.', ['sont', 'est'], 'Les petites chattes = elles.', fill='v'),
    Q('Le grand garçon est ___.', ['venu', 'venue', 'venus'], 'Garçon : masculin singulier.', fill='v')]),
 E('methode', 'coche', 'Je vérifie une phrase', 'girl', 'Je trouve le nom noyau, puis je vérifie chaque mot.',
   [('Les vieille maisons est fermé.', 'Il y a des erreurs !'),
    ('^Les^ ~vieille~ |maisons| est fermé.', '1. Le nom noyau : maisons → féminin pluriel.'),
    ('^Les^ ~vieille*s*~ |maisons| est fermé.', '2. J’accorde le GN.'),
    ('[Les vieilles maisons] (sont fermé*es*).', '3. J’accorde le verbe, puis le participe.')],
   Q('Mes cousine est parti.', ['Mes cousines sont parties.', 'Mes cousines est parties.', 'Mes cousine sont partis.'], 'Cousines : féminin pluriel. Tout s’accorde.', 'Quelle est la bonne correction ?'),
   [Q('Les grand arbres est tombé.', ['Les grands arbres sont tombés.', 'Les grands arbres est tombés.', 'Les grand arbres sont tombé.'], 'Arbres : masculin pluriel.', 'Quelle est la bonne correction ?'),
    Q('La petit fille sont arrivé.', ['La petite fille est arrivée.', 'La petite fille sont arrivée.', 'La petit fille est arrivé.'], 'Fille : féminin singulier.', 'Quelle est la bonne correction ?')]),
]
save('G7', {'id': 'G7', 'f': 'G', 'ceinture': 'Violette', 'titre': 'La chaîne des accords', 'sous': 'GN, sujet-verbe, participe passé', 'lesson': True}, sections, ecrans, zones)
