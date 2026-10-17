"""Écrans en plus pour les leçons CM2.
Une leçon CM2 = la leçon CM1 du même numéro + ces écrans (placés après le dernier écran de leur section)
+ un encadré « En CM2, j'apprends aussi » sous la carte.
Lancer :  python3 lecons/cm2_ajouts.py   puis   python3 inserer_cm2.py"""
import os, sys, json
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from lhelp import E, Q, C, SV, V

OUT = {}
H = 'hl'


def lecon(lid, points, *ecrans):
    ec = []
    for e in ecrans:
        e = dict(e); e['plus'] = e.pop('_plus'); e['cm2'] = True; ec.append(e)
    html = ('<div class="cm2-box"><h3>En CM2, j’apprends aussi</h3><ul>'
            + ''.join(f'<li>{p}</li>' for p in points) + '</ul></div>')
    OUT[lid] = {'html': html, 'ecrans': ec}


# =============================================================== GRAMMAIRE
lecon('G1', ['Le <b>sujet inversé</b> : il peut être placé <b>après le verbe</b>. <i>Dans la forêt vivent des loups.</i>',
             'Je le trouve en encadrant : <b>c’est… qui</b>.'],
 E('sujet', 'deplacer', 'Le sujet inversé', 'boy', 'Parfois, le sujet est placé après le verbe.',
   [('Dans la forêt (vivent) [des loups].', 'Qui est-ce qui vit dans la forêt ? des loups.'),
    ('Où (vas)-[tu] ?', 'Dans une question, le sujet peut suivre le verbe.'),
    ('« Bonjour ! » (dit) [la maîtresse].', 'Après des paroles, le sujet suit souvent le verbe.')],
   SV('Au loin (sonnent) [les cloches].'),
   [SV('Dans le pré (galopent) [les chevaux].'), SV('« J’arrive ! » (crie) [le facteur].'), SV('Que (fais)-[tu] ?')]),
 E('sujet', 'loupe', 'Je prouve avec « c’est… qui »', 'girl', 'J’encadre le sujet avec « c’est… qui ».',
   ['Sur la branche chantent deux merles.',
    ('C’est [deux merles] qui (chantent) sur la branche.', 'Je prouve : c’est deux merles qui chantent.')],
   Q('Dans la mare nagent des canards.', ['des canards', 'la mare', 'nagent'], 'Encadre avec « c’est… qui ».', 'Quel est le sujet ?'),
   [Q('Au bout du chemin apparaît une maison.', ['une maison', 'le chemin', 'apparaît'], 'Encadre avec « c’est… qui ».', 'Quel est le sujet ?'),
    Q('Que disent tes parents ?', ['tes parents', 'que', 'disent'], 'Encadre avec « c’est… qui ».', 'Quel est le sujet ?')]))

lecon('G2', ['Une <b>phrase simple</b> a <b>un seul verbe conjugué</b> ; une <b>phrase complexe</b> en a <b>plusieurs</b>.',
             'Les parties d’une phrase complexe sont reliées par <b>et, mais, donc, quand, parce que, si</b>… ou par une virgule.',
             'Les types et les formes de phrase : je les reconnais dans des phrases plus longues.'],
 E('decl', 'point', 'Phrase simple ou complexe ?', 'girl', 'Je compte les verbes conjugués.',
   [('Le chat (dort).', 'Un seul verbe conjugué : une phrase simple.'),
    ('Le chat (dort) et le chien (aboie).', 'Deux verbes conjugués : une phrase complexe.'),
    ('Quand il (pleut), je (reste) à la maison.', 'Deux verbes conjugués : une phrase complexe.')],
   Q('Le soleil brille et les oiseaux chantent.', ['complexe : deux verbes conjugués', 'simple : un seul verbe conjugué'], 'Compte les verbes conjugués.', 'Cette phrase est…'),
   [Q('Mon frère lit une bande dessinée.', ['simple : un seul verbe conjugué', 'complexe : deux verbes conjugués'], 'Compte les verbes conjugués.', 'Cette phrase est…'),
    Q('Je mange parce que j’ai faim.', ['complexe : deux verbes conjugués', 'simple : un seul verbe conjugué'], 'Compte les verbes conjugués.', 'Cette phrase est…'),
    Q('Nous partirons demain matin.', ['simple : un seul verbe conjugué', 'complexe : deux verbes conjugués'], 'Compte les verbes conjugués.', 'Cette phrase est…')]),
 E('decl', 'wagon', 'Des mots qui relient', 'boy', 'Un petit mot peut relier deux parties de la phrase.',
   [('Il (pleut). Je (prends) mon parapluie.', 'Deux phrases simples.'),
    ('Il (pleut), |donc| je (prends) mon parapluie.', 'Une phrase complexe : « donc » relie les deux parties.'),
    ('Je (prends) mon parapluie |parce qu’|il (pleut).', '« parce que », « quand », « si » relient aussi.')],
   Q('Je mets mon manteau ___ il fait froid.', ['parce qu’', 'ou', 'mais'], 'Il dit pourquoi.', 'Quel mot relie les deux parties ?', fill='pr'),
   [Q('Je rentrerai ___ la nuit tombera.', ['quand', 'ou', 'mais'], 'Il dit à quel moment.', 'Quel mot relie les deux parties ?', fill='pr'),
    Q('Tu auras un dessert ___ tu finis ta soupe.', ['si', 'ou', 'mais'], 'Il pose une condition.', 'Quel mot relie les deux parties ?', fill='pr')]))

