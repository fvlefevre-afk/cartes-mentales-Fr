import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from mapgen import build, TL, TC, TR
from lhelp import *

E_ = lambda t: f'<span class="e">{t}</span>'
boxes = [
 dict(id='regle', col='bleu', geom=TL, title='La règle', html=f'''
  <p class="txt" style="font-size:22px">Le <span class="v">verbe</span> s’accorde avec son <span class="s">sujet</span>.</p>
  <div class="ex" style="font-size:22px;margin-top:14px;line-height:1.6"><span class="s">L’enfant</span> <span class="v">joue</span>.<br><span class="s">Les enfants</span> <span class="v">jou{E_('ent')}</span>.</div>
  <p style="margin:10px 0 0;line-height:1.5;font-size:20px">tu <span class="arrow">→</span> <b>-s</b> · nous <span class="arrow">→</span> <b>-ons</b> · vous <span class="arrow">→</span> <b>-ez</b><br>ils, elles <span class="arrow">→</span> <b>-ent</b></p>'''),
 dict(id='pronom', col='vert', geom=TC, title='Le sujet → un pronom', html='''
  <p class="txt">Je remplace le sujet par un pronom.</p>
  <div class="ex" style="font-size:20px;line-height:1.4">
   <span class="s">Les enfants</span> = ils<br><span class="s">Mes sœurs</span> = elles<br>
   <span class="s">Léa et moi</span> = nous<br><span class="s">Toi et Tom</span> = vous</div>'''),
 dict(id='pieges', col='rouge', geom=TR, title='Attention aux pièges !', avatar=('girl', 1255, 285), html='''
  <ul style="font-size:20px;line-height:1.35">
   <li><b>Le sujet est loin</b> :<br><span class="s">Le chat</span> des voisins <span class="v">miaule</span>.</li>
   <li><b>Le sujet est après</b> :<br>Dans le pré <span class="v">courent</span> <span class="s">les chevaux</span>.</li>
   <li><b>Un petit mot devant</b> :<br><span class="s">Je</span> les <span class="v">regarde</span>.</li></ul>'''),
 dict(id='groupe2', col='violet', geom=(18, 568, 560, 350), title='Les verbes du 2e groupe', style='padding-top:52px', html=f'''
  <p class="txt">Infinitif en <b>-ir</b>, avec {E_('-iss-')} à nous, vous, ils.</p>
  <div class="ex" style="font-size:20px;line-height:1.5">je fin<b>is</b> · tu fin<b>is</b> · il fin<b>it</b><br>nous fin{E_('iss')}ons · vous fin{E_('iss')}ez · ils fin{E_('iss')}ent</div>
  <p style="font-size:20px;margin:10px 0 6px">finir, choisir, grandir, rougir, remplir…</p>
  <p style="font-size:20px;margin:0">Pas de -iss- : <b>partir</b> <span class="arrow">→</span> nous partons : ce n’est pas le 2e groupe.</p>'''),
 dict(id='methode', col='orange', geom=(612, 568, 770, 350), title='Ma méthode', style='padding-top:52px', avatar=('boy', 1250, 610), html='''
  <ol style="margin:0;padding-left:26px;font-size:22px;line-height:1.5;padding-right:110px">
   <li>Je trouve le <span class="v">verbe</span>.</li>
   <li>Je trouve le <span class="s">sujet</span> : « Qui est-ce qui… ? »</li>
   <li>Je remplace le sujet par un pronom.</li>
   <li>J’écris la bonne terminaison.</li></ol>
  <div class="ex" style="text-align:center;font-size:21px"><span class="s">Les élèves</span> (= ils) <span class="v">écout<span class="e">ent</span></span> la maîtresse.</div>'''),
]
legend = '<span class="s">sujet</span> · <span class="v">verbe</span>'
out, zones = build('G5', 'L’accord<br>sujet-verbe', 'Grammaire — G5 — CM1', legend, boxes, title_size=38)

