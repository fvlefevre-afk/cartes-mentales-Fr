"""G3 (le groupe nominal) : BANQUE de phrases écrites et relues à la main (16/11/2026), à la place des phrases fabriquées par g3_beaucoup.py.

Règles suivies (programme du cycle 3, annexe du cycle 2, cahiers de progrès ; voir programmes/diagnostic-exercices-ceintures.md) :
  - phrase simple, un seul verbe, sujet avant le verbe (sujet inversé en CM2 seulement) ; pas de proposition subordonnée ;
  - CE2 : phrases avec un verbe ; complément du nom en CM2 seulement ;
  - structures variées (déclaratives, interrogatives, impératives, négatives, exclamatives, « Il y a », « Voici »…) ;
  - JAMAIS d'écriture fausse montrée : les propositions sont de vraies formes (contrôle au dictionnaire dans `controler()`), ou un trou de quelques lettres ;
  - écrans « clique » : tout autre groupe nominal / déterminant / adjectif de la phrase est marqué ou absent (pas de « ce matin », « du four »… non marqués).

Écrans 1 à 6 : les exercices d'origine sont gardés, 12 de la banque sont ajoutés par classe.
Écrans 7, 8, 9, 11, 12, 13 : tout est remplacé (16 exercices par classe) car les anciens montraient des formes inventées ;
écran 10 : tout est remplacé (12 par classe) car les anciens faisaient choisir parmi des groupes nominaux mal accordés.
Usage : python3 g3_banque.py   (réécrit PLUS['G3'] et NIV_ATOI['G3'] dans index.html ; relançable sans danger)."""
import json, os, re, sys, random

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from niveaux_lib import CHEMIN
from g3_beaucoup import PL_X, PL_AUX, PL_INV, PLUS_ORIGINE, NIV_ORIGINE, cap

