import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from mapgen import build, PAL, TL, TC, TR
from lhelp import *

BLx = (18, 568, 440, 350)
BCx = (485, 568, 430, 350)
BRx = (952, 568, 430, 350)
boxes = [
 dict(id='gn', col='vert', geom=TL, title='Les mots du GN', avatar=('girl', 322, 122), html='''
  <p class="txt" style="padding-right:100px">Le <b style="color:#1f5fc4">nom</b> : une personne, un animal, une chose, une idée.</p>
  <p class="txt" style="padding-right:100px">L’<span class="a">adjectif</span> dit comment est le nom.</p>
  <div class="ex big" style="margin-top:14px"><span class="d">une</span> <span class="a">jolie</span> <span class="n">robe</span></div>
  <p class="small" style="margin:8px 0 0">Le <span class="d">déterminant</span> est devant le nom.</p>'''),
 dict(id='det', col='orange', geom=TC, title='Les déterminants', html='''
  <p style="margin:0 0 6px;font-size:19px;line-height:1.35"><b>Articles</b> : <span class="d">le, la, les, un, une, des</span></p>
  <p style="margin:0 0 6px;font-size:19px;line-height:1.35"><b>Possessifs</b> (à qui ?) : <span class="d">mon, ton, son, ma, ta, sa, mes, tes, ses, notre, votre, leur, nos, vos, leurs</span></p>
  <p style="margin:0 0 8px;font-size:19px;line-height:1.35"><b>Démonstratifs</b> (je montre) : <span class="d">ce, cet, cette, ces</span></p>
  <div class="ex" style="text-align:center;padding:4px 10px;margin-top:4px"><span class="d">mon</span> vélo · <span class="d">cet</span> arbre · <span class="d">ces</span> fleurs</div>'''),
 dict(id='verbe', col='rouge', geom=TR, title='Verbe et pronom', avatar=('boy', 1250, 122), html='''
  <ul style="padding-right:96px;font-size:20px">
   <li>Le <span class="v">verbe</span> se conjugue : il change avec le temps et le sujet.</li>
   <li>Le <b>pronom</b> remplace un nom.</li></ul>
  <div class="ex" style="text-align:center"><span class="s">Léa</span> <span class="v">chante</span> <span class="arrow">→</span> <span class="s">Elle</span> <span class="v">chante</span></div>
  <p class="small" style="margin:6px 0 0;font-size:16px;line-height:1.35"><b>sujets</b> : je, tu, il, elle, on, nous, vous, ils, elles<br><b>compléments</b> : me, te, le, la, les, lui, leur</p>'''),
 dict(id='adv', col='violet', geom=BLx, title='L’adverbe', style='padding-top:50px', html='''
  <ul style="font-size:20px">
   <li>Il précise un <span class="v">verbe</span>, un adjectif ou un autre adverbe.</li>
   <li>Beaucoup finissent par <span class="e">-ment</span>.</li></ul>
  <div class="ex" style="text-align:center;font-size:22px">Le lapin <span class="v">court</span> <span class="rond">très</span> <span class="rond">vite</span>.</div>
  <p class="small" style="margin:8px 0 0">hier, souvent, toujours, bien, très, lentement…</p>'''),
 dict(id='conj', col='turquoise', geom=BCx, title='Les mots qui relient', style='padding-top:50px', html='''
  <p class="txt">Les <b>conjonctions de coordination</b> relient deux mots ou deux parties de phrase.</p>
  <div class="ex big" style="font-size:21px;padding:6px 4px;white-space:nowrap">mais · ou · et · donc · or · ni · car</div>
  <p class="small" style="margin:6px 0 4px;text-align:center"><i>« Mais où est donc Ornicar ? »</i></p>
  <p class="txt" style="text-align:center">Il pleut <span class="rond">mais</span> je sors.</p>'''),
 dict(id='inv', col='rose', geom=BRx, title='Variable ou invariable ?', style='padding-top:50px', html='''
  <p class="txt"><b>Variables</b> (ils changent) : nom, déterminant, adjectif, verbe, pronom.</p>
  <p class="txt"><b>Invariables</b> (ils ne changent jamais) : adverbe, conjonction.</p>
  <div class="ex" style="font-size:20px">il parle <span class="rond">doucement</span><br>elles parlent <span class="rond">doucement</span></div>'''),
]
legend = '<span class="d">dét.</span> · <b style="color:#1f5fc4">nom</b> · <span class="a">adjectif</span> · <span class="v">verbe</span>'
out, zones = build('G4', 'Les classes<br>de mots', 'Grammaire — G4 — CM1', legend, boxes, sub='', title_size=38)

