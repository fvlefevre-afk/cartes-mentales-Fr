from niveaux_lib import *
def adj(p, bon, mal): return C(p, '', bon, mal, 'Le nom noyau commande : l’adjectif s’accorde avec lui.', 'pr')
def vb(p, bon, mal, hint): return C(p, '', bon, mal, hint, 'v')
def phr(bon, mal, ask='Quelle phrase est bien accordée ?'): return C('', ask, bon, mal, 'Je trouve le nom noyau du sujet, puis je vérifie chaque mot.')
def corr(p, bon, mal): return C(p, 'Quelle est la bonne correction ?', bon, mal, 'Je trouve le nom noyau, puis je vérifie chaque mot.')
PE = 'Avec être, le participe passé s’accorde avec le sujet.'; PA = 'Avec avoir, le participe passé ne s’accorde pas avec le sujet.'
niv = {
 'Le nom noyau commande': (
  [adj('des ___ fleurs', 'belles', ['belle', 'beaux']), adj('une ___ histoire', 'longue', ['long', 'longs']), adj('des maisons ___', 'blanches', ['blanche', 'blancs']), adj('un ___ chat', 'petit', ['petite', 'petits'])],
  [adj('Dans la vallée, de ___ montagnes se dressent.', 'hautes', ['haute', 'hauts']), adj('Les ___ arbres du parc donnent de l’ombre.', 'vieux', ['vieille', 'vieilles']),
   adj('Elle a reçu de ___ nouvelles de son amie.', 'bonnes', ['bon', 'bonne']), adj('Nous admirons ces ___ statues de marbre blanc.', 'anciennes', ['ancien', 'anciens'])]),
 'Deux adjectifs, un seul noyau': (
  [adj('une ___ maison blanche', 'grande', ['grand', 'grands']), adj('des chats noirs et ___', 'blancs', ['blanc', 'blanche']), adj('un garçon gentil et ___', 'poli', ['polie', 'polis']), adj('des filles ___ et rapides', 'fortes', ['fort', 'forte'])],
  [adj('La cuisine est pleine de ___ odeurs sucrées.', 'bonnes', ['bon', 'bons']), adj('Mes cousines sont grandes, blondes et ___ .', 'souriantes', ['souriante', 'souriants']), adj('Ce vieux château est grand, froid et ___ .', 'sombre', ['sombres', 'sombrent']),
   adj('Les rues sont étroites et ___ .', 'sinueuses', ['sinueux', 'sinueuse'])]),
 'Le sujet commande le verbe': (
  [vb('Les chiens du voisin ___ la nuit.', 'aboient', ['aboie', 'aboies'], 'Le sujet est « les chiens » : pluriel.'), vb('Mes cousines ___ en vacances.', 'partent', ['part', 'pars'], 'Mes cousines = elles.'),
   vb('Le frère de mes amis ___ loin.', 'habite', ['habitent', 'habites'], 'Le sujet est « le frère » : singulier.'), vb('Les fleurs du jardin ___ vite.', 'poussent', ['pousse', 'pousses'], 'Le sujet est « les fleurs » : pluriel.')],
  [vb('Les enfants de la voisine ___ chaque mercredi à la piscine.', 'vont', ['va', 'vas'], 'Le sujet est « les enfants » : pluriel.'), vb('Le facteur du village ___ le courrier avant midi.', 'distribue', ['distribuent', 'distribues'], 'Le sujet est « le facteur » : singulier.'),
   vb('Mes deux sœurs ___ souvent au bord de la mer.', 'jouent', ['joue', 'joues'], 'Le sujet est « mes deux sœurs » : pluriel.'), vb('La voisine de mes grands-parents ___ des fleurs.', 'cultive', ['cultivent', 'cultives'], 'Le sujet est « la voisine » : singulier.')]),
 'Le groupe sujet s’accorde': (
  [vb('Le chat et le chien ___ ensemble.', 'jouent', ['joue', 'jouons'], 'Deux sujets reliés par « et » : ils.'), vb('Ma sœur et moi ___ au parc.', 'allons', ['allez', 'vont'], 'Ma sœur et moi = nous.'),
   vb('Tom et Léa ___ contents.', 'sont', ['est', 'es'], 'Tom et Léa = ils.'), vb('Toi et lui ___ en retard.', 'êtes', ['est', 'sont'], 'Toi et lui = vous.')],
  [vb('Mon père et ma mère ___ toujours à l’heure pour le dîner.', 'sont', ['est', 'es'], 'Plusieurs sujets : ils.'), vb('Les élèves de la classe et leur maîtresse ___ partis en sortie.', 'sont', ['est', 'es'], 'Plusieurs sujets : ils.'),
   vb('Ma cousine et moi ___ la même passion pour la musique.', 'avons', ['ont', 'avez'], 'Ma cousine et moi = nous.'), vb('Toi et tes amis ___ invités à la fête.', 'êtes', ['sont', 'est'], 'Toi et tes amis = vous.')]),
 'Avec être, le participe s’accorde': (
  [vb('Tom est ___ tôt.', 'arrivé', ['arrivée', 'arrivés'], PE), vb('Mes cousines sont ___ hier soir.', 'arrivées', ['arrivé', 'arrivés'], PE),
   vb('Léa est ___ à l’école.', 'allée', ['allé', 'allés'], PE), vb('Mes amis sont ___ hier.', 'venus', ['venu', 'venues'], PE)],
  [vb('Les enfants de la voisine sont ___ très tôt ce matin.', 'partis', ['parti', 'partie'], PE), vb('Ma grand-mère est ___ de l’hôpital hier soir.', 'sortie', ['sorti', 'sortis'], PE),
   vb('Nos voisines sont ___ au marché ce matin.', 'allées', ['allés', 'allée'], PE), vb('Le facteur est ___ pendant la tempête.', 'passé', ['passée', 'passés'], PE)]),
 'Comme un adjectif': (
  [vb('Les fleurs sont ___ .', 'fanées', ['fané', 'fanés'], 'Le participe s’accorde comme un adjectif.'), vb('La porte est ___ .', 'fermée', ['fermé', 'fermés'], 'Le participe s’accorde comme un adjectif.'),
   vb('Les fenêtres sont ___ .', 'ouvertes', ['ouvert', 'ouverte'], 'Le participe s’accorde comme un adjectif.'), vb('Mes amies sont ___ trop tard.', 'arrivées', ['arrivé', 'arrivés'], 'Le participe s’accorde comme un adjectif.')],
  [vb('Dans la cour, les feuilles mortes sont ___ par le vent.', 'emportées', ['emporté', 'emportés'], 'Le participe s’accorde comme un adjectif.'), vb('La maison est ___ depuis dix ans.', 'abandonnée', ['abandonné', 'abandonnés'], 'Le participe s’accorde comme un adjectif.'),
   vb('Les deux frères sont ___ à la gare.', 'descendus', ['descendu', 'descendues'], 'Le participe s’accorde comme un adjectif.'), vb('Ma tante est ___ en Italie pour les vacances.', 'restée', ['resté', 'restés'], 'Le participe s’accorde comme un adjectif.')]),
 'Avec avoir, c’est différent': (
  [vb('Léa a ___ un gâteau.', 'préparé', ['préparée', 'préparés'], PA), vb('Mes amis ont ___ un film.', 'regardé', ['regardés', 'regardées'], PA),
   vb('Nous avons ___ une chanson.', 'chanté', ['chantés', 'chantées'], PA), vb('Les filles ont ___ leurs devoirs.', 'fini', ['finies', 'finis'], PA)],
  [vb('Hier soir, mes cousines ont ___ une longue promenade.', 'fait', ['faites', 'faits'], PA), vb('Les élèves ont ___ la leçon avec beaucoup d’attention.', 'écouté', ['écoutés', 'écoutées'], PA),
   vb('Ma sœur et moi avons ___ toute la soirée devant la télévision.', 'passé', ['passées', 'passés'], PA), vb('Les voisines ont ___ leurs fleurs au printemps.', 'planté', ['plantées', 'plantés'], PA)]),
 'Toute la chaîne': (
  [phr('Mes petites sœurs sont arrivées.', ['Mes petite sœurs sont arrivées.', 'Mes petites sœurs est arrivées.']), phr('Les vieilles maisons sont tombées.', ['Les vieille maisons sont tombées.', 'Les vieilles maisons sont tombé.']),
   phr('La grande fille est partie.', ['La grand fille est partie.', 'La grande fille est parti.']), phr('Les petits chats sont rentrés.', ['Les petits chats est rentrés.', 'Les petit chats sont rentré.'])],
  [phr('Les deux jeunes voisines de ma cousine sont arrivées hier.', ['Les deux jeunes voisine de ma cousine sont arrivées hier.', 'Les deux jeunes voisines de ma cousine est arrivées hier.']),
   phr('Mes vieux amis du village sont venus me voir.', ['Mes vieux amis du village est venus me voir.', 'Mes vieux amis du village sont venu me voir.']),
   phr('Les petites filles de la voisine sont allées au parc.', ['Les petites filles de la voisine sont allé au parc.', 'Les petite filles de la voisine sont allées au parc.']),
   phr('Ma grande sœur et sa meilleure amie sont parties ensemble.', ['Ma grande sœur et sa meilleure amie est partie ensemble.', 'Ma grande sœur et sa meilleure amie sont partis ensemble.'])]),
 'Je change le sujet': (
  [C('Le chat est rentré. → Les chats ___ rentrés.', '', 'sont', ['est', 'es'], 'Si le sujet change, toute la chaîne change.', 'v'), C('La fille est venue. → Les filles sont ___ .', '', 'venues', ['venue', 'venus'], 'Les filles : féminin pluriel.', 'v'),
   C('Le garçon est tombé. → Les garçons sont ___ .', '', 'tombés', ['tombé', 'tombées'], 'Les garçons : masculin pluriel.', 'v'), C('La voisine est arrivée. → Les voisines ___ arrivées.', '', 'sont', ['est', 'es'], 'Les voisines : pluriel.', 'v')],
  [C('Le petit garçon est parti hier. → Les petits garçons ___ partis hier.', '', 'sont', ['est', 'es'], 'Si le sujet change, toute la chaîne change.', 'v'), C('Ma cousine est restée à la maison. → Mes cousines sont ___ à la maison.', '', 'restées', ['restée', 'restés'], 'Mes cousines : féminin pluriel.', 'v'),
   C('Le vieux chat est rentré tard. → Les vieux chats sont ___ tard.', '', 'rentrés', ['rentré', 'rentrées'], 'Les vieux chats : masculin pluriel.', 'v'), C('La grande fenêtre est restée ouverte. → Les grandes fenêtres ___ restées ouvertes.', '', 'sont', ['est', 'es'], 'Les grandes fenêtres : pluriel.', 'v')]),
 'Je vérifie une phrase': (
  [corr('Les petit chat est rentré.', 'Les petits chats sont rentrés.', ['Les petits chats est rentrés.', 'Les petit chats sont rentré.']), corr('La grand fille sont arrivé.', 'La grande fille est arrivée.', ['La grande fille sont arrivée.', 'La grand fille est arrivé.']),
   corr('Mes ami sont venu.', 'Mes amis sont venus.', ['Mes amis est venus.', 'Mes ami sont venus.']), corr('Les fleur est tombé.', 'Les fleurs sont tombées.', ['Les fleurs est tombées.', 'Les fleur sont tombées.'])],
  [corr('Mes deux petit cousine est parti hier.', 'Mes deux petites cousines sont parties hier.', ['Mes deux petites cousines est parties hier.', 'Mes deux petit cousines sont partis hier.']), corr('La vieille voisine et son chat est sorti.', 'La vieille voisine et son chat sont sortis.', ['La vieille voisine et son chat est sortie.', 'La vieille voisine et son chat sont sortie.']),
   corr('Les grand arbre du parc est tombé.', 'Les grands arbres du parc sont tombés.', ['Les grands arbres du parc est tombés.', 'Les grand arbres du parc sont tombé.']), corr('Mes cousines sont arrivé hier soir.', 'Mes cousines sont arrivées hier soir.', ['Mes cousines est arrivées hier soir.', 'Mes cousine sont arrivées hier soir.'])]),
 'Je me corrige': (
  [corr('Les élèves joue dans la cour.', 'Les élèves jouent dans la cour.', ['Les élèves jouons dans la cour.', 'Les élève jouent dans la cour.']), corr('Ma sœur est parti.', 'Ma sœur est partie.', ['Ma sœur est partis.', 'Ma sœur sont partie.']),
   corr('Mes amis ont arrivé.', 'Mes amis sont arrivés.', ['Mes amis sont arrivé.', 'Mes amis ont arrivés.']), corr('Les belle fleurs poussent.', 'Les belles fleurs poussent.', ['Les belles fleur poussent.', 'Les belle fleurs pousse.'])],
  [corr('Les enfants de la voisine joue dehors.', 'Les enfants de la voisine jouent dehors.', ['Les enfants de la voisine jouons dehors.', 'Les enfant de la voisine jouent dehors.']), corr('Mes cousines sont parti hier soir.', 'Mes cousines sont parties hier soir.', ['Mes cousines sont partis hier soir.', 'Mes cousines est parties hier soir.']),
   corr('Les petite filles ont mangées une glace.', 'Les petites filles ont mangé une glace.', ['Les petites filles ont mangées une glace.', 'Les petite filles ont mangé une glace.']), corr('Toi et ton frère sont en retard.', 'Toi et ton frère êtes en retard.', ['Toi et ton frère est en retard.', 'Toi et ton frère sommes en retard.'])]),
}
def n(sec, picto, titre, guide, bulle, steps, atoi, plus): return {'sec': sec, 'picto': picto, 'titre': titre, 'guide': guide, 'bulle': bulle, 'steps': steps, 'atoi': atoi, 'plus': plus}
nouveaux = [
 ('Le nom noyau commande', n('gn', 'mots', 'Deux adjectifs, un seul noyau', 'girl', 'Tous les adjectifs s’accordent avec le même nom noyau.',
   [{'p': 'une ~grande~ maison ~blanche~'}, {'p': 'des ~grandes~ maisons ~blanches~', 'c': 'Maisons est au pluriel : les deux adjectifs aussi.'}, {'p': 'un ~grand~ chat ~blanc~', 'c': 'Chat est masculin : pas de e.'}],
   adj('une ___ maison blanche', 'grande', ['grand', 'grands']), [adj('des chats noirs et ___', 'blancs', ['blanc', 'blanche']), adj('un garçon gentil et ___', 'poli', ['polie', 'polis'])])),
 ('Le sujet commande le verbe', n('sv', 'remplacer', 'Le groupe sujet s’accorde', 'boy', 'Plusieurs sujets reliés par « et » : le verbe est au pluriel.',
   [{'p': '[Le chat] (joue).'}, {'p': '[Le chat et le chien] (jouent).', 'c': 'Deux sujets : le verbe prend -ent.'}, {'p': '[Ma sœur et moi] (jouons).', 'c': 'Ma sœur et moi = nous.'}],
   vb('Le chat et le chien ___ ensemble.', 'jouent', ['joue', 'jouons'], 'Deux sujets reliés par « et » : ils.'), [vb('Ma sœur et moi ___ au parc.', 'allons', ['allez', 'vont'], 'Ma sœur et moi = nous.'), vb('Tom et Léa ___ contents.', 'sont', ['est', 'es'], 'Tom et Léa = ils.')])),
 ('Je vérifie une phrase', n('methode', 'coche', 'Je me corrige', 'girl', 'Je relis, je repère les erreurs et je corrige chaque mot.',
   [{'p': 'Les élèves joue dans la cour.', 'c': 'Il y a une erreur.'}, {'p': '[Les élèves] (jouent) dans la cour.', 'c': '1. Le sujet est pluriel : -ent.'}, {'p': 'Mes cousines sont ^partie^ ; mes cousines sont ^parties^.', 'c': '2. Avec être, le participe s’accorde.'}],
   corr('Les élèves joue dans la cour.', 'Les élèves jouent dans la cour.', ['Les élèves jouons dans la cour.', 'Les élève jouent dans la cour.']), [corr('Ma sœur est parti.', 'Ma sœur est partie.', ['Ma sœur est partis.', 'Ma sœur sont partie.']), corr('Les belle fleurs poussent.', 'Les belles fleurs poussent.', ['Les belles fleur poussent.', 'Les belle fleurs pousse.'])])),
]
if __name__ == '__main__':
    appliquer('G7', niv, nouveaux)