# ============================================================ écrans « clique » : phrases avec <…>
CLIQUE = {
 1: dict(ask={'CE2': 'Clique sur le groupe nominal.', 'CM1': 'Clique sur les 2 groupes nominaux.', 'CM2': 'Clique sur les 3 groupes nominaux.'},
         hint={'CE2': 'Cherche un nom avec son déterminant.', 'CM1': 'Cherche les noms avec leur déterminant.', 'CM2': 'Cherche les noms avec leur déterminant.'},
  CE2=['<Un gros chat> dort.', 'Regarde <cet oiseau bleu> !', 'Tu portes <une jolie robe> !', '<Mon petit frère> pleure.', 'Voici <ma nouvelle maison>.',
       'Il y a <un nuage noir> là-haut.', 'Prête-moi <ton crayon rouge>, s’il te plaît.', '<La neige blanche> tombe doucement.', 'Je n’aime pas <les araignées velues>.',
       'Tu as perdu <ta casquette bleue> ?', 'Je vois <un magnifique arc-en-ciel> !', '<Les petits oiseaux> chantent.'],
  CM1=['Dans <la cour>, <les élèves> jouent ensemble.', 'Il y a <un chat noir> sur <le toit>.', 'Voici <ma cousine> et <son nouveau chien>.', 'Ne perds pas <ta clé> et <ton écharpe> !',
       'Pendant <la nuit>, <la neige> est tombée.', 'As-tu vu <mes lunettes rondes> et <ma casquette> ?', 'Dans <le verger>, <les arbres> fleurissent.',
       'Sous <le grand chêne>, <un renard> se repose.', '<Les nuages gris> cachent <le soleil>.', '<Mon père> et <ma mère> sourient.',
       'Dans <le panier>, il y a <des pommes rouges>.', 'Lis <cette histoire> à <ton petit frère> !'],
  CM2=['Dans <le salon>, <ma grand-mère> tricote <une écharpe>.', 'Derrière <la haie>, <un hérisson> cherche <des escargots>.', 'Sur <le quai>, <les voyageurs> attendent <le train>.',
       'Offre <ces fleurs> à <ta voisine> avec <un grand sourire> !', 'Au fond de <la classe>, <une élève> lit <un roman>.', 'Près de <la fenêtre>, <le chat> guette <un oiseau>.',
       'Sur <la falaise>, <le soleil> éclaire <les vieilles pierres>.', 'Dans <mon jardin> poussent <de jolies roses> et <des tulipes jaunes>.',
       'Pour <la fête>, <les parents> décorent <la salle>.', 'Chez <mes grands-parents>, <un vieux chien> garde <la maison>.', 'Sur <le port>, <les pêcheurs> réparent <leurs filets>.',
       'Sur <la plage>, <les enfants> construisent <un grand château>.']),
 2: dict(ask={'CE2': 'Clique sur le déterminant.', 'CM1': 'Clique sur le déterminant.', 'CM2': 'Clique sur les 2 déterminants.'},
         hint={'CE2': 'C’est le petit mot devant le nom.', 'CM1': 'C’est le petit mot devant le nom.', 'CM2': 'Ce sont les petits mots devant les noms.'},
  CE2=['<Mes> crayons sont neufs.', 'Il lit <un> livre.', '<Cette> fleur sent bon.', 'Elle mange <la> tarte.', '<Ses> amis arrivent.', 'Nous aimons <notre> école.',
       'Regarde <ce> bel oiseau !', '<Les> enfants jouent.', 'Où est <ton> cartable ?', 'Elle ouvre <une> boîte.', '<Leurs> chiens aboient.', 'Je prends <mon> manteau.'],
  CM1=['Léa range <ses> affaires.', 'Hugo cherche <son> chat partout.', '<Ces> nuages arrivent vite.', 'Maya a oublié <sa> trousse chez Tom.', 'Hugo et Maya écoutent <la> maîtresse.',
       'Nous visitons <un> château avec Sacha.', 'Ne touche pas à <mon> cahier, Tom !', 'Samir aime <les> histoires drôles.', '<Notre> équipe gagne toujours.',
       'Elle a perdu <ses> lunettes hier.', 'Tom, prête-moi <ton> stylo !', 'Léa mange <une> pomme rouge.'],
  CM2=['<Les> élèves rangent <leurs> cahiers.', 'Sur <le> banc, Hugo lit <un> journal.', '<Mon> frère répare <son> vélo.', 'Dans <la> cuisine, Maya prépare <une> tarte.',
       '<Ces> fleurs sentent <le> printemps.', '<Notre> voisine offre <des> bonbons à Tom.', 'Pour <la> fête, Samir apporte <un> gâteau.', 'Tom cherche <sa> casquette sous <le> lit.',
       'Chez <mes> grands-parents, Léa nourrit <les> poules.', 'Sur <la> plage, Nina ramasse <des> coquillages.', 'Dans <ma> chambre, il y a <un> grand lit.',
       'Sous <ce> chêne, Hugo cherche <des> glands.']),
 3: dict(ask={'CE2': 'Clique sur le nom noyau.', 'CM1': 'Clique sur le nom noyau du groupe sujet.', 'CM2': 'Clique sur le nom noyau du groupe sujet.'},
         hint={'CE2': 'Quel mot ne peut-on pas enlever ?', 'CM1': 'Le sujet est au début : qui est-ce qui… ?', 'CM2': 'Le sujet est au début : qui est-ce qui… ?'},
  CE2=['Le petit <chat> noir dort.', 'Une grande <maison> blanche apparaît.', 'Mes vieux <livres> sentent bon.', 'Les jolies <fleurs> jaunes poussent.', 'Ton gros <sac> bleu est lourd.',
       'La petite <souris> grise court.', 'Un joli <oiseau> rouge chante.', 'Cette belle <robe> verte me plaît.', 'Mon grand <frère> blond arrive.', 'Le vieux <pont> fragile tremble.',
       'Les petites <filles> rieuses jouent.', 'Une grosse <pomme> mûre tombe.'],
  CM1=['Mon petit <frère> blond aime le chocolat.', 'Les grands <arbres> verts protègent le jardin.', 'Une vieille <dame> aimable traverse la rue.', 'Ces jolis <oiseaux> bleus mangent des graines.',
       'Notre nouvelle <voisine> sympathique habite ici.', 'Le gros <chien> noir garde la maison.', 'Mes deux petites <sœurs> jumelles chantent.', 'Un vieux <pêcheur> fatigué rentre au port.',
       'Ses nouvelles <chaussures> rouges brillent.', 'La longue <route> sinueuse monte vers le village.', 'Des <nuages> gris couvrent le ciel.', 'Le jeune <musicien> timide accorde sa guitare.'],
  CM2=['Le vieux <château> abandonné domine toute la vallée.', 'Les petits <enfants> de ma voisine jouent dans la cour.', 'Une délicieuse <odeur> de pain chaud flotte dans la cuisine.',
       'Les grands <rochers> gris de la côte résistent aux vagues.', 'Ces énormes <camions> rouges transportent du sable.', 'La jolie <maison> de mes grands-parents sent le bon pain.',
       'Le petit <garçon> aux cheveux bouclés rit aux éclats.', 'Les belles <vacances> d’été passent trop vite.', 'Un gros <nuage> sombre cache le soleil.', 'La vieille <horloge> du salon sonne midi.',
       'Des <oiseaux> migrateurs traversent le ciel au printemps.', 'Mon vieux <voisin> à la barbe blanche arrose ses fleurs.']),
 5: dict(ask={'CE2': 'Clique sur l’adjectif.', 'CM1': 'Clique sur l’adjectif.', 'CM2': 'Clique sur les 2 adjectifs.'},
         hint={'CE2': 'Il dit comment est le nom.', 'CM1': 'Il dit comment est le nom.', 'CM2': 'Ils disent comment sont les noms.'},
  CE2=['Le ciel est <bleu>.', 'Il porte un <gros> sac.', 'Voici une fleur <rouge> !', 'Elle ouvre la porte <lourde>.', 'Quel <joli> dessin !', 'Nous aimons ce jardin <calme>.',
       'La soupe est <chaude>.', 'Tu as un chat <noir> ?', 'Ils construisent une <haute> tour.', 'Prends cette pomme <mûre> !', 'Un <petit> oiseau chante.', 'Elle lit un livre <passionnant>.'],
  CM1=['Maya porte une écharpe <douce>.', 'Hugo regarde un film <drôle>.', 'Nous cueillons de <belles> fraises.', 'Léa écoute une histoire <passionnante>.', 'Un vent <froid> souffle sur la plage.',
       'Mon grand-père plante un <jeune> arbre.', 'Sacha dessine un soleil <jaune>.', 'Ne mange pas ce fruit <vert> !', 'Tom habite dans une <grande> maison.',
       'Le facteur apporte une lettre <importante>.', 'Sa voisine arrose des fleurs <rouges>.', 'As-tu vu mon <nouveau> vélo ?'],
  CM2=['Une <petite> fille <blonde> pousse la lourde porte.', 'Mon <vieux> voisin plante des rosiers <blancs>.', 'Un chat <noir> guette une <jolie> souris.', 'La <grande> maison <blanche> domine le village.',
       'Ce <gros> livre <ancien> sent la poussière.', 'Des <jeunes> arbres <fragiles> poussent près du chemin.', 'Un <long> serpent <vert> traverse le sentier.',
       'Maya porte une <belle> robe <rouge> pour la fête.', 'Le <vieux> pêcheur répare son filet <troué>.', 'Une <douce> brise <fraîche> caresse la plage.',
       'Un <bon> gâteau <chaud> refroidit sur la table.', 'Les <petits> enfants rangent leurs jouets <neufs>.']),
}
# écran 4 (choix : le nom qui ne s'enlève pas) : (groupe nominal, nom noyau, adjectifs)
NOYAU = {
 'CE2': [('ma grande sœur blonde', 'sœur', ['grande', 'blonde']), ('un gros ballon rouge', 'ballon', ['gros', 'rouge']), ('une vieille maison grise', 'maison', ['vieille', 'grise']),
         ('mes nouvelles chaussures blanches', 'chaussures', ['nouvelles', 'blanches']), ('un joli oiseau bleu', 'oiseau', ['joli', 'bleu']), ('le petit chat noir', 'chat', ['petit', 'noir']),
         ('une grande tortue verte', 'tortue', ['grande', 'verte']), ('ce vieux livre usé', 'livre', ['vieux', 'usé']), ('un petit lapin blanc', 'lapin', ['petit', 'blanc']),
         ('la grosse pomme rouge', 'pomme', ['grosse', 'rouge']), ('mon nouveau vélo bleu', 'vélo', ['nouveau', 'bleu']), ('une belle fleur rose', 'fleur', ['belle', 'rose'])],
 'CM1': [('le grand chêne vert', 'chêne', ['grand', 'vert']), ('une longue route droite', 'route', ['longue', 'droite']), ('mes petits cousins blonds', 'cousins', ['petits', 'blonds']),
         ('ces belles roses rouges', 'roses', ['belles', 'rouges']), ('un vieux pêcheur fatigué', 'pêcheur', ['vieux', 'fatigué']), ('la haute montagne blanche', 'montagne', ['haute', 'blanche']),
         ('un gros nuage gris', 'nuage', ['gros', 'gris']), ('notre jeune voisine sympathique', 'voisine', ['jeune', 'sympathique']), ('des fraises sucrées', 'fraises', ['sucrées']),
         ('une petite boîte ronde', 'boîte', ['petite', 'ronde']), ('le bon gâteau chaud', 'gâteau', ['bon', 'chaud']), ('ses nouvelles bottes noires', 'bottes', ['nouvelles', 'noires'])],
 'CM2': [('le vieux château de ma tante', 'château', ['vieux']), ('une odeur de pain chaud', 'odeur', ['chaud']), ('les grands arbres du parc', 'arbres', ['grands']),
         ('mes deux petits frères jumeaux', 'frères', ['petits', 'jumeaux']), ('la jolie maison de mes grands-parents', 'maison', ['jolie']), ('un grand sac de toile bleue', 'sac', ['grand', 'bleue']),
         ('les belles vacances d’été', 'vacances', ['belles']), ('le petit garçon aux cheveux bouclés', 'garçon', ['petit', 'bouclés']), ('une vieille horloge du salon', 'horloge', ['vieille']),
         ('ces énormes camions rouges', 'camions', ['énormes', 'rouges']), ('la longue histoire du vieux marin', 'histoire', ['longue']), ('un bol de lait chaud', 'bol', ['chaud'])],
}
# ============================================================ écrans « choix » avec trou
# écran 6 : (phrase, bon, [adverbe, infinitif], nom pour l'indice)
ENRICHIS = {
 'CE2': [('une ___ girafe', 'grande', ['vite', 'courir'], 'la girafe'), ('un chien ___', 'gentil', ['souvent', 'dormir'], 'le chien'), ('une robe ___', 'rouge', ['demain', 'porter'], 'la robe'),
         ('un ___ bonbon', 'sucré', ['tard', 'croquer'], 'le bonbon'), ('une ___ souris', 'petite', ['lentement', 'grignoter'], 'la souris'), ('des fleurs ___', 'jaunes', ['toujours', 'pousser'], 'les fleurs'),
         ('un ciel ___', 'bleu', ['hier', 'briller'], 'le ciel'), ('une voiture ___', 'rapide', ['bientôt', 'rouler'], 'la voiture'), ('un ___ jardin', 'fleuri', ['partout', 'arroser'], 'le jardin'),
         ('une classe ___', 'calme', ['vite', 'écouter'], 'la classe'), ('un ___ nuage', 'gros', ['souvent', 'passer'], 'le nuage'), ('des chaussures ___', 'neuves', ['encore', 'courir'], 'les chaussures')],
 'CM1': [('Maya porte une écharpe ___ .', 'douce', ['souvent', 'tricoter'], 'l’écharpe'), ('Le boulanger vend un pain ___ .', 'chaud', ['vite', 'cuire'], 'le pain'),
         ('Hugo regarde un film ___ .', 'drôle', ['tard', 'rire'], 'le film'), ('Nous cueillons de ___ fraises.', 'belles', ['souvent', 'manger'], 'les fraises'),
         ('Léa écoute une histoire ___ .', 'passionnante', ['attentivement', 'raconter'], 'l’histoire'), ('Tom habite dans une ___ maison.', 'grande', ['loin', 'habiter'], 'la maison'),
         ('Un vent ___ souffle sur la plage.', 'froid', ['encore', 'courir'], 'le vent'), ('Mon grand-père plante un ___ arbre.', 'jeune', ['bientôt', 'planter'], 'l’arbre'),
         ('Elle range ses crayons dans une boîte ___ .', 'ronde', ['vite', 'ranger'], 'la boîte'), ('Sacha dessine un soleil ___ .', 'jaune', ['lentement', 'dessiner'], 'le soleil'),
         ('Les enfants construisent une ___ cabane.', 'solide', ['ensemble', 'construire'], 'la cabane'), ('Le facteur apporte une lettre ___ .', 'importante', ['tôt', 'apporter'], 'la lettre')],
 'CM2': [('Pendant les vacances, nous visitons un village ___ .', 'ancien', ['souvent', 'visiter'], 'le village'), ('Dans la vitrine, on voit une montre ___ .', 'dorée', ['toujours', 'voir'], 'la montre'),
         ('Au bord de la rivière, un héron ___ attend.', 'gris', ['longtemps', 'voler'], 'le héron'), ('Chaque soir, ma grand-mère prépare une soupe ___ .', 'chaude', ['vite', 'préparer'], 'la soupe'),
         ('Sur la table du salon, un vase ___ contient des roses.', 'transparent', ['souvent', 'remplir'], 'le vase'), ('Pour son anniversaire, Léo reçoit un ___ vélo.', 'nouveau', ['bientôt', 'recevoir'], 'le vélo'),
         ('Dans le grenier, Maya découvre un coffre ___ .', 'mystérieux', ['lentement', 'découvrir'], 'le coffre'), ('Le long du chemin, de ___ arbres donnent de l’ombre.', 'grands', ['souvent', 'donner'], 'les arbres'),
         ('Après la pluie, une odeur ___ monte du jardin.', 'fraîche', ['vite', 'monter'], 'l’odeur'), ('Devant la maison, un chat ___ guette les oiseaux.', 'affamé', ['patiemment', 'guetter'], 'le chat'),
         ('Au marché, Tom achète des pommes ___ .', 'mûres', ['souvent', 'acheter'], 'les pommes'), ('Dans la forêt, nous suivons un sentier ___ .', 'étroit', ['lentement', 'suivre'], 'le sentier')],
}
# adjectifs : clé -> (masc sg, fém sg, masc pl, fém pl)
ADJ = {
 'vert': ('vert', 'verte', 'verts', 'vertes'), 'noir': ('noir', 'noire', 'noirs', 'noires'), 'bleu': ('bleu', 'bleue', 'bleus', 'bleues'), 'blond': ('blond', 'blonde', 'blonds', 'blondes'),
 'petit': ('petit', 'petite', 'petits', 'petites'), 'grand': ('grand', 'grande', 'grands', 'grandes'), 'haut': ('haut', 'haute', 'hauts', 'hautes'), 'joli': ('joli', 'jolie', 'jolis', 'jolies'),
 'poli': ('poli', 'polie', 'polis', 'polies'), 'content': ('content', 'contente', 'contents', 'contentes'), 'fatigué': ('fatigué', 'fatiguée', 'fatigués', 'fatiguées'),
 'plein': ('plein', 'pleine', 'pleins', 'pleines'), 'rond': ('rond', 'ronde', 'ronds', 'rondes'), 'carré': ('carré', 'carrée', 'carrés', 'carrées'), 'ouvert': ('ouvert', 'ouverte', 'ouverts', 'ouvertes'),
 'fermé': ('fermé', 'fermée', 'fermés', 'fermées'), 'court': ('court', 'courte', 'courts', 'courtes'), 'lourd': ('lourd', 'lourde', 'lourds', 'lourdes'), 'chaud': ('chaud', 'chaude', 'chauds', 'chaudes'),
 'froid': ('froid', 'froide', 'froids', 'froides'), 'sucré': ('sucré', 'sucrée', 'sucrés', 'sucrées'), 'salé': ('salé', 'salée', 'salés', 'salées'), 'mûr': ('mûr', 'mûre', 'mûrs', 'mûres'),
 'brun': ('brun', 'brune', 'bruns', 'brunes'), 'rouge': ('rouge', 'rouge', 'rouges', 'rouges'), 'jaune': ('jaune', 'jaune', 'jaunes', 'jaunes'), 'calme': ('calme', 'calme', 'calmes', 'calmes'),
 'rapide': ('rapide', 'rapide', 'rapides', 'rapides'), 'timide': ('timide', 'timide', 'timides', 'timides'), 'joyeux': ('joyeux', 'joyeuse', 'joyeux', 'joyeuses'),
 'gentil': ('gentil', 'gentille', 'gentils', 'gentilles'), 'gros': ('gros', 'grosse', 'gros', 'grosses'), 'doux': ('doux', 'douce', 'doux', 'douces'), 'heureux': ('heureux', 'heureuse', 'heureux', 'heureuses'),
 'neuf': ('neuf', 'neuve', 'neufs', 'neuves'), 'blanc': ('blanc', 'blanche', 'blancs', 'blanches'), 'long': ('long', 'longue', 'longs', 'longues'), 'léger': ('léger', 'légère', 'légers', 'légères'),
 'frais': ('frais', 'fraîche', 'frais', 'fraîches'), 'ancien': ('ancien', 'ancienne', 'anciens', 'anciennes'), 'épais': ('épais', 'épaisse', 'épais', 'épaisses'), 'bon': ('bon', 'bonne', 'bons', 'bonnes'),
 'curieux': ('curieux', 'curieuse', 'curieux', 'curieuses'), 'courageux': ('courageux', 'courageuse', 'courageux', 'courageuses'), 'paresseux': ('paresseux', 'paresseuse', 'paresseux', 'paresseuses'),
 'peureux': ('peureux', 'peureuse', 'peureux', 'peureuses'), 'délicieux': ('délicieux', 'délicieuse', 'délicieux', 'délicieuses'), 'vif': ('vif', 'vive', 'vifs', 'vives'),
 'sérieux': ('sérieux', 'sérieuse', 'sérieux', 'sérieuses'), 'lumineux': ('lumineux', 'lumineuse', 'lumineux', 'lumineuses'), 'violet': ('violet', 'violette', 'violets', 'violettes'),
 'meilleur': ('meilleur', 'meilleure', 'meilleurs', 'meilleures'), 'nouveau': ('nouveau', 'nouvelle', 'nouveaux', 'nouvelles'), 'gris': ('gris', 'grise', 'gris', 'grises'),
}
REGLE = {'gros': 'gros → grosse : deux s.', 'doux': 'doux → douce.', 'gentil': 'gentil → gentille : la consonne se double.', 'heureux': 'heureux → heureuse.', 'neuf': 'neuf → neuve.',
         'blanc': 'blanc → blanche.', 'long': 'long → longue.', 'léger': 'léger → légère.', 'frais': 'frais → fraîche.', 'ancien': 'ancien → ancienne : le n se double.', 'épais': 'épais → épaisse.',
         'bon': 'bon → bonne : le n se double.', 'curieux': 'curieux → curieuse.', 'courageux': 'courageux → courageuse.', 'paresseux': 'paresseux → paresseuse.', 'peureux': 'peureux → peureuse.',
         'délicieux': 'délicieux → délicieuse.', 'vif': 'vif → vive.', 'sérieux': 'sérieux → sérieuse.', 'lumineux': 'lumineux → lumineuse.', 'joyeux': 'joyeux → joyeuse.'}