lecon('G3', ['Le <b>complément du nom</b> précise le nom ; il commence souvent par <b>de, à, en</b> : <i>un pull en laine</i>.',
             'L’adjectif <b>épithète</b> est collé au nom (<i>un chat noir</i>) ; l’<b>attribut du sujet</b> est relié par être, sembler, devenir… (<i>Le chat est noir.</i>).'],
 E('adj', 'loupe', 'Le complément du nom', 'girl', 'Un groupe de mots peut préciser le nom.',
   [('un pull |en laine|', '« en laine » précise le nom : un complément du nom.'),
    ('la maison |de ma tante|', 'Il commence souvent par de, à, en.'),
    ('une tasse |à café|', 'On peut l’enlever : le groupe nominal reste correct.')],
   C('une boîte <à chaussures>', 'Clique sur le complément du nom.', 'Il précise le nom « boîte ».'),
   [C('le vélo <de mon frère>', 'Clique sur le complément du nom.', 'Il précise le nom « vélo ».'),
    C('un sac <en cuir> noir', 'Clique sur le complément du nom.', 'Il commence par « en ».')]),
 E('adj', 'remplacer', 'Épithète ou attribut ?', 'boy', 'L’adjectif est collé au nom, ou relié par le verbe être.',
   [('un chat ~noir~', 'Collé au nom : l’adjectif est épithète.'),
    ('Le chat (est) ~noir~.', 'Relié au sujet par « être » : il est attribut du sujet.'),
    ('La soupe (semble) ~chaude~.', 'Avec être, sembler, paraître, devenir, rester : attribut.')],
   Q('Ma sœur est contente.', ['attribut du sujet', 'épithète'], 'Il est relié au sujet par le verbe être.', '« contente » est…'),
   [Q('une robe rouge', ['épithète', 'attribut du sujet'], 'Il est collé au nom.', '« rouge » est…'),
    Q('Ces pommes paraissent mûres.', ['attribut du sujet', 'épithète'], 'Il est relié par « paraître ».', '« mûres » est…'),
    Q('un grand arbre', ['épithète', 'attribut du sujet'], 'Il est collé au nom.', '« grand » est…')]))

lecon('G4', ['Les <b>prépositions</b> (à, de, sur, sous, dans, avec, pour, sans, chez…) sont invariables.',
             '<b>le, la, les</b> : déterminant devant un nom, <b>pronom</b> devant un verbe.',
             'Les <b>conjonctions de subordination</b> (quand, si, parce que, comme, lorsque) relient une partie qui dépend de l’autre.'],
 E('conj', 'mots', 'Les prépositions', 'girl', 'Un petit mot invariable, devant un groupe nominal.',
   [('Le livre est |sur| la table.', '« sur » : une préposition.'),
    ('Je vais |à| l’école |avec| mon frère.', 'à, de, sur, sous, dans, avec, pour, sans, chez : des prépositions.'),
    ('Elles ne changent jamais.', 'Ce sont des mots invariables.')],
   C('Le chat dort <sous> le lit.', 'Clique sur la préposition.', 'Un petit mot invariable devant « le lit ».'),
   [C('Je joue <avec> mes amis.', 'Clique sur la préposition.', 'Un petit mot invariable devant « mes amis ».'),
    C('Il part <chez> sa grand-mère.', 'Clique sur la préposition.', 'Un petit mot invariable devant « sa grand-mère ».')]),
 E('verbe', 'etiquette', 'le, la, les : déterminant ou pronom ?', 'boy', 'Je regarde le mot qui suit : un nom ou un verbe ?',
   [('^les^ pommes', 'Devant un nom : un déterminant.'),
    ('Je |les| (mange).', 'Devant un verbe : un pronom, il remplace « les pommes ».'),
    ('Je (vois) ^la^ mer. Je |la| (regarde).', 'Déterminant, puis pronom.')],
   Q('Je la vois.', ['un pronom', 'un déterminant'], 'Il est devant un verbe.', 'Ici, « la » est…'),
   [Q('la fenêtre', ['un déterminant', 'un pronom'], 'Il est devant un nom.', 'Ici, « la » est…'),
    Q('Mes clés ? Je les cherche.', ['un pronom', 'un déterminant'], 'Il est devant un verbe.', 'Ici, « les » est…')]),
 E('conj', 'wagon', 'Les conjonctions de subordination', 'girl', 'Elles relient une partie de phrase qui ne tient pas toute seule.',
   [('Je reste |parce qu’|il pleut.', '« parce qu’il pleut » ne tient pas tout seul.'),
    ('Je sortirai |quand| j’aurai fini.', ''),
    ('Viens |si| tu veux.', 'quand, si, parce que, comme, lorsque, puisque.')],
   C('Je souris <quand> je te vois.', 'Clique sur la conjonction de subordination.', 'Un mot qui relie : quand, si, parce que…'),
   [Q('', ['une conjonction de coordination', 'une conjonction de subordination'], 'mais, ou, et, donc, or, ni, car : coordination.', '« mais » est…'),
    Q('', ['une conjonction de subordination', 'une conjonction de coordination'], 'Comme « quand ».', '« lorsque » est…')]))

lecon('G5', ['Le sujet peut être <b>après le verbe</b>, même dans une question : <i>Que disent les élèves ?</i>',
             'L’<b>attribut du sujet</b> s’accorde avec le sujet : <i>Les fleurs sont belles.</i>'],
 E('pieges', 'deplacer', 'Le sujet après le verbe', 'boy', 'Je cherche le sujet, même après le verbe.',
   [('Que (disent) [les élèves] ?', 'Le sujet est après le verbe : les élèves → ils → -ent.'),
    ('Dans le ciel (volent) [des oiseaux].', 'des oiseaux → ils → -ent.')],
   Q('Que ___ les oiseaux ?', ['chantent', 'chante', 'chantes'], 'Le sujet est « les oiseaux », après le verbe.', 'Complète avec le bon verbe.', fill='v'),
   [Q('Dans la mare ___ des grenouilles.', ['sautent', 'saute', 'sautes'], 'Le sujet est « des grenouilles ».', 'Complète avec le bon verbe.', fill='v'),
    Q('Quand ___ tes parents ?', ['arrivent', 'arrive', 'arrives'], 'Le sujet est « tes parents ».', 'Complète avec le bon verbe.', fill='v')]),
 E('regle', 'remplacer', 'Le sujet et l’attribut', 'girl', 'L’attribut du sujet s’accorde avec le sujet.',
   [('[Les fleurs] (sont) ~belles~.', 'Les fleurs : féminin pluriel, donc belles.'),
    ('[Mon frère] (semble) ~fatigué~.', 'Mon frère : masculin singulier.'),
    ('[Ma sœur] (devient) ~grande~.', 'Ma sœur : féminin singulier.')],
   Q('Les routes sont ___.', ['glissantes', 'glissant', 'glissante'], 'Les routes : féminin pluriel.', 'Complète avec l’attribut bien accordé.', fill='pr'),
   [Q('Ces garçons paraissent ___.', ['heureux', 'heureuse', 'heureuses'], 'Ces garçons : masculin pluriel.', 'Complète avec l’attribut bien accordé.', fill='pr'),
    Q('La porte reste ___.', ['ouverte', 'ouvert', 'ouverts'], 'La porte : féminin singulier.', 'Complète avec l’attribut bien accordé.', fill='pr')]))

