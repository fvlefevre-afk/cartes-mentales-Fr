import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from mapgen import build, TL, TC, TR
from lhelp import *
from hlib import A
from clib import T, S, conj

boxes = [
 dict(id='form', col='violet', geom=TL, title='Pour parler de demain', avatar=('girl', 322, 122), html=f'''
  <p class="txt" style="padding-right:100px">Le <b>futur</b> dit ce qui <b>va se passer</b>.</p>
  <p class="txt" style="padding-right:100px">J’ajoute la <b>terminaison</b> à l’<b>infinitif</b> :</p>
  <div class="exl" style="font-size:21px;margin-top:10px">chanter + {T("ai")} {A} je chanter{T("ai")}</div>
  <p class="small" style="margin:8px 0 0">Toujours un <b>r</b> avant la terminaison : c’est la marque du futur.</p>'''),
 dict(id='term', col='bleu', geom=TC, title='Les terminaisons', html=f'''
  <div style="display:flex;gap:26px">{conj([("je","chanter","ai"),("tu","chanter","as"),("il, elle","chanter","a")],19)}
  {conj([("nous","chanter","ons"),("vous","chanter","ez"),("ils, elles","chanter","ont")],19)}</div>
  <p class="txt" style="margin-top:10px">2e groupe : je finir{T("ai")}, nous grandir{T("ons")}</p>
  <p class="small" style="margin:0">jouer {A} je jou<b>e</b>r{T("ai")} : le <b>e</b> s’écrit, même si on ne l’entend pas.</p>'''),
 dict(id='etre', col='vert', geom=TR, title='être et avoir', html=f'''
  <div style="display:flex;gap:22px">{conj([("je","ser","ai"),("tu","ser","as"),("il","ser","a"),("nous","ser","ons"),("vous","ser","ez"),("ils","ser","ont")])}
  {conj([("j’","aur","ai"),("tu","aur","as"),("il","aur","a"),("nous","aur","ons"),("vous","aur","ez"),("ils","aur","ont")])}</div>'''),
 dict(id='irr', col='orange', geom=(18, 568, 700, 350), title='Les verbes irréguliers', style='padding-top:52px', html=f'''
  <p class="txt">Le <b>radical</b> change : je l’apprends. Les terminaisons restent les mêmes.</p>
  <div style="display:flex;gap:40px;margin-top:6px">{conj([("aller","j’ir","ai"),("faire","je fer","ai"),("dire","je dir","ai"),("venir","je viendr","ai")],23)}
  {conj([("pouvoir","je pourr","ai"),("voir","je verr","ai"),("vouloir","je voudr","ai"),("prendre","je prendr","ai")],23)}</div>'''),
 dict(id='att', col='rouge', geom=(752, 568, 630, 350), title='Attention !', style='padding-top:52px', avatar=('boy', 1250, 610), html='''
  <ul style="font-size:21px;line-height:1.45;padding-right:110px">
   <li>Toujours un <b>r</b> avant la terminaison.</li>
   <li>Deux <b>r</b> : je pou<b>rr</b>ai, je ve<b>rr</b>ai.</li>
   <li>Verbes en <b>-re</b> : j’enlève le e : prendre <span class="arrow">→</span> je prendrai.</li></ul>'''),
]
legend = '<span class="s">sujet</span> · <span class="t">terminaison</span>'
out, zones = build('C2', 'Le futur<br>simple', 'Conjugaison — C2 — CM1', legend, boxes, title_size=38, legend_pos='right:18px;top:470px')