# écran 7 (masculin / féminin, adjectifs réguliers) : (phrase avec ___, adjectif, nom, genre du nom)
MASCFEM = {
 'CE2': [('une jupe ___', 'vert', 'jupe', 'f'), ('un chat ___', 'noir', 'chat', 'm'), ('ma cousine ___', 'content', 'cousine', 'f'), ('un ciel ___', 'bleu', 'ciel', 'm'), ('cette ___ fille', 'petit', 'fille', 'f'),
         ('un ___ garçon', 'grand', 'garçon', 'm'), ('une boîte ___', 'rond', 'boîte', 'f'), ('un sac ___', 'lourd', 'sac', 'm'), ('la soupe ___', 'chaud', 'soupe', 'f'), ('le lait ___', 'froid', 'lait', 'm'),
         ('une fenêtre ___', 'ouvert', 'fenêtre', 'f'), ('un livre ___', 'fermé', 'livre', 'm'), ('une tour ___', 'haut', 'tour', 'f'), ('un ___ chien', 'joli', 'chien', 'm'), ('la porte ___', 'fermé', 'porte', 'f'),
         ('un gâteau ___', 'sucré', 'gâteau', 'm')],
 'CM1': [('Léa porte une écharpe ___ .', 'vert', 'écharpe', 'f'), ('Hugo caresse un lapin ___ .', 'blond', 'lapin', 'm'), ('Maya regarde la ___ fleur.', 'joli', 'fleur', 'f'), ('Tom prend un ___ gâteau.', 'petit', 'gâteau', 'm'),
         ('Elle ouvre une valise ___ .', 'plein', 'valise', 'f'), ('Il pousse un chariot ___ .', 'plein', 'chariot', 'm'), ('Nous mangeons une pomme ___ .', 'mûr', 'pomme', 'f'), ('Samir cherche son stylo ___ .', 'noir', 'stylo', 'm'),
         ('Léa dessine une maison ___ .', 'carré', 'maison', 'f'), ('Tom ramasse un caillou ___ .', 'rond', 'caillou', 'm'), ('Maya a une jupe ___ .', 'court', 'jupe', 'f'), ('Hugo a un pull ___ .', 'brun', 'pull', 'm'),
         ('Nina boit une soupe ___ .', 'chaud', 'soupe', 'f'), ('Léo boit un jus ___ .', 'froid', 'jus', 'm'), ('Elle regarde la ___ montagne.', 'haut', 'montagne', 'f'), ('Il ouvre le tiroir ___ .', 'fermé', 'tiroir', 'm')],
 'CM2': [('Ce matin, Léa porte une robe ___ .', 'rouge', 'robe', 'f'), ('Ce matin, Hugo porte un manteau ___ .', 'rouge', 'manteau', 'm'), ('Dans la cour, une fille ___ attend.', 'timide', 'fille', 'f'),
         ('Dans la cour, un garçon ___ attend.', 'timide', 'garçon', 'm'), ('Pour la fête, Maya prépare une tarte ___ .', 'sucré', 'tarte', 'f'), ('Pour la fête, Tom prépare un gâteau ___ .', 'sucré', 'gâteau', 'm'),
         ('Au marché, Samir achète une poire ___ .', 'mûr', 'poire', 'f'), ('Au marché, Nina achète un fruit ___ .', 'mûr', 'fruit', 'm'), ('Sur la table, il y a une bouteille ___ .', 'plein', 'bouteille', 'f'),
         ('Sur la table, il y a un verre ___ .', 'plein', 'verre', 'm'), ('Dans le jardin, une ___ fleur s’ouvre.', 'joli', 'fleur', 'f'), ('Dans le jardin, un ___ oiseau chante.', 'joli', 'oiseau', 'm'),
         ('Au bord du lac, une barque ___ flotte.', 'carré', 'barque', 'f'), ('Au bord du lac, un bateau ___ flotte.', 'carré', 'bateau', 'm'), ('Dans le placard, une assiette ___ attend.', 'rond', 'assiette', 'f'),
         ('Dans le placard, un plat ___ attend.', 'rond', 'plat', 'm')],
}
# écran 8 (féminin qui change) : (phrase avec ___, adjectif, nom) — toujours un nom féminin singulier
FEMCHANGE = {
 'CE2': [('une voix ___', 'doux', 'voix'), ('une valise ___', 'gros', 'valise'), ('la fille ___', 'gentil', 'fille'), ('une maman ___', 'heureux', 'maman'), ('une robe ___', 'neuf', 'robe'),
         ('une chemise ___', 'blanc', 'chemise'), ('une corde ___', 'long', 'corde'), ('une plume ___', 'léger', 'plume'), ('une salade ___', 'frais', 'salade'), ('une maison ___', 'ancien', 'maison'),
         ('une soupe ___', 'épais', 'soupe'), ('une glace ___', 'bon', 'glace'), ('une amie ___', 'curieux', 'amie'), ('une élève ___', 'courageux', 'élève'), ('une chatte ___', 'paresseux', 'chatte'),
         ('une brebis ___', 'peureux', 'brebis')],
 'CM1': [('Elle cherche une ___ valise.', 'gros', 'valise'), ('Il écoute une voix ___ .', 'doux', 'voix'), ('Léa a une amie ___ .', 'gentil', 'amie'), ('Maya est une fille ___ .', 'heureux', 'fille'),
         ('Hugo achète une veste ___ .', 'neuf', 'veste'), ('Tom porte une chemise ___ .', 'blanc', 'chemise'), ('Nous suivons une route ___ .', 'long', 'route'), ('Elle lit une histoire ___ .', 'long', 'histoire'),
         ('Il prépare une tarte ___ .', 'délicieux', 'tarte'), ('Samir mange une pomme ___ .', 'frais', 'pomme'), ('Elle regarde une photo ___ .', 'ancien', 'photo'), ('Nina verse une crème ___ .', 'épais', 'crème'),
         ('Léo boit une ___ limonade.', 'bon', 'limonade'), ('Elle caresse une chatte ___ .', 'curieux', 'chatte'), ('Il admire une danseuse ___ .', 'joyeux', 'danseuse'), ('Nous avons une voisine ___ .', 'sérieux', 'voisine')],
 'CM2': [('Pendant les vacances, nous louons une maison ___ .', 'lumineux', 'maison'), ('Pour le goûter, ma tante prépare une crêpe ___ .', 'délicieux', 'crêpe'), ('Dans le jardin, Léa arrose une plante ___ .', 'vif', 'plante'),
         ('Sur le chemin, nous croisons une vache ___ .', 'paresseux', 'vache'), ('Au zoo, Hugo observe une girafe ___ .', 'curieux', 'girafe'), ('À l’école, Maya a une maîtresse ___ .', 'gentil', 'maîtresse'),
         ('Après l’orage, une brise ___ se lève.', 'frais', 'brise'), ('Au marché, Tom choisit une pastèque ___ .', 'gros', 'pastèque'), ('Dans l’armoire, il y a une couverture ___ .', 'épais', 'couverture'),
         ('Sur la plage, une mouette ___ vole.', 'blanc', 'mouette'), ('Au musée, nous admirons une statue ___ .', 'ancien', 'statue'), ('Dans la cuisine, une odeur ___ flotte.', 'bon', 'odeur'),
         ('Pour la fête, Nina étrenne une robe ___ .', 'neuf', 'robe'), ('Au marché, une marchande ___ vend des fruits.', 'joyeux', 'marchande'), ('Sur la table, une plume ___ attend.', 'léger', 'plume'),
         ('Dans le salon, ma grand-mère raconte une histoire ___ .', 'long', 'histoire')],
}
# écran 9 (singulier ou pluriel) : (phrase avec ___, adjectif, nom, genre du nom) — nom au pluriel
SINGPLUR = {
 'CE2': [('des lampes ___', 'bleu', 'lampes', 'f'), ('les ballons ___', 'rouge', 'ballons', 'm'), ('nos ___ poules', 'petit', 'poules', 'f'), ('ces filles ___', 'content', 'filles', 'f'), ('les arbres ___', 'haut', 'arbres', 'm'),
         ('mes ___ chaussures', 'neuf', 'chaussures', 'f'), ('des fleurs ___', 'jaune', 'fleurs', 'f'), ('les chats ___', 'noir', 'chats', 'm'), ('ces ___ maisons', 'grand', 'maisons', 'f'), ('des sacs ___', 'lourd', 'sacs', 'm'),
         ('les soupes ___', 'chaud', 'soupes', 'f'), ('des gâteaux ___', 'sucré', 'gâteaux', 'm'), ('mes ___ livres', 'joli', 'livres', 'm'), ('les pommes ___', 'mûr', 'pommes', 'f'), ('des portes ___', 'fermé', 'portes', 'f'),
         ('les ciels ___', 'bleu', 'ciels', 'm')],
 'CM1': [('Elles choisissent des sacs ___ .', 'plein', 'sacs', 'm'), ('Hugo cherche ses ___ lapins.', 'petit', 'lapins', 'm'), ('Léa lave les assiettes ___ .', 'rond', 'assiettes', 'f'), ('Nous plantons des fleurs ___ .', 'rouge', 'fleurs', 'f'),
         ('Maya ramasse des feuilles ___ .', 'jaune', 'feuilles', 'f'), ('Tom range ses ___ cahiers.', 'grand', 'cahiers', 'm'), ('Samir regarde des chiens ___ .', 'gentil', 'chiens', 'm'),
         ('Nina prépare des tartes ___ .', 'sucré', 'tartes', 'f'), ('Léo achète des bottes ___ .', 'noir', 'bottes', 'f'), ('Elle porte ses ___ robes.', 'joli', 'robes', 'f'), ('Il pousse les portes ___ .', 'lourd', 'portes', 'f'),
         ('Nous goûtons des poires ___ .', 'mûr', 'poires', 'f'), ('Hugo ouvre les volets ___ .', 'fermé', 'volets', 'm'), ('Maya cherche ses chaussettes ___ .', 'blanc', 'chaussettes', 'f'),
         ('Tom regarde les ___ nuages.', 'gros', 'nuages', 'm'), ('Léa écoute ses ___ chansons.', 'bon', 'chansons', 'f')],
 'CM2': [('Pendant les vacances, nous visitons de ___ villages.', 'petit', 'villages', 'm'), ('Chaque matin, Maya donne des carottes ___ à ses lapins.', 'frais', 'carottes', 'f'),
         ('Au marché, Tom choisit des fraises ___ .', 'mûr', 'fraises', 'f'), ('Sur la table, il y a des verres ___ .', 'plein', 'verres', 'm'), ('Dans la cour, de ___ enfants jouent.', 'petit', 'enfants', 'm'),
         ('Dans le jardin, Léa soigne ses roses ___ .', 'rouge', 'roses', 'f'), ('Au bord de la route, des panneaux ___ nous guident.', 'jaune', 'panneaux', 'm'), ('Sur l’étagère, il y a des livres ___ .', 'ancien', 'livres', 'm'),
         ('Dans le panier, Nina met ses ___ pommes.', 'gros', 'pommes', 'f'), ('Pour la fête, Samir porte des chaussures ___ .', 'neuf', 'chaussures', 'f'), ('Dans la forêt, des arbres ___ cachent le ciel.', 'haut', 'arbres', 'm'),
         ('Dans la cuisine, des soupes ___ refroidissent.', 'chaud', 'soupes', 'f'), ('Au zoo, nous observons des girafes ___ .', 'curieux', 'girafes', 'f'), ('À la ferme, Hugo nourrit des moutons ___ .', 'blanc', 'moutons', 'm'),
         ('Dans la vitrine, on voit des robes ___ .', 'léger', 'robes', 'f'), ('Sur la plage, des enfants ___ courent.', 'joyeux', 'enfants', 'm')],
}
# écran 10 (je vérifie les accords) : (groupe nominal avec {}, adjectif, nom, genre, nombre, phrase avec {} ou None)
ACCORDS = {
 'CE2': [('nos {} voisines', 'gentil', 'voisines', 'f', 'p', None), ('des fleurs {}', 'jaune', 'fleurs', 'f', 'p', None), ('un ballon {}', 'rouge', 'ballon', 'm', 's', None), ('la robe {}', 'blanc', 'robe', 'f', 's', None),
         ('les chats {}', 'noir', 'chats', 'm', 'p', None), ('une {} maison', 'grand', 'maison', 'f', 's', None), ('ce {} jardin', 'joli', 'jardin', 'm', 's', None), ('mes {} cahiers', 'neuf', 'cahiers', 'm', 'p', None),
         ('la fille {}', 'content', 'fille', 'f', 's', None), ('des soupes {}', 'chaud', 'soupes', 'f', 'p', None), ('les {} oiseaux', 'petit', 'oiseaux', 'm', 'p', None), ('une pomme {}', 'mûr', 'pomme', 'f', 's', None)],
 'CM1': [('mes {} livres', 'petit', 'livres', 'm', 'p', 'Léa range mes {} livres.'), ('des fleurs {}', 'rouge', 'fleurs', 'f', 'p', 'Hugo cueille des fleurs {}.'),
         ('la cuisine {}', 'lumineux', 'cuisine', 'f', 's', 'Nous aimons la cuisine {}.'), ('ces poires {}', 'mûr', 'poires', 'f', 'p', 'Maya mange ces poires {}.'), ('un chien {}', 'doux', 'chien', 'm', 's', 'Tom caresse un chien {}.'),
         ('les {} arbres', 'haut', 'arbres', 'm', 'p', 'Nous voyons les {} arbres.'), ('une {} voisine', 'gentil', 'voisine', 'f', 's', 'Samir aide une {} voisine.'), ('mes bottes {}', 'noir', 'bottes', 'f', 'p', 'Nina cherche mes bottes {}.'),
         ('ce garçon {}', 'curieux', 'garçon', 'm', 's', 'Léo regarde ce garçon {}.'), ('des gâteaux {}', 'sucré', 'gâteaux', 'm', 'p', 'Elle prépare des gâteaux {}.'), ('la porte {}', 'lourd', 'porte', 'f', 's', 'Il pousse la porte {}.'),
         ('nos {} chaussures', 'neuf', 'chaussures', 'f', 'p', 'Nous portons nos {} chaussures.')],
 'CM2': [('mes {} frères', 'petit', 'frères', 'm', 'p', 'Pendant les vacances, je retrouve mes {} frères.'), ('les maisons {}', 'blanc', 'maisons', 'f', 'p', 'Dans le village, les maisons {} brillent.'),
         ('une odeur {}', 'frais', 'odeur', 'f', 's', 'Dans le jardin, une odeur {} flotte.'), ('ce livre {}', 'ancien', 'livre', 'm', 's', 'Sur l’étagère, ce livre {} attend.'),
         ('des chaussures {}', 'neuf', 'chaussures', 'f', 'p', 'Pour la fête, Nina étrenne des chaussures {}.'), ('les enfants {}', 'joyeux', 'enfants', 'm', 'p', 'Sur la plage, les enfants {} courent.'),
         ('ma cousine {}', 'courageux', 'cousine', 'f', 's', 'Au sommet, ma cousine {} sourit.'), ('les {} nuages', 'gros', 'nuages', 'm', 'p', 'Dans le ciel, les {} nuages avancent.'),
         ('une soupe {}', 'épais', 'soupe', 'f', 's', 'À midi, ma grand-mère sert une soupe {}.'), ('ces fleurs {}', 'violet', 'fleurs', 'f', 'p', 'Dans le vase, ces fleurs {} sentent bon.'),
         ('un garçon {}', 'sérieux', 'garçon', 'm', 's', 'À l’école, un garçon {} travaille.'), ('des chiens {}', 'gentil', 'chiens', 'm', 'p', 'Dans la rue, des chiens {} jouent.')],
}
# écrans 11, 12, 13 : cadres écrits à la main dans g3_beaucoup.py (PL_X, PL_AUX, PL_INV) ; le trou est la fin du mot
PL_AUX2 = PL_AUX + [('minéral', 'minéraux', 'Les ___ brillent au soleil.', 'Dans la vitrine du musée, on voit des ___ de toutes les couleurs.')]

