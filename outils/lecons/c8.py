import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from mapgen import build, TL, TC, TR
from lhelp import *
from hlib import A
from clib import T, S, conj

V = lambda t: f'<span class="v">{t}</span>'
boxes = [
 dict(id='reperes', col='bleu', geom=TL, title='Quel temps ?', html='''
  <table class="tr" style="font-size:20px;margin-top:4px;width:100%"><tr><td><b>aujourd’hui</b></td><td>présent</td></tr>
  <tr><td><b>demain</b></td><td>futur</td></tr><tr><td><b>autrefois</b>, chaque jour…</td><td>imparfait</td></tr>
  <tr><td><b>hier</b>, ce matin…</td><td>passé composé</td></tr></table>
  <p class="small" style="margin:8px 0 0">Les mots qui disent <b>quand</b> m’aident à choisir le temps.</p>'''),
 dict(id='tableau', col='violet', geom=TC, title='Les terminaisons', html=f'''
  <table class="cj" style="font-size:19px"><tr><td></td><td><b>présent</b></td><td><b>futur</b></td><td><b>imparfait</b></td></tr>
  <tr><td>je</td><td>chant{T("e")}</td><td>chanter{T("ai")}</td><td>chant{T("ais")}</td></tr>
  <tr><td>nous</td><td>chant{T("ons")}</td><td>chanter{T("ons")}</td><td>chant{T("ions")}</td></tr>
  <tr><td>ils</td><td>chant{T("ent")}</td><td>chanter{T("ont")}</td><td>chant{T("aient")}</td></tr></table>
  <p class="small" style="margin:8px 0 0">Futur : un <b>r</b>. Imparfait : <b>-ai-</b> ou <b>-i-</b>.</p>'''),
 dict(id='compose', col='vert', geom=TR, title='Le passé composé', html=f'''
  <p class="txt"><b>avoir</b> ou <b>être</b> au présent + <b>participe passé</b></p>
  <div class="exl" style="font-size:20px;line-height:1.6">j’{V("ai")} chant{T("é")} · nous {V("avons")} fin{T("i")}<br>Léa {V("est")} part{T("ie")} · ils {V("sont")} venu{T("s")}</div>
  <p class="small" style="margin:8px 0 0">Avec être, j’accorde avec le sujet.</p>'''),
 dict(id='transpo', col='orange', geom=(18, 568, 700, 350), title='Je transpose', style='padding-top:52px', avatar=('boy', 585, 610), html=f'''
  <p class="txt" style="padding-right:120px">Je change le temps : le <b>sujet</b> et le <b>sens</b> restent les mêmes.</p>
  <table class="tr" style="font-size:20px;width:auto"><tr><td>Aujourd’hui,</td><td>Tom jou{T("e")} dehors.</td></tr>
  <tr><td>Demain,</td><td>Tom jouer{T("a")} dehors.</td></tr><tr><td>Autrefois,</td><td>Tom jou{T("ait")} dehors.</td></tr>
  <tr><td>Hier,</td><td>Tom {V("a")} jou{T("é")} dehors.</td></tr></table>'''),
 dict(id='att', col='rouge', geom=(752, 568, 630, 350), title='Je vérifie', style='padding-top:52px', html='''
  <ol style="margin:0;padding-left:26px;font-size:21px;line-height:1.5">
   <li>Je trouve le <span class="s">sujet</span> : il donne la terminaison.</li>
   <li>Je cherche la <b>marque du temps</b> : r, ai, i…</li>
   <li>Au passé composé : le bon <b>auxiliaire</b>, et l’accord avec être.</li></ol>'''),
]
legend = '<span class="s">sujet</span> · <span class="v">auxiliaire</span> · <span class="t">terminaison</span>'
out, zones = build('C8', 'Mobilisation', 'Conjugaison — C8 — CM1', legend, boxes, title_size=34, sub='tous les temps', legend_pos='right:18px;top:470px')

