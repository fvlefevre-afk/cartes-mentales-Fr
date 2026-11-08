from niveaux_lib import *
CO = 'Clique sur le complément d’objet.'; COh = 'Il répond à « quoi ? » ou « à qui ? ».'
QO = 'Quel est le complément d’objet ?'
def cod(p, cmp_, mal, ask=QO): return C(p, ask, cmp_, mal, 'Il est collé au verbe : on ne peut ni le supprimer ni le déplacer.')
def cc(p, g, bon, mal): return C(p, f'« {g} » répond à la question…', bon, mal, 'Où ? Quand ? Comment ?')
def supp(p, bon, mal, ask='Quel groupe peut-on supprimer ?'): return C(p, ask, bon, mal, 'Un complément circonstanciel peut être supprimé.')
def depl(p, bon, mal): return C(p, 'Quelle phrase déplace bien le complément ?', bon, mal, 'Le complément circonstanciel peut changer de place.')
def coi(p, g, bon, mal): return C(p, f'« {g} » est…', bon, mal, 'Avec un petit mot (à, de…) entre le verbe et le complément : COI. Sans petit mot : COD.')
def virg(bon, mal): return C('', 'Quelle phrase est bien écrite ?', bon, mal, 'En début de phrase, le complément circonstanciel est suivi d’une virgule.')
def nb(p, n, mal): return C(p, 'Combien de compléments circonstanciels ?', n, mal, 'Je cherche les groupes qui disent où, quand ou comment.')
niv = {
 'Plus que sujet + verbe': (
  [SV('Ce soir, [ma sœur] (prépare) un gâteau dans la cuisine.'), SV('Dans le jardin, [les enfants] (jouent) au ballon.'), SV('Hier, [Léa] (a cueilli) des fleurs au bord du chemin.'), SV('Chaque matin, [le facteur] (distribue) le courrier dans le village.')],
  [SV('Après la classe, [les élèves de CM2] (rangent) soigneusement leurs affaires dans leur cartable.'), SV('Dans la forêt voisine, [un vieux bûcheron] (coupe) du bois depuis l’aube.'),
   SV('Pendant les vacances d’été, [ma famille] (visite) des châteaux au bord de la Loire.'), SV('Le soir, [mon grand-père] (raconte) de merveilleuses histoires à ses petits-enfants.')]),
 'Ce qui s’ajoute au sujet et au verbe': (
  [C('Le soir, Tom lit un livre.', 'Quels groupes ne sont ni le sujet ni le verbe ?', 'Le soir, un livre', ['Tom, lit', 'Tom, un livre'], 'Je trouve d’abord le sujet et le verbe : ce qui reste, ce sont les compléments.'),
   C('Ma sœur range sa chambre le samedi.', 'Quels groupes ne sont ni le sujet ni le verbe ?', 'sa chambre, le samedi', ['Ma sœur, range', 'Ma sœur, sa chambre'], 'Je trouve d’abord le sujet et le verbe.'),
   C('Dans la cour, les enfants jouent aux billes.', 'Quels groupes ne sont ni le sujet ni le verbe ?', 'Dans la cour, aux billes', ['les enfants, jouent', 'les enfants, aux billes'], 'Je trouve d’abord le sujet et le verbe.'),
   C('Demain, Papa répare le vélo.', 'Quels groupes ne sont ni le sujet ni le verbe ?', 'Demain, le vélo', ['Papa, répare', 'Papa, le vélo'], 'Je trouve d’abord le sujet et le verbe.')],
  [C('Hier soir, mes cousins ont mangé une pizza chez nous.', 'Quels groupes ne sont ni le sujet ni le verbe ?', 'Hier soir, une pizza, chez nous', ['mes cousins, ont mangé', 'mes cousins, une pizza'], 'Je trouve le sujet et le verbe : ce qui reste, ce sont les compléments.'),
   C('Chaque matin, la boulangère prépare du pain frais dans son fournil.', 'Quels groupes ne sont ni le sujet ni le verbe ?', 'Chaque matin, du pain frais, dans son fournil', ['la boulangère, prépare', 'la boulangère, du pain frais'], 'Je trouve le sujet et le verbe.'),
   C('Pendant les vacances, ma famille visite des châteaux avec un guide.', 'Quels groupes ne sont ni le sujet ni le verbe ?', 'Pendant les vacances, des châteaux, avec un guide', ['ma famille, visite', 'ma famille, des châteaux'], 'Je trouve le sujet et le verbe.'),
   C('Le dimanche, mon grand-père lit son journal dans le jardin.', 'Quels groupes ne sont ni le sujet ni le verbe ?', 'Le dimanche, son journal, dans le jardin', ['mon grand-père, lit', 'mon grand-père, son journal'], 'Je trouve le sujet et le verbe.')]),
 'Le complément d’objet': (
  [K('Mon frère prépare <le repas> ce soir.', CO, COh), K('Tom écrit <à sa grand-mère> chaque semaine.', CO, COh), K('Les élèves écoutent <la maîtresse> avec attention.', CO, COh), K('Léa cherche <ses lunettes> partout.', CO, COh)],
  [K('Dans la cuisine, ma tante prépare <un délicieux gâteau au chocolat> pour la fête.', CO, COh), K('Hier soir, mon père a téléphoné <à son vieil ami> pendant une heure.', CO, COh),
   K('Les randonneurs ont admiré <le magnifique paysage de montagne> depuis le sommet.', CO, COh), K('Chaque été, nous rendons visite <à nos grands-parents> dans le Midi.', CO, COh)]),
 'Il est collé au verbe': (
  [cod('Papa répare le vélo ce matin.', 'le vélo', ['ce matin', 'Papa']), cod('Les élèves lisent un conte en classe.', 'un conte', ['en classe', 'Les élèves']),
   cod('Ma sœur range sa chambre le samedi.', 'sa chambre', ['le samedi', 'Ma sœur']), cod('Le chat attrape une souris dans le jardin.', 'une souris', ['dans le jardin', 'Le chat'])],
  [cod('Pendant les vacances, ma tante a préparé un énorme gâteau aux fraises.', 'un énorme gâteau aux fraises', ['Pendant les vacances', 'ma tante']), cod('Au bord de la rivière, le pêcheur surveille patiemment sa ligne.', 'sa ligne', ['Au bord de la rivière', 'patiemment']),
   cod('Chaque matin, le boulanger vend du pain frais à ses clients.', 'du pain frais', ['Chaque matin', 'à ses clients']), cod('Avant la sortie, les élèves rangent soigneusement leurs affaires.', 'leurs affaires', ['Avant la sortie', 'soigneusement'])]),
 'COD ou COI ?': (
  [coi('Léa téléphone à sa cousine.', 'à sa cousine', 'un COI', ['un COD']), coi('Tom range ses affaires.', 'ses affaires', 'un COD', ['un COI']),
   coi('Nous parlons à la maîtresse.', 'à la maîtresse', 'un COI', ['un COD']), coi('Papa lit le journal.', 'le journal', 'un COD', ['un COI'])],
  [coi('Ma tante écrit une longue lettre à son amie d’enfance.', 'une longue lettre', 'un COD', ['un COI']), coi('Mon frère pense à ses prochaines vacances au bord de la mer.', 'à ses prochaines vacances', 'un COI', ['un COD']),
   coi('La maîtresse distribue les cahiers corrigés aux élèves.', 'les cahiers corrigés', 'un COD', ['un COI']), coi('Les voisins s’intéressent à l’histoire de notre village.', 'à l’histoire de notre village', 'un COI', ['un COD'])]),
 'Où ? Quand ? Comment ?': (
  [cc('Le train arrive à midi.', 'à midi', 'quand ?', ['où ?', 'comment ?']), cc('Elle chante avec joie.', 'avec joie', 'comment ?', ['où ?', 'quand ?']),
   cc('Nous mangeons au restaurant.', 'au restaurant', 'où ?', ['quand ?', 'comment ?']), cc('Il parle à voix basse.', 'à voix basse', 'comment ?', ['où ?', 'quand ?'])],
  [cc('Pendant les vacances, nous irons à la montagne.', 'Pendant les vacances', 'quand ?', ['où ?', 'comment ?']), cc('Les randonneurs avancent lentement sur le sentier escarpé.', 'lentement', 'comment ?', ['où ?', 'quand ?']),
   cc('Mon grand-père cultive des tomates derrière sa maison.', 'derrière sa maison', 'où ?', ['quand ?', 'comment ?']), cc('Elle a répondu à la question avec beaucoup de calme.', 'avec beaucoup de calme', 'comment ?', ['où ?', 'quand ?'])]),
 'Je supprime': (
  [supp('Les enfants jouent dans la cour.', 'dans la cour', ['Les enfants', 'jouent']), supp('Le facteur arrive demain.', 'demain', ['Le facteur', 'arrive']),
   supp('Le chat dort sous la table ce matin.', 'sous la table', ['Le chat', 'dort']), supp('Ma sœur chante dans la salle de bains.', 'dans la salle de bains', ['Ma sœur', 'chante'])],
  [supp('Pendant les vacances, ma sœur a lu trois romans.', 'Pendant les vacances', ['trois romans', 'ma sœur']), supp('Mon frère répare son vélo dans le garage depuis ce matin.', 'dans le garage', ['son vélo', 'Mon frère']),
   supp('Le soir, le vieux marin raconte une histoire aux enfants.', 'Le soir', ['une histoire', 'le vieux marin']), supp('Les élèves ont visité le musée avec leur maîtresse.', 'avec leur maîtresse', ['le musée', 'Les élèves'])]),
 'Je déplace': (
  [depl('Léa lit au jardin.', 'Au jardin, Léa lit.', ['Léa au jardin lit.', 'Lit Léa au jardin.']), depl('Le train part à midi.', 'À midi, le train part.', ['Le train à midi part.', 'Part le train à midi.']),
   depl('Nous jouons dans la cour.', 'Dans la cour, nous jouons.', ['Nous dans la cour jouons.', 'Jouons nous dans la cour.']), depl('Tom range sa chambre le soir.', 'Le soir, Tom range sa chambre.', ['Tom le soir range sa chambre.', 'Sa chambre, Tom range le soir.'])],
  [depl('Les élèves rangent leurs affaires avant la sortie.', 'Avant la sortie, les élèves rangent leurs affaires.', ['Leurs affaires, les élèves rangent avant la sortie.', 'Rangent les élèves leurs affaires avant la sortie.']),
   depl('Mon grand-père cultive des tomates derrière sa maison.', 'Derrière sa maison, mon grand-père cultive des tomates.', ['Des tomates, mon grand-père cultive derrière sa maison.', 'Mon grand-père derrière sa maison cultive des tomates.']),
   depl('Ma tante prépare un gâteau pour la fête de demain.', 'Pour la fête de demain, ma tante prépare un gâteau.', ['Un gâteau, ma tante prépare pour la fête de demain.', 'Ma tante pour la fête de demain prépare un gâteau.']),
   depl('Les randonneurs atteignent le sommet avant la nuit.', 'Avant la nuit, les randonneurs atteignent le sommet.', ['Le sommet, les randonneurs atteignent avant la nuit.', 'Atteignent les randonneurs le sommet avant la nuit.'])]),
 'Complément d’objet ou circonstanciel ?': (
  [cod('Tom mange une pomme dans la cuisine.', 'une pomme', ['dans la cuisine']), cod('Le soir, Léa lit un conte.', 'un conte', ['Le soir']),
   cod('Ma sœur prépare un gâteau pour demain.', 'un gâteau', ['pour demain']), cod('Dans le jardin, Papa plante un arbre.', 'un arbre', ['Dans le jardin'])],
  [cod('Chaque dimanche, mon grand-père lit son journal dans le jardin.', 'son journal', ['Chaque dimanche', 'dans le jardin']), cod('Hier, au marché, ma mère a acheté des fruits frais.', 'des fruits frais', ['Hier', 'au marché']),
   cod('Pendant la récréation, les élèves jouent aux billes dans la cour.', 'aux billes', ['Pendant la récréation', 'dans la cour']), cod('Le soir, la voisine arrose ses fleurs avec un petit arrosoir.', 'ses fleurs', ['Le soir', 'avec un petit arrosoir'])]),
 'La virgule': (
  [virg('Demain matin, nous partirons.', ['Demain matin nous, partirons.', 'Demain, matin nous partirons.']), virg('Dans le jardin, les enfants jouent.', ['Dans le jardin les enfants, jouent.', 'Dans, le jardin les enfants jouent.']),
   virg('Le soir, Papa lit le journal.', ['Le soir Papa, lit le journal.', 'Le, soir Papa lit le journal.']), virg('Hier matin, il a plu.', ['Hier, matin il a plu.', 'Hier matin il, a plu.'])],
  [virg('Pendant les vacances d’été, nous irons chez nos cousins.', ['Pendant les vacances, d’été nous irons chez nos cousins.', 'Pendant les vacances d’été nous irons, chez nos cousins.']), virg('Au bord de la rivière, le pêcheur surveille sa ligne.', ['Au bord de la rivière le pêcheur, surveille sa ligne.', 'Au bord, de la rivière le pêcheur surveille sa ligne.']),
   virg('Chaque soir après le dîner, ma mère lit une histoire.', ['Chaque soir, après le dîner ma mère lit une histoire.', 'Chaque soir après le dîner ma mère, lit une histoire.']), virg('Dans la forêt voisine, un bûcheron coupe du bois.', ['Dans la forêt voisine un bûcheron, coupe du bois.', 'Dans la forêt, voisine un bûcheron coupe du bois.'])]),
 'Plusieurs compléments': (
  [nb('Hier soir, Tom a joué dans le jardin.', '2', ['1', '3']), nb('Le chat dort sur le canapé.', '1', ['2', '0']), nb('Ce matin, nous sommes partis à l’école avec nos amis.', '3', ['2', '1']), nb('Léa mange une pomme.', '0', ['1', '2'])],
  [nb('Chaque soir, après le dîner, mon père lit dans le salon.', '3', ['2', '1']), nb('Hier, au marché, ma mère a acheté des fruits frais.', '2', ['1', '3']), nb('Pendant les vacances, nous irons en Bretagne avec nos cousins.', '3', ['2', '1']), nb('Marie lit un livre.', '0', ['1', '2'])]),
}
nouveaux = [
 ('Plus que sujet + verbe', {'sec': 'phrase', 'picto': 'loupe', 'titre': 'Ce qui s’ajoute au sujet et au verbe', 'guide': 'boy', 'bulle': 'Je trouve d’abord le sujet et le verbe : ce qui reste, ce sont les compléments.',
   'steps': [{'p': 'Le soir, Tom lit un livre dans son lit.'}, {'p': 'Le soir, [Tom] (lit) un livre dans son lit.', 'c': '1. Je trouve le sujet et le verbe.'}, {'p': 'Le soir, [Tom] (lit) ^un livre^ ^dans son lit^.', 'c': '2. Ce qui reste, ce sont les compléments.'}],
   'atoi': C('Le soir, Tom lit un livre.', 'Quels groupes ne sont ni le sujet ni le verbe ?', 'Le soir, un livre', ['Tom, lit', 'Tom, un livre'], 'Je trouve d’abord le sujet et le verbe : ce qui reste, ce sont les compléments.'),
   'plus': [C('Ma sœur range sa chambre le samedi.', 'Quels groupes ne sont ni le sujet ni le verbe ?', 'sa chambre, le samedi', ['Ma sœur, range', 'Ma sœur, sa chambre'], 'Je trouve d’abord le sujet et le verbe.'),
            C('Demain, Papa répare le vélo.', 'Quels groupes ne sont ni le sujet ni le verbe ?', 'Demain, le vélo', ['Papa, répare', 'Papa, le vélo'], 'Je trouve d’abord le sujet et le verbe.')]}),
]
if __name__ == '__main__':
    appliquer('G6', niv, nouveaux)