# ============================================================ fabrication
def click(p, ask, hint):
    t = {'click': 'x', 'ask': ask, 'hint': hint}
    n = p.count('<')
    if n > 1: t['n'] = n
    return {'p': p, 'tasks': [t]}
def choix(p, bon, mauvais, hint, ask=None, fill='pr'):
    t = {'choose': [bon] + list(mauvais), 'ok': 0, 'hint': hint}
    if ask: t['ask'] = ask
    if fill: t['fill'] = fill
    return {'p': p, 'tasks': [t]}
def autres(bon, formes):
    out = []
    for f in formes:
        if f != bon and f not in out: out.append(f)
    return out[:2]

def ecran_clique(k, cl):
    d = CLIQUE[k]; return [click(p, d['ask'][cl], d['hint'][cl]) for p in d[cl]]
def ecran4(cl):
    return [choix(gn, noy, adj, 'C’est le nom noyau.', 'Quel mot ne peut-on pas enlever ?', None) for gn, noy, adj in NOYAU[cl]]
def ecran6(cl):
    return [choix(p, bon, mauv, 'Cherche un mot qui dit comment est %s.' % nom, None if cl == 'CE2' else 'Complète avec l’adjectif qui convient.') for p, bon, mauv, nom in ENRICHIS[cl]]