lecon('G6', ['Le <b>COI</b> commence par une <b>préposition</b> (à, de) : <i>Je parle à ma voisine.</i>',
             'Les compléments circonstanciels de <b>temps</b> (quand ?), de <b>lieu</b> (où ?), de <b>cause</b> (pourquoi ?).',
             'L’<b>attribut du sujet</b> (avec être, sembler, devenir…) n’est pas un complément d’objet : <i>Paul est un bon élève.</i>'],
 E('cod', 'wagon', 'La préposition du COI', 'girl', 'Le COI commence par une préposition : à, de.',
   [('Je (parle) |à ma voisine|.', 'à ma voisine : un COI, il commence par « à ».'),
    ('Il (rêve) |de vacances|.', 'de vacances : un COI, il commence par « de ».'),
    ('Je (pense) |à toi|.', '')],
   C('Elle téléphone <à sa grand-mère>.', 'Clique sur le COI.', 'Il commence par à ou de.'),
   [C('Nous jouons <aux cartes>.', 'Clique sur le COI.', 'Il commence par « aux » : à + les.'),
    C('Il obéit <à ses parents>.', 'Clique sur le COI.', 'Il commence par « à ».')]),
 E('cc', 'horloge', 'Temps, lieu ou cause ?', 'boy', 'Je pose la question : quand ? où ? pourquoi ?',
   [('|Hier|, je suis allé au cinéma.', 'Quand ? Un complément circonstanciel de temps.'),
    ('Je joue |dans le jardin|.', 'Où ? Un complément circonstanciel de lieu.'),
    ('Il est resté chez lui |à cause de la pluie|.', 'Pourquoi ? Un complément circonstanciel de cause.')],
   Q('Le match est annulé à cause de l’orage.', ['de cause', 'de temps', 'de lieu'], 'Pose la question « pourquoi ? ».', '« à cause de l’orage » : complément circonstanciel…'),
   [Q('Nous partirons le mois prochain.', ['de temps', 'de lieu', 'de cause'], 'Pose la question « quand ? ».', '« le mois prochain » : complément circonstanciel…'),
    Q('Les enfants jouent sous le préau.', ['de lieu', 'de temps', 'de cause'], 'Pose la question « où ? ».', '« sous le préau » : complément circonstanciel…'),
    Q('Il tremble de froid.', ['de cause', 'de lieu', 'de temps'], 'Pose la question « pourquoi ? ».', '« de froid » : complément circonstanciel…')]),
 E('att', 'attention', 'Attribut ou complément d’objet ?', 'girl', 'Avec le verbe être, ce qui suit dit qui est le sujet.',
   [('Paul (est) |un bon élève|.', 'Paul = un bon élève : c’est un attribut du sujet.'),
    ('Paul (aide) |un bon élève|.', 'Ce n’est pas Paul : c’est un complément d’objet.')],
   Q('Ma tante est médecin.', ['attribut du sujet', 'COD'], 'Ma tante = médecin, avec le verbe être.', '« médecin » est…'),
   [Q('Ma tante soigne les enfants.', ['COD', 'attribut du sujet'], 'Ma tante n’est pas les enfants.', '« les enfants » est…'),
    Q('Ce chien devient énorme.', ['attribut du sujet', 'COD'], 'Ce chien = énorme, avec « devenir ».', '« énorme » est…')]))

lecon('G7', ['La chaîne des accords va jusqu’à l’<b>attribut du sujet</b> : <i>Les petites filles sont contentes.</i>'],
 E('chaine', 'liste', 'L’attribut dans la chaîne', 'boy', 'Tout s’accorde : déterminant, adjectif, nom, verbe et attribut.',
   [('^La^ petite fille (est) contente.', 'Au singulier.'),
    ('^Les^ petite*s* fille*s* (sont) content*es*.', 'Au pluriel, toute la chaîne change.')],
   Q('Les chemins sont ___.', ['étroits', 'étroit', 'étroites'], 'Les chemins : masculin pluriel.', 'Complète avec l’attribut bien accordé.', fill='pr'),
   [Q('Mes cousines semblent ___.', ['ravies', 'ravi', 'ravis'], 'Mes cousines : féminin pluriel.', 'Complète avec l’attribut bien accordé.', fill='pr'),
    Q('Ces gâteaux paraissent ___.', ['délicieux', 'délicieuse', 'délicieuses'], 'Ces gâteaux : masculin pluriel.', 'Complète avec l’attribut bien accordé.', fill='pr')]))

# =============================================================== HOMOPHONES (règle des jumeaux : aucun jumeau dans la ceinture)
lecon('H1', ['Le verbe peut être <b>avant le sujet</b>, dans une question : <i>Quel âge a ton frère ?</i> Je prouve encore avec l’imparfait.'],
 E('forme', 'loupe', 'Le verbe avant le sujet', 'girl', 'Dans une question, le verbe peut être avant le sujet.',
   [('Quel âge |a| ton frère ?', 'Le sujet « ton frère » est après le verbe.'),
    ('Quel âge |avait| ton frère ?', 'Je prouve : je dis « avait ».'),
    ('Où |est| ta trousse ? Où |était| ta trousse ?', 'Je prouve avec « était ».')],
   Q('Depuis quand ___ tes voisins ce chien ?', ['ont', 'sont'], 'Je prouve : « avaient ».', 'Complète avec le bon verbe.', fill='circ'),
   [Q('Comme ___ grande, ta sœur !', ['est', 'a'], 'Je prouve : « était ».', 'Complète avec le bon verbe.', fill='circ'),
    Q('Que ___-tu dans ta poche ?', ['as', 'es'], 'Je prouve : « avais ».', 'Complète avec le bon verbe.', fill='circ')]))

