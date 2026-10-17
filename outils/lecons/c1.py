import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from mapgen import build, TL, TC, TR
from lhelp import *
from hlib import A
from clib import T, S, conj

boxes = [
 dict(id='rad', col='bleu', geom=TL, title='Un verbe conjugué', avatar=('girl', 322, 122), html=f'''
  <p class="txt" style="padding-right:100px">Un verbe conjugué = <b>radical</b> + <span class="t">terminaison</span>.</p>
  <div class="exl" style="font-size:22px;text-align:center;margin-top:34px">chant{T("ons")} · fin{T("issez")}</div>
  <p class="txt" style="margin-top:8px">La terminaison change avec le <span class="s">sujet</span>.</p>
  <p class="small" style="margin:0">L’<b>infinitif</b> est le nom du verbe : chanter, finir, prendre.</p>'''),
 dict(id='g1', col='violet', geom=TC, title='1er groupe : -er', html=f'''
  <div style="display:flex;gap:26px">{conj([("je","chant","e"),("tu","chant","es"),("il, elle","chant","e")],20)}
  {conj([("nous","chant","ons"),("vous","chant","ez"),("ils, elles","chant","ent")],20)}</div>
  <p class="small" style="margin:10px 0 4px">Infinitif en <b>-er</b> (sauf aller).</p>
  <p class="small" style="margin:0">Le radical peut changer : je l<b>è</b>ve, j’appe<b>ll</b>e, j’essu<b>i</b>e, nous commen<b>ç</b>ons, nous mang<b>e</b>ons.</p>'''),
 dict(id='g2', col='vert', geom=TR, title='2e groupe : -ir', html=f'''
  <div style="display:flex;gap:26px">{conj([("je","fin","is"),("tu","fin","is"),("il, elle","fin","it")],20)}
  {conj([("nous","fin","issons"),("vous","fin","issez"),("ils, elles","fin","issent")],20)}</div>
  <p class="small" style="margin:10px 0 0">Infinitif en <b>-ir</b>, avec <b>-iss-</b> à nous, vous, ils.</p>'''),
 dict(id='verbes', col='orange', geom=(18, 568, 700, 350), title='être, avoir et les verbes à connaître', hstyle='font-size:26px', style='padding-top:52px', html=f'''
  <div style="display:flex;gap:30px">{conj([("je","","suis"),("tu","","es"),("il","","est"),("nous","","sommes"),("vous","","êtes"),("ils","","sont")],20).replace('class="t"','style="font-weight:700"')}
  {conj([("j’","","ai"),("tu","","as"),("il","","a"),("nous","","avons"),("vous","","avez"),("ils","","ont")],20).replace('class="t"','style="font-weight:700"')}
  {conj([("aller","je ","vais"),("faire","je ","fais"),("dire","vous ","dites"),("venir","ils ","viennent"),("prendre","ils ","prennent"),("vouloir","je ","veux")],20).replace('class="t"','style="font-weight:700"')}</div>
  <p class="small" style="margin:4px 0 0">Le tableau complet des verbes à connaître est sous la carte.</p>'''),
 dict(id='att', col='rouge', geom=(752, 568, 630, 350), title='Attention !', style='padding-top:52px', avatar=('boy', 1250, 610), html=f'''
  <ul style="font-size:19px;line-height:1.4;padding-right:108px">
   <li>tu <b>-s</b> ou <b>-x</b> : tu veu{T("x")}, tu peu{T("x")}.</li>
   <li>vous <b>-ez</b>, sauf : vous <b>êtes</b>, <b>faites</b>, <b>dites</b>.</li>
   <li>ils <b>-ent</b>, sauf : ils <b>sont</b>, <b>ont</b>, <b>vont</b>, <b>font</b>.</li>
   <li>Un sujet composé = <b>nous</b> ou <b>ils</b> : <i>Léa et moi chantons.</i></li></ul>'''),
]
legend = '<span class="s">sujet</span> · <span class="t">terminaison</span>'
out, zones = build('C1', 'Le présent', 'Conjugaison — C1 — CM1', legend, boxes, title_size=40, legend_pos='right:18px;top:470px')