sections = [
 {'id': 'reperes', 'nom': 'Quel temps ?', 'couleur': '#1f5fc4'},
 {'id': 'tableau', 'nom': 'Les terminaisons', 'couleur': '#7b3fa0'},
 {'id': 'compose', 'nom': 'Le passé composé', 'couleur': '#23845a'},
 {'id': 'transpo', 'nom': 'Je transpose', 'couleur': '#e67e22'},
 {'id': 'att', 'nom': 'Je vérifie', 'couleur': '#c62828'},
]
ecrans = [
 E('reperes', 'horloge', 'Quel temps ?', 'girl', 'Les mots qui disent quand m’aident à choisir le temps.',
   [('Aujourd’hui, [Léa] lit.', 'aujourd’hui : présent'),
    ('Demain, [Léa] lir§a§.', 'demain : futur'),
    ('Autrefois, [Léa] lis§ait§.', 'autrefois : imparfait'),
    ('Hier, [Léa] (a) lu.', 'hier : passé composé')],
   Q('Hier, nous ___ un château.', ['avons visité', 'visiterons', 'visitons'], 'Hier : une action terminée.', 'Complète avec le bon temps.', fill='v'),
   [Q('Autrefois, les enfants ___ à pied.', ['allaient', 'iront', 'vont'], 'Autrefois : l’imparfait.', 'Complète avec le bon temps.', fill='t'),
    Q('Demain, tu ___ ton cartable.', ['prendras', 'prenais', 'as pris'], 'Demain : le futur.', 'Complète avec le bon temps.', fill='t'),
    Q('Aujourd’hui, vous ___ en classe.', ['êtes', 'serez', 'étiez'], 'Aujourd’hui : le présent.', 'Complète avec le bon temps.', fill='t')]),
 E('tableau', 'tableau', 'Les terminaisons', 'boy', 'Je reconnais le temps grâce à la marque du temps.',
   [('[je] chant§e§ · [je] chanter§ai§ · [je] chant§ais§', 'présent · futur (r) · imparfait (ai)'),
    ('[nous] chant§ons§ · [nous] chanter§ons§ · [nous] chant§ions§', 'présent · futur (r) · imparfait (i)')],
   Q('nous finirons', ['futur', 'imparfait', 'présent'], 'J’entends le r du futur.', 'À quel temps est ce verbe ?'),
   [Q('ils jouaient', ['imparfait', 'futur', 'présent'], 'La marque -ai- de l’imparfait.', 'À quel temps est ce verbe ?'),
    Q('tu as rangé', ['passé composé', 'imparfait', 'futur'], 'avoir + participe passé.', 'À quel temps est ce verbe ?'),
    Q('vous dites', ['présent', 'futur', 'imparfait'], 'Ni r du futur, ni -i- de l’imparfait.', 'À quel temps est ce verbe ?')]),
 E('compose', 'wagon', 'Le passé composé', 'girl', 'avoir ou être au présent + participe passé.',
   [('[j’](ai) chant§é§ · [nous] (avons) fin§i§', 'avec avoir'),
    ('[Léa] (est) part§i§*e* · [ils] (sont) ven§us§', 'avec être : j’accorde avec le sujet')],
   Q('Mes cousines sont ___ hier.', ['arrivées', 'arrivé', 'arrivés'], 'Avec être : féminin pluriel.', 'Complète avec le participe passé.', fill='t'),
   [Q('Nous ___ nos devoirs.', ['avons fini', 'sommes finis', 'avons finis'], 'finir se conjugue avec avoir.', 'Complète avec le passé composé.', fill='v')]),
 E('transpo', 'remplacer', 'Je transpose', 'boy', 'Je change le temps : le sujet et le sens restent les mêmes.',
   ['Aujourd’hui, [Tom] jou§e§ dehors.',
    ('Demain, [Tom] jouer§a§ dehors.', 'futur'),
    ('Autrefois, [Tom] jou§ait§ dehors.', 'imparfait'),
    ('Hier, [Tom] (a) jou§é§ dehors.', 'passé composé')],
   Q('Aujourd’hui, je vais à l’école. Demain, j’___ à l’école.', ['irai', 'allais', 'suis allé'], 'Demain : le futur d’aller.', 'Complète avec le verbe transposé.', fill='t'),
   [Q('Aujourd’hui, nous faisons un gâteau. Autrefois, nous ___ un gâteau.', ['faisions', 'ferons', 'avons fait'], 'Autrefois : l’imparfait.', 'Complète avec le verbe transposé.', fill='t'),
    Q('Aujourd’hui, elle part. Hier, elle ___ .', ['est partie', 'a parti', 'partira'], 'partir : avec être, et j’accorde.', 'Complète avec le verbe transposé.', fill='v')]),
 E('att', 'coche', 'Je vérifie', 'girl', 'Sujet, marque du temps, auxiliaire : je vérifie tout.',
   [('Demain, [les enfants] jouer§ont§.', '1. Le sujet : ils → -ont.'),
    ('jouer§ont§ → le r du futur', '2. La marque du temps.'),
    ('Hier, [les filles] (sont) sort§ies§.', '3. L’auxiliaire, et l’accord avec être.')],
   Q('', ['Demain, nous partirons tôt.', 'Demain, nous partions tôt.', 'Demain, nous partirent tôt.'], 'Demain : le futur, avec le r.', 'Quelle phrase est bien écrite ?'),
   [Q('', ['Hier, Léa est tombée.', 'Hier, Léa a tombée.', 'Hier, Léa est tombé.'], 'tomber : avec être, et j’accorde.', 'Quelle phrase est bien écrite ?'),
    Q('', ['Autrefois, ils jouaient aux billes.', 'Autrefois, ils jouait aux billes.', 'Autrefois, ils joueront aux billes.'], 'Autrefois : l’imparfait, ils → -aient.', 'Quelle phrase est bien écrite ?')]),
]
save('C8', {'id': 'C8', 'f': 'C', 'ceinture': 'Marron', 'titre': 'Mobilisation', 'sous': 'tous les temps de C1 à C5', 'lesson': True}, sections, ecrans, zones)