lecon('H2', ['<b>qu’elle</b> = que + elle. Je prouve : je remplace par <b>qu’il</b> (au pluriel : qu’elles → qu’ils).'],
 E('mix', 'remplacer', 'qu’elle : que + elle', 'boy', 'qu’elle, c’est « que » + « elle ».',
   [('Je crois |qu’elle| viendra.', 'qu’elle = que + elle.'),
    ('Je crois |qu’il| viendra.', 'Je prouve : je remplace par « qu’il ».'),
    ('Je pense |qu’elles| sont parties.', 'Au pluriel : qu’elles → qu’ils.')],
   Q('Mes sœurs disent ___ veulent jouer.', ['qu’elles', 'qu’elle'], 'Je prouve : « qu’ils ».', 'Complète.', fill='circ'),
   [Q('Ma tante dit ___ arrive demain.', ['qu’elle', 'qu’elles'], 'Je prouve : « qu’il ».', 'Complète.', fill='circ'),
    Q('Il faut ___ se dépêchent, les filles !', ['qu’elles', 'qu’elle'], '« se dépêchent » : pluriel, donc « qu’ils ».', 'Complète.', fill='circ')]))

lecon('H3', ['<b>sans</b> : le contraire de « avec ». Je prouve : je remplace par <b>avec</b>.'],
 E('a', 'non', 'sans : le contraire de avec', 'girl', 'sans est un petit mot qui ne change pas : le contraire de « avec ».',
   [('un gâteau |sans| sucre', 'sans : le contraire de « avec ».'),
    ('un gâteau |avec| du sucre', 'Je prouve : je remplace par « avec ».'),
    ('Il part |sans| son manteau.', '')],
   Q('', ['Je remplace par « avec » : il sort avec son parapluie.', 'Je remplace par « avait ».'], 'sans est le contraire de « avec ».', 'Comment je prouve « sans » dans « Il sort sans parapluie » ?'),
   [Q('Je suis venu ___ mon frère.', ['sans', 'à'], 'Le contraire de « avec ».', 'Complète.', fill='circ'),
    Q('Elle boit son thé ___ lait.', ['sans', 'à'], 'Le contraire de « avec ».', 'Complète.', fill='circ')]))

lecon('H4', ['<b>donc</b> annonce la conséquence. Je prouve : je remplace par <b>alors</b>.'],
 E('inv', 'wagon', 'donc : la conséquence', 'boy', 'donc annonce ce qui arrive ensuite.',
   [('Il pleut, |donc| je prends mon parapluie.', 'donc : la conséquence.'),
    ('Il pleut, |alors| je prends mon parapluie.', 'Je prouve : je remplace par « alors ».'),
    ('J’ai faim, |donc| je mange.', '')],
   Q('Il fait froid, ___ je mets un bonnet.', ['donc', 'ou'], 'Je prouve avec « alors ».', 'Complète.', fill='circ'),
   [Q('J’ai fini mon travail, ___ je peux jouer.', ['donc', 'ou'], 'Je prouve avec « alors ».', 'Complète.', fill='circ'),
    Q('Le magasin ferme, ___ nous rentrons.', ['donc', 'ou'], 'Je prouve avec « alors ».', 'Complète.', fill='circ')]))

lecon('H5', ['<b>dont</b> remplace un nom précédé de <b>de</b> : <i>le livre dont je parle</i> = je parle de ce livre.'],
 E('mix', 'remplacer', 'dont : de + le nom', 'girl', 'dont remplace un nom avec « de ».',
   [('le livre |dont| je te parle', 'Je parle de ce livre.'),
    ('la fille |dont| le chien aboie', 'Le chien de la fille.'),
    ('un jeu |dont| je connais les règles', 'Les règles de ce jeu.')],
   Q('C’est l’ami ___ je t’ai parlé.', ['dont', 'qui', 'que'], 'Je t’ai parlé de cet ami.', 'Complète.', fill='circ'),
   [Q('Voici la maison ___ le toit est rouge.', ['dont', 'que', 'qui'], 'Le toit de la maison.', 'Complète.', fill='circ'),
    Q('C’est un outil ___ j’ai besoin.', ['dont', 'que', 'qui'], 'J’ai besoin de cet outil.', 'Complète.', fill='circ')]))

lecon('H6', ['<b>quel, quelle, quels, quelles</b> s’accordent avec le nom : <i>Quelle belle robe !</i>'],
 E('acc', 'etiquette', 'quel s’accorde', 'boy', 'quel s’accorde avec le nom qui suit.',
   [('|Quel| beau dessin !', 'dessin : masculin singulier.'),
    ('|Quelle| belle robe !', 'robe : féminin singulier.'),
    ('|Quels| jolis chats ! |Quelles| belles fleurs !', 'Au pluriel : quels, quelles.')],
   Q('___ fleurs préfères-tu ?', ['Quelles', 'Quel', 'Quels'], 'fleurs : féminin pluriel.', 'Complète.', fill='circ'),
   [Q('___ âge as-tu ?', ['Quel', 'Quelle', 'Quels'], 'âge : masculin singulier.', 'Complète.', fill='circ'),
    Q('___ histoire incroyable !', ['Quelle', 'Quel', 'Quelles'], 'histoire : féminin singulier.', 'Complète.', fill='circ')]))

lecon('H7', ['<b>s’en</b> = se + en, devant un verbe : <i>il s’en va</i>. Je prouve : <b>je m’en vais</b>.'],
 E('sest', 'remplacer', 's’en : se + en', 'girl', 's’en = « se » + « en », devant un verbe.',
   [('Il |s’en| va.', 's’en = se + en.'),
    ('Je |m’en| vais. Tu |t’en| vas. Il |s’en| va.', 'Je prouve : je change de personne.'),
    ('Elle |s’en| souvient.', '')],
   Q('Le chat ___ va.', ['s’en', 'se'], 'Je prouve : « je m’en vais ».', 'Complète.', fill='circ'),
   [Q('Elle ___ souvient très bien.', ['s’en', 'se'], 'Je prouve : « je m’en souviens ».', 'Complète.', fill='circ'),
    Q('Mon frère ___ moque.', ['s’en', 's’est'], 'Je prouve : « je m’en moque ».', 'Complète.', fill='circ')]))

