from niveaux_lib import *
def v(p, bon, mal, hint): return C(p, '', bon, mal, hint, 'v')
niv = {
 'Le sujet commande le verbe': (
  [v('Les élèves ___ dans la cour.', 'jouent', ['joue', 'joues'], 'Les élèves : plusieurs, comme « ils ».'), v('Le vent ___ très fort.', 'souffle', ['soufflent', 'souffles'], 'Le vent : un seul, comme « il ».'),
   v('Tu ___ ton cartable.', 'portes', ['porte', 'portent'], 'Avec « tu », le verbe finit par -es.'), v('Mes cousins ___ chez nous.', 'arrivent', ['arrive', 'arrives'], 'Mes cousins : plusieurs, comme « ils ».')],
  [v('Dans la cour de l’école, les élèves ___ au ballon.', 'jouent', ['joue', 'joues'], 'Le sujet « les élèves » est pluriel.'), v('Le vent du nord ___ sur la plaine depuis ce matin.', 'souffle', ['soufflent', 'souffles'], 'Le sujet est « le vent » : singulier.'),
   v('Chaque soir, tu ___ ton cartable avant de dormir.', 'prépares', ['prépare', 'préparent'], 'Avec « tu », le verbe finit par -es.'), v('Depuis hier, mes cousins ___ chez nous pour les vacances.', 'séjournent', ['séjourne', 'séjournes'], 'Le sujet « mes cousins » est pluriel.')]),
 'Les terminaisons à connaître': (
  [v('Vous ___ trop vite.', 'parlez', ['parlons', 'parlent'], 'Avec « vous » : -ez.'), v('Nous ___ le dîner.', 'préparons', ['préparez', 'préparent'], 'Avec « nous » : -ons.'),
   v('Ils ___ la porte.', 'ferment', ['ferme', 'fermez'], 'Avec « ils » : -ent.'), v('Vous ___ le ballon.', 'lancez', ['lançons', 'lancent'], 'Avec « vous » : -ez.')],
  [v('Avec mes amis, nous ___ souvent au bord du lac.', 'pêchons', ['pêchez', 'pêchent'], 'Avec « nous » : -ons.'), v('Les voisins ___ leur jardin chaque dimanche.', 'arrosent', ['arrose', 'arrosez'], 'Avec « ils » : -ent.'),
   v('Pendant les vacances, vous ___ chez vos grands-parents.', 'habitez', ['habitons', 'habitent'], 'Avec « vous » : -ez.'), v('Chaque matin, nous ___ l’autobus à sept heures.', 'prenons', ['prenez', 'prennent'], 'Avec « nous » : -ons.')]),
 'Je remplace le sujet': (
  [v('Ma grand-mère ___ des gâteaux.', 'prépare', ['préparent', 'prépares'], 'Ma grand-mère = elle.'), v('Les voitures ___ vite.', 'roulent', ['roule', 'roules'], 'Les voitures = elles.'),
   v('Mes parents ___ le journal.', 'lisent', ['lit', 'lis'], 'Mes parents = ils.'), v('Le facteur ___ le courrier.', 'distribue', ['distribuent', 'distribues'], 'Le facteur = il.')],
  [v('Les enfants du voisin ___ dans la rue.', 'jouent', ['joue', 'joues'], 'Les enfants = ils.'), v('La petite sœur de mon ami ___ du piano.', 'joue', ['jouent', 'joues'], 'La petite sœur = elle.'),
   v('Les voitures de course ___ à toute vitesse sur le circuit.', 'roulent', ['roule', 'roules'], 'Les voitures de course = elles.'), v('Le directeur de l’école ___ les nouveaux élèves.', 'accueille', ['accueillent', 'accueilles'], 'Le directeur = il.')]),
 'Plusieurs sujets': (
  [v('Léa et Tom ___ au parc.', 'jouent', ['joue', 'jouons'], 'Léa et Tom = ils.'), v('Mon père et ma mère ___ le dîner.', 'préparent', ['prépare', 'préparons'], 'Mon père et ma mère = ils.'),
   v('Toi et moi ___ ensemble.', 'travaillons', ['travaillez', 'travaillent'], 'Toi et moi = nous.'), v('Le chat et le chien ___ dans le jardin.', 'dorment', ['dort', 'dormons'], 'Le chat et le chien = ils.')],
  [v('Mon frère et mes deux cousins ___ au football chaque mercredi.', 'jouent', ['joue', 'jouons'], 'Plusieurs sujets reliés par « et » = ils.'), v('Ma sœur et moi ___ la table avant le repas.', 'mettons', ['mettez', 'mettent'], 'Ma sœur et moi = nous.'),
   v('Le facteur et la boulangère ___ chaque matin dans la rue.', 'discutent', ['discute', 'discutons'], 'Le facteur et la boulangère = ils.'), v('Toi et ton frère ___ souvent en retard.', 'arrivez', ['arrivent', 'arrivons'], 'Toi et ton frère = vous.')]),
 'Le sujet est loin du verbe': (
  [v('Le chien de mes voisins ___ la nuit.', 'aboie', ['aboient', 'aboies'], 'Le sujet est « le chien » : singulier.'), v('Les enfants de la classe ___ fort.', 'chantent', ['chante', 'chantes'], 'Le sujet est « les enfants » : pluriel.'),
   v('La porte des toilettes ___ souvent.', 'grince', ['grincent', 'grinces'], 'Le sujet est « la porte » : singulier.'), v('Les livres de la bibliothèque ___ sur l’étagère.', 'restent', ['reste', 'restes'], 'Le sujet est « les livres » : pluriel.')],
  [v('Les élèves de la classe de ma sœur ___ un spectacle chaque année.', 'préparent', ['prépare', 'prépares'], 'Le sujet est « les élèves » : pluriel.'), v('Le stylo de mon meilleur ami ___ depuis ce matin.', 'fuit', ['fuient', 'fuis'], 'Le sujet est « le stylo » : singulier.'),
   v('Les cris des enfants de la cour ___ jusqu’à la maison.', 'résonnent', ['résonne', 'résonnes'], 'Le sujet est « les cris » : pluriel.'), v('La voisine de mes cousins ___ ses fleurs tous les soirs.', 'arrose', ['arrosent', 'arroses'], 'Le sujet est « la voisine » : singulier.')]),
 'Le sujet est après le verbe': (
  [v('Dans le pré ___ les vaches.', 'broutent', ['broute'], 'Qui est-ce qui broute ? Les vaches : pluriel.'), v('Sous la table ___ le chat.', 'dort', ['dorment'], 'Qui est-ce qui dort ? Le chat : singulier.'),
   v('Au loin ___ des cloches.', 'sonnent', ['sonne'], 'Qui est-ce qui sonne ? Des cloches : pluriel.'), v('Où ___ tes parents ?', 'travaillent', ['travaille'], 'Qui est-ce qui travaille ? Tes parents : pluriel.')],
  [v('Dans le jardin de mes grands-parents ___ de magnifiques rosiers.', 'poussent', ['pousse'], 'Qui est-ce qui pousse ? De magnifiques rosiers : pluriel.'), v('Au fond du couloir ___ les élèves de la classe.', 'attendent', ['attend'], 'Qui est-ce qui attend ? Les élèves : pluriel.'),
   v('Quand ___ ton frère et ta sœur ?', 'arrivent', ['arrive'], 'Qui est-ce qui arrive ? Ton frère et ta sœur : pluriel.'), v('Sur la colline ___ un vieux moulin.', 'se dresse', ['se dressent'], 'Qui est-ce qui se dresse ? Un vieux moulin : singulier.')]),
 'Le petit mot devant le verbe': (
  [v('Léa les ___.', 'regarde', ['regardent'], 'Le sujet est « Léa », pas « les ».'), v('Mes amis me ___ souvent.', 'téléphonent', ['téléphone'], 'Le sujet est « mes amis », pas « me ».'),
   v('Le maître nous ___ une histoire.', 'raconte', ['racontent'], 'Le sujet est « le maître », pas « nous ».'), v('Papa leur ___ un cadeau.', 'offre', ['offrent'], 'Le sujet est « papa », pas « leur ».')],
  [v('Ma tante nous ___ chaque été dans sa maison au bord de la mer.', 'invite', ['invitent'], 'Le sujet est « ma tante », pas « nous ».'), v('Mes voisins vous ___ à leur fête dimanche prochain.', 'invitent', ['invite'], 'Le sujet est « mes voisins », pas « vous ».'),
   v('La maîtresse les ___ avant de partir en sortie.', 'rassemble', ['rassemblent'], 'Le sujet est « la maîtresse », pas « les ».'), v('Mes cousins nous ___ souvent des cartes postales.', 'envoient', ['envoie'], 'Le sujet est « mes cousins », pas « nous ».')]),
 'Le 2e groupe : -ir avec -iss-': (
  [v('Les plantes ___ vite au printemps.', 'grandissent', ['grandent', 'grandit'], 'Je dis « nous grandissons » : 2e groupe.'), v('Nous ___ notre travail.', 'finissons', ['finons', 'finisons'], 'Avec « nous » : -issons.'),
   v('Elles ___ leurs devoirs.', 'finissent', ['finissons', 'finit'], 'Avec « elles » : -issent.'), v('Vous ___ ce gâteau.', 'choisissez', ['choisisez', 'choisissons'], 'Avec « vous » : -issez.')],
  [v('Les élèves ___ leur exposé avant la fin de l’heure.', 'finissent', ['finit', 'finisent'], 'Avec « ils » : -issent.'), v('Chaque année, mes cousins ___ d’un centimètre.', 'grandissent', ['grandit', 'grandent'], 'Avec « ils » : -issent.'),
   v('Vous ___ la couleur de la peinture avec soin.', 'choisissez', ['choisissons', 'choisisez'], 'Avec « vous » : -issez.'), v('Le public ___ le chanteur à la fin du concert.', 'applaudit', ['applaudissent', 'applaudis'], 'Le sujet « le public » est singulier : -it.')]),
 'Pas tous les verbes en -ir': (
  [C('', 'Lequel est du 2e groupe ?', 'finir', ['partir', 'courir'], 'Je dis « nous… » : j’entends -iss- ?'), C('', 'Lequel est du 2e groupe ?', 'grandir', ['sortir', 'venir'], 'Je dis « nous… » : j’entends -iss- ?'),
   C('', 'Lequel n’est PAS du 2e groupe ?', 'dormir', ['réussir', 'applaudir'], 'Nous dormons : pas de -iss-.'), C('', 'Lequel est du 2e groupe ?', 'remplir', ['ouvrir', 'servir'], 'Nous remplissons : -iss-.')],
  [C('', 'Quel verbe est du 2e groupe ?', 'réfléchir', ['courir', 'mentir'], 'Nous réfléchissons : j’entends -iss-.'), C('', 'Quel verbe n’est PAS du 2e groupe ?', 'tenir', ['bâtir', 'rougir'], 'Nous tenons : pas de -iss-.'),
   C('', 'Quel verbe est du 2e groupe ?', 'atterrir', ['dormir', 'venir'], 'Nous atterrissons : -iss-.'), C('', 'Quel verbe n’est PAS du 2e groupe ?', 'offrir', ['grossir', 'vieillir'], 'Nous offrons : pas de -iss-.')]),
 'Ma méthode en 4 étapes': (
  [v('Les élèves de la classe ___ bien.', 'travaillent', ['travaille'], 'Verbe, sujet, pronom : ils travaillent.'), v('Le chat de ma voisine ___ sur le mur.', 'dort', ['dorment'], 'Sujet : le chat = il.'),
   v('Ma sœur et moi ___ les devoirs.', 'faisons', ['font', 'faites'], 'Ma sœur et moi = nous.'), v('Ils nous ___ des bonbons.', 'donnent', ['donne'], 'Le sujet est « ils », pas « nous ».')],
  [v('Les enfants de la voisine qui habite au bout de la rue ___ souvent chez nous.', 'jouent', ['joue'], 'Je cherche le sujet : les enfants = ils.'), v('Dans la cour de récréation ___ des centaines de billes colorées.', 'roulent', ['roule'], 'Qui est-ce qui roule ? Des centaines de billes.'),
   v('Ma cousine et moi ___ toujours ensemble nos vacances à la mer.', 'passons', ['passent', 'passez'], 'Ma cousine et moi = nous.'), v('Les voisins de mes grands-parents nous ___ chaque été des fruits de leur verger.', 'apportent', ['apporte'], 'Le sujet est « les voisins », pas « nous ».')]),
 'Je vérifie ma phrase': (
  [C('', 'Quelle phrase est bien écrite ?', 'Les enfants de la voisine jouent dehors.', ['Les enfants de la voisine joue dehors.', 'Les enfants de la voisine jouez dehors.'], 'Je remplace le sujet par un pronom : ils jouent.'),
   C('', 'Quelle phrase est bien écrite ?', 'Mon frère et moi mangeons une pomme.', ['Mon frère et moi mangent une pomme.', 'Mon frère et moi mange une pomme.'], 'Mon frère et moi = nous.'),
   C('', 'Quelle phrase est bien écrite ?', 'Le chat de mes voisins dort sur le toit.', ['Le chat de mes voisins dorment sur le toit.', 'Le chat de mes voisins dors sur le toit.'], 'Le sujet est « le chat » : il dort.'),
   C('', 'Quelle phrase est bien écrite ?', 'Tu lances le ballon très loin.', ['Tu lance le ballon très loin.', 'Tu lancent le ballon très loin.'], 'Avec « tu » : -es.')],
  [C('', 'Quelle phrase est bien écrite ?', 'Dans le jardin poussent de belles fleurs.', ['Dans le jardin pousse de belles fleurs.', 'Dans le jardin poussons de belles fleurs.'], 'Qui est-ce qui pousse ? De belles fleurs : elles poussent.'),
   C('', 'Quelle phrase est bien écrite ?', 'Mes parents nous lisent une histoire le soir.', ['Mes parents nous lit une histoire le soir.', 'Mes parents nous lisons une histoire le soir.'], 'Le sujet est « mes parents » : ils lisent.'),
   C('', 'Quelle phrase est bien écrite ?', 'La voisine de mes grands-parents arrose ses fleurs.', ['La voisine de mes grands-parents arrosent ses fleurs.', 'La voisine de mes grands-parents arroses ses fleurs.'], 'Le sujet est « la voisine » : elle arrose.'),
   C('', 'Quelle phrase est bien écrite ?', 'Toi et ta sœur choisissez un jeu.', ['Toi et ta sœur choisissent un jeu.', 'Toi et ta sœur choisit un jeu.'], 'Toi et ta sœur = vous.')]),
}
nouveaux = [
 ('Ma méthode en 4 étapes', {'sec': 'methode', 'picto': 'coche', 'titre': 'Je vérifie ma phrase', 'guide': 'girl', 'bulle': 'Après avoir écrit, je relis : je trouve le sujet et je vérifie le verbe.',
   'steps': [{'p': 'Les enfants de la voisine (jouent) dehors.'}, {'p': '[Les enfants de la voisine] (jouent) dehors.', 'c': '1. Je cherche le sujet.'}, {'p': '[*Ils*] (jouent) dehors.', 'c': '2. Je le remplace : ils → -ent.'}],
   'atoi': C('', 'Quelle phrase est bien écrite ?', 'Les enfants de la voisine jouent dehors.', ['Les enfants de la voisine joue dehors.', 'Les enfants de la voisine jouez dehors.'], 'Je remplace le sujet par un pronom : ils jouent.'),
   'plus': [C('', 'Quelle phrase est bien écrite ?', 'Mon frère et moi mangeons une pomme.', ['Mon frère et moi mangent une pomme.', 'Mon frère et moi mange une pomme.'], 'Mon frère et moi = nous.'),
            C('', 'Quelle phrase est bien écrite ?', 'Le chat de mes voisins dort sur le toit.', ['Le chat de mes voisins dorment sur le toit.', 'Le chat de mes voisins dors sur le toit.'], 'Le sujet est « le chat » : il dort.')]}),
]
if __name__ == '__main__':
    appliquer('G5', niv, nouveaux)
