from niveaux_lib import *
CL = 'Quelle est la classe de ce mot ?'
NA = 'Clique sur le nom qui fait l’action.'; NAh = 'Qui est-ce qui fait l’action ?'
VB = 'Clique sur le verbe.'; VBh = 'Le verbe change avec le temps et avec le sujet.'
AV = 'Clique sur l’adverbe.'; AVh = 'Il précise le verbe, il ne change jamais.'
def nat(p, mot, bon, mal): return C(p, f'« {mot} » est…', bon, mal, 'Je me pose des questions sur le mot : à quoi sert-il dans la phrase ?')
def art(ph, mot, bon, mal): return C('', f'Dans « {ph} », « {mot} » est…', bon, mal, 'L’article défini désigne quelque chose de connu (le, la, l’, les) ; l’indéfini, quelque chose de nouveau (un, une, des).')
POS = 'Il dit à qui est la chose.'; DEM = 'Il montre : ce, cet, cette, ces.'
niv = {
 'Le nom': (
  [K('Dans la cour, le <maître> surveille les enfants.', NA, NAh), K('Ce matin, ma <sœur> a préparé un gâteau.', NA, NAh), K('Sur la table, le <chat> dort.', NA, NAh), K('Pendant la récréation, les <élèves> jouent aux billes.', NA, NAh)],
  [K('Au bord du lac, un jeune <pêcheur> surveille patiemment sa ligne.', NA, NAh), K('Dans le grenier, une vieille <malle> cachait des lettres jaunies.', NA, NAh),
   K('Depuis ce matin, la <pluie> mouille les rues du village.', NA, NAh), K('Devant la porte, le <facteur> dépose le courrier du matin.', NA, NAh)]),
 'Je trouve la classe d’un mot': (
  [nat('Mon petit frère dort.', 'petit', 'un adjectif', ['un nom', 'un verbe']), nat('Les oiseaux chantent le matin.', 'chantent', 'un verbe', ['un nom', 'un adjectif']),
   nat('Le grand arbre perd ses feuilles.', 'feuilles', 'un nom', ['un verbe', 'un adjectif']), nat('Ces fleurs sentent bon.', 'Ces', 'un déterminant', ['un nom', 'un verbe'])],
  [nat('Le vieux marin raconte une histoire passionnante.', 'passionnante', 'un adjectif', ['un nom', 'un verbe']), nat('Pendant la nuit, la tempête a ravagé la côte.', 'tempête', 'un nom', ['un verbe', 'un adjectif']),
   nat('Mes voisins cultivent de beaux légumes dans leur jardin.', 'cultivent', 'un verbe', ['un nom', 'un adjectif']), nat('Chaque dimanche, nous rendons visite à nos grands-parents.', 'nos', 'un déterminant', ['un nom', 'un pronom'])]),
 'Nature ou fonction ?': (
  [nat('Tom lit un livre.', 'livre', 'un nom, complément du verbe', ['un nom, sujet du verbe', 'un verbe']), nat('Le chien aboie.', 'chien', 'un nom, sujet du verbe', ['un nom, complément du verbe', 'un adjectif']),
   nat('Papa répare la voiture.', 'Papa', 'un nom, sujet du verbe', ['un nom, complément du verbe', 'un verbe']), nat('Maman cuisine un gâteau.', 'gâteau', 'un nom, complément du verbe', ['un nom, sujet du verbe', 'un adjectif'])],
  [nat('Ma voisine arrose les fleurs du jardin.', 'voisine', 'un nom, sujet du verbe', ['un nom, complément du verbe', 'un adjectif']), nat('Les élèves rangent leurs affaires dans le casier.', 'affaires', 'un nom, complément du verbe', ['un nom, sujet du verbe', 'un verbe']),
   nat('Le vent froid secoue les branches.', 'vent', 'un nom, sujet du verbe', ['un nom, complément du verbe', 'un adjectif']), nat('Mon grand-père répare la vieille barrière.', 'barrière', 'un nom, complément du verbe', ['un nom, sujet du verbe', 'un adjectif'])]),
 'Les articles': (
  [art('un cadeau', 'un', 'un article indéfini', ['un article défini', 'un déterminant possessif']), art('les enfants', 'les', 'un article défini', ['un article indéfini', 'un déterminant démonstratif']),
   art('l’école', 'l’', 'un article défini', ['un article indéfini', 'un déterminant possessif']), art('des bonbons', 'des', 'un article indéfini', ['un article défini', 'un déterminant démonstratif'])],
  [art('J’ai vu un écureuil dans le parc.', 'le', 'un article défini', ['un article indéfini', 'un déterminant possessif']), art('Elle a acheté des pommes au marché.', 'des', 'un article indéfini', ['un article défini', 'un déterminant démonstratif']),
   art('Le facteur apporte une lettre à la voisine.', 'une', 'un article indéfini', ['un article défini', 'un déterminant possessif']), art('Les élèves écoutent la maîtresse.', 'la', 'un article défini', ['un article indéfini', 'un déterminant démonstratif'])]),
 'Les déterminants possessifs': (
  [C('Léa range ___ jouets.', POS, 'ses', ['son', 'ces'], 'Il y a plusieurs jouets : ses.', 'et'), C('Nous rangeons ___ affaires.', POS, 'nos', ['notre', 'vos'], 'Plusieurs affaires, à nous : nos.', 'et'),
   C('Tom a oublié ___ cahier.', POS, 'son', ['sa', 'ses'], 'Un seul cahier, masculin : son.', 'et'), C('Les enfants cherchent ___ ballon.', POS, 'leur', ['leurs', 'ses'], 'Plusieurs enfants, un seul ballon : leur.', 'et')],
  [C('Mes cousins ont oublié ___ valises à la gare.', POS, 'leurs', ['leur', 'ses'], 'Plusieurs cousins, plusieurs valises : leurs.', 'et'), C('Vous devez ranger ___ affaires avant de partir.', POS, 'vos', ['votre', 'nos'], 'Avec « vous », plusieurs affaires : vos.', 'et'),
   C('Ma tante a perdu ___ lunettes dans le jardin.', POS, 'ses', ['sa', 'son'], 'Une seule personne, plusieurs lunettes : ses.', 'et'), C('Nous avons invité ___ voisins à notre fête.', POS, 'nos', ['notre', 'vos'], 'Avec « nous », plusieurs voisins : nos.', 'et')]),
 'Les déterminants démonstratifs': (
  [C('___ garçon est grand.', DEM, 'Ce', ['Cette', 'Ces'], 'Garçon est masculin singulier.', 'et'), C('___ école est ancienne.', DEM, 'Cette', ['Ce', 'Cet'], 'École est féminin.', 'et'),
   C('J’aime ___ arbre.', DEM, 'cet', ['ce', 'cette'], 'Arbre commence par une voyelle : cet.', 'et'), C('Regarde ___ fleurs !', DEM, 'ces', ['cette', 'ce'], 'Fleurs est pluriel.', 'et')],
  [C('Dans le jardin, ___ arbre centenaire donne de l’ombre.', DEM, 'cet', ['ce', 'cette'], 'Arbre commence par une voyelle : cet.', 'et'), C('Pendant ___ vacances, nous visiterons la Bretagne.', DEM, 'ces', ['cette', 'ce'], 'Vacances est pluriel.', 'et'),
   C('___ histoire m’a beaucoup ému.', DEM, 'Cette', ['Ce', 'Ces'], 'Histoire est féminin singulier.', 'et'), C('Tu as vu ___ immense bateau ?', DEM, 'cet', ['ce', 'cette'], 'Immense commence par une voyelle : cet immense bateau.', 'et')]),
 'Le verbe se conjugue': (
  [K('[Mes cousins] (arrivent) demain.', VB, VBh, 'v'), K('[Le train] (part) à midi.', VB, VBh, 'v'), K('Hier, [nous] (avons mangé) des crêpes.', VB, VBh, 'v'), K('[Tu] (liras) ce livre.', VB, VBh, 'v')],
  [K('Quand la cloche sonne, [les élèves] (se rangent) dans la cour.', VB, VBh, 'v'), K('Demain, [ma sœur] (partira) en voyage avec ses amis.', VB, VBh, 'v'),
   K('Hier soir, [mes parents] (ont regardé) un film.', VB, VBh, 'v'), K('Chaque matin, [le boulanger] (prépare) du pain frais.', VB, VBh, 'v')]),
 'Verbe ou nom ?': (
  [C('Le ___ des oiseaux est joli.', '', 'chant', ['chante'], 'Après « le », c’est un nom.', 'circ'), C('Mon frère ___ sous la douche.', '', 'chante', ['chant'], 'Avec le sujet « mon frère », c’est un verbe.', 'v'),
   C('Léa mange une ___ .', '', 'pêche', ['pêchent'], 'Après « une », c’est un nom.', 'circ'), C('Les enfants ___ dans la cour.', '', 'dansent', ['danse'], 'Le sujet est pluriel : un verbe au pluriel.', 'v')],
  [C('À la plage, nous mangeons une ___ juteuse.', '', 'pêche', ['pêchent'], 'Après « une », c’est un nom.', 'circ'), C('Chaque dimanche, mes oncles ___ au bord de la rivière.', '', 'pêchent', ['pêche'], 'Le sujet est pluriel : un verbe au pluriel.', 'v'),
   C('Le vieux marin ___ une chanson de son pays.', '', 'chante', ['chant'], 'Avec le sujet « le vieux marin », c’est un verbe.', 'v'), C('Le ___ des oiseaux réveille tout le quartier.', '', 'chant', ['chante'], 'Après « le », c’est un nom.', 'circ')]),
 'Le pronom remplace le nom': (
  [C('Ma sœur lit un livre. ___ est contente.', '', 'Elle', ['Il', 'Ils'], 'Ma sœur : une fille, une seule.', 's'), C('Mes amis arrivent. ___ sont en avance.', '', 'Ils', ['Elles', 'Il'], 'Mes amis : plusieurs garçons ou un groupe mixte.', 's'),
   C('Léa et Inès jouent. ___ rient.', '', 'Elles', ['Ils', 'Elle'], 'Deux filles : elles.', 's'), C('Papa cuisine. ___ prépare un gâteau.', '', 'Il', ['Elle', 'Ils'], 'Papa : un homme, un seul.', 's')],
  [C('Les élèves de la classe partent en voyage. ___ sont très impatients.', '', 'Ils', ['Elles', 'Il'], 'Les élèves : plusieurs, masculin ou groupe mixte.', 's'), C('Ma cousine et ma tante habitent à Lyon. ___ viennent nous voir en été.', '', 'Elles', ['Ils', 'Elle'], 'Deux femmes : elles.', 's'),
   C('Le directeur ouvre la porte de l’école. ___ salue chaque enfant.', '', 'Il', ['Elle', 'Ils'], 'Le directeur : un homme, un seul.', 's'), C('Mon frère et moi construisons une cabane. ___ travaillons depuis ce matin.', '', 'Nous', ['Vous', 'Ils'], 'Mon frère et moi : nous.', 's')]),
 'Pronoms sujets et compléments': (
  [C('Je regarde mes amis. Je ___ regarde.', '', 'les', ['le', 'lui'], 'Mes amis : pluriel, complément direct : les.', 'circ'), C('Tom mange une pomme. Tom ___ mange.', '', 'la', ['le', 'les'], 'Une pomme : féminin singulier : la.', 'circ'),
   C('Je téléphone à Léa. Je ___ téléphone.', '', 'lui', ['la', 'leur'], 'À Léa : complément indirect : lui.', 'circ'), C('Nous aidons nos voisins. Nous ___ aidons.', '', 'les', ['leur', 'lui'], 'Nos voisins : pluriel, complément direct : les.', 'circ')],
  [C('Mes parents prêtent leur voiture à mon oncle. Ils ___ prêtent leur voiture.', '', 'lui', ['le', 'leur'], 'À mon oncle : complément indirect, une personne : lui.', 'circ'), C('La maîtresse corrige les cahiers. Elle ___ corrige.', '', 'les', ['le', 'leur'], 'Les cahiers : pluriel, complément direct : les.', 'circ'),
   C('Nous écrivons à nos grands-parents. Nous ___ écrivons.', '', 'leur', ['les', 'lui'], 'À nos grands-parents : complément indirect, pluriel : leur.', 'circ'), C('Mon frère prépare le repas. Il ___ prépare.', '', 'le', ['la', 'lui'], 'Le repas : masculin singulier : le.', 'circ')]),
 'L’adverbe précise': (
  [K('Il parle <doucement>.', AV, AVh), K('Elle marche <vite>.', AV, AVh), K('<Demain>, nous partons.', AV, AVh), K('Il court <rapidement>.', AV, AVh)],
  [K('Le cycliste monte <lentement> la côte.', AV, AVh), K('Mon frère se lève <tôt> chaque matin.', AV, AVh), K('Les enfants sont <très> contents.', AV, AVh), K('Nous irons <bientôt> au bord de la mer.', AV, AVh)]),
 'Des adverbes en -ment': (
  [C('lent → ___', 'Je forme l’adverbe :', 'lentement', ['lentment', 'lente'], 'J’ajoute -ment à l’adjectif au féminin.', 'circ'), C('doux → ___', 'Je forme l’adverbe :', 'doucement', ['douxment', 'douce'], 'doux → douce → doucement.', 'circ'),
   C('joyeux → ___', 'Je forme l’adverbe :', 'joyeusement', ['joyeuxment', 'joyeuse'], 'joyeux → joyeuse → joyeusement.', 'circ'), C('rapide → ___', 'Je forme l’adverbe :', 'rapidement', ['rapideement', 'rapides'], 'J’ajoute -ment à rapide.', 'circ')],
  [C('Le chat marche ___ sur le toit. (silencieux)', 'Je forme l’adverbe :', 'silencieusement', ['silencieuxment', 'silencieusment'], 'silencieux → silencieuse → silencieusement.', 'circ'), C('Ils ont répondu ___ à la question. (poli)', 'Je forme l’adverbe :', 'poliment', ['polimment', 'politement'], 'poli → poliment.', 'circ'),
   C('Elle a travaillé ___ toute la journée. (courageux)', 'Je forme l’adverbe :', 'courageusement', ['courageuxment', 'courageument'], 'courageux → courageuse → courageusement.', 'circ'), C('Nous avançons ___ dans la nuit. (prudent)', 'Je forme l’adverbe :', 'prudemment', ['prudentment', 'prudentement'], 'Les adjectifs en -ent donnent -emment ou -amment : prudent → prudemment.', 'circ')]),
 'Les mots qui relient': (
  [C('Tu veux du pain ___ du fromage ?', '', 'ou', ['mais', 'car'], 'Il propose un choix.', 'circ'), C('J’aime les pommes ___ les poires.', '', 'et', ['car', 'or'], 'Il ajoute.', 'circ'),
   C('Il est petit ___ très fort.', '', 'mais', ['donc', 'ou'], 'Il oppose deux idées.', 'circ'), C('Léa a faim ___ elle mange.', '', 'donc', ['mais', 'ni'], 'Il donne la conséquence.', 'circ')],
  [C('Elle s’est dépêchée ___ elle était en retard.', '', 'car', ['donc', 'mais'], 'Il donne la cause.', 'circ'), C('Il pleuvait fort, ___ nous avons décidé de rester à la maison.', '', 'donc', ['mais', 'car'], 'Il donne la conséquence.', 'circ'),
   C('Mon frère aime le football ___ ma sœur préfère la natation.', '', 'mais', ['donc', 'car'], 'Il oppose deux idées.', 'circ'), C('Veux-tu partir à pied ___ à vélo ?', '', 'ou', ['et', 'car'], 'Il propose un choix.', 'circ')]),
 'Choisir le bon mot': (
  [C('Il fait beau, ___ nous allons au parc.', '', 'donc', ['mais', 'car'], 'Il donne la conséquence.', 'circ'), C('Je suis fatigué ___ j’ai mal dormi.', '', 'car', ['donc', 'ou'], 'Il donne la cause.', 'circ'),
   C('Il a plu ___ nous avons joué dehors.', '', 'mais', ['donc', 'car'], 'Il oppose deux idées.', 'circ'), C('Tu viens avec nous ___ tu restes ici ?', '', 'ou', ['donc', 'mais'], 'Il propose un choix.', 'circ')],
  [C('Le randonneur s’est arrêté ___ ses chaussures lui faisaient mal.', '', 'car', ['donc', 'ou'], 'Il donne la cause.', 'circ'), C('Il avait beaucoup travaillé, ___ il a réussi son examen.', '', 'donc', ['mais', 'car'], 'Il donne la conséquence.', 'circ'),
   C('Nous voulions aller à la plage, ___ la mer était trop agitée.', '', 'mais', ['donc', 'car'], 'Il oppose deux idées.', 'circ'), C('Tu peux choisir un gâteau ___ une glace pour le dessert.', '', 'ou', ['donc', 'mais'], 'Il propose un choix.', 'circ')]),
 'Variable ou invariable ?': (
  [C('', 'Quel mot est invariable ?', 'toujours', ['chanteur', 'grand'], 'Un mot invariable ne change jamais.'), C('', 'Quel mot ne change jamais ?', 'très', ['petite', 'maison'], 'Un mot invariable ne change jamais.'),
   C('', 'Quel mot est invariable ?', 'aujourd’hui', ['travail', 'gentil'], 'Un mot invariable ne change jamais.'), C('', 'Quel mot ne prend jamais de s ?', 'bien', ['fleur', 'joli'], 'Un mot invariable ne change jamais.')],
  [C('', 'Parmi ces mots, lequel est invariable ?', 'pourtant', ['voisin', 'généreux'], 'Il ne change ni en genre ni en nombre.'), C('', 'Quel mot ne s’accorde jamais ?', 'souvent', ['rapide', 'cheval'], 'Il ne change ni en genre ni en nombre.'),
   C('', 'Quelle liste contient seulement des mots invariables ?', 'très, bien, souvent', ['petit, grand, joli', 'maison, jardin, arbre'], 'Les adverbes sont invariables.'), C('', 'Quel mot est invariable ?', 'parfois', ['jolie', 'courageux'], 'Il ne change ni en genre ni en nombre.')]),
 'Les mots invariables': (
  [C('', 'Quel mot ne change jamais ?', 'souvent', ['petit', 'chat'], 'Il ne prend ni e, ni s.'), C('', 'Quel mot ne change jamais ?', 'mais', ['maison', 'joli'], 'Il ne prend ni e, ni s.'),
   C('', 'Quel mot ne change jamais ?', 'bien', ['fleur', 'grand'], 'Il ne prend ni e, ni s.'), C('', 'Quel mot ne change jamais ?', 'trop', ['gros', 'ami'], 'Il ne prend ni e, ni s.')],
  [C('', 'Quel mot reste toujours identique ?', 'toujours', ['voisine', 'curieux'], 'Il ne prend ni e, ni s.'), C('', 'Quel mot reste toujours identique ?', 'cependant', ['généreux', 'travail'], 'Il ne prend ni e, ni s.'),
   C('', 'Quel mot reste toujours identique ?', 'assez', ['étudiante', 'ancien'], 'Il ne prend ni e, ni s.'), C('', 'Quel mot reste toujours identique ?', 'vraiment', ['animal', 'sauvage'], 'Un adverbe est invariable.')]),
}
nouveaux = [
 ('L’adverbe précise', {'sec': 'adv', 'picto': 'mots', 'titre': 'Des adverbes en -ment', 'guide': 'girl', 'bulle': 'Beaucoup d’adverbes se terminent par -ment.',
   'steps': [{'p': 'lent → lente → lente*ment*', 'c': 'J’ajoute -ment à l’adjectif au féminin.'}, {'p': 'doux → douce → douce*ment*'}, {'p': 'joyeux → joyeuse → joyeuse*ment*'}],
   'atoi': C('lent → ___', 'Je forme l’adverbe :', 'lentement', ['lentment', 'lente'], 'J’ajoute -ment à l’adjectif au féminin.', 'circ'),
   'plus': [C('doux → ___', 'Je forme l’adverbe :', 'doucement', ['douxment', 'douce'], 'doux → douce → doucement.', 'circ'), C('joyeux → ___', 'Je forme l’adverbe :', 'joyeusement', ['joyeuxment', 'joyeuse'], 'joyeux → joyeuse → joyeusement.', 'circ')]}),
 ('Variable ou invariable ?', {'sec': 'inv', 'picto': 'liste', 'titre': 'Les mots invariables', 'guide': 'boy', 'bulle': 'Certains mots ne changent jamais : ni e, ni s.',
   'steps': [{'p': 'une fleur → des fleur*s*', 'c': 'Le nom est variable.'}, {'p': 'très · bien · souvent · mais · aujourd’hui', 'c': 'Ces mots ne changent jamais : ils sont invariables.'}],
   'atoi': C('', 'Quel mot ne change jamais ?', 'souvent', ['petit', 'chat'], 'Il ne prend ni e, ni s.'),
   'plus': [C('', 'Quel mot ne change jamais ?', 'mais', ['maison', 'joli'], 'Il ne prend ni e, ni s.'), C('', 'Quel mot ne change jamais ?', 'bien', ['fleur', 'grand'], 'Il ne prend ni e, ni s.')]}),
]
if __name__ == '__main__':
    appliquer('G4', niv, nouveaux)