lecon('H8', ['Les nouvelles paires du CM2 : <b>sans / s’en</b>, <b>donc / dont</b>, <b>quel / qu’elle</b>.'],
 E('autres', 'liste', 'Les paires du CM2', 'boy', 'Pour chaque mot, je fais la preuve.',
   [('|sans| ou |s’en|', 'sans → avec ; s’en → je m’en.'),
    ('|donc| ou |dont|', 'donc → alors ; dont → de + le nom.'),
    ('|quel| ou |qu’elle|', 'quel → quelle, quels ; qu’elle → qu’il.')],
   Q('Il part ___ dire au revoir.', ['sans', 's’en'], 'Je prouve : « avec ».', 'Complète.', fill='circ'),
   [Q('Elle ___ souvient.', ['s’en', 'sans'], 'Je prouve : « je m’en souviens ».', 'Complète.', fill='circ'),
    Q('Je pense ___ a raison.', ['qu’elle', 'quelle'], 'Je prouve : « qu’il ».', 'Complète.', fill='circ'),
    Q('C’est le livre ___ je rêvais.', ['dont', 'donc'], 'Je rêvais de ce livre.', 'Complète.', fill='circ')]))

# =============================================================== VOCABULAIRE
lecon('V1', ['Le mot-étiquette s’appelle aussi <b>mot générique</b> ; les mots précis sont des <b>mots spécifiques</b>.',
             'Un mot peut être spécifique et générique à la fois : <i>véhicule → voiture → cabriolet</i>.'],
 E('echelle', 'liste', 'Générique ou spécifique ?', 'girl', 'Un mot générique regroupe ; un mot spécifique est précis.',
   [('|instrument| : piano, violon, flûte', '« instrument » : un mot générique.'),
    ('piano, violon, flûte', 'Ce sont des mots spécifiques.'),
    ('|véhicule| → |voiture| → |cabriolet|', '« voiture » est spécifique pour véhicule, et générique pour cabriolet.')],
   Q('', ['légume', 'carotte', 'poireau'], 'Il regroupe les autres.', 'Quel est le mot générique ?'),
   [Q('', ['outil', 'marteau', 'scie'], 'Il regroupe les autres.', 'Quel est le mot générique ?'),
    Q('', ['mammifère', 'baleine', 'chien'], 'Il regroupe les autres.', 'Quel est le mot générique ?')]))

lecon('V2', ['Quand les indices ne suffisent pas, j’utilise le <b>dictionnaire</b> (papier ou numérique).',
             'Les mots sont rangés dans l’<b>ordre alphabétique</b> ; l’article donne la classe du mot (n., v., adj.), la définition et un exemple.',
             'Si le mot a plusieurs sens, je choisis celui qui va avec la phrase.'],
 E('methode', 'liste', 'Le dictionnaire', 'girl', 'Je cherche le mot dans l’ordre alphabétique.',
   [('|abeille| · |avion| · |azur|', 'Même première lettre : je regarde la deuxième.'),
    ('Les mots-repères en haut de la page', 'Ils donnent le premier et le dernier mot de la page.'),
    ('fournil, n. m. : pièce où le boulanger cuit le pain.', 'n. m. : nom masculin ; puis la définition.')],
   Q('', ['bateau, bille, bus', 'bille, bateau, bus', 'bus, bille, bateau'], 'Regarde la deuxième lettre : a, i, u.', 'Quel est l’ordre alphabétique ?'),
   [Q('', ['un verbe', 'un nom', 'un adjectif'], '« v. » veut dire verbe.', 'Dans le dictionnaire, « galoper, v. » : galoper est…'),
    Q('', ['la définition', 'l’exemple', 'la classe du mot'], 'Elle explique le sens du mot.', '« pièce où le boulanger cuit le pain » est…')]),
 E('att', 'loupe', 'Plusieurs sens : je choisis', 'boy', 'Le dictionnaire donne parfois plusieurs sens : je choisis grâce à la phrase.',
   [('feuille : 1. partie d’une plante. 2. morceau de papier.', 'Deux sens numérotés.'),
    ('J’écris sur une |feuille|.', 'Ici, c’est le sens 2.')],
   Q('La feuille du chêne est tombée.', ['le sens 1 : partie d’une plante', 'le sens 2 : morceau de papier'], 'Lis toute la phrase.', 'Quel sens du dictionnaire ?'),
   [Q('Prends une feuille et un crayon.', ['le sens 2 : morceau de papier', 'le sens 1 : partie d’une plante'], 'Lis toute la phrase.', 'Quel sens du dictionnaire ?')]))

lecon('V3', ['Des <b>racines latines et grecques</b> : télé (loin), aqua (l’eau), bio (la vie), géo (la Terre).',
             'Je <b>classe</b> préfixes et suffixes par sens : le contraire (dé-, in-, mal-), à nouveau (re-), la personne (-eur, -iste, -ier), petit (-ette, -on).'],
 E('mot', 'loupe', 'Des racines latines et grecques', 'girl', 'Certains morceaux de mots viennent du latin ou du grec.',
   [('|télé|phone · |télé|scope', 'télé : loin.'),
    ('|aqua|rium · |aqua|tique', 'aqua : l’eau.'),
    ('|bio|logie · |géo|graphie', 'bio : la vie ; géo : la Terre.')],
   Q('', ['la Terre', 'l’eau', 'la vie'], 'Pense à « géographie ».', 'Dans « géologie », « géo » veut dire…'),
   [Q('', ['loin', 'petit', 'à nouveau'], 'Pense à « téléphone ».', 'Dans « télécommande », « télé » veut dire…'),
    Q('', ['l’eau', 'le feu', 'l’air'], 'Pense à « aquarium ».', 'Dans « aquatique », « aqua » veut dire…')]),
 E('sens', 'liste', 'Je classe par sens', 'boy', 'Je range les préfixes et les suffixes selon leur sens.',
   [('|dé|faire · |in|connu · |mal|honnête', 'Le contraire.'),
    ('chant|eur| · fleur|iste| · boulang|er|', 'La personne, le métier.'),
    ('fill|ette| · ch|aton|', 'Petit.')],
   Q('', ['le contraire', 'à nouveau', 'une personne'], 'Pense à « déplier ».', 'Les préfixes dé-, in-, mal- expriment…'),
   [Q('', ['une personne ou un métier', 'petit', 'le contraire'], 'chanteur, fleuriste…', 'Les suffixes -eur, -iste, -ier expriment…'),
    Q('', ['petit', 'le contraire', 'à nouveau'], 'fillette, maisonnette…', 'Le suffixe -ette exprime…')]))

