import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from mapgen import build, TL, TC, TR
from lhelp import *
from hlib import A
from clib import T, S, conj

V = lambda t: f'<span class="v">{t}</span>'
E_ = lambda t: f'<span class="e">{t}</span>'
boxes = [
 dict(id='deux', col='bleu', geom=TL, title='être + participe passé', avatar=('girl', 322, 122), html=f'''
  <p class="txt" style="padding-right:100px">Certains verbes font leur passé composé avec l’auxiliaire <b>être</b>.</p>
  <div class="exl" style="font-size:22px;text-align:center;margin-top:14px">Hier, je {V("suis")} part{T("i")}.<br>Tom {V("est")} arriv{T("é")}.</div>'''),
 dict(id='verbes', col='vert', geom=TC, title='Les verbes avec être', html='''
  <p class="txt">Surtout des verbes de <b>mouvement</b> :</p>
  <div class="exl" style="font-size:20px;line-height:1.55">aller · venir · partir · arriver<br>entrer · sortir · monter · descendre<br>tomber · rester · naître</div>'''),
 dict(id='accord', col='violet', geom=TR, title='J’accorde avec le sujet', avatar=('boy', 1250, 122), html=f'''
  <p class="txt" style="padding-right:110px">Avec être, le participe passé s’accorde avec le <span class="s">sujet</span>.</p>
  <div class="exl" style="font-size:20px;line-height:1.55">{S("Tom")} est parti.<br>{S("Léa")} est parti{E_("e")}.<br>{S("Ils")} sont parti{E_("s")}.<br>{S("Elles")} sont parti{E_("es")}.</div>'''),
 dict(id='etre', col='orange', geom=(18, 568, 560, 350), title='être au présent', style='padding-top:52px', html=f'''
  <div style="display:flex;gap:36px">{conj([("je","","suis"),("tu","","es"),("il, elle","","est")],23).replace('class="t"','class="v"')}
  {conj([("nous","","sommes"),("vous","","êtes"),("ils, elles","","sont")],23).replace('class="t"','class="v"')}</div>
  <p class="txt" style="margin-top:12px">Le verbe être est ici l’<b>auxiliaire</b>.</p>'''),
 dict(id='att', col='rouge', geom=(612, 568, 770, 350), title='Attention !', style='padding-top:52px', html='''
  <ul style="font-size:21px;line-height:1.5">
   <li>Avec <b>être</b> : j’accorde. Avec <b>avoir</b> : je n’accorde pas avec le sujet.<br><i>Elle est tombée. · Elle a joué.</i></li>
   <li>Les verbes avec <b>se</b> se conjuguent aussi avec être : <i>il s’est levé, elle s’est levée</i>.</li></ul>'''),
]
legend = '<span class="s">sujet</span> · <span class="v">auxiliaire</span> · <span class="t">terminaison</span>'
out, zones = build('C5', 'Le passé<br>composé', 'Conjugaison — C5 — CM1', legend, boxes, title_size=38, sub='avec être', legend_pos='right:18px;top:470px')

