import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from mapgen import build, TL, TC, TR
from lhelp import *
from hlib import A
from clib import T, S, conj

V = lambda t: f'<span class="v">{t}</span>'
boxes = [
 dict(id='deux', col='bleu', geom=TL, title='Un temps en deux parties', hstyle='font-size:26px', avatar=('girl', 322, 122), html=f'''
  <p class="txt" style="padding-right:100px">Le <b>passé composé</b> parle d’une action <b>terminée</b>.</p>
  <p class="txt" style="padding-right:100px"><b>avoir</b> au présent + <b>participe passé</b></p>
  <div class="exl" style="font-size:22px;text-align:center;margin-top:10px">Hier, j’{V("ai")} chant{T("é")}.<br>Nous {V("avons")} fin{T("i")}.</div>'''),
 dict(id='avoir', col='vert', geom=TC, title='avoir au présent', html=f'''
  <div style="display:flex;gap:26px">{conj([("j’","",""),("tu","",""),("il, elle","","")],20).replace("<td></td>","")}</div>'''.replace('{conj', '{conj') ),
 dict(id='pp', col='violet', geom=TR, title='Le participe passé', html=f'''
  <table class="tr" style="font-size:20px"><tr><td>1er groupe</td><td>chanter {A} chant{T("é")}</td></tr>
  <tr><td>2e groupe</td><td>finir {A} fin{T("i")}</td></tr></table>
  <p class="txt" style="margin-top:8px">Je retrouve l’<b>infinitif</b> :<br>j’ai rempl{T("i")} {A} remplir</p>'''),
 dict(id='neg', col='orange', geom=(18, 568, 560, 350), title='À la forme négative', style='padding-top:52px', avatar=('boy', 445, 610), html=f'''
  <p class="txt" style="padding-right:110px"><b>ne… pas</b> encadre l’<b>auxiliaire</b> avoir.</p>
  <div class="exl" style="font-size:22px;line-height:1.6;margin-right:110px">Je <b>n’</b>{V("ai")} <b>pas</b> chant{T("é")}.<br>Tu <b>n’</b>{V("as")} <b>jamais</b> fin{T("i")}.<br>Ils <b>n’</b>{V("ont")} <b>plus</b> jou{T("é")}.</div>'''),
 dict(id='att', col='rouge', geom=(612, 568, 770, 350), title='Attention !', style='padding-top:52px', html=f'''
  <ul style="font-size:21px;line-height:1.5">
   <li>Le participe passé du 1er groupe finit par <b>-é</b>, pas par -er : j’ai mang{T("é")}.</li>
   <li>Pour vérifier, je remplace par <b>vendu</b> : j’ai <i>vendu</i> <span class="arrow">→</span> j’ai mangé.</li>
   <li>Avec avoir, le participe passé ne s’accorde pas avec le sujet : <i>elles ont chanté</i>.</li></ul>'''),
]
# boîte « avoir au présent » écrite à la main (tableau simple)
boxes[1]['html'] = f'''
  <div style="display:flex;gap:30px;margin-top:4px">{conj([("j’","","ai"),("tu","","as"),("il, elle","","a")],22).replace('class="t"','class="v"')}
  {conj([("nous","","avons"),("vous","","avez"),("ils, elles","","ont")],22).replace('class="t"','class="v"')}</div>
  <p class="txt" style="margin-top:12px">Le verbe avoir s’appelle ici l’<b>auxiliaire</b>.</p>'''
legend = '<span class="s">sujet</span> · <span class="v">auxiliaire</span> · <span class="t">terminaison</span>'
out, zones = build('C4', 'Le passé<br>composé', 'Conjugaison — C4 — CM1', legend, boxes, title_size=38, sub='avec avoir', legend_pos='right:18px;top:470px')