lecon('V4', ['Un mot peut être <b>simple</b> (terre), <b>dérivé</b> (terrain, enterrer) ou <b>composé</b> (pomme de terre, porte-monnaie).'],
 E('trouver', 'ciseaux', 'Simple, dérivé ou composé ?', 'girl', 'Je regarde comment le mot est fabriqué.',
   [('|terre|', 'Un mot simple : on ne peut pas le couper.'),
    ('|terr|ain · en|terr|er', 'Des mots dérivés : un mot simple + un préfixe ou un suffixe.'),
    ('pomme de terre · porte-monnaie', 'Des mots composés : plusieurs mots réunis.')],
   Q('', ['un mot dérivé', 'un mot simple', 'un mot composé'], 'jardin + -ier', '« jardinier » est…'),
   [Q('', ['un mot composé', 'un mot dérivé', 'un mot simple'], 'arc + en + ciel', '« arc-en-ciel » est…'),
    Q('', ['un mot simple', 'un mot dérivé', 'un mot composé'], 'On ne peut pas le couper.', '« lune » est…')]))

lecon('V5', ['Le <b>champ lexical</b> : les mots qui parlent d’un même thème, de toutes les classes (<i>mer : vague, plage, nager, salé</i>).'],
 E('syn', 'mots', 'Le champ lexical', 'boy', 'Des mots qui parlent du même thème.',
   [('|vague| · |plage| · |sable| · |coquillage|', 'Ils parlent tous de la mer.'),
    ('|nager| · |salé| · |marin|', 'Des verbes et des adjectifs aussi : c’est le champ lexical de la mer.'),
    ('Dans un texte, il crée une ambiance.', '')],
   Q('', ['flocon', 'plage', 'tondeuse'], 'Pense au froid et à la neige.', 'Quel mot appartient au champ lexical de l’hiver ?'),
   [Q('', ['l’école', 'la forêt', 'la mer'], 'cartable, maîtresse, récréation…', '« cartable, maîtresse, récréation » : quel champ lexical ?'),
    Q('', ['sapin', 'dauphin', 'cartable'], 'Pense aux arbres.', 'Quel mot appartient au champ lexical de la forêt ?')]))

lecon('V6', ['Un mot <b>polysémique</b> a plusieurs sens proches : <i>la tête d’une personne, la tête de la course, la tête d’un clou</i>.',
             'Homonymes : deux mots différents, même son. Polysémie : un seul mot, plusieurs sens.'],
 E('pareil', 'etiquette', 'Un mot, plusieurs sens', 'girl', 'Un même mot peut avoir plusieurs sens proches.',
   [('la |tête| d’une personne', 'une partie du corps'),
    ('la |tête| de la course', 'la première place'),
    ('la |tête| d’un clou', 'le haut : « tête » est un mot polysémique.')],
   Q('Elle est en tête de la course.', ['la première place', 'la partie du corps'], 'Lis toute la phrase.', 'Ici, « tête » veut dire…'),
   [Q('Le pied de la table est cassé.', ['le bas qui soutient', 'la partie du corps'], 'Lis toute la phrase.', 'Ici, « pied » veut dire…'),
    Q('La souris de l’ordinateur ne marche plus.', ['un objet pour cliquer', 'un petit animal'], 'Lis toute la phrase.', 'Ici, « souris » veut dire…')]),
 E('reb', 'liste', 'Homonymes ou polysémie ?', 'boy', 'Deux mots différents, ou un seul mot avec plusieurs sens ?',
   [('|verre| · |vert|', 'Deux mots différents, même son : des homonymes.'),
    ('la |tête| de la course · ma |tête|', 'Un seul mot, plusieurs sens : la polysémie.')],
   Q('la feuille de l’arbre · la feuille de papier', ['un mot polysémique', 'deux homonymes'], 'Un seul mot qui a plusieurs sens.', '« feuille » est…'),
   [Q('le ver de terre · le verre d’eau', ['deux homonymes', 'un mot polysémique'], 'Deux mots différents, même son.', 'Ce sont…')]))

# =============================================================== CONJUGAISON
lecon('C1', ['Des <b>radicaux qui changent</b> aussi au 3e groupe : <i>je peux, nous pouvons, ils peuvent</i>.'],
 E('verbes', 'attention', 'Des radicaux qui changent au 3e groupe', 'girl', 'Pour certains verbes, le radical change avec la personne.',
   ['je peu§x§ · nous pouv§ons§ · ils peuv§ent§',
    'je vien§s§ · nous ven§ons§ · ils vienn§ent§',
    ('je prend§s§ · nous pren§ons§ · ils prenn§ent§', 'Le radical change : je les apprends.')],
   Q('Nous ___ venir.', ['pouvons', 'peuvons', 'pouvez'], 'Avec nous, le radical est pouv-.', 'Complète avec « pouvoir ».', fill='v'),
   [Q('Ils ___ à l’école.', ['viennent', 'venent', 'vienent'], 'Avec ils, le radical est vienn-.', 'Complète avec « venir ».', fill='v'),
    Q('Elles ___ le bus.', ['prennent', 'prenent', 'prendent'], 'Avec elles, le radical est prenn-.', 'Complète avec « prendre ».', fill='v')]))

lecon('C2', ['Dans la terminaison : la <b>marque du temps</b> (r pour le futur) et la <b>marque de personne</b> (ai, as, a, ons, ez, ont).'],
 E('term', 'loupe', 'Marque de temps, marque de personne', 'boy', 'La terminaison a deux morceaux.',
   [('je chante|r|§ai§', 'r : la marque du futur ; ai : la marque de personne.'),
    ('nous fini|r|§ons§', 'La marque du futur ne change pas.'),
    ('vous chante|r|§ez§', 'La marque de personne change avec le sujet.')],
   Q('', ['r', 'ons', 'chant'], 'La marque du futur est toujours la même.', 'Dans « nous chanterons », quelle est la marque du futur ?'),
   [Q('', ['ez', 'r', 'chante'], 'Elle change avec la personne.', 'Dans « vous chanterez », quelle est la marque de personne ?')]))

