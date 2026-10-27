"""Ceintures CM2 seulement : C8 (plus-que-parfait) et C9 (passé simple : 2e groupe et verbes irréguliers).
Identifiants sur le site : C8-CM2 et C9-CM2 (code affiché : C8, C9). Anciens codes C6 et C7 jusqu'au 27/10/2026."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from mapgen import build, TL, TC, TR
from lhelp import *
from clib import T, S, conj

V = lambda t: f'<span class="v">{t}</span>'
E_ = lambda t: f'<span class="e">{t}</span>'
BL = (18, 568, 560, 350)
BR = (612, 568, 770, 350)
legend = '<span class="s">sujet</span> · <span class="v">auxiliaire</span> · <span class="t">terminaison</span>'
SEC = lambda *l: [{'id': i, 'nom': n, 'couleur': c} for (i, n), c in zip(l, ['#1f5fc4', '#23845a', '#7b3fa0', '#e67e22', '#c62828'])]

# ================================================================ C8
boxes = [
 dict(id='quand', col='bleu', geom=TL, title='Encore avant', avatar=('girl', 322, 122), html=f'''
  <p class="txt" style="padding-right:100px">Le plus-que-parfait dit ce qui s’est passé <b>avant</b> une autre action passée.</p>
  <div class="exl" style="font-size:20px;line-height:1.5;margin-top:10px">Quand je suis arrivé,<br>le film {V("avait")} commenc{T("é")}.</div>'''),
 dict(id='forme', col='vert', geom=TC, title='Deux parties', html=f'''
  <p class="txt">Auxiliaire <b>à l’imparfait</b> + participe passé.</p>
  <div class="exl" style="font-size:21px;line-height:1.55">j’{V("avais")} mang{T("é")}<br>nous {V("étions")} part{T("is")}</div>'''),
 dict(id='avoir', col='violet', geom=TR, title='avoir à l’imparfait', html=f'''
  <div style="display:flex;gap:28px;margin-top:6px">{conj([("j’","","avais"),("tu","","avais"),("il, elle","","avait")],22).replace('class="t"','class="v"')}
  {conj([("nous","","avions"),("vous","","aviez"),("ils, elles","","avaient")],22).replace('class="t"','class="v"')}</div>'''),
 dict(id='etre', col='orange', geom=BL, title='Avec être, j’accorde', style='padding-top:52px', avatar=('boy', 445, 610), html=f'''
  <p class="txt" style="padding-right:110px">Avec <b>être</b>, le participe passé s’accorde avec le <span class="s">sujet</span>.</p>
  <div class="exl" style="font-size:21px;line-height:1.55;margin-right:110px">{S("Léa")} {V("était")} parti{E_("e")}.<br>{S("Ils")} {V("étaient")} parti{E_("s")}.</div>'''),
 dict(id='att', col='rouge', geom=BR, title='Attention !', style='padding-top:52px', html=f'''
  <ul style="font-size:21px;line-height:1.5">
   <li>Passé composé : auxiliaire au <b>présent</b> → j’{V("ai")} mangé.<br>Plus-que-parfait : à l’<b>imparfait</b> → j’{V("avais")} mangé.</li>
   <li>Négation : ne… pas encadre l’auxiliaire → je <b>n’</b>{V("avais")} <b>pas</b> mangé.</li></ul>'''),
]
out, zones = build('C8-CM2', 'Le plus-que-<br>parfait', 'Conjugaison — C8 — CM2', legend, boxes, title_size=36, legend_pos='right:18px;top:470px')
sections = SEC(('quand', 'Encore avant'), ('forme', 'Deux parties'), ('avoir', 'avoir à l’imparfait'), ('etre', 'Avec être, j’accorde'), ('att', 'Attention !'))
ecrans = [
 E('quand', 'horloge', 'Encore avant', 'girl', 'Le plus-que-parfait dit ce qui s’est passé avant une autre action passée.',
   ['Quand je suis arrivé, le film avait commencé.',
    ('Quand je suis arrivé, le film |avait commencé|.', 'D’abord le film a commencé, puis je suis arrivé.'),
    ('Il |avait plu| : la route était mouillée.', 'La pluie est venue avant.')],
   Q('Il avait neigé toute la nuit : le jardin était blanc.', ['Il a neigé.', 'Le jardin était blanc.'], 'Le plus-que-parfait dit ce qui s’est passé avant.', 'Qu’est-ce qui s’est passé en premier ?'),
   [Q('Quand nous sommes arrivés, le train était parti.', ['Le train est parti.', 'Nous sommes arrivés.'], 'Le plus-que-parfait dit ce qui s’est passé avant.', 'Qu’est-ce qui s’est passé en premier ?'),
    Q('Il avait faim car il n’avait rien mangé.', ['Il n’a rien mangé.', 'Il avait faim.'], 'Le plus-que-parfait dit ce qui s’est passé avant.', 'Qu’est-ce qui s’est passé en premier ?')]),
 E('forme', 'wagon', 'Deux parties', 'boy', 'Auxiliaire à l’imparfait + participe passé.',
   [('[j’] (avais) mang§é§', 'avoir à l’imparfait + participe passé.'),
    ('[tu] (avais) fin§i§', ''),
    ('[nous] (étions) part§is§', 'être à l’imparfait + participe passé.')],
   Q('Elle ___ son goûter.', ['avait mangé', 'a mangé', 'mangeait'], 'Auxiliaire à l’imparfait + participe passé.', 'Complète avec « manger » au plus-que-parfait.', fill='v'),
   [Q('Nous ___ nos exercices.', ['avions fini', 'avons fini', 'finissions'], 'Auxiliaire à l’imparfait + participe passé.', 'Complète avec « finir » au plus-que-parfait.', fill='v'),
    Q('Tu ___ ce film.', ['avais vu', 'as vu', 'voyais'], 'Auxiliaire à l’imparfait + participe passé.', 'Complète avec « voir » au plus-que-parfait.', fill='v')]),
 E('avoir', 'tableau', 'avoir à l’imparfait', 'girl', 'L’auxiliaire avoir se conjugue à l’imparfait.',
   ['[j’] (avais) · [tu] (avais) · [il] (avait)',
    ('[nous] (avions) · [vous] (aviez) · [ils] (avaient)', 'avoir à l’imparfait : c’est l’auxiliaire.'),
    ('[Les enfants] (avaient) pris le bus.', 'Les enfants = ils → avaient.')],
   Q('Vous ___ oublié vos clés.', ['aviez', 'avions', 'avaient'], 'Vous → aviez.', 'Complète avec l’auxiliaire.', fill='v'),
   [Q('Les enfants ___ joué dehors.', ['avaient', 'avait', 'aviez'], 'Les enfants = ils.', 'Complète avec l’auxiliaire.', fill='v'),
    Q('J’___ dit bonjour.', ['avais', 'avait', 'avions'], 'Je → avais.', 'Complète avec l’auxiliaire.', fill='v')]),
 E('etre', 'remplacer', 'Avec être, j’accorde', 'boy', 'Avec être, le participe passé s’accorde avec le sujet.',
   [('[Léa] (était) part§i§*e*.', 'Léa : féminin → e.'),
    ('[Ils] (étaient) arriv§é§*s*.', 'Pluriel → s.'),
    ('[Elles] (étaient) sort§i§*es*.', 'Féminin pluriel → es.')],
   Q('Mes cousines étaient ___.', ['venues', 'venu', 'venus'], 'Mes cousines : féminin pluriel.', 'Complète avec le participe passé.', fill='t'),
   [Q('Mon frère était ___.', ['parti', 'partie', 'partis'], 'Mon frère : masculin singulier.', 'Complète avec le participe passé.', fill='t'),
    Q('Les filles étaient ___ tard.', ['rentrées', 'rentré', 'rentrés'], 'Les filles : féminin pluriel.', 'Complète avec le participe passé.', fill='t')]),
 E('att', 'non', 'À la forme négative', 'girl', 'ne… pas encadre l’auxiliaire.',
   [('Je |n’|avais |pas| mangé.', 'ne… pas encadre l’auxiliaire « avais ».'),
    ('Ils |n’|étaient |pas| venus.', '')],
   Q('', ['Il n’avait pas fini.', 'Il avait ne pas fini.', 'Il n’avait fini pas.'], 'ne… pas encadre l’auxiliaire.', 'Quelle phrase est bien écrite ?'),
   [Q('', ['Nous n’étions pas partis.', 'Nous étions ne pas partis.', 'Nous n’étions partis pas.'], 'ne… pas encadre l’auxiliaire.', 'Quelle phrase est bien écrite ?')]),
 E('att', 'attention', 'Passé composé ou plus-que-parfait ?', 'boy', 'Je regarde le temps de l’auxiliaire.',
   [('j’(ai) mang§é§', 'Auxiliaire au présent : le passé composé.'),
    ('j’(avais) mang§é§', 'Auxiliaire à l’imparfait : le plus-que-parfait.')],
   Q('Ils étaient tombés.', ['le plus-que-parfait', 'le passé composé'], 'L’auxiliaire est à l’imparfait.', 'Quel temps ?'),
   [Q('Ils sont tombés.', ['le passé composé', 'le plus-que-parfait'], 'L’auxiliaire est au présent.', 'Quel temps ?'),
    Q('Tu avais crié.', ['le plus-que-parfait', 'le passé composé'], 'L’auxiliaire est à l’imparfait.', 'Quel temps ?')]),
]
save('C8-CM2', {'id': 'C8-CM2', 'code': 'C8', 'niveau': 'CM2', 'f': 'C', 'ceinture': 'Rouge', 'titre': 'Le plus-que-parfait', 'sous': 'avoir ou être à l’imparfait + participe passé', 'lesson': True}, sections, ecrans, zones)

# ================================================================ C9
boxes = [
 dict(id='ps', col='bleu', geom=TL, title='Le passé simple', avatar=('girl', 322, 122), html=f'''
  <p class="txt" style="padding-right:100px">Le temps du <b>récit</b>, surtout avec il et ils.</p>
  <div class="exl" style="font-size:20px;line-height:1.55;margin-top:10px">1er groupe (C3) :<br>il chant{T("a")} · ils chant{T("èrent")}</div>'''),
 dict(id='g2', col='vert', geom=TC, title='2e groupe : -is, -it', html=f'''
  <div style="display:flex;gap:26px">{conj([("je","fin","is"),("tu","fin","is"),("il","fin","it")],21)}{conj([("nous","fin","îmes"),("vous","fin","îtes"),("ils","fin","irent")],21)}</div>'''),
 dict(id='i', col='violet', geom=TR, title='Des verbes en i', html=f'''
  <div class="exl" style="font-size:20px;line-height:1.5">faire : il f{T("it")} · ils f{T("irent")}<br>dire : il d{T("it")} · ils d{T("irent")}<br>prendre : il pr{T("it")} · ils pr{T("irent")}<br>voir : il v{T("it")} · ils v{T("irent")}</div>'''),
 dict(id='u', col='orange', geom=BL, title='Des verbes en u, en in', style='padding-top:52px', avatar=('boy', 445, 610), html=f'''
  <div class="exl" style="font-size:21px;line-height:1.6;margin-right:110px">pouvoir : il p{T("ut")} · ils p{T("urent")}<br>vouloir : il voul{T("ut")} · ils voul{T("urent")}<br>venir : il v{T("int")} · ils v{T("inrent")}</div>'''),
 dict(id='att', col='rouge', geom=BR, title='Attention !', style='padding-top:52px', html=f'''
  <ul style="font-size:21px;line-height:1.5">
   <li><b>aller</b> fait comme le 1er groupe : il all{T("a")}, ils all{T("èrent")}.</li>
   <li><i>il finit</i>, <i>il dit</i> : présent ou passé simple ? <b>La phrase m’aide</b> (hier, soudain…).</li></ul>'''),
]
legend = '<span class="t">terminaison</span>'
out, zones = build('C9-CM2', 'Le passé<br>simple', 'Conjugaison — C9 — CM2', legend, boxes, title_size=38, sub='2e groupe et verbes irréguliers', legend_pos='right:18px;top:470px')
sections = SEC(('ps', 'Le passé simple'), ('g2', '2e groupe : -is, -it'), ('i', 'Des verbes en i'), ('u', 'Des verbes en u, en in'), ('att', 'Attention !'))
ecrans = [
 E('ps', 'horloge', 'Le passé simple', 'girl', 'Le passé simple raconte les actions d’un récit.',
   [('Il |chanta|. Ils |chantèrent|.', '1er groupe : -a, -èrent (ceinture C3).'),
    ('Il |finit|. Ils |finirent|.', '2e groupe : -it, -irent.'),
    ('Il |prit|. Il |put|. Il |vint|.', 'Les verbes irréguliers : en i, en u, en in.')],
   Q('', ['le passé simple', 'l’imparfait', 'le futur'], 'Un seul mot, terminaison -irent.', '« ils bondirent » est au…'),
   [Q('', ['le passé simple', 'le présent', 'le futur'], 'Terminaison -èrent.', '« ils marchèrent » est au…')]),
 E('g2', 'liste', '2e groupe : -is, -it', 'boy', 'Les verbes du 2e groupe : is, is, it, îmes, îtes, irent.',
   ['je fin§is§ · tu fin§is§ · il fin§it§',
    'nous fin§îmes§ · vous fin§îtes§ · ils fin§irent§',
    ('Les soldats obé§irent§.', 'Avec ils : -irent.')],
   Q('Les oiseaux ___ dans le ciel.', ['surgirent', 'surgissaient', 'surgiront'], 'Passé simple, avec ils : -irent.', 'Complète avec « surgir » au passé simple.', fill='v'),
   [Q('Le chevalier ___ son épée.', ['saisit', 'saisissait', 'saisira'], 'Passé simple, avec il : -it.', 'Complète avec « saisir » au passé simple.', fill='v'),
    Q('Nous ___ la course.', ['finîmes', 'finissions', 'finirons'], 'Passé simple, avec nous : -îmes.', 'Complète avec « finir » au passé simple.', fill='v')]),
 E('i', 'mots', 'Des verbes en i', 'girl', 'faire, dire, prendre, voir : un passé simple en i.',
   ['faire : il f§it§ · ils f§irent§',
    'dire : il d§it§ · ils d§irent§',
    ('prendre : il pr§it§ · voir : il v§it§', 'Je les apprends par cœur.')],
   Q('Le magicien ___ un tour.', ['fit', 'faisa', 'faisit'], 'faire → il fit.', 'Complète avec « faire » au passé simple.', fill='v'),
   [Q('Ils ___ le chemin du retour.', ['prirent', 'prenèrent', 'prendirent'], 'prendre → ils prirent.', 'Complète avec « prendre » au passé simple.', fill='v'),
    Q('Elle ___ un loup.', ['vit', 'voya', 'voyit'], 'voir → elle vit.', 'Complète avec « voir » au passé simple.', fill='v')]),
 E('u', 'etiquette', 'Des verbes en u, en in', 'boy', 'pouvoir, vouloir : en u ; venir : en in.',
   ['pouvoir : il p§ut§ · ils p§urent§',
    'vouloir : il voul§ut§ · ils voul§urent§',
    ('venir : il v§int§ · ils v§inrent§', 'Je les apprends par cœur.')],
   Q('Le prince ___ entrer.', ['voulut', 'voulit', 'voula'], 'vouloir → il voulut.', 'Complète avec « vouloir » au passé simple.', fill='v'),
   [Q('Les secours ___ vite.', ['vinrent', 'venirent', 'venèrent'], 'venir → ils vinrent.', 'Complète avec « venir » au passé simple.', fill='v'),
    Q('Il ne ___ pas répondre.', ['put', 'pouva', 'pouvit'], 'pouvoir → il put.', 'Complète avec « pouvoir » au passé simple.', fill='v')]),
 E('att', 'attention', 'Les pièges', 'girl', 'aller fait comme le 1er groupe ; la phrase m’aide pour le temps.',
   [('il |alla| · ils |allèrent|', 'aller : comme le 1er groupe.'),
    ('Chaque jour, il |finit| son travail.', 'Ici, c’est le présent.'),
    ('Soudain, il |finit| son travail et partit.', 'Ici, c’est le passé simple : la phrase m’aide.')],
   Q('Ils ___ au marché.', ['allèrent', 'allirent', 'allurent'], 'aller : comme le 1er groupe.', 'Complète avec « aller » au passé simple.', fill='v'),
   [Q('Le roi ___ : « Silence ! »', ['dit', 'disa', 'dut'], 'dire → il dit.', 'Complète avec « dire » au passé simple.', fill='v'),
    Q('Ils ___ : « Bravo ! »', ['dirent', 'disèrent', 'durent'], 'dire → ils dirent.', 'Complète avec « dire » au passé simple.', fill='v')]),
]
save('C9-CM2', {'id': 'C9-CM2', 'code': 'C9', 'niveau': 'CM2', 'f': 'C', 'ceinture': 'Violette', 'titre': 'Le passé simple', 'sous': '2e groupe et verbes irréguliers', 'lesson': True}, sections, ecrans, zones)
