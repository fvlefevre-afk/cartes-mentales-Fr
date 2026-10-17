import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from mapgen import build, TL, TC, TR
from lhelp import *
from hlib import R, rows, table, A

def grid(pairs, size=19):
    return (f'<div style="display:grid;grid-template-columns:1fr 1fr;gap:7px 12px;font-size:{size}px;line-height:1.25">' +
            ''.join(f'<div style="white-space:nowrap">{R(a)} {A} {b}</div>' for a, b in pairs) + '</div>')

boxes = [
 dict(id='verbes', col='bleu', geom=TL, title='Les verbes cachés', avatar=('girl', 322, 122), html=
   '<p class="txt" style="padding-right:100px">Je dis le verbe à l’<b>imparfait</b> : si ça marche, c’est le verbe !</p>' +
   '<div style="margin-top:14px">' + grid([('a', 'avait'), ('ont', 'avaient'), ('est', 'était'), ('sont', 'étaient'), ('s’est', 'je me suis')], 18) + '</div>'),
 dict(id='det', col='vert', geom=TC, title='Devant un nom', html=
   '<p class="txt">J’essaie un autre petit mot devant le nom.</p>' +
   grid([('la', 'une, le'), ('ce', 'ces'), ('ces', 'ce, cette'), ('ses', 'son, sa'), ('son', 'mon'), ('mes', 'mon, ma')])),
 dict(id='autres', col='orange', geom=TR, title='Les petits mots', html=
   grid([('on', 'quelqu’un'), ('là', 'ici'), ('ou', 'ou bien'), ('où', 'un lieu'), ('et', 'j’ajoute'), ('mais', 'contraire'), ('à', 'ne change pas'), ('c’est', 'c’était'), ('se', 'je me')], 18)),
 dict(id='methode', col='violet', geom=(18, 568, 560, 350), title='Ma méthode en dictée', style='padding-top:52px', html='''
  <ol style="margin:0;padding-left:26px;font-size:23px;line-height:1.55">
   <li>Je repère le mot qui se prononce pareil.</li>
   <li>Je regarde le mot d’après : un nom ? un verbe ?</li>
   <li>Je <b>prouve</b> avec une manipulation.</li>
   <li>J’écris, puis je <b>relis</b>.</li></ol>'''),
 dict(id='relire', col='rouge', geom=(612, 568, 770, 350), title='Je relis et je corrige', style='padding-top:52px', avatar=('boy', 1250, 610), html=f'''
  <p class="txt" style="padding-right:110px">Avant de rendre mon texte, je vérifie chaque homophone.</p>
  <div class="exl" style="font-size:20px;line-height:1.6;margin-right:110px"><span class="barre">Mais</span> copains <span class="barre">on</span> fini et ils <span class="barre">son</span> contents.<br>
  <span class="arrow">→</span> {R("Mes")} copains {R("ont")} fini et ils {R("sont")} contents.</div>
  <div class="exl" style="font-size:20px;line-height:1.6;margin-right:110px;margin-top:10px">Léa <span class="barre">à</span> mal <span class="barre">a</span> la tête.<br>
  <span class="arrow">→</span> Léa {R("a")} mal {R("à")} la tête.</div>'''),
]
out, zones = build('H8', 'Transfert', 'Homophones — H8 — CM1', None, boxes, title_size=40, sub='toutes les paires')