lecon('C3', ['Les <b>temps du récit</b> : l’imparfait décrit le décor, le <b>passé simple</b> raconte les actions.',
             'Passé simple du 1er groupe : je chantai, tu chantas, il chanta, nous chantâmes, vous chantâtes, ils chantèrent.',
             'être : je fus, il fut, ils furent ; avoir : j’eus, il eut, ils eurent.'],
 E('quand', 'horloge', 'Les temps du récit', 'girl', 'Dans un récit, l’imparfait et le passé simple travaillent ensemble.',
   [('Il |faisait| beau.', 'L’imparfait décrit le décor.'),
    ('Soudain, l’orage |éclata|.', 'Le passé simple raconte une action.'),
    ('On le trouve surtout dans les livres, avec il et ils.', '')],
   Q('Soudain, le loup sortit du bois.', ['le passé simple', 'l’imparfait', 'le futur'], 'Une action soudaine, dans un récit.', '« sortit » est au…'),
   [Q('La nuit était noire.', ['l’imparfait', 'le passé simple', 'le futur'], 'Il décrit le décor.', '« était » est à…')]),
 E('term', 'liste', 'Le passé simple du 1er groupe', 'boy', 'Au passé simple, les verbes en -er ont des terminaisons en a.',
   ['je chant§ai§ · tu chant§as§ · il chant§a§',
    'nous chant§âmes§ · vous chant§âtes§ · ils chant§èrent§',
    ('Il march§a§ longtemps. Ils arriv§èrent§ le soir.', 'Avec il : -a ; avec ils : -èrent.')],
   Q('Ils ___ le château.', ['visitèrent', 'visitaient', 'visiteront'], 'Passé simple, avec ils : -èrent.', 'Complète avec « visiter » au passé simple.', fill='v'),
   [Q('Le loup ___ la porte.', ['poussa', 'poussait', 'poussera'], 'Passé simple, avec il : -a.', 'Complète avec « pousser » au passé simple.', fill='v'),
    Q('Nous ___ la rivière.', ['traversâmes', 'traversions', 'traverserons'], 'Passé simple, avec nous : -âmes.', 'Complète avec « traverser » au passé simple.', fill='v')]),
 E('etre', 'point', 'être et avoir au passé simple', 'girl', 'être et avoir sont à connaître par cœur.',
   [('je |fus| · il |fut| · ils |furent|', 'être'),
    ('j’|eus| · il |eut| · ils |eurent|', 'avoir'),
    ('Il |fut| surpris. Ils |eurent| peur.', '')],
   Q('Le roi ___ très en colère.', ['fut', 'eut', 'furent'], 'être au passé simple, avec il.', 'Complète avec « être » au passé simple.', fill='v'),
   [Q('Les enfants ___ froid.', ['eurent', 'furent', 'eut'], 'avoir au passé simple, avec ils.', 'Complète avec « avoir » au passé simple.', fill='v'),
    Q('Nous ___ les premiers.', ['fûmes', 'eûmes', 'furent'], 'être au passé simple, avec nous.', 'Complète avec « être » au passé simple.', fill='v')]))

lecon('C4', ['Avec avoir, le participe passé s’accorde avec le <b>COD placé avant</b> le verbe : <i>Les pommes, je les ai mangées.</i>',
             'À la forme négative, ne… pas encadre l’<b>auxiliaire</b> : <i>je n’ai pas mangé</i>.'],
 E('pp', 'attention', 'Le COD placé avant', 'boy', 'Avec avoir, je regarde où est le COD.',
   [('J’ai mangé les pommes.', 'Le COD est après le verbe : pas d’accord.'),
    ('Les pommes, je |les| ai mangé*es*.', 'Le COD « les » est avant : le participe s’accorde avec lui.'),
    ('La lettre ? Je |l’|ai écrit*e*.', 'l’ = la lettre : féminin singulier.')],
   Q('Ces fleurs, je les ai ___.', ['cueillies', 'cueilli', 'cueillis'], '« les » = ces fleurs, placé avant : féminin pluriel.', 'Complète.', fill='v'),
   [Q('J’ai ___ deux gâteaux.', ['mangé', 'mangés'], 'Le COD est après le verbe : pas d’accord.', 'Complète.', fill='v'),
    Q('Ta robe ? Je l’ai ___.', ['lavée', 'lavé', 'lavées'], 'l’ = ta robe : féminin singulier.', 'Complète.', fill='v')]))

lecon('C5', ['Avec être, le participe s’accorde avec le sujet, même quand le sujet est <b>après le verbe</b> : <i>Hier sont arrivées mes cousines.</i>'],
 E('accord', 'deplacer', 'Le sujet après le verbe', 'girl', 'Je cherche le sujet, même après le verbe.',
   [('Hier sont arrivé*es* [mes cousines].', 'Qui est arrivé ? mes cousines : féminin pluriel.'),
    ('Où est allé*e* [ta sœur] ?', 'ta sœur : féminin singulier.')],
   Q('Dans la cour sont ___ les filles.', ['entrées', 'entré', 'entrés'], 'Le sujet « les filles » est après le verbe.', 'Complète.', fill='v'),
   [Q('Quand est ___ ta tante ?', ['partie', 'parti', 'parties'], 'Le sujet « ta tante » est après le verbe.', 'Complète.', fill='v'),
    Q('Au loin sont ___ les bateaux.', ['apparus', 'apparu', 'apparues'], 'Le sujet « les bateaux » est après le verbe.', 'Complète.', fill='v')]))

lecon('C8', ['Deux temps de plus : le <b>plus-que-parfait</b> (C6) et le <b>passé simple</b> (C3 et C7).'],
 E('reperes', 'horloge', 'Les temps du CM2', 'boy', 'Je reconnais aussi le plus-que-parfait et le passé simple.',
   [('il |avait chanté|', 'avoir à l’imparfait + participe passé : le plus-que-parfait.'),
    ('il |chanta|', 'Un seul mot : le passé simple.')],
   Q('Elles étaient parties.', ['le plus-que-parfait', 'le passé composé', 'l’imparfait'], 'Auxiliaire à l’imparfait + participe passé.', 'Quel temps ?'),
   [Q('Il arriva.', ['le passé simple', 'l’imparfait', 'le futur'], 'Un seul mot, terminaison en -a.', 'Quel temps ?'),
    Q('Nous avons fini.', ['le passé composé', 'le plus-que-parfait', 'le passé simple'], 'Auxiliaire au présent + participe passé.', 'Quel temps ?')]))