sections = [
 {'id': 'rad', 'nom': 'Un verbe conjugué', 'couleur': '#1f5fc4'},
 {'id': 'g1', 'nom': '1er groupe', 'couleur': '#7b3fa0'},
 {'id': 'g2', 'nom': '2e groupe', 'couleur': '#23845a'},
 {'id': 'verbes', 'nom': 'être, avoir, verbes à connaître', 'couleur': '#e67e22'},
 {'id': 'att', 'nom': 'Attention !', 'couleur': '#c62828'},
]
ecrans = [
 E('rad', 'ciseaux', 'Radical + terminaison', 'girl', 'Un verbe conjugué = radical + terminaison.',
   ['[nous] chant§ons§',
    ('chant + §ons§', 'Le radical, puis la terminaison.'),
    ('chanter · finir · prendre', 'L’infinitif est le nom du verbe.')],
   Q('vous jouez', ['-ez', 'jou-', 'vous'], 'La terminaison est à la fin du verbe.', 'Quelle est la terminaison ?'),
   [Q('ils finissent', ['-issent', 'fin-', 'ils'], 'La terminaison est à la fin du verbe.', 'Quelle est la terminaison ?'),
    Q('nous dansons', ['danser', 'dansons', 'danse'], 'L’infinitif est le nom du verbe.', 'Quel est l’infinitif ?')]),
 E('rad', 'sv', 'La terminaison change avec le sujet', 'girl', 'Le radical reste, la terminaison change avec le sujet.',
   ['[je] chant§e§ · [tu] chant§es§',
    ('[nous] chant§ons§ · [ils] chant§ent§', 'Le radical reste : chant-. La terminaison change.')],
   Q('Ils ___ fort.', ['crient', 'crie', 'cries'], 'Ils → -ent.', 'Complète avec le verbe au présent.', fill='t'),
   [Q('Tu ___ une chanson.', ['chantes', 'chante', 'chantez'], 'Tu → -es.', 'Complète avec le verbe au présent.', fill='t'),
    Q('Nous ___ dehors.', ['jouons', 'jouez', 'jouent'], 'Nous → -ons.', 'Complète avec le verbe au présent.', fill='t')]),
 E('g1', 'tableau', 'Le 1er groupe : -er', 'boy', 'Infinitif en -er : je chante, nous chantons.',
   ['[je] chant§e§ · [tu] chant§es§ · [il] chant§e§',
    ('[nous] chant§ons§ · [vous] chant§ez§ · [ils] chant§ent§', '-e, -es, -e, -ons, -ez, -ent')],
   Q('Vous ___ vos mains.', ['lavez', 'lavons', 'lavent'], 'Vous → -ez.', 'Complète avec le verbe au présent.', fill='t'),
   [Q('Le chat ___ .', ['saute', 'sautes', 'sautent'], 'Le chat = il → -e.', 'Complète avec le verbe au présent.', fill='t'),
    Q('Mes parents ___ un film.', ['regardent', 'regarde', 'regardez'], 'Mes parents = ils → -ent.', 'Complète avec le verbe au présent.', fill='t')]),
E('g1', 'attention', 'Des radicaux qui changent (1)', 'boy', 'Pour certains verbes en -er, le radical change un peu.',
   [('lever → [je] l%è%v§e§ · [nous] lev§ons§', 'Devant une terminaison muette, e devient è.'),
    ('répéter → [je] rép%è%t§e§ · [nous] répét§ons§', 'é devient è.'),
    ('acheter → [j’]ach%è%t§e§ · appeler → [j’]appe%ll%§e§', '-eter, -eler : un è, ou deux consonnes.')],
   Q('Je ___ la main.', ['lève', 'leve', 'lèves'], 'Devant -e muet : è.', 'Complète avec le verbe au présent.', fill='t'),
   [Q('Tu ___ ton frère.', ['appelles', 'appeles', 'appelle'], '-eler : deux l devant -es.', 'Complète avec le verbe au présent.', fill='t'),
    Q('Ils ___ la leçon.', ['répètent', 'répétent', 'répètes'], 'é devient è devant -ent.', 'Complète avec le verbe au présent.', fill='t'),
    Q('Nous ___ du pain.', ['achetons', 'achètons', 'achettons'], 'Avec nous, pas de è.', 'Complète avec le verbe au présent.', fill='t')]),
 E('g1', 'attention', 'Des radicaux qui changent (2)', 'boy', '-yer, -cer, -ger : attention au radical !',
   [('essuyer → [j’]essu%i%§e§ · [nous] essuy§ons§', '-yer : y devient i devant un e muet.'),
    ('commencer → [nous] commen%ç%§ons§', '-cer : ç devant o.'),
    ('manger → [nous] mang%e%§ons§', '-ger : un e devant o.')],
   Q('Nous ___ des légumes.', ['mangeons', 'mangons', 'mangeont'], '-ger : un e devant -ons.', 'Complète avec le verbe au présent.', fill='t'),
   [Q('J’___ la table.', ['essuie', 'essuye', 'essuies'], '-yer : i devant le e muet.', 'Complète avec le verbe au présent.', fill='t'),
    Q('Nous ___ à lire.', ['commençons', 'commencons', 'commenceons'], '-cer : ç devant -ons.', 'Complète avec le verbe au présent.', fill='t'),
    Q('Ils ___ le sol.', ['nettoient', 'nettoyent', 'nettoies'], '-yer : i devant -ent.', 'Complète avec le verbe au présent.', fill='t')]),
 E('g2', 'tableau', 'Le 2e groupe : -ir avec -iss-', 'boy', 'Infinitif en -ir, avec -iss- à nous, vous, ils.',
   ['[je] fin§is§ · [tu] fin§is§ · [il] fin§it§',
    ('[nous] fin§issons§ · [vous] fin§issez§ · [ils] fin§issent§', 'J’entends -iss- : c’est le 2e groupe.')],
   Q('Nous ___ nos devoirs.', ['finissons', 'finons', 'finirons'], 'Nous → -issons.', 'Complète avec le verbe au présent.', fill='t'),
   [Q('Tu ___ vite.', ['grandis', 'grandit', 'grandissez'], 'Tu → -is.', 'Complète avec le verbe au présent.', fill='t'),
    Q('Les élèves ___ un livre.', ['choisissent', 'choisent', 'choisit'], 'Ils → -issent.', 'Complète avec le verbe au présent.', fill='t')]),
 E('verbes', 'tableau', 'être et avoir', 'girl', 'Deux verbes très utiles, à connaître par cœur.',
   ['[je] suis · [tu] es · [il] est · [nous] sommes · [vous] êtes · [ils] sont',
    ('[j’]ai · [tu] as · [il] a · [nous] avons · [vous] avez · [ils] ont', 'être et avoir au présent.')],
   Q('Vous ___ en retard.', ['êtes', 'avez', 'sont'], 'être avec vous : êtes.', 'Complète avec le verbe au présent.', fill='t'),
   [Q('Nous ___ un chien.', ['avons', 'sommes', 'ont'], 'avoir avec nous : avons.', 'Complète avec le verbe au présent.', fill='t'),
    Q('Je ___ content.', ['suis', 'es', 'est'], 'être avec je : suis.', 'Complète avec le verbe au présent.', fill='t')]),
 E('verbes', 'liste', 'Les verbes à connaître', 'girl', 'Leur radical change : je les apprends dans le tableau.',
   [('aller → [je] vais · [nous] allons · [ils] vont', ''),
    ('faire → [je] fais · [vous] faites · [ils] font', ''),
    ('venir → [ils] viennent · prendre → [ils] prennent', 'Le tableau complet est sous la carte.')],
   Q('Vous ___ la vérité.', ['dites', 'disez', 'dittes'], 'dire avec vous : dites.', 'Complète avec le verbe au présent.', fill='t'),
   [Q('Ils ___ à la piscine.', ['vont', 'allent', 'vas'], 'aller avec ils : vont.', 'Complète avec le verbe au présent.', fill='t'),
    Q('Elles ___ le bus.', ['prennent', 'prendent', 'prenent'], 'prendre avec elles : prennent.', 'Complète avec le verbe au présent.', fill='t'),
    Q('Nous ___ la mer.', ['voyons', 'voions', 'voyez'], 'voir avec nous : voyons.', 'Complète avec le verbe au présent.', fill='t')]),
 E('att', 'attention', 'tu : -s ou -x', 'boy', 'Avec tu, le verbe finit par -s… ou par -x.',
   ['[tu] chant§es§ · [tu] fin§is§',
    ('[tu] veu§x§ · [tu] peu§x§', 'Avec tu : -s, ou -x pour vouloir et pouvoir.')],
   Q('Tu ___ un gâteau ?', ['veux', 'veut', 'veus'], 'vouloir avec tu : -x.', 'Complète avec le verbe au présent.', fill='t'),
   [Q('Tu ___ venir.', ['peux', 'peut', 'peus'], 'pouvoir avec tu : -x.', 'Complète avec le verbe au présent.', fill='t')]),
 E('att', 'attention', 'Les exceptions', 'boy', 'vous -ez et ils -ent… sauf quelques verbes !',
   [('[vous] êtes · [vous] faites · [vous] dites', 'Pas de -ez pour ces trois verbes.'),
    ('[ils] sont · [ils] ont · [ils] vont · [ils] font', 'Pas de -ent pour ces quatre verbes.')],
   Q('Ils ___ du vélo.', ['font', 'faisent', 'fait'], 'faire avec ils : font.', 'Complète avec le verbe au présent.', fill='t'),
   [Q('Vous ___ un dessin.', ['faites', 'faisez', 'faitez'], 'faire avec vous : faites.', 'Complète avec le verbe au présent.', fill='t')]),
 E('att', 'wagon', 'Le sujet composé', 'girl', 'Plusieurs noms reliés : un seul sujet, comme nous ou ils.',
   [('[#Léa et moi] chant§ons§.', 'Léa et moi = nous'),
    ('[#Léa et Tom] chant§ent§.', 'Léa et Tom = ils')],
   Q('Mon frère et moi ___ au foot.', ['jouons', 'jouent', 'joue'], 'Mon frère et moi = nous.', 'Complète avec le verbe au présent.', fill='t'),
   [Q('Le chat et le chien ___ .', ['dorment', 'dort', 'dormons'], 'Le chat et le chien = ils.', 'Complète avec le verbe au présent.', fill='t')]),
]
save('C1', {'id': 'C1', 'f': 'C', 'ceinture': 'Blanche', 'titre': 'Le présent', 'sous': 'être, avoir, 1er et 2e groupes, verbes à connaître', 'lesson': True}, sections, ecrans, zones)