sections = [
 {'id': 'form', 'nom': 'Pour parler de demain', 'couleur': '#7b3fa0'},
 {'id': 'term', 'nom': 'Les terminaisons', 'couleur': '#1f5fc4'},
 {'id': 'etre', 'nom': 'être et avoir', 'couleur': '#23845a'},
 {'id': 'irr', 'nom': 'Les verbes irréguliers', 'couleur': '#e67e22'},
 {'id': 'att', 'nom': 'Attention !', 'couleur': '#c62828'},
]
ecrans = [
 E('form', 'horloge', 'Pour parler de demain', 'girl', 'Le futur dit ce qui va se passer.',
   ['Aujourd’hui, [je] chant§e§.',
    ('Demain, [je] chanter§ai§.', 'Le futur parle de ce qui va se passer.'),
    ('chanter + §ai§ → [je] chanter§ai§', 'J’ajoute la terminaison à l’infinitif.')],
   Q('Demain, nous ___ au parc.', ['jouerons', 'jouons', 'jouions'], 'Demain : le futur.', 'Complète avec le verbe au futur.', fill='t'),
   [Q('L’été prochain, je ___ à la mer.', ['nagerai', 'nage', 'nageais'], 'L’été prochain : le futur.', 'Complète avec le verbe au futur.', fill='t'),
    Q('Ce soir, Léa ___ un film.', ['regardera', 'regarde', 'regardait'], 'Ce soir : bientôt, au futur.', 'Complète avec le verbe au futur.', fill='t')]),
 E('form', 'liste', 'Présent ou futur ?', 'girl', 'Je regarde les mots qui disent quand.',
   [('Aujourd’hui, [Tom] mang§e§.', 'aujourd’hui : présent'),
    ('Demain, [Tom] manger§a§.', 'demain : futur')],
   Q('Demain, Léa ___ un livre.', ['lira', 'lit'], 'Demain : le futur.', 'Complète avec le bon temps.', fill='t'),
   [Q('En ce moment, il ___ .', ['dort', 'dormira'], 'En ce moment : le présent.', 'Complète avec le bon temps.', fill='t')]),
 E('term', 'tableau', 'Les terminaisons du futur', 'boy', 'Toujours un r avant la terminaison : c’est la marque du futur.',
   ['[je] chanter§ai§ · [tu] chanter§as§ · [il] chanter§a§',
    '[nous] chanter§ons§ · [vous] chanter§ez§ · [ils] chanter§ont§',
    ('-rai · -ras · -ra · -rons · -rez · -ront', 'Le r est la marque du futur.')],
   Q('Vous ___ vos devoirs.', ['finirez', 'finissez', 'finirai'], 'Vous → -ez, avec le r du futur.', 'Complète avec le verbe au futur.', fill='t'),
   [Q('Tu ___ tes amis.', ['inviteras', 'invites', 'inviterais'], 'Tu → -as, avec le r du futur.', 'Complète avec le verbe au futur.', fill='t'),
    Q('Ils ___ la porte.', ['fermeront', 'ferment', 'fermerons'], 'Ils → -ont.', 'Complète avec le verbe au futur.', fill='t')]),
 E('term', 'attention', '2e groupe et le e muet', 'boy', 'Je garde tout l’infinitif, même le e qu’on n’entend pas.',
   [('finir → [je] finir§ai§', '2e groupe : finir + ai.'),
    ('grandir → [nous] grandir§ons§', ''),
    ('jouer → [je] jouer§ai§', 'On n’entend pas le e, mais on l’écrit.')],
   Q('Les fleurs ___ au printemps.', ['fleuriront', 'fleurissent', 'fleurirons'], 'Les fleurs = elles → -ront.', 'Complète avec le verbe au futur.', fill='t'),
   [Q('Je n’___ pas ton anniversaire.', ['oublierai', 'oublirai', 'oublie'], 'oublier + ai : le e s’écrit.', 'Complète avec le verbe au futur.', fill='t'),
    Q('Nous ___ un dessin.', ['choisirons', 'choisissons', 'choisirez'], 'Nous → -rons.', 'Complète avec le verbe au futur.', fill='t')]),
 E('etre', 'tableau', 'être et avoir', 'girl', 'Le radical change, les terminaisons restent les mêmes.',
   [('[je] ser§ai§ · [tu] ser§as§ · [il] ser§a§', 'être : ser-'),
    ('[j’]aur§ai§ · [nous] aur§ons§ · [ils] aur§ont§', 'avoir : aur-')],
   Q('Demain, nous ___ en vacances.', ['serons', 'aurons', 'sommes'], 'être au futur avec nous.', 'Complète avec le verbe au futur.', fill='t'),
   [Q('Tu ___ un cadeau.', ['auras', 'seras', 'as'], 'avoir au futur avec tu.', 'Complète avec le verbe au futur.', fill='t'),
    Q('Ils ___ contents.', ['seront', 'auront', 'sont'], 'être au futur avec ils.', 'Complète avec le verbe au futur.', fill='t')]),
 E('irr', 'liste', 'Les verbes irréguliers', 'boy', 'Pour ces verbes, le radical change : je l’apprends.',
   [('aller → [j’]ir§ai§ · faire → [je] fer§ai§', ''),
    ('venir → [je] viendr§ai§ · voir → [je] verr§ai§', ''),
    ('pouvoir → [je] pourr§ai§ · vouloir → [je] voudr§ai§', 'Le radical change, les terminaisons restent les mêmes.')],
   Q('Demain, j’___ à la piscine.', ['irai', 'allerai', 'vais'], 'aller au futur : j’ir-.', 'Complète avec le verbe au futur.', fill='t'),
   [Q('Tu ___ un gâteau.', ['feras', 'faireras', 'fais'], 'faire au futur : fer-.', 'Complète avec le verbe au futur.', fill='t'),
    Q('Nous ___ la mer.', ['verrons', 'voirons', 'voyons'], 'voir au futur : verr-.', 'Complète avec le verbe au futur.', fill='t'),
    Q('Ils ___ demain.', ['viendront', 'veniront', 'viennent'], 'venir au futur : viendr-.', 'Complète avec le verbe au futur.', fill='t')]),
 E('irr', 'ciseaux', 'dire et prendre', 'boy', 'Verbes en -re : j’enlève le e de l’infinitif.',
   [('dire → [je] dir§ai§', 'dir(e) + ai'),
    ('prendre → [je] prendr§ai§', 'prendr(e) + ai')],
   Q('Vous ___ le bus.', ['prendrez', 'prenderez', 'prenez'], 'prendr(e) + ez.', 'Complète avec le verbe au futur.', fill='t'),
   [Q('Je te ___ un secret.', ['dirai', 'direrai', 'dis'], 'dir(e) + ai.', 'Complète avec le verbe au futur.', fill='t'),
    Q('Elle ___ venir.', ['pourra', 'poura', 'pouvra'], 'pouvoir : pourr-, deux r.', 'Complète avec le verbe au futur.', fill='t')]),
E('att', 'attention', 'Les radicaux qui changent', 'boy', 'Au futur, le radical qui change au présent change aussi.',
   [('lever → [je] l%è%ver§ai§', 'Le è reste au futur.'),
    ('appeler → [j’]appe%ll%er§ai§ · acheter → [j’]ach%è%ter§ai§', ''),
    ('essuyer → [j’]essu%i%er§ai§', '-yer : i au futur.')],
   Q('Demain, je t’___ .', ['appellerai', 'appelerai', 'appelrai'], 'appeler : deux l au futur.', 'Complète avec le verbe au futur.', fill='t'),
   [Q('Tu ___ la vaisselle.', ['essuieras', 'essuyeras', 'essuiras'], '-yer : i au futur.', 'Complète avec le verbe au futur.', fill='t'),
    Q('Nous ___ du pain.', ['achèterons', 'acheterons', 'achetrons'], 'acheter : è au futur.', 'Complète avec le verbe au futur.', fill='t')]),
 E('att', 'attention', 'Les pièges', 'girl', 'Un r avant la terminaison, et parfois deux !',
   [('[je] jouer§ai§ · [je] finir§ai§ · [je] fer§ai§', 'Toujours un r avant la terminaison.'),
    ('[je] pou%rr%ai · [je] ve%rr%ai', 'Deux r pour pouvoir et voir.')],
   Q('', ['Je pourrai venir.', 'Je pourai venir.', 'Je pouvrai venir.'], 'pouvoir au futur : deux r.', 'Quelle phrase est bien écrite ?'),
   [Q('', ['Nous verrons la tour.', 'Nous voirons la tour.', 'Nous verons la tour.'], 'voir au futur : verr-.', 'Quelle phrase est bien écrite ?')]),
]
save('C2', {'id': 'C2', 'f': 'C', 'ceinture': 'Jaune', 'titre': 'Le futur simple', 'sous': 'être, avoir, 1er et 2e groupes, irréguliers', 'lesson': True}, sections, ecrans, zones)
