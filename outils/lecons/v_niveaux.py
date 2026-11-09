from niveaux_lib import *
def et(p, bon, mal): return C(p, 'Quel est le mot-étiquette ?', bon, mal, 'Quel mot regroupe tous les autres ?')
def sous(l, e, bon): return K(l, f'Clique sur le mot précis qui va sous « {e} ».', 'Quel mot appartient à cette étiquette ?')
def intrus(l): return K(l, 'Clique sur l’intrus.', 'Quel mot ne va pas avec les autres ?')
def ex(e, bon, mal): return C('', f'Quel mot va sous l’étiquette « {e} » ?', bon, mal, 'Cherche un mot qui appartient à cette famille de sens.')
def ech(bon, m1, m2): return C('', 'Quelle échelle va du plus général au plus précis ?', bon, [m1, m2], 'Je pars du mot qui regroupe le plus, vers le plus précis.')
def rep(p, bon, mal): return C(p, '', bon, mal, 'Je choisis un mot qui évite la répétition : l’étiquette.', 'et')
def ind(p, mot, h='Quels mots expliquent le mot difficile ?'): return K(p, f'Clique sur un indice pour comprendre « {mot} ».', h)
def sens(p, q, bon, mal): return C(p, q, bon, mal, 'Je lis toute la phrase : les autres mots m’aident.')
def cache(m, bon, mal): return C(m, 'Quel mot connu est caché dedans ?', bon, mal, 'Je cherche un mot que je connais, caché dans le mot.')
def decoupe(m, bon, mal): return C(m, 'Comment se découpe ce mot ?', bon, mal, 'Je sépare le préfixe ou le suffixe du mot de base.')
def bm(q, bon, mal, h='Je pense au préfixe ou au suffixe.'): return C('', q, bon, mal, h)
def fam(m, bon, mal): return C('', f'Quel mot est de la famille de « {m} » ?', bon, mal, 'Il a une partie commune et il parle du même sujet.')
niv = {
 'Un mot qui regroupe': (
  [et('rouge · bleu · vert', 'couleurs', ['jours', 'fleurs']), et('chien · chat · cheval', 'animaux', ['métiers', 'jouets']), et('pantalon · robe · chemise', 'vêtements', ['meubles', 'fruits']), et('marteau · tournevis · scie', 'outils', ['instruments', 'légumes'])],
  [et('sapin · chêne · bouleau', 'arbres', ['fleurs', 'fruits']), et('violon · flûte · trompette', 'instruments de musique', ['outils', 'jouets']), et('poire · cerise · abricot', 'fruits', ['légumes', 'arbres']), et('juin · mars · octobre', 'mois', ['saisons', 'jours'])]),
 'Les mots rangés dessous': (
  [sous('chaise · <poire> · stylo · nuage', 'fruits', 1), sous('livre · <robe> · pomme · chat', 'vêtements', 1), sous('table · <hibou> · crayon · soleil', 'animaux', 1), sous('vélo · <jaune> · pain · chaise', 'couleurs', 1)],
  [sous('pomme · <poireau> · lait · crayon', 'légumes', 1), sous('banane · <tournevis> · chat · rose', 'outils', 1), sous('piano · <natation> · ciseaux · tulipe', 'sports', 1), sous('chaise · <boulanger> · tulipe · sac', 'métiers', 1)]),
 'Des exemples': (
  [ex('fruits', 'fraise', ['carotte', 'table']), ex('jours', 'jeudi', ['juin', 'hiver']), ex('meubles', 'armoire', ['assiette', 'tulipe']), ex('outils', 'scie', ['cuillère', 'bonbon'])],
  [ex('instruments de musique', 'clarinette', ['perceuse', 'raquette']), ex('moyens de transport', 'tramway', ['fourchette', 'bibliothèque']), ex('sports', 'escrime', ['menuiserie', 'couture']), ex('vêtements', 'manteau', ['canapé', 'couteau'])]),
 'Du général au précis': (
  [ech('animal → oiseau → moineau', 'moineau → oiseau → animal', 'oiseau → animal → moineau'), ech('vêtement → pantalon → jean', 'jean → pantalon → vêtement', 'pantalon → vêtement → jean'),
   ech('fruit → agrume → orange', 'orange → agrume → fruit', 'agrume → fruit → orange'), ech('plante → arbre → chêne', 'chêne → arbre → plante', 'arbre → plante → chêne')],
  [ech('véhicule → avion → hydravion', 'hydravion → avion → véhicule', 'avion → véhicule → hydravion'), ech('meuble → siège → fauteuil', 'fauteuil → siège → meuble', 'siège → meuble → fauteuil'),
   ech('sport → sport collectif → handball', 'handball → sport collectif → sport', 'sport collectif → sport → handball'), ech('outil → outil de jardin → râteau', 'râteau → outil de jardin → outil', 'outil de jardin → outil → râteau')]),
 'Convenir à tous les mots': (
  [intrus('tulipe · rose · <carotte> · marguerite'), intrus('pomme · poire · <chaise> · banane'), intrus('lundi · mardi · <mars> · jeudi'), intrus('chat · chien · <table> · lapin')],
  [intrus('violon · flûte · <marteau> · trompette'), intrus('été · hiver · <lundi> · automne'), intrus('chêne · sapin · <rose> · hêtre'), intrus('tracteur · camion · <stylo> · autobus')]),
 'Éviter les répétitions': (
  [rep('Papa a acheté un pommier. Il plante cet ___ dans le jardin.', 'arbre', ['pommier', 'chêne']), rep('Ma sœur joue de la guitare. Elle range son ___ dans sa chambre.', 'instrument', ['guitare', 'piano']),
   rep('Nous mangeons une fraise. Ce ___ est très sucré.', 'fruit', ['fraise', 'légume']), rep('Léa porte un pantalon. Ce ___ est neuf.', 'vêtement', ['pantalon', 'chapeau'])],
  [rep('Mon oncle conduit un camion. Ce ___ transporte des meubles.', 'véhicule', ['camion', 'tracteur']), rep('Le cuisinier prépare une tarte. Ce ___ est très gourmand.', 'dessert', ['tarte', 'légume']),
   rep('Ma grand-mère cultive des tulipes et des roses. Ces ___ sont magnifiques.', 'fleurs', ['tulipes', 'légumes']), rep('Hugo joue au football. Ce ___ est son préféré.', 'sport', ['football', 'jeu vidéo'])]),
 # --- V2
 'Les autres mots m’aident': (
  [ind('Le matin, mon frère était si <pressé> qu’il a <couru> jusqu’à l’école et est arrivé essoufflé.', 'essoufflé', 'Quels mots expliquent pourquoi il est essoufflé ?'),
   ind('Après la course, les coureurs, <fatigués>, se sont <reposés> longuement sur l’herbe, épuisés.', 'épuisés', 'Quels mots parlent de la fatigue ?'),
   ind('Ce soir, il y a un <orage> : le ciel est <noir> et le tonnerre gronde.', 'gronde', 'Quels mots parlent de l’orage ?'),
   ind('Mon petit frère a <peur> du noir : il tremble et <se cache> sous sa couverture.', 'tremble', 'Quels mots disent pourquoi il tremble ?')],
  [ind('Le randonneur, exténué après <dix heures de marche>, s’effondre sur un rocher et <reprend son souffle péniblement>.', 'exténué', 'Quels mots disent pourquoi il est exténué ?'),
   ind('La route était verglacée : les voitures <glissaient> dangereusement et les piétons <avançaient avec précaution>.', 'verglacée', 'Quels mots montrent l’effet de la glace ?'),
   ind('Le professeur nous a parlé d’un animal nocturne : il <dort le jour> et <chasse la nuit>.', 'nocturne', 'Quels mots expliquent « nocturne » ?'),
   ind('Mon grand-père est très économe : il <n’achète que le nécessaire> et <garde tout ce qui peut servir>.', 'économe', 'Quels mots expliquent « économe » ?')]),
 'Un mot caché dans le mot': (
  [cache('dentiste', 'dent', ['denti', 'iste']), cache('tablette', 'table', ['tabl', 'ette']), cache('fourmilière', 'fourmi', ['fourm', 'lière']), cache('livret', 'livre', ['liv', 'vret'])],
  [cache('montagneux', 'montagne', ['montag', 'neux']), cache('poissonnier', 'poisson', ['poiss', 'nnier']), cache('bagagiste', 'bagage', ['baga', 'agiste']), cache('fourchette', 'fourche', ['fourch', 'hette'])]),
 'Ma méthode en 4 étapes': (
  [sens('L’oiseau plane au-dessus de la vallée.', 'Planer veut dire…', 'voler sans battre des ailes', ['marcher lentement', 'dormir']), sens('Le voleur s’enfuit par la fenêtre.', '« s’enfuit » veut dire…', 's’échappe en courant', ['entre', 'reste']),
   sens('Maman savoure une glace à la fraise.', 'Savourer veut dire…', 'manger en appréciant', ['jeter', 'oublier']), sens('Le chien aboie contre le facteur.', 'Aboyer veut dire…', 'crier, pour un chien', ['dormir', 'ronger'])],
  [sens('Le vieux marin scrute l’horizon.', 'Scruter veut dire…', 'observer attentivement', ['ignorer', 'dessiner']), sens('Les élèves peinent à comprendre cette consigne.', 'Peiner veut dire…', 'avoir de la difficulté', ['se reposer', 's’amuser']),
   sens('Le promeneur longe la rivière.', 'Longer veut dire…', 'marcher le long de', ['traverser', 'éviter']), sens('Le chef a mijoté ce plat pendant des heures.', 'Mijoter veut dire…', 'faire cuire doucement', ['brûler', 'congeler'])]),
 'Quand la phrase ne suffit pas': (
  [C('Léa a acheté un kiwi.', 'Cette phrase suffit-elle pour savoir ce qu’est un kiwi ?', 'non, je sais seulement qu’elle l’a acheté', ['oui, tout est expliqué'], 'Si la phrase n’explique pas le mot, je cherche ailleurs.'),
   C('Le fennec vit dans le désert.', 'Cette phrase suffit-elle pour savoir ce qu’est un fennec ?', 'non, je sais seulement où il vit', ['oui, tout est expliqué'], 'Si la phrase n’explique pas le mot, je cherche ailleurs.'),
   C('Nous avons croisé un chamois en montagne.', 'Cette phrase suffit-elle pour savoir ce qu’est un chamois ?', 'non, je sais seulement que nous l’avons croisé', ['oui, tout est expliqué'], 'Si la phrase n’explique pas le mot, je cherche ailleurs.'),
   C('', 'Que faire si la phrase ne suffit pas ?', 'je lis la suite ou je demande', ['j’invente un sens', 'je saute le mot'], 'Je lis la suite ou je demande.')],
  [C('Le fennec vit dans le désert. C’est un petit renard aux grandes oreilles.', 'Qu’est-ce qu’un fennec ?', 'un petit renard', ['un oiseau', 'un poisson'], 'La phrase suivante explique le mot.'),
   C('Mon oncle est apiculteur. Il s’occupe de ruches et récolte le miel.', 'Qu’est-ce qu’un apiculteur ?', 'quelqu’un qui élève des abeilles', ['un boulanger', 'un pilote'], 'La phrase suivante explique le mot.'),
   C('Le chamois grimpe sur les rochers. C’est un animal de montagne, proche de la chèvre.', 'Qu’est-ce qu’un chamois ?', 'un animal de montagne', ['un poisson', 'un oiseau'], 'La phrase suivante explique le mot.'),
   C('Une clé à molette sert à serrer ou desserrer des écrous.', 'À quoi sert une clé à molette ?', 'à serrer des écrous', ['à ouvrir une boîte', 'à couper du bois'], 'La phrase explique à quoi sert l’objet.')]),
 # --- V3
 'Un mot en morceaux': (
  [decoupe('replacer', 're + placer', ['rep + lacer', 'repla + cer']), decoupe('lavable', 'lav + able', ['la + vable', 'lava + ble']), decoupe('défaire', 'dé + faire', ['déf + aire', 'défa + ire']), decoupe('joueur', 'jou + eur', ['j + oueur', 'joue + ur'])],
  [decoupe('impossible', 'im + possible', ['imp + ossible', 'impo + ssible']), decoupe('inattendu', 'in + attendu', ['ina + ttendu', 'inatt + endu']), decoupe('repeindre', 're + peindre', ['rep + eindre', 'repe + indre']), decoupe('illisible', 'il + lisible', ['ill + isible', 'illis + ible'])]),
 're- : à nouveau': (
  [bm('Refaire, c’est…', 'faire à nouveau', ['ne pas faire', 'faire avant']), bm('Recommencer, c’est…', 'commencer à nouveau', ['ne pas commencer', 'commencer avant']), bm('Redire, c’est…', 'dire encore', ['ne pas dire', 'dire avant']), bm('Revoir, c’est…', 'voir à nouveau', ['ne pas voir', 'voir avant'])],
  [bm('Que signifie « reconstruire » ?', 'construire à nouveau', ['détruire', 'construire avant']), bm('Quel mot signifie « chauffer à nouveau » ?', 'réchauffer', ['échauffer', 'chauffeur']), bm('Que signifie « rouvrir » ?', 'ouvrir de nouveau', ['ne pas ouvrir', 'fermer']), bm('Quel mot signifie « écrire à nouveau » ?', 'réécrire', ['décrire', 'inscrire'])]),
 'dé-, in-, im-, mal- : le contraire': (
  [bm('Le contraire de « heureux » :', 'malheureux', ['reheureux', 'heureusement']), bm('Le contraire de « connu » :', 'inconnu', ['reconnu', 'connaisseur']), bm('Le contraire de « possible » :', 'impossible', ['repossible', 'possiblement']), bm('Le contraire de « couvrir » :', 'découvrir', ['recouvrir', 'couverture'])],
  [bm('Le contraire de « patient » :', 'impatient', ['dépatient', 'malpatient']), bm('Le contraire de « honnête » :', 'malhonnête', ['déshonnête', 'inhonnête']), bm('Le contraire de « lisible » :', 'illisible', ['délisible', 'mallisible']), bm('Le contraire de « monter » :', 'démonter', ['immonter', 'malmonter'])]),
 'Les personnes et les métiers': (
  [bm('Une personne qui chante :', 'un chanteur', ['un chant', 'une chanson']), bm('La personne qui vend des fleurs :', 'un fleuriste', ['une fleur', 'un fleurir']), bm('Une personne qui danse :', 'une danseuse', ['une dansée', 'un danser']), bm('La personne qui coiffe :', 'un coiffeur', ['un coiffé', 'une coiffure'])],
  [bm('La personne qui fabrique des meubles :', 'un menuisier', ['une menuiserie', 'un meuble']), bm('La personne qui fait du pain :', 'un boulanger', ['une boulangerie', 'un pain']), bm('La personne qui joue de la guitare :', 'un guitariste', ['une guitare', 'un guitarage']), bm('La personne qui travaille dans une pharmacie :', 'un pharmacien', ['une pharmacie', 'un pharmaceutique'])]),
 'Petit, possible, manière': (
  [bm('Un petit chat :', 'un chaton', ['un chatier', 'un chatable']), bm('Une chose qu’on peut lire :', 'lisible', ['lisant', 'liser']), bm('Marcher d’une manière rapide :', 'rapidement', ['rapide', 'rapidité']), bm('Un petit livre :', 'un livret', ['un livrable', 'un livrer'])],
  [bm('Une chose qu’on peut manger :', 'mangeable', ['mangeur', 'mangement']), bm('Une petite maison :', 'une maisonnette', ['une maisonner', 'une maisonnable']), bm('Agir d’une manière prudente :', 'prudemment', ['prudence', 'prudentable']), bm('Un objet qu’on peut réparer :', 'réparable', ['réparateur', 'réparation'])]),
 'Je comprends un mot inconnu': (
  [sens('Ce paysage est inoubliable.', '« inoubliable » veut dire…', 'qu’on ne peut pas oublier', ['qu’on oublie souvent', 'très oublié']), sens('Cette histoire est incroyable.', '« incroyable » veut dire…', 'qu’on ne peut pas croire', ['qu’on croit toujours', 'déjà cru']),
   sens('Ce jouet est réparable.', '« réparable » veut dire…', 'qu’on peut réparer', ['qu’on ne peut pas réparer', 'déjà réparé']), sens('Cette lettre est illisible.', '« illisible » veut dire…', 'qu’on ne peut pas lire', ['qu’on peut lire', 'très lue'])],
  [sens('Ce vieux livre est introuvable.', '« introuvable » veut dire…', 'qu’on ne peut pas trouver', ['qu’on trouve facilement', 'déjà trouvé']), sens('Le champion est invincible.', '« invincible » veut dire…', 'qu’on ne peut pas vaincre', ['qu’on vainc souvent', 'déjà vaincu']),
   sens('Cette consigne est incompréhensible.', '« incompréhensible » veut dire…', 'qu’on ne peut pas comprendre', ['qu’on comprend vite', 'déjà comprise']), sens('Le pont est infranchissable.', '« infranchissable » veut dire…', 'qu’on ne peut pas franchir', ['qu’on franchit facilement', 'déjà franchi'])]),
 'Les pièges': (
  [bm('Lequel contient vraiment un préfixe ?', 'défaire', ['dehors', 'demain']), bm('Lequel contient vraiment un préfixe ?', 'redire', ['rendre', 'reste']), bm('Quel mot est bien écrit ?', 'impossible', ['inpossible']), bm('Quel mot est bien écrit ?', 'immobile', ['inmobile'])],
  [bm('Quel mot est bien écrit ?', 'irrégulier', ['inrégulier', 'irégulier']), bm('Quel mot est bien écrit ?', 'illisible', ['inlisible', 'ilisible']), bm('Lequel contient vraiment un préfixe ?', 'désagréable', ['désert', 'désir']), bm('Lequel contient vraiment un préfixe ?', 'malchance', ['malade', 'malin'])]),
 # --- V4
 'Une famille de mots': (
  [fam('terre', 'terrain', ['tarte', 'tirer']), fam('mer', 'marin', ['mère', 'mur']), fam('chanter', 'chanson', ['chaussure', 'chasser']), fam('lire', 'lecture', ['lime', 'lier'])],
  [fam('montagne', 'montagnard', ['monnaie', 'montre']), fam('peindre', 'peinture', ['pendre', 'pointure']), fam('nuit', 'nocturne', ['nu', 'nuage']), fam('terre', 'enterrer', ['terrible', 'tarte'])]),
 'Je fabrique des mots': (
  [fam('jour', 'journée', ['jouer', 'joue']), fam('lune', 'lunaire', ['lutin', 'lourd']), fam('fruit', 'fruitier', ['fruste', 'frite']), fam('peur', 'peureux', ['pur', 'pleurs'])],
  [fam('terre', 'atterrir', ['tarte', 'terminer']), fam('neige', 'enneigé', ['nager', 'neuf']), fam('plume', 'plumage', ['plombier', 'pluie']), fam('sel', 'salière', ['selle', 'sol'])]),
 'L’intrus': (
  [C('porte · portier · portail · porter', 'Quel est l’intrus ?', 'porter', ['portier', 'portail'], 'Il ressemble, mais il ne parle pas de la même chose.'), C('mer · marin · marée · mère', 'Quel est l’intrus ?', 'mère', ['marin', 'marée'], 'Il ressemble, mais il ne parle pas de la même chose.'),
   C('dent · dentiste · dentier · danse', 'Quel est l’intrus ?', 'danse', ['dentiste', 'dentier'], 'Il ressemble, mais il ne parle pas de la même chose.'), C('terre · terrain · enterrer · tarte', 'Quel est l’intrus ?', 'tarte', ['terrain', 'enterrer'], 'Il ressemble, mais il ne parle pas de la même chose.')],
  [C('montagne · montagnard · monter · montagneux', 'Quel est l’intrus ?', 'monter', ['montagnard', 'montagneux'], 'Il ressemble, mais il ne parle pas de la même chose.'), C('chant · chanteur · chantier · chanson', 'Quel est l’intrus ?', 'chantier', ['chanteur', 'chanson'], 'Il ressemble, mais il ne parle pas de la même chose.'),
   C('fleur · fleuriste · fleurir · flûte', 'Quel est l’intrus ?', 'flûte', ['fleuriste', 'fleurir'], 'Il ressemble, mais il ne parle pas de la même chose.'), C('nuit · nocturne · nuage · minuit', 'Quel est l’intrus ?', 'nuage', ['nocturne', 'minuit'], 'Il ressemble, mais il ne parle pas de la même chose.')]),
 'La famille m’aide à écrire': (
  [C('', '« chant » finit par t, car on dit…', 'chanter', ['chanson', 'chantier'], 'J’entends la lettre muette dans un mot de la famille.'), C('', '« grand » finit par d, car on dit…', 'grandir', ['grandeur', 'grain'], 'J’entends la lettre muette dans un mot de la famille.'),
   C('', '« lent » finit par t, car on dit…', 'lenteur', ['lentille', 'lier'], 'J’entends la lettre muette dans un mot de la famille.'), C('', '« froid » finit par d, car on dit…', 'froideur', ['froisser', 'fronde'], 'J’entends la lettre muette dans un mot de la famille.')],
  [C('', '« éclat » finit par t, car on dit…', 'éclater', ['éclaircir', 'éclore'], 'J’entends la lettre muette dans un mot de la famille.'), C('', '« lait » finit par t, car on dit…', 'laitier', ['laiton', 'lainage'], 'J’entends la lettre muette dans un mot de la famille.'),
   C('', '« mont » finit par t, car on dit…', 'montagne', ['montrer', 'monnaie'], 'J’entends la lettre muette dans un mot de la famille.'), C('', '« long » finit par g, car on dit…', 'longue', ['longer', 'lourd'], 'J’entends la lettre muette dans un mot de la famille.')]),
 'Des morceaux que je connais': (
  [C('lavable', 'Le morceau ajouté est…', '-able, à la fin', ['lav-, au début'], 'Je cherche le préfixe ou le suffixe.'), C('défaire', 'Le préfixe est…', 'dé-, au début', ['-aire, à la fin'], 'Je cherche le préfixe ou le suffixe.'),
   C('chanteur', 'Le suffixe est…', '-eur, à la fin', ['chan-, au début'], 'Je cherche le préfixe ou le suffixe.'), C('relire', 'Le préfixe est…', 're-, au début', ['-ire, à la fin'], 'Je cherche le préfixe ou le suffixe.')],
  [C('impossible', 'Le préfixe est…', 'im-, au début', ['-ible, à la fin'], 'Je cherche le préfixe ou le suffixe.'), C('maisonnette', 'Le suffixe est…', '-ette, à la fin', ['mais-, au début'], 'Je cherche le préfixe ou le suffixe.'),
   C('', 'Dans la famille de « manger », « mangeable » veut dire…', 'qu’on peut manger', ['qui mange', 'pas mangé'], 'Je retrouve le suffixe.'), C('', 'Dans la famille de « lire », « illisible » veut dire…', 'qu’on ne peut pas lire', ['qu’on lit vite', 'lu deux fois'], 'Je retrouve le préfixe et le suffixe.')]),
 # --- V5
 'Même sens : les synonymes': (
  [bm('Un synonyme de « joli » :', 'beau', ['laid', 'petit']), bm('Un synonyme de « rapide » :', 'vite', ['lent', 'faible']), bm('Un synonyme de « un enfant » :', 'un gamin', ['un adulte', 'un animal']), bm('Un synonyme de « parler » :', 'discuter', ['écouter', 'dormir'])],
  [bm('Un synonyme de « fatigué » :', 'épuisé', ['reposé', 'content']), bm('Un synonyme de « effrayé » :', 'terrifié', ['rassuré', 'amusé']), bm('Un synonyme de « un logement » :', 'une habitation', ['une promenade', 'un outil']), bm('Un synonyme de « commencer » :', 'débuter', ['finir', 'continuer'])]),
 'Le bon synonyme pour la phrase': (
  [C('Un vent fort', 'Un synonyme de « fort » dans cette phrase :', 'violent', ['musclé', 'bruyant'], 'Je regarde la phrase.'), C('Un élève fort en maths', 'Un synonyme de « fort » dans cette phrase :', 'doué', ['violent', 'lourd'], 'Je regarde la phrase.'),
   C('Un petit gâteau', 'Un synonyme de « petit » dans cette phrase :', 'minuscule', ['court', 'jeune'], 'Je regarde la phrase.'), C('Un long voyage', 'Un synonyme de « long » dans cette phrase :', 'interminable', ['grand', 'haut'], 'Je regarde la phrase.')],
  [C('Cette décision est grave.', 'Un synonyme de « grave » dans cette phrase :', 'sérieuse', ['basse', 'forte'], 'Je regarde la phrase.'), C('Il parle d’une voix grave.', 'Un synonyme de « grave » dans cette phrase :', 'profonde', ['sérieuse', 'triste'], 'Je regarde la phrase.'),
   C('Il a pris un air sec.', 'Un synonyme de « sec » dans cette phrase :', 'froid', ['aride', 'rôti'], 'Je regarde la phrase.'), C('La terre est très sèche.', 'Un synonyme de « sèche » dans cette phrase :', 'aride', ['froide', 'dure'], 'Je regarde la phrase.')]),
 'Sens opposé : les contraires': (
  [bm('Le contraire de « grand » :', 'petit', ['gros', 'haut']), bm('Le contraire de « jour » :', 'nuit', ['soleil', 'matin']), bm('Le contraire de « riche » :', 'pauvre', ['gentil', 'fort']), bm('Le contraire de « avant » :', 'après', ['pendant', 'hier'])],
  [bm('Le contraire de « courageux » :', 'lâche', ['brave', 'fort']), bm('Le contraire de « accepter » :', 'refuser', ['demander', 'donner']), bm('Le contraire de « ancien » :', 'moderne', ['vieux', 'lointain']), bm('Le contraire de « accélérer » :', 'ralentir', ['avancer', 'courir'])]),
 'Un préfixe pour le contraire': (
  [bm('Le contraire de « poli » :', 'impoli', ['repoli', 'polissant']), bm('Le contraire de « monter » :', 'démonter', ['remonter', 'monteur']), bm('Le contraire de « content » :', 'mécontent', ['recontent', 'contentement']), bm('Le contraire de « lisible » :', 'illisible', ['relisible', 'lisiblement'])],
  [bm('Le contraire de « patient » :', 'impatient', ['dépatient', 'repatient']), bm('Le contraire de « agréable » :', 'désagréable', ['malagréable', 'reagréable']), bm('Le contraire de « honnête » :', 'malhonnête', ['inhonnête', 'déshonnête']), bm('Le contraire de « atteignable » :', 'inatteignable', ['désatteignable', 'malatteignable'])]),
 'La même classe de mots': (
  [bm('Le contraire du nom « la joie » :', 'la tristesse', ['triste', 'attrister']), bm('Le contraire du verbe « monter » :', 'descendre', ['bas', 'descente']), bm('Le contraire de l’adjectif « chaud » :', 'froid', ['froideur', 'refroidir']), bm('Le contraire du nom « la guerre » :', 'la paix', ['paisible', 'pacifier'])],
  [bm('Le contraire du nom « la peur » :', 'le courage', ['courageux', 'encourager']), bm('Le contraire du verbe « construire » :', 'détruire', ['destruction', 'constructeur']), bm('Le contraire de l’adjectif « mince » :', 'épais', ['épaisseur', 'épaissir']), bm('Le contraire du nom « la hauteur » :', 'la profondeur', ['profond', 'approfondir'])]),
 'Avec une famille de mots': (
  [bm('Le contraire de « lentement » :', 'rapidement', ['rapide', 'rapidité']), bm('Le contraire de « la joie » et de « heureux » :', 'la tristesse et triste', ['la tristesse et tristement', 'triste et la tristesse'], 'Je garde la même classe de mots.'),
   bm('Le contraire de « gentiment » :', 'méchamment', ['méchant', 'méchanceté']), bm('Le contraire de « courageusement » :', 'lâchement', ['lâche', 'lâcheté'])],
  [bm('Dans la famille de « fort », le contraire de « fortement » :', 'faiblement', ['faible', 'faiblesse']), bm('Dans la famille de « propre », le contraire de « la propreté » :', 'la saleté', ['sale', 'salement']),
   bm('Quelle paire est faite de deux adverbes ?', 'calmement ↔ nerveusement', ['calme ↔ nerveux', 'calme ↔ nervosité']), bm('Quelle paire est faite de deux noms ?', 'le courage ↔ la peur', ['courageux ↔ apeuré', 'courageusement ↔ peureusement'])]),
 # --- V6
 'Même son, autre sens': (
  [bm('Lequel est un homonyme de « mer » ?', 'mère', ['mur', 'mare']), bm('Lequel est un homonyme de « cent » ?', 'sans', ['maison', 'cinq'], 'Il se prononce pareil.'), bm('Lequel est un homonyme de « chant » ?', 'champ', ['chat', 'chaud']), bm('Lequel est un homonyme de « sot » ?', 'seau', ['sol', 'soif'])],
  [bm('Lequel est un homonyme de « saut » ?', 'seau', ['sec', 'soie']), bm('Lequel est un homonyme de « mois » ?', 'moi', ['mort', 'mouton']), bm('Lequel est un homonyme de « foie » ?', 'foi', ['fou', 'fil']), bm('Lequel est un homonyme de « cours » ?', 'court', ['coup', 'cou'])]),
 'Écrits autrement': (
  [C('Je range mes cahiers dans mon ___.', 'Complète avec le bon mot.', 'sac', ['sec', 'sacs'], 'Je lis la phrase : le mot doit avoir du sens.', 'circ'), C('Il y a de l’___ dans le seau.', 'Complète avec le bon mot.', 'eau', ['haut', 'os'], 'Je lis la phrase : le mot doit avoir du sens.', 'circ'),
   C('Mon ___ travaille à la banque.', 'Complète avec le bon mot.', 'père', ['paire', 'pair'], 'Je lis la phrase : le mot doit avoir du sens.', 'circ'), C('Léa a mal au ___.', 'Complète avec le bon mot.', 'dos', ['dot', 'do'], 'Je lis la phrase : le mot doit avoir du sens.', 'circ')],
  [C('Le ___ de la cathédrale est très haut.', 'Complète avec le bon mot.', 'clocher', ['cloche', 'clochers'], 'Je lis la phrase : le mot doit avoir du sens.', 'circ'), C('Le vent a emporté la ___ du bateau.', 'Complète avec le bon mot.', 'voile', ['voir', 'voix'], 'Je lis la phrase : le mot doit avoir du sens.', 'circ'),
   C('Je mange une ___ de pain avec du beurre.', 'Complète avec le bon mot.', 'tranche', ['trancher', 'tranchée'], 'Je lis la phrase : le mot doit avoir du sens.', 'circ'), C('Le ___ a chassé toute la nuit.', 'Complète avec le bon mot.', 'loup', ['lou', 'loupe'], 'Je lis la phrase : le mot doit avoir du sens.', 'circ')]),
 'Écrits pareil': (
  [C('Mon père a un nouveau livre.', 'Ici, « livre » veut dire…', 'un objet à lire', ['un poids'], 'Le déterminant m’aide : un/le → masculin ; une/la → féminin.'), C('J’achète une livre de beurre.', 'Ici, « livre » veut dire…', 'un poids', ['un objet à lire'], 'Le déterminant m’aide.'),
   C('Il fait le tour du lac.', 'Ici, « tour » veut dire…', 'un trajet qui revient au départ', ['un grand bâtiment'], 'Le déterminant m’aide.'), C('Nous avons visité la tour de la cathédrale.', 'Ici, « tour » veut dire…', 'un grand bâtiment', ['un trajet'], 'Le déterminant m’aide.')],
  [C('Le vase est posé sur la table.', 'Ici, « vase » veut dire…', 'un récipient pour les fleurs', ['de la boue'], 'Le déterminant m’aide : un/le vase ; la vase.'), C('Le bateau s’est enlisé dans la vase.', 'Ici, « vase » veut dire…', 'de la boue', ['un récipient'], 'Le déterminant m’aide.'),
   C('Le mousse monte sur le bateau.', 'Ici, « mousse » veut dire…', 'un jeune marin', ['une plante'], 'Le déterminant m’aide : le mousse ; la mousse.'), C('La mousse pousse sur le tronc.', 'Ici, « mousse » veut dire…', 'une plante', ['un jeune marin'], 'Le déterminant m’aide.')]),
 'Un mot, plusieurs sens': (
  [C('La souris grignote le fromage.', 'Ici, « souris » veut dire…', 'un animal', ['un objet d’ordinateur'], 'La phrase m’aide.'), C('Je clique avec la souris de l’ordinateur.', 'Ici, « souris » veut dire…', 'un objet d’ordinateur', ['un animal'], 'La phrase m’aide.'),
   C('Le pied de la table est cassé.', 'Ici, « pied » veut dire…', 'le support du meuble', ['une partie du corps'], 'La phrase m’aide.'), C('Il a mal au pied après la course.', 'Ici, « pied » veut dire…', 'une partie du corps', ['le support d’un meuble'], 'La phrase m’aide.')],
  [C('Le pilote attend la clé du moteur.', 'Ici, « clé » veut dire…', 'un objet pour démarrer', ['un signe de musique'], 'La phrase m’aide.'), C('Sur la portée, le musicien lit la clé de sol.', 'Ici, « clé » veut dire…', 'un signe de musique', ['un objet pour ouvrir'], 'La phrase m’aide.'),
   C('Ce mot a plusieurs sens : j’ouvre le dictionnaire.', 'Pour comprendre un mot à plusieurs sens, je…', 'lis la phrase en entier', ['choisis le premier sens', 'saute le mot'], 'La phrase m’aide.'), C('Ce film dure deux heures : c’est un long métrage.', 'Ici, « long » veut dire…', 'qui dure longtemps', ['qui mesure plusieurs mètres'], 'La phrase m’aide.')]),
 'La phrase m’aide': (
  [C('Je mets du ___ dans mon café.', 'Complète avec le bon mot.', 'sucre', ['sucré', 'sucrer'], 'Je lis toute la phrase.', 'circ'), C('Léa a perdu son ___ de gomme.', 'Complète avec le bon mot.', 'morceau', ['morceaux', 'moulin'], 'Je lis toute la phrase.', 'circ'),
   C('Le ___ pousse dans la forêt : c’est un arbre.', 'Complète avec le bon mot.', 'sapin', ['sapine', 'sabot'], 'Je lis toute la phrase.', 'circ'), C('Pour aller en classe, je prends le ___.', 'Complète avec le bon mot.', 'bus', ['bûche', 'bis'], 'Je lis toute la phrase.', 'circ')],
  [C('Les musiciens accordent leurs ___ avant le concert.', 'Complète avec le bon mot.', 'instruments', ['instrument', 'instrumental'], 'Je lis toute la phrase.', 'circ'), C('La ___ du roi était très haute.', 'Complète avec le bon mot.', 'tour', ['tourte', 'tourner'], 'Je lis toute la phrase.', 'circ'),
   C('Le chien aboie : on entend son ___ jusqu’au village.', 'Complète avec le bon mot.', 'aboiement', ['aboyer', 'abeille'], 'Je lis toute la phrase.', 'circ'), C('Il a plu toute la nuit : les ___ sont boueux.', 'Complète avec le bon mot.', 'chemins', ['chemin', 'cheminée'], 'Je lis toute la phrase.', 'circ')]),
 'Homonyme ou synonyme ?': (
  [C('mère · mer', 'Ces deux mots sont…', 'des homonymes', ['des synonymes', 'des contraires'], 'Même son ? Même sens ?'), C('triste · malheureux', 'Ces deux mots sont…', 'des synonymes', ['des homonymes', 'des contraires'], 'Même son ? Même sens ?'),
   C('lourd · léger', 'Ces deux mots sont…', 'des contraires', ['des synonymes', 'des homonymes'], 'Même son ? Même sens ?'), C('mot · maux', 'Ces deux mots sont…', 'des homonymes', ['des synonymes', 'des contraires'], 'Même son ? Même sens ?')],
  [C('brave · courageux', 'Ces deux mots sont…', 'des synonymes', ['des homonymes', 'des contraires'], 'Même son ? Même sens ?'), C('vert · verre', 'Ces deux mots sont…', 'des homonymes', ['des synonymes', 'des contraires'], 'Même son ? Même sens ?'),
   C('accepter · refuser', 'Ces deux mots sont…', 'des contraires', ['des synonymes', 'des homonymes'], 'Même son ? Même sens ?'), C('chant · champ', 'Ces deux mots sont…', 'des homonymes', ['des synonymes', 'des contraires'], 'Même son ? Même sens ?')]),
}

if __name__ == '__main__':
    for g in ('V1', 'V2', 'V3', 'V4', 'V5', 'V6'):
        titres = [e['titre'] for e in lessons_json(g)['ecrans']]
        appliquer(g, {t: niv[t] for t in titres})