def ecran7(cl):
    out = []
    for p, a, nom, g in MASCFEM[cl]:
        ms, fs, mp, fp = ADJ[a]; bon = fs if g == 'f' else ms
        mauv = autres(bon, [ms, mp, fp] if g == 'f' else [fs, mp, fp])
        hint = ('%s est féminin : j’ajoute un e.' if g == 'f' and fs != ms else '%s est féminin : l’adjectif se termine déjà par e.' if g == 'f' else '%s est masculin singulier.') % cap(nom)
        out.append(choix(p, bon, mauv, hint))
    return out
def ecran8(cl):
    out = []
    for p, a, nom in FEMCHANGE[cl]:
        ms, fs, mp, fp = ADJ[a]
        out.append(choix(p, fs, autres(fs, [ms, mp, fp]), REGLE.get(a, '%s → %s.' % (ms, fs)), 'Complète avec l’adjectif au féminin.' if cl == 'CE2' else 'Complète avec l’adjectif qui convient.'))
    return out
def ecran9(cl):
    out = []
    for p, a, nom, g in SINGPLUR[cl]:
        ms, fs, mp, fp = ADJ[a]; bon = mp if g == 'm' else fp
        mauv = autres(bon, [ms, fs, fp, mp] if g == 'm' else [fs, ms, mp])
        out.append(choix(p, bon, mauv, '%s est pluriel %s.' % (cap(nom), 'masculin' if g == 'm' else 'féminin')))
    return out