sections = [
 {'id': 'deux', 'nom': 'être + participe passé', 'couleur': '#1f5fc4'},
 {'id': 'verbes', 'nom': 'Les verbes avec être', 'couleur': '#23845a'},
 {'id': 'accord', 'nom': 'J’accorde avec le sujet', 'couleur': '#7b3fa0'},
 {'id': 'etre', 'nom': 'être au présent', 'couleur': '#e67e22'},
 {'id': 'att', 'nom': 'Attention !', 'couleur': '#c62828'},
]
ecrans = [
 E('deux', 'horloge', 'être + participe passé', 'girl', 'Certains verbes font leur passé composé avec être.',
   ['Aujourd’hui, [je] par§s§.',
    ('Hier, [je] (suis) part§i§.', 'L’auxiliaire est être.'),
    ('[Tom] (est) arriv§é§.', 'être au présent + participe passé.')],
   Q('Hier, nous ___ au cinéma.', ['sommes allés', 'avons allé', 'allons'], 'aller se conjugue avec être.', 'Complète avec le passé composé.', fill='v'),
   [Q('Ce matin, Tom ___ en retard.', ['est arrivé', 'a arrivé', 'arrive'], 'arriver se conjugue avec être.', 'Complète avec le passé composé.', fill='v'),
    Q('Le chat ___ de l’arbre.', ['est tombé', 'a tombé', 'tombe'], 'tomber se conjugue avec être.', 'Complète avec le passé composé.', fill='v')]),
 E('verbes', 'deplacer', 'Les verbes avec être', 'boy', 'Surtout des verbes de mouvement.',
   [('aller · venir · partir · arriver', 'Des verbes de mouvement.'),
    ('entrer · sortir · monter · descendre', ''),
    ('tomber · rester · naître', 'Ils se conjuguent avec être.')],
   Q('', ['venir', 'manger', 'chanter'], 'Un verbe de mouvement.', 'Lequel se conjugue avec être ?'),
   [Q('', ['sortir', 'finir', 'jouer'], 'Un verbe de mouvement.', 'Lequel se conjugue avec être ?'),
    Q('Nous ___ à la maison.', ['sommes restés', 'avons resté', 'restons'], 'rester se conjugue avec être.', 'Complète avec le passé composé.', fill='v')]),
 E('accord', 'wagon', 'J’accorde avec le sujet', 'girl', 'Avec être, le participe passé s’accorde avec le sujet.',
   ['[Tom] (est) part§i§.',
    ('[Léa] (est) part§i§*e*.', 'Léa : féminin → e.'),
    ('[Ils] (sont) part§i§*s*.', 'Pluriel → s.'),
    ('[Elles] (sont) part§i§*es*.', 'Féminin pluriel → es.')],
   Q('Ma sœur est ___.', ['tombée', 'tombé', 'tombés'], 'Ma sœur : féminin singulier.', 'Complète avec le participe passé.', fill='t'),
   [Q('Mes amis sont ___.', ['venus', 'venu', 'venues'], 'Mes amis : masculin pluriel.', 'Complète avec le participe passé.', fill='t'),
    Q('Les filles sont ___ au parc.', ['allées', 'allé', 'allés'], 'Les filles : féminin pluriel.', 'Complète avec le participe passé.', fill='t'),
    Q('Mon père est ___ tard.', ['rentré', 'rentrée', 'rentrés'], 'Mon père : masculin singulier.', 'Complète avec le participe passé.', fill='t')]),
 E('etre', 'tableau', 'L’auxiliaire être', 'boy', 'L’auxiliaire être se conjugue au présent.',
   ['[je] (suis) · [tu] (es) · [il] (est)',
    ('[nous] (sommes) · [vous] (êtes) · [ils] (sont)', 'être au présent : c’est l’auxiliaire.'),
    ('[Les enfants] (sont) sort§is§.', 'Les enfants = ils → sont.')],
   Q('Vous ___ arrivés à l’heure.', ['êtes', 'sommes', 'sont'], 'Vous → êtes.', 'Complète avec l’auxiliaire.', fill='v'),
   [Q('Les oiseaux ___ partis.', ['sont', 'est', 'êtes'], 'Les oiseaux = ils.', 'Complète avec l’auxiliaire.', fill='v'),
    Q('Je ___ monté au grenier.', ['suis', 'es', 'est'], 'Je → suis.', 'Complète avec l’auxiliaire.', fill='v')]),
 E('att', 'attention', 'être ou avoir ?', 'girl', 'Avec être, j’accorde. Avec avoir, je n’accorde pas avec le sujet.',
   [('[Elle] (est) tomb§é§*e*.', 'avec être : j’accorde.'),
    ('[Elle] (a) jou§é§.', 'avec avoir : pas d’accord avec le sujet.'),
    ('[Il] s’(est) lev§é§ · [Elle] s’(est) lev§é§*e*', 'Les verbes avec se : avec être aussi.')],
   Q('Mes sœurs ont ___ une glace.', ['mangé', 'mangées', 'mangés'], 'Avec avoir, pas d’accord avec le sujet.', 'Complète avec le participe passé.', fill='t'),
   [Q('Mes sœurs sont ___.', ['sorties', 'sorti', 'sortis'], 'Avec être : féminin pluriel.', 'Complète avec le participe passé.', fill='t'),
    Q('Léa s’est ___ tôt.', ['réveillée', 'réveillé', 'réveiller'], 'Avec se, être : j’accorde avec Léa.', 'Complète avec le participe passé.', fill='t')]),
]
save('C5', {'id': 'C5', 'f': 'C', 'ceinture': 'Bleue', 'titre': 'Le passé composé avec être', 'sous': 'le participe passé et son accord', 'lesson': True}, sections, ecrans, zones)
