import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from mapgen import build, TL, TC, TR
from lhelp import *
from hlib import A
from clib import T, S, conj

boxes = [
 dict(id='quand', col='bleu', geom=TL, title='Pour parler d’avant', avatar=('girl', 322, 122), html=f'''
  <p class="txt" style="padding-right:100px">L’<b>imparfait</b> parle du <b>passé</b> : ce qui durait, ce qui se répétait.</p>
  <div class="exl" style="font-size:20px;line-height:1.55;margin-top:14px">Autrefois, je jou{T("ais")} dehors.<br>Quand il pleuv{T("ait")}, je lis{T("ais")}.</div>'''),
 dict(id='term', col='violet', geom=TC, title='Les terminaisons', html=f'''
  <div style="display:flex;gap:26px">{conj([("je","chant","ais"),("tu","chant","ais"),("il, elle","chant","ait")],19)}
  {conj([("nous","chant","ions"),("vous","chant","iez"),("ils, elles","chant","aient")],19)}</div>
  <p class="txt" style="margin:10px 0 4px">2e groupe : je finiss{T("ais")}, nous finiss{T("ions")}</p>
  <p class="small" style="margin:0">La marque de l’imparfait : <b>-ai-</b> ou <b>-i-</b>.</p>'''),
 dict(id='radical', col='vert', geom=TR, title='Le radical de « nous »', html=f'''
  <p class="txt">Je prends le radical du verbe avec <b>nous</b> au présent.</p>
  <div class="exl" style="font-size:20px;line-height:1.6">nous chant<s>ons</s> {A} je chant{T("ais")}<br>nous finiss<s>ons</s> {A} je finiss{T("ais")}<br>nous fais<s>ons</s> {A} je fais{T("ais")}</div>'''),
 dict(id='etre', col='orange', geom=(18, 568, 700, 350), title='être, avoir et les irréguliers', style='padding-top:52px', html=f'''
  <div style="display:flex;gap:36px">{conj([("être","j’ét","ais"),("avoir","j’av","ais"),("aller","j’all","ais"),("faire","je fais","ais"),("dire","je dis","ais")],22)}
  {conj([("venir","je ven","ais"),("pouvoir","je pouv","ais"),("voir","je voy","ais"),("vouloir","je voul","ais"),("prendre","je pren","ais")],22)}</div>
  <p class="small" style="margin:6px 0 0"><b>être</b> est le seul qui ne suit pas la règle de « nous » : j’<b>ét</b>ais.</p>'''),
 dict(id='att', col='rouge', geom=(752, 568, 630, 350), title='Attention !', style='padding-top:52px', avatar=('boy', 1250, 610), html=f'''
  <ul style="font-size:21px;line-height:1.45;padding-right:110px">
   <li>-ger : je mang<b>e</b>{T("ais")}, mais nous mang{T("ions")}.</li>
   <li>-cer : je commen<b>ç</b>{T("ais")}, mais nous commenc{T("ions")}.</li>
   <li>Deux i : nous cri{T("ions")}, vous cri{T("iez")}.</li></ul>'''),
]
legend = '<span class="s">sujet</span> · <span class="t">terminaison</span>'
out, zones = build('C3', 'L’imparfait', 'Conjugaison — C3 — CM1', legend, boxes, title_size=38, legend_pos='right:18px;top:470px')