def ecran10(cl):
    out = []
    for i, (gnp, a, nom, g, nb, sent) in enumerate(ACCORDS[cl]):
        ms, fs, mp, fp = ADJ[a]; bon = {('m', 's'): ms, ('f', 's'): fs, ('m', 'p'): mp, ('f', 'p'): fp}[(g, nb)]
        gtxt = ('féminin' if g == 'f' else 'masculin') + (' pluriel' if nb == 'p' else ' singulier')
        bare = gnp.format(bon)
        mots = re.findall(r'[\wéèêàçôîûœ’-]+', gnp.replace('{}', ''))
        mot = [m for m in mots if m == nom][0]; det = mots[0]
        t = i % 3
        if t == 0:
            frame = (sent or gnp).replace('{}', '___')
            out.append(choix(frame, bon, autres(bon, [ms, fs, mp, fp]), 'Le nom noyau « %s » est %s : l’adjectif s’accorde avec lui.' % (mot, gtxt), 'Complète avec la bonne forme.' if cl != 'CE2' else None))
        elif t == 1:
            out.append(choix(bare, mot, [det, bon] if det != bon else [bon], 'L’adjectif prend le genre et le nombre du nom noyau.', 'Avec quel mot « %s » s’accorde-t-il ?' % bon, None))
        else:
            autres_g = [x for x in ['féminin pluriel', 'masculin pluriel', 'féminin singulier', 'masculin singulier'] if x != gtxt][:2]
            out.append(choix(bare, 'Parce que « %s » est %s.' % (mot, gtxt), ['Parce que « %s » est %s.' % (mot, x) for x in autres_g],
                             'Je cherche le nom noyau, puis je regarde son genre et son nombre.', 'Pourquoi « %s » s’écrit-il ainsi ?' % bon, None))
    return out