sections = [
 {'id': 'regle', 'nom': 'La règle', 'couleur': '#1f5fc4'},
 {'id': 'pronom', 'nom': 'Le sujet → un pronom', 'couleur': '#23845a'},
 {'id': 'pieges', 'nom': 'Les pièges', 'couleur': '#c62828'},
 {'id': 'groupe2', 'nom': 'Le 2e groupe', 'couleur': '#7b3fa0'},
 {'id': 'methode', 'nom': 'Ma méthode', 'couleur': '#e67e22'},
]
ecrans = [
 E('regle', 'sv', 'Le sujet commande le verbe', 'girl', 'Le verbe s’accorde avec son sujet.',
   ['[L’enfant] (joue).',
    ('[Les enfants] (jou*ent*).', 'Le sujet change : le verbe change aussi.'),
    ('[Tu] (joue*s*) · [Nous] (jou*ons*)', 'Le verbe s’accorde avec son sujet.')],
   Q('Les oiseaux ___.', ['chantent', 'chante', 'chantes'], 'Les oiseaux = ils.', fill='v'),
   [Q('Le bébé ___.', ['pleure', 'pleurent', 'pleures'], 'Le bébé = il.', fill='v'),
    Q('Tu ___ vite.', ['manges', 'mange', 'mangent'], 'Avec tu, le verbe finit par -s.', fill='v'),
    Q('Les filles ___ à la corde.', ['sautent', 'saute', 'sautes'], 'Les filles = elles.', fill='v')]),
 E('regle', 'tableau', 'Les terminaisons à connaître', 'girl', 'Ces terminaisons reviennent presque toujours.',
   ['je joue · tu joue*s* · il joue',
    'nous jou*ons* · vous jou*ez* · ils jou*ent*',
    ('tu → -s · nous → -ons · vous → -ez · ils → -ent', 'À retenir !')],
   Q('Vous ___ au ballon.', ['jouez', 'jouer', 'jouent'], 'Avec vous, le verbe finit par -ez.', fill='v'),
   [Q('Nous ___ une chanson.', ['chantons', 'chantez', 'chantent'], 'Avec nous : -ons.', fill='v'),
    Q('Ils ___ la télé.', ['regardent', 'regarde', 'regardez'], 'Avec ils : -ent.', fill='v'),
    Q('Tu ___ ton vélo.', ['ranges', 'range', 'rangent'], 'Avec tu : -s.', fill='v')]),
 E('pronom', 'remplacer', 'Je remplace le sujet', 'boy', 'Je remplace le sujet par il, elle, ils ou elles.',
   ['[Les filles] (dansent).', '[~Les filles] (dansent).',
    ('[*Elles*] (dans*ent*).', 'elles → -ent')],
   Q('Mes parents ___ le journal.', ['lisent', 'lit', 'lis'], 'Mes parents = ils.', fill='v'),
   [Q('Ma grand-mère ___ un gâteau.', ['prépare', 'préparent', 'prépares'], 'Ma grand-mère = elle.', fill='v'),
    Q('Les voitures ___ vite.', ['roulent', 'roule', 'roules'], 'Les voitures = elles.', fill='v')]),
 E('pronom', 'wagon', 'Plusieurs sujets', 'boy', 'Plusieurs noms reliés : un seul sujet !',
   [('[#Léa et moi] (parl*ons*).', 'Léa et moi = nous'),
    ('[#Toi et Tom] (parl*ez*).', 'Toi et Tom = vous'),
    ('[#Léa et Tom] (parl*ent*).', 'Léa et Tom = ils')],
   Q('Mon frère et moi ___ au foot.', ['jouons', 'jouent', 'joue'], 'Mon frère et moi = nous.', fill='v'),
   [Q('Le chat et le chien ___.', ['dorment', 'dort', 'dormez'], 'Le chat et le chien = ils.', fill='v'),
    Q('Toi et ta sœur ___ en retard.', ['arrivez', 'arrivent', 'arrivons'], 'Toi et ta sœur = vous.', fill='v')]),
 E('pieges', 'deplacer', 'Le sujet est loin du verbe', 'girl', 'Des mots peuvent séparer le sujet du verbe.',
   ['Le chat des voisins miaule.',
    ('[Le chat] des voisins (miaule).', 'Qui est-ce qui miaule ? Le chat, pas les voisins.'),
    ('[Le chat] {{des voisins}} (miaule).', 'Je barre ce qui sépare le sujet du verbe.')],
   Q('Les fleurs du jardin ___.', ['poussent', 'pousse'], 'Qui est-ce qui pousse ? Les fleurs.', fill='v'),
   [Q('Le stylo de mes amis ___.', ['fuit', 'fuient'], 'Qui est-ce qui fuit ? Le stylo.', fill='v'),
    Q('Les enfants de ma voisine ___ fort.', ['crient', 'crie'], 'Qui est-ce qui crie ? Les enfants.', fill='v')]),
 E('pieges', 'deplacer', 'Le sujet est après le verbe', 'girl', 'Parfois, le sujet se cache après le verbe.',
   ['Dans le pré courent les chevaux.',
    ('Dans le pré (courent) [les chevaux].', 'Qui est-ce qui court ? Les chevaux.'),
    ('[*Les chevaux*] (courent) dans le pré.', 'Je remets le sujet avant le verbe.')],
   Q('Dans la mare ___ les grenouilles.', ['sautent', 'saute'], 'Qui est-ce qui saute ? Les grenouilles.', fill='v'),
   [Q('Sur la branche ___ deux oiseaux.', ['chantent', 'chante'], 'Qui est-ce qui chante ? Deux oiseaux.', fill='v'),
    Q('Où ___ tes amis ?', ['habitent', 'habite'], 'Qui est-ce qui habite ? Tes amis.', fill='v')]),
 E('pieges', 'attention', 'Le petit mot devant le verbe', 'girl', 'Le petit mot juste devant le verbe n’est pas toujours le sujet !',
   ['Je les regarde.',
    ('[Je] |les| (regarde).', 'les n’est pas le sujet !'),
    ('[*Je*] les (regarde).', 'Qui est-ce qui regarde ? Je → regarde, sans -nt.')],
   Q('Tom les ___.', ['appelle', 'appellent'], 'Qui est-ce qui appelle ? Tom.', fill='v'),
   [Q('Mes parents me ___.', ['parlent', 'parle'], 'Qui est-ce qui parle ? Mes parents.', fill='v'),
    Q('La maîtresse leur ___ une histoire.', ['lit', 'lisent'], 'Qui est-ce qui lit ? La maîtresse.', fill='v')]),
 E('groupe2', 'tableau', 'Le 2e groupe : -ir avec -iss-', 'boy', 'J’entends -iss- avec nous : c’est le 2e groupe.',
   ['finir',
    ('nous fin*iss*ons · vous fin*iss*ez · ils fin*iss*ent', 'On entend -iss- : 2e groupe.'),
    ('je fin*is* · tu fin*is* · il fin*it*', 'Au singulier : -is, -is, -it.')],
   Q('Nous ___ nos devoirs.', ['finissons', 'finons', 'finisons'], 'Au 2e groupe, nous → -issons.', fill='v'),
   [Q('Les enfants ___ vite.', ['grandissent', 'grandent', 'grandit'], 'Ils → -issent.', fill='v'),
    Q('Tu ___ un livre.', ['choisis', 'choisit', 'choisissent'], 'Avec tu : -is.', fill='v'),
    Q('Il ___ de honte.', ['rougit', 'rougis', 'rougissent'], 'Avec il : -it.', fill='v')]),
 E('groupe2', 'attention', 'Pas tous les verbes en -ir', 'boy', 'Je dis « nous… » : si j’entends -iss-, c’est le 2e groupe.',
   [('partir → nous part*ons*', 'Pas de -iss- : ce n’est pas le 2e groupe.'),
    ('grandir → nous grand*iss*ons', '-iss- : c’est le 2e groupe ✔'),
    'choisir · grandir · rougir · finir · remplir…'],
   Q('', ['choisir', 'partir', 'venir'], 'Dis « nous … » : entends-tu -iss- ?', 'Lequel est du 2e groupe ?'),
   [Q('', ['remplir', 'courir', 'dormir'], 'Nous remplissons, nous courons, nous dormons…', 'Lequel est du 2e groupe ?'),
    Q('', ['sortir', 'réussir', 'applaudir'], 'Nous sortons : pas de -iss-.', 'Lequel n’est PAS du 2e groupe ?')]),
 E('methode', 'liste', 'Ma méthode en 4 étapes', 'girl', 'Verbe, sujet, pronom, terminaison.',
   [('Les élèves (écout…) la maîtresse.', '1. Je trouve le verbe.'),
    ('[Les élèves] (écout…) la maîtresse.', '2. Je trouve le sujet : qui est-ce qui écoute ?'),
    ('[Ils] (écout…) la maîtresse.', '3. Je le remplace par un pronom.'),
    ('[Les élèves] (écout*ent*) la maîtresse.', '4. J’écris la terminaison : ils → -ent.')],
   Q('Les élèves de ma classe ___ bien.', ['travaillent', 'travaille'], 'Qui est-ce qui travaille ? Les élèves = ils.', fill='v'),
   [Q('Dans la forêt ___ les loups.', ['hurlent', 'hurle'], 'Qui est-ce qui hurle ? Les loups.', fill='v'),
    Q('Ma sœur et moi ___ le repas.', ['préparons', 'préparent', 'prépare'], 'Ma sœur et moi = nous.', fill='v'),
    Q('Le chien de mes cousins ___.', ['aboie', 'aboient'], 'Qui est-ce qui aboie ? Le chien.', fill='v')]),
]
save('G5', {'id': 'G5', 'f': 'G', 'ceinture': 'Verte', 'titre': "L'accord sujet-verbe", 'sous': 'et les verbes du 2e groupe', 'lesson': True}, sections, ecrans, zones)
