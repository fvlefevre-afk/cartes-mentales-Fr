from niveaux_lib import *
GN = 'Clique sur le groupe nominal.'; GNh = 'Cherche un nom avec son déterminant.'
DT = 'Clique sur le déterminant.'; DTh = 'C’est le petit mot devant le nom.'
NN = 'Clique sur le nom noyau.'; NNh = 'Quel mot ne peut-on pas enlever ?'
AD = 'Clique sur l’adjectif.'; ADh = 'Il dit comment est le nom.'
ENL = 'Quel mot ne peut-on pas enlever ?'; ENLh = 'C’est le nom noyau.'
COMP = 'Complète avec l’adjectif qui convient.'
niv = {
 'Des mots autour d’un nom': (
  [K('Les enfants regardent <un vieux film> en noir et blanc.', GN, GNh), K('Mon voisin cultive <de beaux légumes> dans son jardin.', GN, GNh),
   K('Elle porte <une longue écharpe rouge> en hiver.', GN, GNh), K('Tom range <ses petites voitures> dans la boîte.', GN, GNh)],
  [K('Pendant les vacances, nous avons visité <un magnifique château médiéval> au sommet de la colline.', GN, GNh), K('Dans la forêt voisine, <de grands chênes centenaires> abritent de nombreux oiseaux.', GN, GNh),
   K('Ma sœur a offert <un joli bouquet de fleurs sauvages> à notre grand-mère.', GN, GNh), K('Les élèves écoutent attentivement <la longue histoire du vieux marin>.', GN, GNh)]),
 'Le déterminant': (
  [K('<Mes> cousins arrivent demain soir.', DT, DTh), K('Papa lit <le> journal dans le salon.', DT, DTh), K('Nous cueillons <des> pommes mûres.', DT, DTh), K('Elle admire <cette> belle montagne.', DT, DTh)],
  [K('Pendant <les> vacances d’été, nous irons à la mer.', DT, DTh), K('Mon frère a lu <un> livre passionnant sur les volcans.', DT, DTh),
   K('<Ces> vieilles maisons de pierre ont plus de trois siècles.', DT, DTh), K('<Nos> voisins ont repeint toute leur maison en blanc.', DT, DTh)]),
 'Le mot le plus important': (
  [K('Le petit <chat> noir dort près du feu.', NN, NNh), K('Une grande <maison> blanche domine la colline.', NN, NNh), K('Mon vieux <vélo> rouge est tombé en panne.', NN, NNh), K('Les jolies <fleurs> jaunes poussent au bord du chemin.', NN, NNh)],
  [K('Le vieux <château> abandonné domine toute la vallée depuis des siècles.', NN, NNh), K('Ces énormes <rochers> gris barrent le chemin de la montagne.', NN, NNh),
   K('Une délicieuse <odeur> de pain chaud flottait dans toute la cuisine.', NN, NNh), K('Mes deux petits <frères> jumeaux jouent dans le jardin.', NN, NNh)]),
 'Le noyau ne s’enlève pas': (
  [C('un énorme chien noir', ENL, 'chien', ['énorme', 'noir'], ENLh), C('la belle robe rouge', ENL, 'robe', ['belle', 'rouge'], ENLh),
   C('mes vieux livres poussiéreux', ENL, 'livres', ['vieux', 'poussiéreux'], ENLh), C('une petite souris grise', ENL, 'souris', ['petite', 'grise'], ENLh)],
  [C('le grand arbre centenaire du jardin', ENL, 'arbre', ['grand', 'centenaire'], ENLh), C('une magnifique maison blanche au bord de la mer', ENL, 'maison', ['magnifique', 'blanche'], ENLh),
   C('ces vieux livres jaunis par le temps', ENL, 'livres', ['vieux', 'jaunis'], ENLh), C('un petit chat noir aux yeux verts', ENL, 'chat', ['petit', 'noir'], ENLh)]),
 'Il dit comment est le nom': (
  [K('Elle porte une robe <bleue>.', AD, ADh), K('Un <gros> nuage cache le soleil.', AD, ADh), K('Le <vieux> pont de pierre est fragile.', AD, ADh), K('Tom mange une pomme <rouge>.', AD, ADh)],
  [K('Au loin, on aperçoit une <immense> forêt de sapins.', AD, ADh), K('Le chat <affamé> miaule devant sa gamelle vide.', AD, ADh),
   K('Mon grand-père raconte toujours des histoires <extraordinaires>.', AD, ADh), K('Ce <vieux> cheval connaît tous les chemins de la forêt.', AD, ADh)]),
 'J’enrichis le GN': (
  [C('une histoire ___', COMP, 'passionnante', ['rapidement', 'raconter'], 'Cherche un mot qui dit comment est le nom.', 'pr'), C('un ___ chat', COMP, 'mignon', ['doucement', 'dormir'], 'Cherche un mot qui dit comment est le nom.', 'pr'),
   C('des nuages ___', COMP, 'sombres', ['soudain', 'passer'], 'Cherche un mot qui dit comment est le nom.', 'pr'), C('une ___ tempête', COMP, 'violente', ['souvent', 'éclater'], 'Cherche un mot qui dit comment est le nom.', 'pr')],
  [C('Dans le grenier, nous avons découvert un ___ coffre.', COMP, 'ancien', ['souvent', 'ouvrir'], 'Un adjectif dit comment est le nom.', 'pr'), C('Le randonneur gravit un sentier ___ .', COMP, 'escarpé', ['lentement', 'monter'], 'Un adjectif dit comment est le nom.', 'pr'),
   C('Une brise ___ caresse les feuilles des arbres.', COMP, 'légère', ['doucement', 'souffler'], 'Un adjectif dit comment est le nom.', 'pr'), C('Mon oncle conduit une voiture ___ .', COMP, 'rapide', ['vite', 'rouler'], 'Un adjectif dit comment est le nom, pas comment on fait l’action.', 'pr')]),
 'Masculin ou féminin': (
  [C('Ma cousine porte une jupe ___ .', '', 'verte', ['vert', 'verts'], 'Jupe est féminin : j’ajoute un e.', 'pr'), C('Mon frère a un chat ___ .', '', 'noir', ['noire', 'noirs'], 'Chat est masculin singulier.', 'pr'),
   C('La ___ voisine arrive.', '', 'bonne', ['bon', 'bons'], 'Voisine est féminin.', 'pr'), C('Nous admirons une ___ montagne.', '', 'haute', ['haut', 'hauts'], 'Montagne est féminin.', 'pr')],
  [C('Léa a reçu une ___ lettre de son amie.', '', 'longue', ['long', 'longs'], 'Lettre est féminin.', 'pr'), C('Mon oncle est un homme très ___ .', '', 'généreux', ['généreuse', 'généreuxe'], 'Homme est masculin.', 'pr'),
   C('Ma tante est une femme très ___ .', '', 'généreuse', ['généreux', 'généreuxe'], 'Femme est féminin : -x devient -se.', 'pr'), C('La maîtresse a posé une question ___ .', '', 'difficile', ['difficiles', 'difficils'], 'Question est féminin singulier.', 'pr')]),
 'Des féminins qui changent': (
  [C('Elle a une amie ___ .', COMP, 'gentille', ['gentile', 'gentil'], 'gentil → gentille : la consonne se double.', 'pr'), C('C’est une fille ___ .', COMP, 'heureuse', ['heureuxe', 'heureux'], 'heureux → heureuse.', 'pr'),
   C('Cette cliente est très ___ .', COMP, 'fidèle', ['fidel', 'fidèlle'], 'fidèle est déjà féminin.', 'pr'), C('Elle porte une veste ___ .', COMP, 'neuve', ['neufe', 'neuf'], 'neuf → neuve.', 'pr')],
  [C('Ma cousine est une danseuse très ___ .', COMP, 'talentueuse', ['talentueuxe', 'talentueux'], '-eux devient -euse.', 'pr'), C('La reine, ___ et généreuse, était aimée de son peuple.', COMP, 'douce', ['douse', 'doux'], 'doux → douce.', 'pr'),
   C('Ma grand-mère a préparé une soupe ___ .', COMP, 'épaisse', ['épais', 'épaiss'], 'épais → épaisse.', 'pr'), C('Cette boulangère est une femme très ___ .', COMP, 'courageuse', ['courageux', 'courageuxe'], '-eux devient -euse.', 'pr')]),
 'Singulier ou pluriel': (
  [C('Les enfants portent des manteaux ___ .', '', 'chauds', ['chaud', 'chaude'], 'Manteaux est pluriel masculin.', 'pr'), C('Nous avons planté de ___ arbres.', '', 'petits', ['petit', 'petite'], 'Arbres est pluriel masculin.', 'pr'),
   C('Les ___ oiseaux chantent.', '', 'jolis', ['joli', 'jolie'], 'Oiseaux est pluriel.', 'pr'), C('J’aime les histoires ___ .', '', 'drôles', ['drôle', 'drôl'], 'Histoires est pluriel.', 'pr')],
  [C('Dans la cour, les ___ élèves jouent aux billes avec leurs camarades.', '', 'petits', ['petit', 'petite'], 'Élèves est pluriel.', 'pr'), C('Les nuages ___ annoncent un orage violent pour ce soir.', '', 'noirs', ['noir', 'noire'], 'Nuages est pluriel masculin.', 'pr'),
   C('Ces ___ maisons de pierre ont plus de trois siècles.', '', 'vieilles', ['vieille', 'vieux'], 'Maisons est féminin pluriel.', 'pr'), C('Mes parents ont acheté des meubles ___ pour la cuisine.', '', 'neufs', ['neuf', 'neuve'], 'Meubles est pluriel masculin.', 'pr')]),
 'Je vérifie les accords': (
  [C('', 'Quel GN est bien accordé ?', 'les petites filles', ['les petit filles', 'les petites fille'], 'Chaque mot s’accorde avec le nom noyau.'), C('', 'Quel GN est bien accordé ?', 'des fleurs jaunes', ['des fleur jaunes', 'des fleurs jaune'], 'Chaque mot s’accorde avec le nom noyau.'),
   C('', 'Quel GN est bien accordé ?', 'mes vieux livres', ['mes vieux livre', 'mes vieille livres'], 'Chaque mot s’accorde avec le nom noyau.'), C('', 'Quel GN est bien accordé ?', 'une grande maison', ['un grande maison', 'une grand maison'], 'Chaque mot s’accorde avec le nom noyau.')],
  [C('', 'Quel GN est bien accordé ?', 'ces vieilles maisons grises', ['ces vieille maisons grises', 'ces vieilles maison grises'], 'Je cherche le nom noyau, puis je vérifie chaque mot.'),
   C('', 'Quel GN est bien accordé ?', 'les nombreux oiseaux migrateurs', ['les nombreux oiseaux migrateur', 'les nombreuse oiseaux migrateurs'], 'Je cherche le nom noyau, puis je vérifie chaque mot.'),
   C('', 'Quel GN est bien accordé ?', 'une longue route sinueuse', ['une long route sinueuse', 'une longue route sinueux'], 'Je cherche le nom noyau, puis je vérifie chaque mot.'),
   C('', 'Quel GN est bien accordé ?', 'mes deux petites sœurs jumelles', ['mes deux petite sœurs jumelles', 'mes deux petites sœurs jumeaux'], 'Je cherche le nom noyau, puis je vérifie chaque mot.')]),
 'Des pluriels en x': (
  [C('Les enfants construisent des ___ en sable.', '', 'châteaux', ['châteaus', 'château'], 'Les mots en -eau prennent un x au pluriel.', 'circ'), C('Les ___ s’envolent dans le ciel.', '', 'oiseaux', ['oiseaus', 'oiseau'], 'Les mots en -eau prennent un x au pluriel.', 'circ'),
   C('Elle a de longs ___ blonds.', '', 'cheveux', ['cheveus', 'cheveu'], 'Les mots en -eu prennent un x au pluriel.', 'circ'), C('Nous jouons à des ___ de société.', '', 'jeux', ['jeus', 'jeu'], 'Les mots en -eu prennent un x au pluriel.', 'circ')],
  [C('Dans les vitrines, de nombreux ___ attirent les passants.', '', 'manteaux', ['manteaus', 'manteau'], 'Les mots en -eau prennent un x au pluriel.', 'circ'), C('Pour son anniversaire, elle a reçu de très beaux ___ .', '', 'cadeaux', ['cadeaus', 'cadeau'], 'Les mots en -eau prennent un x au pluriel.', 'circ'),
   C('Les ___ de la ferme dorment dans la grange.', '', 'agneaux', ['agneaus', 'agneau'], 'Les mots en -eau prennent un x au pluriel.', 'circ'), C('Les ___ du peintre sont exposés dans la galerie.', '', 'tableaux', ['tableaus', 'tableau'], 'Les mots en -eau prennent un x au pluriel.', 'circ')]),
 'Des pluriels en -aux': (
  [C('Les ___ broutent dans le pré.', '', 'chevaux', ['chevals', 'chevauxs'], '-al devient -aux.', 'circ'), C('Les ___ du zoo mangent à midi.', '', 'animaux', ['animals', 'animauxs'], '-al devient -aux.', 'circ'),
   C('Mon père lit les ___ chaque matin.', '', 'journaux', ['journals', 'journauxs'], '-al devient -aux.', 'circ'), C('Les ___ de l’usine sont terminés.', '', 'travaux', ['travails', 'travauxs'], '-ail devient -aux pour ce mot.', 'circ')],
  [C('Dans cette ville, il y a trois ___ .', '', 'hôpitaux', ['hôpitals', 'hôpitaus'], '-al devient -aux.', 'circ'), C('Les ___ de Venise sont célèbres dans le monde entier.', '', 'canaux', ['canals', 'canaus'], '-al devient -aux.', 'circ'),
   C('Les ___ du roi traversent la plaine au galop.', '', 'chevaux', ['chevals', 'chevauxs'], '-al devient -aux.', 'circ'), C('Les ___ de la ferme paissent dans le grand pré.', '', 'animaux', ['animals', 'animauxs'], '-al devient -aux.', 'circ')]),
 'Des mots qui ne changent pas': (
  [C('Les ___ grises courent dans le grenier.', '', 'souris', ['souriss', 'sourix'], 'Souris finit déjà par s.', 'circ'), C('Les clowns ont des ___ rouges.', '', 'nez', ['nezs', 'nezx'], 'Nez finit déjà par z.', 'circ'),
   C('Nous écoutons des ___ douces.', '', 'voix', ['voixs', 'voie'], 'Voix finit déjà par x.', 'circ'), C('Les acrobates agitent leurs ___ .', '', 'bras', ['brass', 'brax'], 'Bras finit déjà par s.', 'circ')],
  [C('Dans la forêt, on entend des ___ lointaines.', '', 'voix', ['voixs', 'voie'], 'Voix finit déjà par x.', 'circ'), C('Ces ___ ont mangé tout le fromage de la cuisine.', '', 'souris', ['souriss', 'sourix'], 'Souris finit déjà par s.', 'circ'),
   C('Les jumeaux ont des ___ identiques.', '', 'nez', ['nezs', 'nezx'], 'Nez finit déjà par z.', 'circ'), C('Pendant le concert, plusieurs ___ ont chanté en même temps.', '', 'voix', ['voixs', 'voies'], 'Voix finit déjà par x.', 'circ')]),
}
if __name__ == '__main__':
    appliquer('G3', niv)