def trou(p, stem, bon, mauv, hint, ask=None):
    return choix(p.replace('___', stem + '___'), bon, mauv, hint, ask, 'circ')
def melanger(L, graine):
    L = L[:]; random.Random(graine).shuffle(L); return L
def ecran11(cl, c):
    ph = {'eau': 'Les mots en -eau prennent un x au pluriel.', 'eu': 'Les mots en -eu prennent un x au pluriel.', 'au': 'Les mots en -au prennent un x au pluriel.'}
    out = []
    for sg, pl, f, court, long_ in melanger(PL_X, 11 + c)[:16]:
        p = 'un %s → des ___' % sg if cl == 'CE2' else (court if cl == 'CM1' else long_)
        out.append(trou(p, pl[:-1], 'x', ['s'], ph[f], 'Complète avec la fin du mot.'))
    return out
def ecran12(cl, c):
    out = []
    for sg, pl, court, long_ in melanger(PL_AUX2, 12 + c)[:16]:
        p = 'un %s → des ___' % sg if cl == 'CE2' else (court if cl == 'CM1' else long_)
        out.append(trou(p, pl[:-3], 'aux', ['als'], '-al devient -aux.', 'Complète avec la fin du mot.'))
    return out
AUTRES_NOMS = ['le chat', 'le cheval', 'le livre', 'la table', 'la fleur', 'le bateau', 'le gâteau', 'l’oiseau', 'la maison', 'le journal', 'l’arbre', 'le stylo', 'le jeu', 'le cadeau', 'l’animal', 'la robe']
def ecran13(cl, c):
    out = []
    inv = melanger(PL_INV, 13 + c); autre = melanger(AUTRES_NOMS, 130 + c)
    n1 = 16 if cl == 'CE2' else 8
    FEM = {'souris', 'voix', 'noix', 'croix'}
    for i in range(n1):
        w = inv[i][0]; art = ('la ' + w) if w in FEM else ('le ' + w)
        mauv = [autre[(2 * i) % len(autre)], autre[(2 * i + 1) % len(autre)]]
        out.append(choix('', art, mauv, '%s finit déjà par %s : on n’ajoute rien au pluriel.' % (cap(w), w[-1]), 'Quel nom ne change pas au pluriel ?', None))
    for i in range(16 - n1):
        w = inv[n1 + i][0]; fin = w[-1]
        out.append(choix('un %s → plusieurs %s' % (w, w), 'Rien : il finit déjà par %s.' % fin, ['J’ajoute un s.', 'J’ajoute un x.'], '%s finit déjà par %s.' % (cap(w), fin),
                         'Que fait-on pour écrire le pluriel de « %s » ?' % w, None))
    return out