# =============================================================== ORTHOGRAPHE
lecon('O1', ['Les préfixes <b>en-</b> et <b>in-</b> deviennent <b>em-</b> et <b>im-</b> devant m, b, p : emporter, impossible, immangeable.'],
 E('regle', 'liste', 'Avec un préfixe', 'girl', 'Le préfixe en- ou in- suit la règle aussi.',
   [('%em%|p|orter · %em%|b|arquer · %im%|p|ossible', 'Devant m, b, p : em-, im-.'),
    ('%in%|u|tile · %en%|l|ever', 'Devant les autres lettres : in-, en-.'),
    ('%im%|m|angeable · %em%|m|ener', 'Devant m aussi.')],
   Q('___buvable', ['im', 'in'], 'Après, il y a un b.', 'Complète : im ou in ?', fill=H),
   [Q('___patient', ['im', 'in'], 'Après, il y a un p.', 'Complète : im ou in ?', fill=H),
    Q('___capable', ['in', 'im'], 'Après, il y a un c.', 'Complète : im ou in ?', fill=H)]))

lecon('O2', ['Des familles moins faciles : accro<b>c</b> → accrocher, respe<b>ct</b> → respecter, fusi<b>l</b> → fusiller.'],
 E('famille', 'mots', 'Des familles moins faciles', 'boy', 'Je cherche bien : un mot de la famille fait entendre la lettre.',
   [('un accro%c% → accro|c|her', 'Dans « accrocher », j’entends c.'),
    ('le respe%ct% → respe|ct|er', 'Deux lettres muettes !'),
    ('un fusi%l% → fusi|ll|er', '')],
   Q('un tapi___', ['s', 't', 'x'], 'Pense à « tapisser ».', 'Quelle lettre muette faut-il écrire ?', fill=H),
   [Q('un ban___', ['c', 't', 's'], 'Pense à « banquette ».', 'Quelle lettre muette faut-il écrire ?', fill=H),
    Q('un clima___', ['t', 's', 'x'], 'Pense à « climatique ».', 'Quelle lettre muette faut-il écrire ?', fill=H)]))

lecon('O3', ['Le son « s » peut s’écrire <b>t</b> devant -ion : attention, opération, récréation.'],
 E('c', 'attention', '-tion : le t fait « s »', 'girl', 'Devant -ion, le t fait souvent le son « s ».',
   [('une atten%t%|i|on', 'Devant -ion, le t fait « s ».'),
    ('une opéra%t%|i|on · la récréa%t%|i|on', ''),
    ('une pa%ss%ion · une émi%ss%ion', 'Mais certains mots s’écrivent -ssion : je les mémorise.')],
   Q('une addi___ion', ['t', 'ss', 'c'], 'Le mot finit par -tion.', 'Complète avec la bonne lettre.', fill=H),
   [Q('la na___ion', ['t', 'ss', 'c'], 'Le mot finit par -tion.', 'Complète avec la bonne lettre.', fill=H),
    Q('une pro___ection', ['t', 'ss', 'c'], 'Ici, le t ne fait pas « s » : pro-tec-tion.', 'Complète avec la bonne lettre.', fill=H)]))

lecon('O4', ['Le son « k » s’écrit parfois <b>ch</b> (chorale, orchestre) ou <b>cc</b> (accord, occuper).'],
 E('k', 'etiquette', 'ch et cc', 'boy', 'Quelques mots écrivent le son « k » autrement.',
   [('une %ch%orale · un or%ch%estre', 'ch : des mots à mémoriser.'),
    ('un a%cc%ord · o%cc%uper', 'cc devant a, o, u.'),
    ('un a%cc%ident', 'Attention : cc devant i fait « ks ».')],
   Q('', ['une chorale', 'une korale', 'une corale'], 'Un mot avec ch.', 'Quel mot est bien écrit ?'),
   [Q('', ['accompagner', 'acompagner'], 'cc devant o.', 'Quel mot est bien écrit ?'),
    Q('', ['un orchestre', 'un orkestre'], 'Un mot avec ch.', 'Quel mot est bien écrit ?')]))

lecon('O5', ['Dans les verbes en <b>-guer</b>, le u reste partout : nous naviguons, il conjuguait.'],
 E('gu', 'remplacer', 'Les verbes en -guer', 'girl', 'Dans les verbes en -guer, le u reste à toutes les personnes.',
   [('nous navi%gu%|o|ns', 'Le verbe est « naviguer » : le u reste.'),
    ('il fati%gu%|a|it', ''),
    ('nous conju%gu%|o|ns', 'Même devant a et o.')],
   Q('nous conju___ons', ['gu', 'g', 'ge'], 'Le verbe est « conjuguer » : le u reste.', 'Complète avec les bonnes lettres.', fill=H),
   [Q('il distin___ait', ['gu', 'g', 'ge'], 'Le verbe est « distinguer ».', 'Complète avec les bonnes lettres.', fill=H),
    Q('nous dialo___ons', ['gu', 'g', 'ge'], 'Le verbe est « dialoguer ».', 'Complète avec les bonnes lettres.', fill=H)]))

lecon('O6', ['Masculin <b>-eil, -ail, -euil</b> ; féminin <b>-eille, -aille, -euille</b>. Après c ou g : <b>-ueil</b> (accueil, orgueil).'],
 E('ill', 'attention', '-eil ou -eille ?', 'boy', 'Le nom est masculin ou féminin ?',
   [('le révei%l% · la boutei%lle%', 'Masculin : -eil ; féminin : -eille.'),
    ('un fauteu%il% · une feu%ille%', ''),
    ('un acc%ueil% · l’org%ueil%', 'Après c ou g : -ueil.')],
   Q('une corb___', ['eille', 'eil'], 'C’est un nom féminin.', 'Complète avec les bonnes lettres.', fill=H),
   [Q('un appar___', ['eil', 'eille'], 'C’est un nom masculin.', 'Complète avec les bonnes lettres.', fill=H),
    Q('un acc___', ['ueil', 'euil'], 'Après c : -ueil.', 'Complète avec les bonnes lettres.', fill=H)]))

D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'sortie')
os.makedirs(D, exist_ok=True)
json.dump(OUT, open(os.path.join(D, 'CM2_PLUS.json'), 'w'), ensure_ascii=False, indent=1)
print(len(OUT), 'leçons,', sum(len(v['ecrans']) for v in OUT.values()), 'écrans CM2,',
      sum(len(e['plus']) + 1 for v in OUT.values() for e in v['ecrans']), 'exercices')