sections = [
 {'id': 'quand', 'nom': 'Pour parler d’avant', 'couleur': '#1f5fc4'},
 {'id': 'term', 'nom': 'Les terminaisons', 'couleur': '#7b3fa0'},
 {'id': 'radical', 'nom': 'Le radical de « nous »', 'couleur': '#23845a'},
 {'id': 'etre', 'nom': 'être, avoir, irréguliers', 'couleur': '#e67e22'},
 {'id': 'att', 'nom': 'Attention !', 'couleur': '#c62828'},
]
ecrans = [
 E('quand', 'horloge', 'Pour parler d’avant', 'girl', 'L’imparfait parle du passé : ce qui durait, ce qui se répétait.',
   ['Aujourd’hui, [je] jou§e§ dehors.',
    ('Autrefois, [je] jou§ais§ dehors.', 'Autrefois : le passé, à l’imparfait.'),
    ('Chaque été, [nous] partions à la mer.', 'Une chose qui se répétait.')],
   Q('Autrefois, mon grand-père ___ à pied.', ['marchait', 'marche', 'marchera'], 'Autrefois : l’imparfait.', 'Complète avec le verbe à l’imparfait.', fill='t'),
   [Q('Quand j’étais petit, je ___ des bonbons.', ['mangeais', 'mange', 'mangerai'], 'Quand j’étais petit : le passé.', 'Complète avec le verbe à l’imparfait.', fill='t'),
    Q('Avant, les enfants ___ à la marelle.', ['jouaient', 'jouent', 'joueront'], 'Avant : le passé.', 'Complète avec le verbe à l’imparfait.', fill='t')]),
 E('quand', 'liste', 'Présent, futur ou imparfait ?', 'girl', 'Je regarde les mots qui disent quand.',
   [('Aujourd’hui, [Léa] dans§e§.', 'aujourd’hui : présent'),
    ('Demain, [Léa] danser§a§.', 'demain : futur'),
    ('Autrefois, [Léa] dans§ait§.', 'autrefois : imparfait')],
   Q('Autrefois, il ___ souvent.', ['neigeait', 'neige', 'neigera'], 'Autrefois : l’imparfait.', 'Complète avec le bon temps.', fill='t'),
   [Q('Demain, nous ___ à vélo.', ['roulerons', 'roulions', 'roulons'], 'Demain : le futur.', 'Complète avec le bon temps.', fill='t'),
    Q('En ce moment, tu ___ .', ['chantes', 'chantais', 'chanteras'], 'En ce moment : le présent.', 'Complète avec le bon temps.', fill='t')]),
 E('term', 'tableau', 'Les terminaisons de l’imparfait', 'boy', 'Les mêmes terminaisons pour tous les verbes.',
   ['[je] chant§ais§ · [tu] chant§ais§ · [il] chant§ait§',
    '[nous] chant§ions§ · [vous] chant§iez§ · [ils] chant§aient§',
    ('-ais · -ais · -ait · -ions · -iez · -aient', 'La marque de l’imparfait : -ai- ou -i-.')],
   Q('Vous ___ beaucoup.', ['riiez', 'riez', 'riaient'], 'Vous → -iez.', 'Complète avec le verbe à l’imparfait.', fill='t'),
   [Q('Les oiseaux ___ .', ['chantaient', 'chantait', 'chantiez'], 'Ils → -aient.', 'Complète avec le verbe à l’imparfait.', fill='t'),
    Q('Tu ___ toujours en retard.', ['arrivais', 'arrivait', 'arrives'], 'Tu → -ais.', 'Complète avec le verbe à l’imparfait.', fill='t')]),
 E('radical', 'remplacer', 'Le radical de « nous »', 'girl', 'Je prends le radical du verbe avec nous au présent.',
   [('[nous] chant%ons% → [je] chant§ais§', 'chant- : le radical de nous.'),
    ('[nous] finiss%ons% → [je] finiss§ais§', '2e groupe : finiss-.'),
    ('[nous] fais%ons% → [je] fais§ais§', 'faire : fais-.')],
   Q('Autrefois, les arbres ___ vite.', ['grandissaient', 'grandaient', 'grandiront'], 'nous grandissons → grandiss-.', 'Complète avec le verbe à l’imparfait.', fill='t'),
   [Q('Je ___ toujours mes devoirs.', ['finissais', 'finais', 'finirai'], 'nous finissons → finiss-.', 'Complète avec le verbe à l’imparfait.', fill='t'),
    Q('Tu ___ des gâteaux.', ['faisais', 'fairais', 'fais'], 'nous faisons → fais-.', 'Complète avec le verbe à l’imparfait.', fill='t')]),
 E('etre', 'tableau', 'être et avoir', 'boy', 'être a un radical spécial : ét-.',
   [('[j’]ét§ais§ · [tu] ét§ais§ · [il] ét§ait§', 'être : ét-'),
    ('[j’]av§ais§ · [nous] av§ions§ · [ils] av§aient§', 'avoir : av- (nous avons)')],
   Q('Hier, nous ___ fatigués.', ['étions', 'avions', 'sommes'], 'être à l’imparfait avec nous.', 'Complète avec le verbe à l’imparfait.', fill='t'),
   [Q('Tu ___ un chat.', ['avais', 'étais', 'as'], 'avoir à l’imparfait avec tu.', 'Complète avec le verbe à l’imparfait.', fill='t'),
    Q('Ils ___ contents.', ['étaient', 'avaient', 'sont'], 'être à l’imparfait avec ils.', 'Complète avec le verbe à l’imparfait.', fill='t')]),
 E('etre', 'liste', 'Les verbes irréguliers', 'boy', 'Avec le radical de « nous », ils suivent la règle !',
   [('[nous] all%ons% → [j’]all§ais§', 'aller'),
    ('[nous] voy%ons% → [je] voy§ais§', 'voir'),
    ('[nous] pren%ons% → [je] pren§ais§', 'prendre')],
   Q('Avant, j’___ à l’école à pied.', ['allais', 'irais', 'vais'], 'nous allons → all-.', 'Complète avec le verbe à l’imparfait.', fill='t'),
   [Q('Nous ___ la mer de la fenêtre.', ['voyions', 'voirions', 'voyons'], 'nous voyons → voy- + ions.', 'Complète avec le verbe à l’imparfait.', fill='t'),
    Q('Elle ___ jouer dehors.', ['voulait', 'voudrait', 'veut'], 'nous voulons → voul-.', 'Complète avec le verbe à l’imparfait.', fill='t'),
    Q('Ils ___ souvent nous voir.', ['venaient', 'viendront', 'viennent'], 'nous venons → ven-.', 'Complète avec le verbe à l’imparfait.', fill='t')]),
E('att', 'remplacer', 'Les radicaux qui changent', 'boy', 'À l’imparfait, je prends le radical de nous : pas de è, pas de double l !',
   [('[nous] lev%ons% → [je] lev§ais§', 'Avec le radical de nous : pas de è.'),
    ('[nous] appel%ons% → [j’]appel§ais§', 'Un seul l.'),
    ('[nous] essuy%ons% → [j’]essuy§ais§', 'Le y reste.')],
   Q('Autrefois, j’___ mon chien Rex.', ['appelais', 'appellais', 'appelai'], 'nous appelons → appel-.', 'Complète avec le verbe à l’imparfait.', fill='t'),
   [Q('Tu ___ toujours la main.', ['levais', 'lèvais', 'levai'], 'nous levons → lev-.', 'Complète avec le verbe à l’imparfait.', fill='t'),
    Q('Nous ___ la vaisselle.', ['essuyions', 'essuiions', 'essuyons'], 'nous essuyons → essuy- + ions.', 'Complète avec le verbe à l’imparfait.', fill='t')]),
 E('att', 'attention', 'Les pièges', 'girl', 'Attention aux verbes en -ger, -cer, et aux deux i !',
   [('[je] mang%e%§ais§ · [nous] mang§ions§', '-ger : un e devant a.'),
    ('[je] commen%ç%§ais§ · [nous] commenc§ions§', '-cer : ç devant a.'),
    ('[nous] cri§ions§ · [vous] cri§iez§', 'Deux i : le i du radical + -ions.')],
   Q('', ['Je nageais vite.', 'Je nagais vite.'], '-ger : un e devant a.', 'Quelle phrase est bien écrite ?'),
   [Q('', ['Tu lançais le ballon.', 'Tu lancais le ballon.'], '-cer : ç devant a.', 'Quelle phrase est bien écrite ?'),
    Q('', ['Nous étudiions ensemble.', 'Nous étudions ensemble hier.'], 'Deux i à l’imparfait avec nous.', 'Quelle phrase est à l’imparfait ?')]),
]
save('C3', {'id': 'C3', 'f': 'C', 'ceinture': 'Orange', 'titre': "L'imparfait", 'sous': 'être, avoir, 1er et 2e groupes, irréguliers', 'lesson': True}, sections, ecrans, zones)