sections = [
 {'id': 'gn', 'nom': 'Les mots du GN', 'couleur': '#23845a'},
 {'id': 'det', 'nom': 'Les déterminants', 'couleur': '#e67e22'},
 {'id': 'verbe', 'nom': 'Verbe et pronom', 'couleur': '#c62828'},
 {'id': 'adv', 'nom': 'L’adverbe', 'couleur': '#7b3fa0'},
 {'id': 'conj', 'nom': 'Les mots qui relient', 'couleur': '#00838f'},
 {'id': 'inv', 'nom': 'Variable ou invariable ?', 'couleur': '#c2185b'},
]
ecrans = [
 E('gn', 'etiquette', 'Le nom', 'girl', 'Un nom désigne une personne, un animal, une chose ou une idée.',
   ['Léa · un chien · une table · la joie',
    ('|*Léa*| · un |*chien*| · une |*table*| · la |*joie*|', 'Ce sont des noms.'),
    ('^*un*^ chien · ^*la*^ joie', 'Je peux mettre un déterminant devant un nom commun.')],
   C('Le <boulanger> sourit.', 'Clique sur le nom.', 'Peux-tu mettre « un » ou « le » devant ?'),
   [C('Ma <sœur> rit.', 'Clique sur le nom.', 'Peux-tu mettre « une » ou « la » devant ?'),
    C('Il a beaucoup de <courage>.', 'Clique sur le nom.', 'Un nom peut aussi désigner une idée.'),
    Q('', ['jardin', 'joli', 'jouer'], 'Peux-tu dire « un … » ?', 'Quel mot est un nom ?')]),
 E('gn', 'loupe', 'Je trouve la classe d’un mot', 'girl', 'Je me pose des questions sur chaque mot.',
   ['Le petit chat dort.',
    ('^Le^ ~petit~ |chat| dort.', 'Le : déterminant · petit : adjectif · chat : nom'),
    ('^Le^ ~petit~ |chat| (dort).', 'dort change avec le temps (il dormait) : c’est un verbe.')],
   Q('une jolie robe', ['un adjectif', 'un nom', 'un verbe'], 'Il dit comment est la robe.', 'Dans ce GN, « jolie » est…'),
   [Q('Mon chien aboie.', ['un verbe', 'un nom', 'un adjectif'], 'Hier, il aboyait : il change avec le temps.', '« aboie » est…'),
    Q('des fleurs rouges', ['un nom', 'un adjectif', 'un déterminant'], 'Peux-tu dire « une … » ?', '« fleurs » est…'),
    Q('un gros ballon', ['un adjectif', 'un nom', 'un verbe'], 'Il dit comment est le ballon.', '« gros » est…')]),
 E('gn', 'etiquette', 'Nature ou fonction ?', 'boy', 'La nature d’un mot, c’est sa classe ; sa fonction, c’est son rôle dans la phrase.',
   [('Le |chat| dort.', 'chat : un nom. C’est sa nature (sa classe).'),
    ('[Le chat] (dort).', 'Le chat : sujet du verbe. C’est sa fonction (son rôle).'),
    ('Léa caresse ^le^ |chat|.', 'chat : toujours un nom, mais ici complément du verbe.')],
   Q('Léa caresse le chat.', ['un nom, complément du verbe', 'un nom, sujet du verbe', 'un verbe'], 'Sa nature ne change pas ; son rôle, oui.', '« chat » est…'),
   [Q('Le chien aboie.', ['un nom, sujet du verbe', 'un nom, complément du verbe', 'un adjectif'], 'Qui est-ce qui aboie ?', '« chien » est…'),
    Q('', ['sa classe : nom, verbe, adjectif…', 'son rôle dans la phrase : sujet, complément…'], 'La nature, c’est la classe.', 'La nature d’un mot, c’est…')]),
 E('det', 'etiquette', 'Les articles', 'girl', 'Les articles sont des déterminants : le, la, l’, les ; un, une, des.',
   [('^le^ chien · ^la^ table · ^l’^arbre · ^les^ fleurs', 'Des articles définis : un nom que l’on connaît.'),
    ('^un^ chien · ^une^ table · ^des^ fleurs', 'Des articles indéfinis : un nom que l’on ne connaît pas encore.')],
   Q('', ['un article défini', 'un article indéfini', 'un déterminant possessif'], 'le, la, l’, les : définis.', 'Dans « la maison », « la » est…'),
   [Q('', ['un article indéfini', 'un article défini', 'un déterminant démonstratif'], 'un, une, des : indéfinis.', 'Dans « des oiseaux », « des » est…'),
    C('J’ai vu <un> écureuil.', 'Clique sur l’article indéfini.', 'un, une, des.')]),
 E('det', 'etiquette', 'Les déterminants possessifs', 'boy', 'Ils disent à qui est la chose.',
   ['^le^ cartable',
    ('^*mon*^ cartable · ^*ton*^ cartable · ^*son*^ cartable', 'À qui ? À moi, à toi, à lui ou à elle.'),
    ('^*notre*^ classe · ^*leurs*^ cahiers', 'mon, ton, son, ma, ta, sa, mes, tes, ses, notre, votre, leur, nos, vos, leurs')],
   Q('Tom range ___ cahiers.', ['ses', 'son', 'ces'], 'Les cahiers sont à Tom, et il y en a plusieurs.', fill='et'),
   [Q('Nous aimons ___ maîtresse.', ['notre', 'nos', 'leur'], 'Elle est à nous, et il n’y en a qu’une.', fill='et'),
    Q('Léa cherche ___ lunettes.', ['ses', 'sa', 'son'], 'Les lunettes sont à Léa, et c’est un mot au pluriel.', fill='et'),
    C('J’ai perdu <mes> crayons.', 'Clique sur le déterminant possessif.', 'Il dit à qui sont les crayons.')]),
 E('det', 'doigt', 'Les déterminants démonstratifs', 'boy', 'Ils montrent : ce, cet, cette, ces.',
   ['^*ce*^ chien · ^*cette*^ maison',
    ('^*cet*^ arbre · ^*cet*^ homme', 'cet devant une voyelle ou un h muet.'),
    ('^*ces*^ fleurs', 'ces au pluriel.')],
   Q('___ oiseau chante.', ['Cet', 'Ce', 'Cette'], 'Oiseau commence par une voyelle.', fill='et'),
   [Q('___ voiture est rapide.', ['Cette', 'Ce', 'Ces'], 'Voiture est féminin singulier.', fill='et'),
    Q('J’aime ___ chansons.', ['ces', 'cette', 'cet'], 'Chansons est au pluriel.', fill='et'),
    Q('___ garçon court vite.', ['Ce', 'Cet', 'Cette'], 'Garçon est masculin et commence par une consonne.', fill='et')]),
 E('verbe', 'horloge', 'Le verbe se conjugue', 'boy', 'Le verbe change avec le temps et avec le sujet.',
   ['Léa (chante).',
    ('Hier, Léa (*chantait*).', 'Il change avec le temps.'),
    ('Nous (*chantons*).', 'Il change avec le sujet.')],
   V('[Les enfants] (jouent) dans la cour.'),
   [V('[Le vent] (souffle) fort.'), V('Demain, [nous] (irons) au cinéma.'),
    Q('', ['grandir', 'grand', 'grandeur'], 'Il peut se conjuguer : je grandis.', 'Quel mot est un verbe ?')]),
E('verbe', 'loupe', 'Verbe ou nom ?', 'boy', 'Un même mot peut être un verbe ou un nom : je regarde son rôle.',
   [('[Tom] (élève) des lapins.', 'Il change avec le temps (il élevait) : c’est un verbe.'),
    ('^Une^ élève lit.', 'Je peux mettre un déterminant devant : c’est un nom.'),
    ('[tu] (élèves) · [elles] (élèvent) / ^des^ élèves', 'Le verbe prend la terminaison du sujet ; le nom prend un s au pluriel.')],
   Q('Mes voisins ___ des poules.', ['élèvent', 'élèves'], 'Mes voisins = ils : c’est un verbe → -ent.', fill='v'),
   [Q('Les ___ écoutent la maîtresse.', ['élèves', 'élèvent'], 'Un déterminant devant : c’est un nom → -s.', fill='circ'),
    Q('J’ai deux ___ dans ma trousse.', ['gommes', 'gomment'], 'Après « deux » : un nom → -s.', fill='circ'),
    Q('Les enfants ___ leurs erreurs.', ['gomment', 'gommes'], 'Les enfants = ils : un verbe → -ent.', fill='v')]),
 E('verbe', 'remplacer', 'Le pronom remplace le nom', 'boy', 'Le pronom évite de répéter le nom.',
   ['[Léa] (chante).', '[~Léa] (chante).',
    ('[*Elle*] (chante).', 'Elle remplace Léa : c’est un pronom.'),
    ('je · tu · il · elle · on · nous · vous · ils · elles', 'Les pronoms personnels.')],
   Q('Mes cousins arrivent. ___ sont en retard.', ['Ils', 'Elles', 'Il'], 'Mes cousins : plusieurs garçons.', fill='s'),
   [Q('Ma tante téléphone. ___ est contente.', ['Elle', 'Il', 'Ils'], 'Ma tante : une seule femme.', fill='s'),
    Q('Tom et moi jouons. ___ sommes dehors.', ['Nous', 'Vous', 'Ils'], 'Tom et moi = nous.', fill='s')]),
 E('verbe', 'remplacer', 'Pronoms sujets et compléments', 'boy', 'Un pronom peut remplacer le sujet… ou un complément.',
   ['[Léa] (regarde) les oiseaux.',
    ('[*Elle*] (regarde) les oiseaux.', 'Elle remplace le sujet : pronom sujet.'),
    ('[Elle] |*les*| (regarde).', 'les remplace « les oiseaux » : pronom complément.'),
    ('me · te · le · la · les · lui · leur', 'Les pronoms compléments se placent devant le verbe.')],
   C('Mes amis ? Je <les> attends.', 'Clique sur le pronom complément.', 'Il remplace « mes amis » et ce n’est pas le sujet.'),
   [Q('Léa range sa chambre. Léa ___ range.', ['la', 'le', 'les'], 'Sa chambre : féminin singulier.', fill='circ'),
    Q('Je téléphone à mon grand-père. Je ___ téléphone.', ['lui', 'le', 'leur'], 'À mon grand-père = à lui.', fill='circ'),
    C('<Nous> leur parlons.', 'Clique sur le pronom sujet.', 'Qui est-ce qui parle ?')]),
 E('adv', 'ampoule', 'L’adverbe précise', 'girl', 'L’adverbe précise un verbe, un adjectif ou un autre adverbe.',
   ['Le lapin (court).',
    ('Le lapin (court) |*vite*|.', 'Comment court-il ? Vite.'),
    ('Le lapin (court) |*très*| |vite|.', 'très précise vite.'),
    ('Il est |*très*| ~grand~.', 'très précise un adjectif.')],
   C('Tom marche <lentement>.', 'Clique sur l’adverbe.', 'Comment marche-t-il ?'),
   [C('Elle chante <bien>.', 'Clique sur l’adverbe.', 'Comment chante-t-elle ?'),
    C('<Hier>, il a neigé.', 'Clique sur l’adverbe.', 'Quand a-t-il neigé ?'),
    C('Ce gâteau est <trop> sucré.', 'Clique sur l’adverbe.', 'Quel mot précise « sucré » ?')]),
 E('conj', 'mots', 'Les mots qui relient', 'girl', 'mais, ou, et, donc, or, ni, car relient des mots ou des phrases.',
   ['Je voulais sortir. Il pleuvait.',
    ('Je voulais sortir |*mais*| il pleuvait.', 'mais relie les deux parties.'),
    ('mais · ou · et · donc · or · ni · car', '« Mais où est donc Ornicar ? »')],
   Q('Tu veux du lait ___ du jus ?', ['ou', 'mais', 'car'], 'Il faut choisir entre les deux.', fill='circ'),
   [Q('J’ai un chat ___ un chien.', ['et', 'car', 'or'], 'J’ai les deux.', fill='circ'),
    Q('', ['mais, ou, et', 'très, bien, vite', 'le, la, les'], 'Mais où est donc Ornicar ?', 'Quelle liste contient seulement des conjonctions ?')]),
 E('conj', 'ampoule', 'Choisir le bon mot', 'girl', 'Chaque mot qui relie a un sens.',
   [('Il est fatigué |car| il a couru.', 'car : la cause (= parce que)'),
    ('Il a couru, |donc| il est fatigué.', 'donc : la conséquence'),
    ('Il est petit |mais| il est fort.', 'mais : une opposition')],
   Q('Je mets mon manteau ___ il fait froid.', ['car', 'mais', 'ou'], 'Pourquoi mettre un manteau ?', fill='circ'),
   [Q('Il a beaucoup révisé, ___ il a réussi.', ['donc', 'mais', 'car'], 'Réussir est la conséquence.', fill='circ'),
    Q('Je voulais venir ___ j’étais malade.', ['mais', 'donc', 'ou'], 'Les deux idées s’opposent.', fill='circ')]),
 E('inv', 'attention', 'Variable ou invariable ?', 'boy', 'Certains mots changent, d’autres jamais.',
   [('^le^ |chat| ~noir~ · ^les^ |chat*s*| ~noir*s*~', 'Le déterminant, le nom et l’adjectif changent : ils sont variables.'),
    ('Il parle |doucement|. / Elles parlent |doucement|.', 'L’adverbe ne change jamais : il est invariable.'),
    ('lent → lente*ment* · doux → douce*ment*', 'Beaucoup d’adverbes finissent par -ment.')],
   Q('', ['souvent', 'souris', 'petit'], 'Cherche l’adverbe.', 'Quel mot ne change jamais ?'),
   [Q('', ['mais', 'maison', 'mange'], 'Cherche le mot qui relie.', 'Quel mot est invariable ?'),
    Q('rapide → ___', ['rapidement', 'rapides', 'rapidité'], 'Beaucoup d’adverbes finissent par -ment.', 'Je forme l’adverbe :', fill='circ')]),
]
save('G4', {'id': 'G4', 'f': 'G', 'ceinture': 'Orange', 'titre': 'Les classes de mots', 'sous': 'nature des mots', 'lesson': True}, sections, ecrans, zones)
