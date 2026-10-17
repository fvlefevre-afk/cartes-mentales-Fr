import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from mapgen import build, TL, TC, TR
from lhelp import *
from hlib import R, rows, table

# H7 — se, s’est. Jumeaux interdits : ce (cet, cette), c’est (et les sons voisins ces / ses).
boxes = [
 dict(id='se', col='bleu', geom=TL, title='se : devant un verbe', html=rows([
   ('se', '<b>pronom</b>, devant un verbe', 'je change la personne : <b>je me</b>', f'Il {R("se")} lave.<br>→ Je me lave.')]) +
   f'<span class="exl" style="margin-top:6px">Les chats {R("se")} cachent.</span>'),
 dict(id='pers', col='vert', geom=TC, title='je me, tu te, il se', html='''
  <p class="txt">Le pronom change avec la personne :</p>
  <div class="exl" style="font-size:20px;line-height:1.55">je <b>me</b> lave · tu <b>te</b> laves<br>il, elle <span class="rond">se</span> lave<br>nous <b>nous</b> lavons · vous <b>vous</b> lavez<br>ils, elles <span class="rond">se</span> lavent</div>'''),
 dict(id='sest', col='orange', geom=TR, title='s’est : au passé composé', hstyle='font-size:26px', html=rows([
   ('s’est', '<b>se</b> + <b>est</b> : le passé composé', 'je change la personne : <b>je me suis</b>', f'Tom {R("s’est")} levé.<br>→ Je me suis levé.')]) +
   '<p class="small" style="margin:6px 0 0">Il se lève (aujourd’hui) <span class="arrow">→</span> il s’est levé (hier).</p>'),
 dict(id='acc', col='violet', geom=(18, 568, 560, 350), title='L’accord avec s’est', style='padding-top:52px', avatar=('girl', 445, 610), html='''
  <p class="txt" style="padding-right:110px">Comme avec <b>être</b>, le participe passé s’accorde avec le <span class="s">sujet</span>.</p>
  <div class="exl" style="font-size:21px;line-height:1.6;margin-right:110px"><span class="s">Tom</span> s’est levé.<br><span class="s">Léa</span> s’est levé<span class="e">e</span>.<br><span class="s">Ils</span> se sont levé<span class="e">s</span>.</div>'''),
 dict(id='att', col='rouge', geom=(612, 568, 770, 350), title='Attention !', style='padding-top:52px', avatar=('boy', 1250, 610), html='''
  <ul style="font-size:22px;line-height:1.5;padding-right:110px">
   <li><b>se</b> est suivi d’un verbe conjugué : <i>il se cache</i>.</li>
   <li><b>s’est</b> est suivi d’un participe passé : <i>il s’est caché</i>.</li>
   <li>Au pluriel, <b>s’est</b> devient <b>se sont</b> : <i>ils se sont cachés</i>.</li></ul>'''),
]
out, zones = build('H7', 'se, s’est', 'Homophones — H7 — CM1', None, boxes, title_size=40, sub='homophones')