sections = [
 {'id': 'verbes', 'nom': 'Les verbes cachés', 'couleur': '#1f5fc4'},
 {'id': 'det', 'nom': 'Devant un nom', 'couleur': '#23845a'},
 {'id': 'autres', 'nom': 'Les petits mots', 'couleur': '#e67e22'},
 {'id': 'methode', 'nom': 'Ma méthode en dictée', 'couleur': '#7b3fa0'},
 {'id': 'relire', 'nom': 'Je relis et je corrige', 'couleur': '#c62828'},
]
ecrans = [
 E('verbes', 'horloge', 'Le truc de l’imparfait', 'girl', 'Si je peux dire le verbe à l’imparfait, c’est bien le verbe !',
   ['il |a| → il avait · ils |ont| → ils avaient',
    'il |est| → il était · ils |sont| → ils étaient',
    ('il |s’est| levé → je me suis levé', 'Je remplace : si la phrase a du sens, c’est le verbe.')],
   Q2('Les enfants ___ contents : ils ___ gagné.',
      ('Premier trou :', ['sont', 'son'], 'Ils étaient contents.', 'circ'),
      ('Deuxième trou :', ['ont', 'on'], 'Ils avaient gagné.', 'circ')),
   [Q2('Léa ___ malade ___ elle reste au lit.',
      ('Premier trou :', ['est', 'et'], 'Léa était malade.', 'circ'),
      ('Deuxième trou :', ['et', 'est'], 'Et puis elle reste au lit.', 'circ')),
    Q2('Tom ___ rendez-vous ___ midi.',
      ('Premier trou :', ['a', 'à'], 'Tom avait rendez-vous.', 'circ'),
      ('Deuxième trou :', ['à', 'a'], 'Petit mot devant midi.', 'circ'))]),
 E('det', 'etiquette', 'Devant un nom', 'boy', 'Devant un nom, je change le nombre ou la personne.',
   [('|ces| fleurs → cette fleur · |ses| fleurs → sa fleur', 'ces : je montre · ses : à elle'),
    ('|son| sac → mon sac · |mes| sacs → mon sac', 'Je change de personne ou de nombre.'),
    ('|la| table → une table · |ce| chien → ces chiens', 'J’ai trouvé le bon mot !')],
   Q2('Léa range ___ jouets dans ___ boîte.',
      ('Premier trou :', ['ses', 'ces'], 'Son jouet → ses jouets : à elle.', 'circ'),
      ('Deuxième trou :', ['la', 'là', 'l’a'], 'Une boîte.', 'circ')),
   [Q2('___ chat dort sur ___ coussin.',
      ('Premier trou :', ['Ce', 'Se'], 'Ces chats → ce.', 'circ'),
      ('Deuxième trou :', ['son', 'sont'], 'Mon coussin.', 'circ')),
    Q2('J’ai perdu ___ gants ___ je les cherche.',
      ('Premier trou :', ['mes', 'mais'], 'Mon gant → mes gants.', 'circ'),
      ('Deuxième trou :', ['et', 'est'], 'Et puis je les cherche.', 'circ'))]),
 E('autres', 'mots', 'Les petits mots', 'girl', 'Chaque petit mot se prouve par une manipulation.',
   [('|On| part ? → Quelqu’un part ?', 'on → quelqu’un'),
    ('Ici |ou| |là|-bas ?', 'ou → ou bien · là → ici'),
    ('|Où| es-tu ?', 'où → le lieu'),
    ('Il pleut, |mais| je sors.', 'mais → deux idées contraires')],
   Q2('___ va au cinéma ___ au parc ?',
      ('Premier trou :', ['On', 'Ont'], 'Quelqu’un va au cinéma.', 'circ'),
      ('Deuxième trou :', ['ou', 'où'], 'Ou bien au parc.', 'circ')),
   [Q2('___ habites-tu ? ___ Paris ?',
      ('Premier trou :', ['Où', 'Ou'], 'Question sur le lieu.', 'circ'),
      ('Deuxième trou :', ['À', 'A'], 'Petit mot, avec un accent même en majuscule.', 'circ')),
    Q2('Mets ton sac ___, ___ pas sur la table !',
      ('Premier trou :', ['là', 'la'], 'Mets-le ici.', 'circ'),
      ('Deuxième trou :', ['mais', 'mes'], 'Deux idées contraires.', 'circ'))]),
 E('autres', 'loupe', 'c’est, s’est, se, ce', 'girl', 'C’était ? Je me suis ? Je me ? Ces ?',
   [('|C’est| la fin : Tom |s’est| endormi.', 'c’était · je me suis endormi'),
    ('|Ce| soir, il |se| couche tôt.', 'ces soirs · je me couche')],
   Q2('___ la fin : Léa ___ endormie.',
      ('Premier trou :', ['C’est', 'S’est'], 'C’était la fin.', 'circ'),
      ('Deuxième trou :', ['s’est', 'c’est'], 'Je me suis endormie.', 'circ')),
   [Q2('___ matin, le chat ___ cache.',
      ('Premier trou :', ['Ce', 'Se'], 'Ces matins → ce.', 'circ'),
      ('Deuxième trou :', ['se', 'ce'], 'Je me cache.', 'circ'))]),
 E('methode', 'liste', 'Ma méthode en dictée', 'boy', 'Repérer, regarder, remplacer, relire.',
   [('Les enfants %on/ont% faim.', '1. Je repère le mot qui se prononce pareil.'),
    ('Les enfants %on/ont% *faim*.', '2. Je regarde le mot d’après.'),
    ('Les enfants *avaient* faim.', '3. Je prouve : avaient → ont.'),
    ('Les enfants |ont| faim.', '4. J’écris, puis je relis.')],
   Q('Mes parents ___ partis.', ['sont', 'son'], 'Mes parents étaient partis.', fill='circ'),
   [Q('Le chien ___ couché.', ['s’est', 'c’est'], 'Je me suis couché.', fill='circ'),
    Q('Tu veux du pain ___ des biscuits ?', ['ou', 'où'], 'Ou bien des biscuits.', fill='circ')]),
 E('relire', 'coche', 'Je corrige une phrase', 'boy', 'Je relis chaque homophone et je le prouve.',
   [('Mais copains on fini et ils son contents.', 'Il y a des erreurs !'),
    ('%Mais% copains %on% fini et ils %son% contents.', 'Je repère les homophones.'),
    ('|Mes| copains |ont| fini et ils |sont| contents.', 'mon copain · avaient fini · étaient contents')],
   Q('Léa à mal a la tête.', ['Léa a mal à la tête.', 'Léa à mal a la tête.', 'Léa a mal a la tête.'], 'Léa avait mal · petit mot à.', 'Quelle est la bonne correction ?'),
   [Q('Il c’est caché sous se lit.', ['Il s’est caché sous ce lit.', 'Il c’est caché sous ce lit.', 'Il s’est caché sous se lit.'], 'Je me suis caché · ces lits → ce.', 'Quelle est la bonne correction ?'),
    Q('Ont a vu ses oiseaux-là.', ['On a vu ces oiseaux-là.', 'Ont a vu ces oiseaux-là.', 'On a vu ses oiseaux-là.'], 'Quelqu’un a vu · cet oiseau → ces oiseaux.', 'Quelle est la bonne correction ?')]),
]
save('H8', {'id': 'H8', 'f': 'H', 'ceinture': 'Marron', 'titre': 'Transfert', 'sous': 'toutes les paires en dictée', 'lesson': True}, sections, ecrans, zones)