# ============================================================ contrôle et écriture
def mots_proposes(e):
    for t in e['tasks']:
        if t.get('choose') and t.get('fill') != 'circ':
            for c in t['choose']:
                yield from re.findall(r'[A-Za-zÀ-ÿœŒ-]+', c)
def controler(tous):
    """Aucun mot proposé ne doit être une forme inventée (dictionnaire français)."""
    W = set(l.strip().lower() for l in open('/usr/share/dict/french', encoding='utf-8', errors='ignore'))
    W |= {'tôt', 'tard', 'là', 'là-bas', 'bientôt', 'ensemble', 'sœur', 'sœurs'}   # mots corrects que le dictionnaire écrit autrement
    return sorted({m for e in tous for m in mots_proposes(e) if m.lower() not in W and len(m) > 1})
def cle(e):
    return e['p'] + '|' + e['tasks'][0].get('ask', '') + '|' + (e['tasks'][0]['choose'][0] if 'choose' in e['tasks'][0] else '')

PROBLEMES = []
def main():
    s = open(CHEMIN, encoding='utf-8').read()
    mp = re.search(r'const PLUS=(\{.*\});\n', s); PLUS = json.loads(mp.group(1))
    mn = re.search(r'const NIV_ATOI=(\{.*\});\n', s); NIV = json.loads(mn.group(1))
    CL = ['CE2', 'CM1', 'CM2']
    tous = []; PROBLEMES.clear()
    for k in range(1, 14):
        for c, cl in enumerate(CL):
            if k in (1, 2, 3, 5): nouv = ecran_clique(k, cl)
            elif k == 4: nouv = ecran4(cl)
            elif k == 6: nouv = ecran6(cl)
            elif k == 7: nouv = ecran7(cl)
            elif k == 8: nouv = ecran8(cl)
            elif k == 9: nouv = ecran9(cl)
            elif k == 10: nouv = ecran10(cl)
            elif k == 11: nouv = ecran11(cl, c)
            elif k == 12: nouv = ecran12(cl, c)
            else: nouv = ecran13(cl, c)
            remplace = k in (7, 8, 9, 10, 11, 12, 13)
            if cl == 'CE2':
                base = [] if remplace else PLUS['G3'][k - 1][:PLUS_ORIGINE[k - 1]]
                PLUS['G3'][k - 1] = base + nouv; final = PLUS['G3'][k - 1]
            else:
                base = [] if remplace else NIV['G3'][str(c + 1)][k - 1][:NIV_ORIGINE]
                NIV['G3'][str(c + 1)][k - 1] = base + nouv; final = NIV['G3'][str(c + 1)][k - 1]
            cles = [cle(e) for e in final]
            PROBLEMES.extend(('doublon', k, cl, x) for x in sorted(set(cles)) if cles.count(x) > 1)
            assert len(nouv) == (12 if k == 10 else 16 if remplace else 12), (k, cl, len(nouv))
            tous += final
    assert not PROBLEMES, PROBLEMES
    bad = controler(tous)
    assert not bad, ('mots inconnus du dictionnaire :', bad)
    s = s[:mp.start(1)] + json.dumps(PLUS, ensure_ascii=False) + s[mp.end(1):]
    mn = re.search(r'const NIV_ATOI=(\{.*\});\n', s)
    s = s[:mn.start(1)] + json.dumps(NIV, ensure_ascii=False) + s[mn.end(1):]
    open(CHEMIN, 'w', encoding='utf-8').write(s)
    print('G3 : banque intégrée (%d exercices contrôlés, aucune forme inventée).' % len(tous))

if __name__ == '__main__':
    main()