sections = [
 {'id': 'deux', 'nom': 'Un temps en deux parties', 'couleur': '#1f5fc4'},
 {'id': 'avoir', 'nom': 'avoir au présent', 'couleur': '#23845a'},
 {'id': 'pp', 'nom': 'Le participe passé', 'couleur': '#7b3fa0'},
 {'id': 'neg', 'nom': 'À la forme négative', 'couleur': '#e67e22'},
 {'id': 'att', 'nom': 'Attention !', 'couleur': '#c62828'},
]
ecrans = [
 E('deux', 'horloge', 'Une action terminée', 'girl', 'Le passé composé parle d’une action terminée.',
   ['Aujourd’hui, [je] chant§e§.',
    ('Hier, [j’](ai) chant§é§.', 'L’action est terminée : passé composé.'),
    ('[j’](ai) + chant§é§', 'Deux parties : l’auxiliaire avoir + le participe passé.')],
   Q('Hier, nous ___ un gâteau.', ['avons préparé', 'préparons', 'préparerons'], 'Hier : une action terminée.', 'Complète avec le passé composé.', fill='v'),
   [Q('Ce matin, Léa ___ son lit.', ['a rangé', 'range', 'rangera'], 'Ce matin : c’est terminé.', 'Complète avec le passé composé.', fill='v'),
    Q('Tu ___ la fenêtre.', ['as fermé', 'fermes', 'fermais'], 'Une action terminée.', 'Complète avec le passé composé.', fill='v')]),
 E('deux', 'liste', 'Quel temps ?', 'girl', 'Présent, futur, imparfait ou passé composé ?',
   [('Demain, [je] jouer§ai§.', 'futur'),
    ('Autrefois, [je] jou§ais§.', 'imparfait'),
    ('Hier, [j’](ai) jou§é§.', 'passé composé')],
   Q('Hier soir, il ___ ses devoirs.', ['a fini', 'finira', 'finit'], 'Hier soir : c’est terminé.', 'Complète avec le bon temps.', fill='v'),
   [Q('Demain, nous ___ tôt.', ['partirons', 'avons parti', 'partions'], 'Demain : le futur.', 'Complète avec le bon temps.', fill='v')]),
 E('avoir', 'tableau', 'L’auxiliaire avoir', 'boy', 'L’auxiliaire avoir se conjugue au présent.',
   ['[j’](ai) · [tu] (as) · [il] (a)',
    ('[nous] (avons) · [vous] (avez) · [ils] (ont)', 'avoir au présent : c’est l’auxiliaire.'),
    ('[Les enfants] (ont) jou§é§.', 'Les enfants = ils → ont.')],
   Q('Les oiseaux ___ chanté.', ['ont', 'a', 'avez'], 'Les oiseaux = ils.', 'Complète avec l’auxiliaire.', fill='v'),
   [Q('Vous ___ gagné !', ['avez', 'avons', 'ont'], 'Vous → avez.', 'Complète avec l’auxiliaire.', fill='v'),
    Q('Mon frère ___ fini.', ['a', 'as', 'ont'], 'Mon frère = il.', 'Complète avec l’auxiliaire.', fill='v')]),
 E('pp', 'etiquette', 'Le participe passé', 'girl', '1er groupe : -é. 2e groupe : -i.',
   [('chanter → [j’](ai) chant§é§', '1er groupe : le participe passé finit par -é.'),
    ('finir → [j’](ai) fin§i§', '2e groupe : il finit par -i.'),
    ('[Tu] (as) grand§i§ → grandir', 'Je retrouve l’infinitif.')],
   Q('Nous avons ___ nos devoirs.', ['fini', 'finé', 'finir'], 'finir : 2e groupe → -i.', 'Complète avec le participe passé.', fill='t'),
   [Q('Léa a ___ sa chambre.', ['rangé', 'rangi', 'ranger'], 'ranger : 1er groupe → -é.', 'Complète avec le participe passé.', fill='t'),
    Q('Ils ont ___ un livre.', ['choisi', 'choisé', 'choisir'], 'choisir : 2e groupe → -i.', 'Complète avec le participe passé.', fill='t'),
    Q('J’ai rempli le verre.', ['remplir', 'remplier', 'remplire'], 'rempli : 2e groupe.', 'L’infinitif de « rempli » :')]),
 E('neg', 'non', 'À la forme négative', 'boy', 'Ne… pas encadre l’auxiliaire.',
   ['[Je] (ai) chant§é§.',
    ('[Je] |n’|(ai) |pas| chant§é§.', 'ne… pas encadre l’auxiliaire, pas le participe passé.'),
    ('[Tu] |n’|(as) |jamais| fin§i§.', 'Même chose avec ne… jamais, ne… plus.')],
   Q('', ['Je n’ai pas mangé.', 'Je n’ai mangé pas.', 'Je ai pas mangé.'], 'ne… pas encadre l’auxiliaire.', 'Quelle phrase est bien écrite ?'),
   [Q('', ['Il n’a jamais menti.', 'Il n’a menti jamais.', 'Il a jamais menti.'], 'ne… jamais encadre l’auxiliaire.', 'Quelle phrase est bien écrite ?'),
    Q('', ['Nous n’avons pas fini.', 'Nous avons ne pas fini.', 'Nous n’avons fini pas.'], 'ne… pas encadre l’auxiliaire.', 'Quelle phrase est bien écrite ?')]),
 E('att', 'attention', 'é ou er ?', 'girl', 'Après l’auxiliaire avoir : -é. Je vérifie avec « vendu ».',
   [('[J’](ai) mang§é§.', 'Après avoir : participe passé en -é.'),
    ('[J’](ai) *vendu*. → [J’](ai) mang§é§.', 'Je remplace par vendu : c’est le participe passé.'),
    ('[Elles] (ont) chant§é§.', 'Avec avoir, pas d’accord avec le sujet.')],
   Q('Tu as ___ la porte.', ['fermé', 'fermer', 'fermez'], 'Tu as vendu → fermé.', 'Complète avec le bon mot.', fill='t'),
   [Q('Mes sœurs ont ___ .', ['dansé', 'dansées', 'danser'], 'Avec avoir, pas d’accord avec le sujet.', 'Complète avec le bon mot.', fill='t'),
    Q('Nous avons ___ le bus.', ['attendu', 'attendre', 'attendé'], 'Ce participe passé finit par -u, comme vendu.', 'Complète avec le bon mot.', fill='t')]),
]
save('C4', {'id': 'C4', 'f': 'C', 'ceinture': 'Verte', 'titre': 'Le passé composé avec avoir', 'sous': '1er et 2e groupes', 'lesson': True}, sections, ecrans, zones)