sections = [
 {'id': 'se', 'nom': 'se : devant un verbe', 'couleur': '#1f5fc4'},
 {'id': 'pers', 'nom': 'je me, tu te, il se', 'couleur': '#23845a'},
 {'id': 'sest', 'nom': 's’est : au passé composé', 'couleur': '#e67e22'},
 {'id': 'acc', 'nom': 'L’accord avec s’est', 'couleur': '#7b3fa0'},
 {'id': 'att', 'nom': 'Attention !', 'couleur': '#c62828'},
]
ecrans = [
 E('se', 'remplacer', 'se : devant un verbe', 'girl', 'Se est un pronom : il est toujours devant un verbe.',
   ['Il |se| lave.',
    ('Je |*me*| lave.', 'Je prouve : je change la personne. se devient me.'),
    ('Les chats |se| cachent.', 'se est devant le verbe.')],
   Q('Le chat ___ cache.', ['se', 's’est'], 'Aujourd’hui : il se cache.', fill='circ'),
   [Q('Léa ___ brosse les dents.', ['se', 's’est'], 'Aujourd’hui : je me brosse les dents.', fill='circ'),
    C('Les oiseaux <se> posent sur le toit.', 'Clique sur le pronom.', 'Il est juste devant le verbe.')]),
 E('pers', 'tableau', 'je me, tu te, il se', 'girl', 'Le pronom change avec la personne.',
   ['je |me| lave · tu |te| laves · il |se| lave',
    ('nous |nous| lavons · vous |vous| lavez · ils |se| lavent', 'se va avec il, elle, on, ils, elles.')],
   Q('Les enfants ___ cachent.', ['se', 'me', 'te'], 'Ils → se.', fill='circ'),
   [Q('Tu ___ réveilles tôt.', ['te', 'se', 'me'], 'Tu → te.', fill='circ'),
    Q('Elle ___ coiffe.', ['se', 'me', 'te'], 'Elle → se.', fill='circ')]),
 E('sest', 'horloge', 's’est : au passé composé', 'boy', 'S’est = se + est : le passé composé.',
   ['Aujourd’hui, Tom |se| lève.',
    ('Hier, Tom |s’est| levé.', 'Au passé composé : se + est = s’est.'),
    ('Hier, je |*me suis*| levé.', 'Je prouve : je change la personne. s’est devient me suis.')],
   Q('Hier, Léa ___ promenée.', ['s’est', 'se'], 'Au passé composé : je me suis promenée.', fill='circ'),
   [Q('Le bébé ___ endormi.', ['s’est', 'se'], 'Je me suis endormi.', fill='circ'),
    Q('Mon frère ___ coupé le doigt.', ['s’est', 'se'], 'Je me suis coupé.', fill='circ')]),
 E('sest', 'loupe', 'se ou s’est ?', 'boy', 'Un verbe conjugué ? se. Un participe passé ? s’est.',
   [('Il |se| lève tôt.', 'aujourd’hui : se + verbe conjugué'),
    ('Il |s’est| levé tôt.', 'hier : s’est + participe passé')],
   Q2('Aujourd’hui, Tom ___ réveille. Hier, il ___ réveillé tard.',
      ('Premier trou :', ['se', 's’est'], 'Aujourd’hui : je me réveille.', 'circ'),
      ('Deuxième trou :', ['s’est', 'se'], 'Hier : je me suis réveillé.', 'circ')),
   [Q2('Le chien ___ couche. Hier, il ___ couché tôt.',
      ('Premier trou :', ['se', 's’est'], 'Aujourd’hui : je me couche.', 'circ'),
      ('Deuxième trou :', ['s’est', 'se'], 'Hier : je me suis couché.', 'circ'))]),
 E('acc', 'wagon', 'L’accord avec s’est', 'girl', 'Comme avec être, le participe passé s’accorde avec le sujet.',
   ['Tom |s’est| levé.',
    ('Léa |s’est| levé*e*.', 'Léa : féminin → e.'),
    ('Ils |se sont| levé*s*.', 'Au pluriel : se sont… et un s.')],
   Q('Ma sœur s’est ___.', ['habillée', 'habillé', 'habillés'], 'Ma sœur : féminin.', fill='v'),
   [Q('Le chat s’est ___.', ['caché', 'cachée', 'cachés'], 'Le chat : masculin singulier.', fill='v'),
    Q('Mes amies se sont ___.', ['amusées', 'amusé', 'amusée'], 'Mes amies : féminin pluriel.', fill='v')]),
 E('att', 'attention', 'Les pièges', 'boy', 'Je regarde le mot qui suit !',
   [('Il |se| *cache*.', 'se + verbe conjugué'),
    ('Il |s’est| *caché*.', 's’est + participe passé'),
    ('Ils |se sont| caché*s*.', 'au pluriel : se sont')],
   Q('', ['Il s’est endormi.', 'Il se endormi.'], 'Passé composé : s’est + participe passé.', 'Quelle phrase est bien écrite ?'),
   [Q('', ['Elles se sont amusées.', 'Elles s’est amusées.'], 'Au pluriel : se sont.', 'Quelle phrase est bien écrite ?')]),
]
save('H7', {'id': 'H7', 'f': 'H', 'ceinture': 'Violette', 'titre': "se, s'est", 'sous': 'le pronom se · s’est au passé composé', 'lesson': True}, sections, ecrans, zones)
