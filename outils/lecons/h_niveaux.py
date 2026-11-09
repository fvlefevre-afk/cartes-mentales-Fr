from niveaux_lib import *
def f(p, bon, mal, h, fill='circ'): return C(p, 'Complète avec le bon mot.', bon, mal, h, fill)
def f2(p, bon, mal, h, fill='circ'): return C(p, 'Premier trou :', bon, mal, h, fill)
def v(p, bon, mal, h): return C(p, '', bon, mal, h, 'v')
def ph(bon, mal, h='Je vérifie chaque mot.', ask='Quelle phrase est bien écrite ?'): return C('', ask, bon, mal, h)
def hier(p, bon, mal): return C(p, 'Avec « hier », je dis :', bon, mal, 'Hier : le mot change, c’est bien le verbe.')
def hi(p, h): return K(p, 'Clique sur le mot.', h)
H = {}
H['H1'] = {
 'Le verbe avoir': (
  [v('Mon frère ___ un nouveau ballon.', 'a', ['as', 'ai'], 'Mon frère = il : il a.'), v('Les élèves ___ un exposé demain.', 'ont', ['a', 'as'], 'Les élèves = ils : ils ont.'), v('J’___ mal au dos.', 'ai', ['as', 'a'], 'Avec « je » : j’ai.'), v('Tu ___ un beau cartable.', 'as', ['a', 'ai'], 'Avec « tu » : tu as.')],
  [v('Hier, mes cousins ___ passé une journée entière chez nous.', 'ont', ['a', 'as'], 'Mes cousins = ils : ils ont.'), v('Chaque soir, ma grand-mère ___ le temps de nous lire une histoire.', 'a', ['as', 'ai'], 'Ma grand-mère = elle : elle a.'),
   v('Aujourd’hui, tu ___ de la chance : le soleil brille.', 'as', ['a', 'ai'], 'Avec « tu » : tu as.'), v('Depuis ce matin, j’___ une idée pour la fête.', 'ai', ['as', 'a'], 'Avec « je » : j’ai.')]),
 'Le verbe être': (
  [v('Les nuages ___ gris.', 'sont', ['est', 'es'], 'Les nuages = ils : ils sont.'), v('Tu ___ très gentil.', 'es', ['est', 'suis'], 'Avec « tu » : tu es.'), v('Je ___ content.', 'suis', ['es', 'est'], 'Avec « je » : je suis.'), v('Mon voisin ___ boulanger.', 'est', ['es', 'sont'], 'Mon voisin = il : il est.')],
  [v('Dans la cour, les élèves ___ très nombreux ce matin.', 'sont', ['est', 'es'], 'Les élèves = ils : ils sont.'), v('Depuis longtemps, tu ___ le meilleur de la classe.', 'es', ['est', 'suis'], 'Avec « tu » : tu es.'),
   v('Aujourd’hui, je ___ fatigué après la longue randonnée.', 'suis', ['es', 'est'], 'Avec « je » : je suis.'), v('Le facteur ___ toujours ponctuel pour distribuer le courrier.', 'est', ['es', 'sont'], 'Le facteur = il : il est.')]),
 'Je vérifie avec « hier »': (
  [hier('Léa a faim.', 'Hier, Léa avait faim.', ['Hier, Léa était faim.']), hier('Mes parents sont fatigués.', 'Hier, mes parents étaient fatigués.', ['Hier, mes parents avaient fatigués.']),
   hier('Tu es en retard.', 'Hier, tu étais en retard.', ['Hier, tu avais en retard.']), hier('Les enfants ont soif.', 'Hier, les enfants avaient soif.', ['Hier, les enfants étaient soif.'])],
  [hier('Mon grand-père a mal au dos depuis longtemps.', 'Hier, mon grand-père avait mal au dos depuis longtemps.', ['Hier, mon grand-père était mal au dos depuis longtemps.']), hier('Les jumeaux sont très heureux de partir.', 'Hier, les jumeaux étaient très heureux de partir.', ['Hier, les jumeaux avaient très heureux de partir.']),
   hier('Tu as de la chance aujourd’hui.', 'Hier, tu avais de la chance.', ['Hier, tu étais de la chance.']), hier('Nos voisins sont absents pendant les vacances.', 'Hier, nos voisins étaient absents.', ['Hier, nos voisins avaient absents.'])]),
 'Je change le sujet': (
  [v('Mon frère est grand. Mes frères ___ grands.', 'sont', ['est', 'ont'], 'Mes frères = ils : ils sont.'), v('Le chat a faim. Les chats ___ faim.', 'ont', ['a', 'sont'], 'Les chats = ils : ils ont.'),
   v('Elle est contente. Elles ___ contentes.', 'sont', ['est', 'ont'], 'Elles : elles sont.'), v('Il a un vélo. Ils ___ un vélo.', 'ont', ['a', 'sont'], 'Ils : ils ont.')],
  [v('Le petit garçon est fatigué après la course. Les petits garçons ___ fatigués après la course.', 'sont', ['est', 'ont'], 'Les petits garçons = ils : ils sont.'), v('La voisine a un grand jardin. Les voisines ___ un grand jardin.', 'ont', ['a', 'sont'], 'Les voisines = elles : elles ont.'),
   v('Ma sœur est malade depuis hier. Mes sœurs ___ malades depuis hier.', 'sont', ['est', 'ont'], 'Mes sœurs = elles : elles sont.'), v('Le chat a trop mangé. Les chats ___ trop mangé.', 'ont', ['a', 'sont'], 'Les chats = ils : ils ont.')]),
 'Le sujet, puis le sens': (
  [v('Léa ___ une nouvelle robe.', 'a', ['est'], 'Le sens : elle possède une robe, c’est avoir.'), v('Les enfants ___ contents.', 'sont', ['ont'], 'Le sens : comment ils sont, c’est être.'), v('Mes amis ___ un chien.', 'ont', ['sont'], 'Le sens : ils possèdent un chien, c’est avoir.'), v('Je ___ malade.', 'suis', ['ai'], 'Le sens : comment je suis, c’est être.')],
  [v('Depuis ce matin, mon père ___ très occupé.', 'est', ['a'], 'Le sens : comment il est, c’est être.'), v('Les voisins ___ un grand jardin derrière leur maison.', 'ont', ['sont'], 'Le sens : ils possèdent, c’est avoir.'),
   v('Ce soir, les élèves de la classe ___ prêts pour la fête.', 'sont', ['ont'], 'Le sens : comment ils sont, c’est être.'), v('Chaque année, ma sœur ___ un cadeau pour chaque anniversaire.', 'a', ['est'], 'Le sens : elle reçoit, c’est avoir.')]),
 'Le sujet se cache': (
  [v('Où ___ mes lunettes ?', 'sont', ['ont', 'est'], 'Le sujet est « mes lunettes » : pluriel.'), v('Dans la cour, les élèves ___ nombreux.', 'sont', ['ont', 'est'], 'Le sujet est « les élèves » : pluriel.'),
   v('Les clés de mon frère ___ introuvables.', 'sont', ['ont', 'est'], 'Le sujet est « les clés » : pluriel.'), v('Les chats de mes voisins ___ souvent faim.', 'ont', ['sont', 'a'], 'Le sujet est « les chats » : pluriel ; avoir faim.')],
  [v('Quel âge ___ vos grands-parents ?', 'ont', ['sont', 'est'], 'Le sujet est « vos grands-parents » : pluriel ; avoir un âge.'), v('Dans le fond de la salle ___ les élèves de CM2.', 'sont', ['ont', 'est'], 'Le sujet est « les élèves » : pluriel.'),
   v('Les amis de ma sœur ___ toujours un grand sourire.', 'ont', ['sont', 'est'], 'Le sujet est « les amis » : pluriel ; avoir un sourire.'), v('Les livres que j’ai empruntés hier ___ très intéressants.', 'sont', ['ont', 'est'], 'Le sujet est « les livres » : pluriel.')]),
 'Je retiens': (
  [f2('Mon frère ___ un vélo. Il ___ rouge.', 'a', ['est'], 'Premier : il possède, avoir.', 'v'), f2('Les enfants ___ des bonbons. Ils ___ contents.', 'ont', ['sont'], 'Premier : ils possèdent, avoir.', 'v'),
   f2('Tu ___ des amis. Tu ___ chanceux.', 'as', ['es'], 'Premier : tu possèdes, avoir.', 'v'), f2('Mes sœurs ___ grandes. Elles ___ de la chance.', 'sont', ['ont'], 'Premier : comment elles sont, être.', 'v')],
  [f2('Mes cousins ___ une grande maison. Ils ___ très fiers de leur jardin.', 'ont', ['sont'], 'Premier : ils possèdent, avoir.', 'v'), f2('Ma tante ___ très gentille. Elle ___ toujours un mot aimable.', 'est', ['a'], 'Premier : comment elle est, être.', 'v'),
   f2('Tu ___ en avance. Tu ___ du temps pour finir.', 'es', ['as'], 'Premier : comment tu es, être.', 'v'), f2('Les voisins ___ un chien. Ils ___ tous très gentils.', 'ont', ['sont'], 'Premier : ils possèdent, avoir.', 'v')]),
}
H['H2'] = {
 'on remplace des personnes': (
  [f('Ce matin, ___ mange des crêpes.', 'on', ['là', 'où'], 'On remplace des personnes.'), f('Chez nous, ___ joue aux cartes.', 'on', ['là', 'où'], 'On remplace des personnes.'), f('Demain, ___ part en vacances.', 'on', ['là', 'où'], 'On remplace des personnes.'), f('Dans ma famille, ___ chante souvent.', 'on', ['là', 'où'], 'On remplace des personnes.')],
  [f('Quand il pleut, ___ reste volontiers dans le salon.', 'on', ['là', 'où'], 'On remplace des personnes : on = nous, les gens.'), f('Chaque dimanche, ___ prépare un grand repas pour toute une tablée.', 'on', ['là', 'où'], 'On remplace des personnes.'),
   f('Pendant les vacances, ___ rend visite à nos grands-parents.', 'on', ['là', 'où'], 'On remplace des personnes.'), f('Dans notre classe, ___ écoute attentivement chaque exposé.', 'on', ['là', 'où'], 'On remplace des personnes.')]),
 'on : le verbe au singulier': (
  [v('On ___ au ballon.', 'joue', ['jouent', 'jouons'], 'Avec on, le verbe se conjugue comme avec il.'), v('Chez nous, on ___ tôt.', 'mange', ['mangent', 'mangeons'], 'On = il : mange.'), v('Ce soir, on ___ un film.', 'regarde', ['regardent', 'regardons'], 'On = il : regarde.'), v('Le samedi, on ___ au marché.', 'va', ['vont', 'allons'], 'On = il : va.')],
  [v('Quand il fait beau, on ___ dehors pendant les récréations.', 'joue', ['jouent', 'jouons'], 'Avec on, le verbe est comme avec il.'), v('Dans ce village, on ___ de très bons fromages.', 'fabrique', ['fabriquent', 'fabriquons'], 'On = il : fabrique.'),
   v('Chaque matin, on ___ le journal avant d’aller travailler.', 'lit', ['lisent', 'lisons'], 'On = il : lit.'), v('Pendant les vacances, on ___ des châteaux de sable.', 'construit', ['construisent', 'construisons'], 'On = il : construit.')]),
 'là : un lieu': (
  [f('Pose ton sac ___, près de moi.', 'là', ['on', 'où'], 'Là indique un lieu : je peux dire « ici ».'), f('Mes clés sont ___, sur le meuble.', 'là', ['on', 'où'], 'Là indique un lieu.'), f('Regarde ___ : un écureuil !', 'là', ['on', 'où'], 'Là indique un lieu.'), f('Mon livre est ___, sous ma chaise.', 'là', ['on', 'où'], 'Là indique un lieu.')],
  [f('Le trésor est caché ___, derrière ce vieux rocher.', 'là', ['on', 'où'], 'Là indique un lieu : je peux dire « ici ».'), f('Mon grand-père s’assoit toujours ___, près de cette fenêtre.', 'là', ['on', 'où'], 'Là indique un lieu.'),
   f('Garez votre voiture ___, devant le portail.', 'là', ['on', 'où'], 'Là indique un lieu.'), f('Les enfants jouent ___, dans le jardin de nos voisins.', 'là', ['on', 'où'], 'Là indique un lieu.')]),
 'où : le lieu': (
  [f('___ vas-tu ce soir ?', 'Où', ['On', 'Là'], 'Où pose une question sur le lieu.'), f('Je ne sais pas ___ j’ai rangé mon cahier.', 'où', ['on', 'là'], 'Où : je réponds par un lieu.'), f('___ habite ta cousine ?', 'Où', ['On', 'Là'], 'Où pose une question sur le lieu.'), f('Dis-moi ___ tu veux aller.', 'où', ['on', 'là'], 'Où : je réponds par un lieu.')],
  [f('Savez-vous ___ se trouve le musée de cette ville ?', 'où', ['on', 'là'], 'Où : je réponds par un lieu.'), f('Je ne comprends pas ___ mon frère a mis ses chaussures.', 'où', ['on', 'là'], 'Où : je réponds par un lieu.'),
   f('___ allons-nous passer nos prochaines vacances ?', 'Où', ['On', 'Là'], 'Où pose une question sur le lieu.'), f('Voici le village ___ j’ai grandi.', 'où', ['on', 'là'], 'Où : le lieu.')]),
 'Je choisis le bon mot': (
  [f2('___ cherche mes clés. ___ sont-elles ?', 'On', ['Où', 'Là'], 'On remplace des personnes ; où demande le lieu.'), f2('Mon chat dort ___, sur mon lit. ___ le caresse souvent.', 'là', ['on', 'où'], 'Là : un lieu ; on : des personnes.'),
   f2('___ part en vacances. ___ vas-tu ?', 'On', ['Où', 'Là'], 'On remplace des personnes ; où demande le lieu.'), f2('Il est ___, devant l’école. ___ le voit bien.', 'là', ['on', 'où'], 'Là : un lieu ; on : des personnes.')],
  [f2('Pendant les vacances, ___ visite des châteaux. ___ irons-nous demain ?', 'on', ['où', 'là'], 'On remplace des personnes ; où demande le lieu.'), f2('Je t’attends ___, près de cet arbre. ___ se retrouve devant l’école.', 'là', ['on', 'où'], 'Là : un lieu ; on : des personnes.'),
   f2('___ pose une question : ___ habitent tes grands-parents ?', 'On', ['Où', 'Là'], 'On remplace des personnes ; où demande le lieu.'), f2('Le trésor est ___, sous ce rocher. ___ le cherche depuis longtemps.', 'là', ['on', 'où'], 'Là : un lieu ; on : des personnes.')]),
 'Les pièges': (
  [ph('On danse.', ['On dansent.', 'On dansez.'], 'Avec on, le verbe est comme avec il.', 'Laquelle est bien écrite ?'), ph('Voilà ton cartable.', ['Voila ton cartable.'], 'Voilà prend un accent grave.', 'Laquelle est bien écrite ?'),
   ph('Mes amis sont là-bas.', ['Mes amis sont labas.'], 'Là-bas prend un trait d’union.', 'Laquelle est bien écrite ?'), ph('On joue ensemble.', ['On jouent ensemble.', 'On jouons ensemble.'], 'Avec on, le verbe est comme avec il.', 'Laquelle est bien écrite ?')],
  [ph('Pendant les vacances, on part toujours en voiture.', ['Pendant les vacances, on partent toujours en voiture.'], 'Avec on, le verbe est comme avec il.', 'Laquelle est bien écrite ?'), ph('Voilà exactement ce que je cherchais.', ['Voila exactement ce que je cherchais.'], 'Voilà prend un accent grave.', 'Laquelle est bien écrite ?'),
   ph('Mes cousins habitent là-bas, près de ce lac.', ['Mes cousins habitent labas, près de ce lac.'], 'Là-bas prend un trait d’union.', 'Laquelle est bien écrite ?'), ph('Dans ce village, on raconte de belles légendes.', ['Dans ce village, on racontent de belles légendes.'], 'Avec on, le verbe est comme avec il.', 'Laquelle est bien écrite ?')]),
}
H['H3'] = {
 'ce, cet, cette': (
  [f('___ ours dort tout l’hiver.', 'Cet', ['Ce', 'Cette'], 'Cet : devant une voyelle, masculin.'), f('___ maison est très ancienne.', 'Cette', ['Ce', 'Cet'], 'Cette : féminin.'), f('___ livre me plaît beaucoup.', 'Ce', ['Cet', 'Cette'], 'Ce : masculin devant une consonne.'), f('___ oiseau chante joliment.', 'Cet', ['Ce', 'Cette'], 'Cet : devant une voyelle, masculin.')],
  [f('Dans ce village, ___ église date du Moyen Âge.', 'cette', ['ce', 'cet'], 'Église est féminin : cette.'), f('Nous admirons ___ immense château depuis la colline.', 'cet', ['ce', 'cette'], 'Immense commence par une voyelle, château est masculin : cet.'),
   f('___ vieux manuscrit est très précieux pour l’historien.', 'Ce', ['Cet', 'Cette'], 'Vieux commence par une consonne, manuscrit est masculin : ce.'), f('Regardez ___ hirondelle qui construit son nid !', 'cette', ['ce', 'cet'], 'Hirondelle est féminin : cette.')]),
 'ces : au pluriel': (
  [f('Je range ___ livres.', 'ces', ['ce', 'cet'], 'Plusieurs livres : ces.'), f('___ enfants jouent bien.', 'Ces', ['Ce', 'Cet'], 'Plusieurs enfants : ces.'), f('J’adore ___ histoires.', 'ces', ['ce', 'cette'], 'Plusieurs histoires : ces.'), f('Regarde ___ oiseaux !', 'ces', ['ce', 'cet'], 'Plusieurs oiseaux : ces.')],
  [f('Nous avons visité ___ vieux châteaux pendant les vacances.', 'ces', ['ce', 'cet'], 'Plusieurs châteaux : ces.'), f('___ nuages noirs annoncent un orage.', 'Ces', ['Ce', 'Cet'], 'Plusieurs nuages : ces.'),
   f('Je ne connais pas ___ personnes.', 'ces', ['ce', 'cette'], 'Plusieurs personnes : ces.'), f('___ montagnes sont couvertes de neige toute l’année.', 'Ces', ['Ce', 'Cette'], 'Plusieurs montagnes : ces.')]),
 'Je change le nombre': (
  [f2('___ chat dort. ___ chats dorment.', 'Ce', ['Cet', 'Ces'], 'Je passe du singulier au pluriel pour prouver.'), f2('___ fleur est belle. ___ fleurs sont belles.', 'Cette', ['Ce', 'Ces'], 'Je passe du singulier au pluriel pour prouver.'),
   f2('___ arbre est grand. ___ arbres sont grands.', 'Cet', ['Ce', 'Ces'], 'Je passe du singulier au pluriel pour prouver.'), f2('___ enfant sourit. ___ enfants sourient.', 'Cet', ['Ce', 'Ces'], 'Je passe du singulier au pluriel pour prouver.')],
  [f2('___ animal vit dans la forêt. ___ animaux vivent dans la forêt.', 'Cet', ['Ce', 'Ces'], 'Je passe du singulier au pluriel pour prouver.'), f2('___ élève travaille bien. ___ élèves travaillent bien.', 'Cet', ['Ce', 'Ces'], 'Je passe du singulier au pluriel pour prouver.'),
   f2('___ voiture roule vite. ___ voitures roulent vite.', 'Cette', ['Ce', 'Ces'], 'Je passe du singulier au pluriel pour prouver.'), f2('___ château date du Moyen Âge. ___ châteaux datent du Moyen Âge.', 'Ce', ['Cet', 'Ces'], 'Je passe du singulier au pluriel pour prouver.')]),
 'à : le petit mot': (
  [f('Nous allons ___ la piscine.', 'à', ['ce', 'ces'], 'À est un petit mot qui ne change jamais.'), f('Je donne un cadeau ___ ma mère.', 'à', ['ce', 'ces'], 'À est un petit mot.'), f('Le train arrive ___ midi.', 'à', ['ce', 'ces'], 'À est un petit mot.'), f('Il pense ___ son anniversaire.', 'à', ['ce', 'ces'], 'À est un petit mot.')],
  [f('Mon frère s’intéresse ___ l’histoire des châteaux.', 'à', ['ce', 'ces'], 'À est un petit mot qui ne change jamais.'), f('Le facteur apporte une lettre ___ ma voisine.', 'à', ['ce', 'ces'], 'À est un petit mot.'),
   f('Nous rentrons ___ pied après le spectacle.', 'à', ['ce', 'ces'], 'À est un petit mot.'), f('Elle téléphone ___ son cousin chaque dimanche.', 'à', ['ce', 'ces'], 'À est un petit mot.')]),
 'à ne change jamais': (
  [f('Léa écrit ___ sa grand-mère.', 'à', ['ce', 'ces'], 'À ne change jamais.'), f('Ils offrent un jouet ___ leur petit frère.', 'à', ['ce', 'ces'], 'À ne change jamais.'), f('Tu penses ___ tes devoirs ?', 'à', ['ce', 'ces'], 'À ne change jamais.'), f('Nous jouons ___ cache-cache.', 'à', ['ce', 'ces'], 'À ne change jamais.')],
  [f('Chaque soir, mon père raconte une histoire ___ mon petit frère.', 'à', ['ce', 'ces'], 'À ne change jamais.'), f('Demain, nous irons ___ la montagne avec nos cousins.', 'à', ['ce', 'ces'], 'À ne change jamais.'),
   f('Nous rêvons ___ partir en voyage avec nos amis.', 'à', ['ce', 'ces'], 'À ne change jamais.'), f('Le professeur parle ___ tous les élèves de l’histoire du village.', 'à', ['ce', 'ces'], 'À ne change jamais.')]),
 'Je choisis le bon mot': (
  [f2('___ matin, nous allons ___ l’école.', 'Ce', ['Ces', 'À'], 'Ce devant un nom masculin ; à est un petit mot.'), f2('Je prête ___ stylos ___ mon voisin.', 'ces', ['ce', 'à'], 'Ces devant un nom pluriel ; à est un petit mot.'),
   f2('___ soir, je pense ___ ma journée.', 'Ce', ['Ces', 'À'], 'Ce devant un nom masculin ; à est un petit mot.'), f2('Je donne ___ fleurs ___ ma mamie.', 'ces', ['ce', 'à'], 'Ces devant un nom pluriel ; à est un petit mot.')],
  [f2('___ après-midi, nous rendons visite ___ nos grands-parents.', 'Cet', ['Ce', 'Ces'], 'Cet : devant une voyelle ; à est un petit mot.'), f2('Je prête ___ vieux livres ___ mon cousin pour les vacances.', 'ces', ['ce', 'à'], 'Ces devant un nom pluriel ; à est un petit mot.'),
   f2('___ été, nous irons ___ la mer avec nos amis.', 'Cet', ['Ce', 'Ces'], 'Cet devant une voyelle ; à est un petit mot.'), f2('Je téléphone ___ ma tante pour la remercier de ___ cadeau.', 'à', ['ce', 'ces'], 'À est un petit mot ; ce devant un nom masculin.')]),
 'Les pièges': (
  [ph('Cet animal est gentil.', ['Ce animal est gentil.']), ph('Ces chiens aboient.', ['Ces chien aboient.']), ph('Cette idée est bonne.', ['Cet idée est bonne.']), ph('Ce village est calme.', ['Cet village est calme.'])],
  [ph('Cet hôtel est ancien.', ['Ce hôtel est ancien.']), ph('Ces vieilles maisons sont jolies.', ['Ces vieille maisons sont jolies.']), ph('Cette école est grande.', ['Cet école est grande.']), ph('Ce jardin est fleuri.', ['Cet jardin est fleuri.'])]),
}
H['H4'] = {
 'et : j’ajoute': (
  [f('Je mange une pomme ___ une poire.', 'et', ['ou', 'mais'], 'Et ajoute.'), f('Tom joue ___ chante.', 'et', ['ou', 'mais'], 'Et ajoute.'), f('Elle porte un bonnet ___ des gants.', 'et', ['ou', 'mais'], 'Et ajoute.'), f('Papa lit ___ maman cuisine.', 'et', ['ou', 'mais'], 'Et ajoute.')],
  [f('Mon frère aime le football ___ le basket.', 'et', ['ou', 'mais'], 'Et ajoute : je peux dire « et aussi ».'), f('Nous avons visité un château ___ nous avons mangé au restaurant.', 'et', ['ou', 'mais'], 'Et ajoute.'),
   f('Ma sœur joue du piano ___ de la guitare.', 'et', ['ou', 'mais'], 'Et ajoute.'), f('Le matin, je lis ___ je dessine.', 'et', ['ou', 'mais'], 'Et ajoute.')]),
 'ou : je choisis': (
  [f('Tu veux du thé ___ du chocolat ?', 'ou', ['et', 'mais'], 'Ou propose un choix : je peux dire « ou bien ».'), f('Nous irons à pied ___ en bus.', 'ou', ['et', 'mais'], 'Ou propose un choix.'), f('Veux-tu jouer dehors ___ dessiner ?', 'ou', ['et', 'mais'], 'Ou propose un choix.'), f('Je prends un croissant ___ un pain au chocolat.', 'ou', ['et', 'mais'], 'Ou propose un choix.')],
  [f('Pour le dessert, vous pouvez choisir un gâteau ___ une glace.', 'ou', ['et', 'mais'], 'Ou propose un choix : je peux dire « ou bien ».'), f('Veux-tu partir ce matin ___ demain soir ?', 'ou', ['et', 'mais'], 'Ou propose un choix.'),
   f('Nous prendrons le train ___ la voiture selon la météo.', 'ou', ['et', 'mais'], 'Ou propose un choix.'), f('Elle hésite : le rouge ___ le bleu ?', 'ou', ['et', 'mais'], 'Ou propose un choix.')]),
 'mais : je m’oppose': (
  [f('Il fait beau, ___ il y a du vent.', 'mais', ['et', 'ou'], 'Mais oppose deux idées.'), f('J’ai faim, ___ je n’ai rien à manger.', 'mais', ['et', 'ou'], 'Mais oppose deux idées.'), f('Léa voulait venir, ___ elle était malade.', 'mais', ['et', 'ou'], 'Mais oppose deux idées.'), f('Il pleut, ___ nous sortons quand même.', 'mais', ['et', 'ou'], 'Mais oppose deux idées.')],
  [f('Je voulais finir mon livre, ___ la nuit tombait déjà.', 'mais', ['et', 'ou'], 'Mais oppose deux idées.'), f('Ce garçon semble petit, ___ il court plus vite que tout le monde.', 'mais', ['et', 'ou'], 'Mais oppose deux idées.'),
   f('Nous avions de la patience, ___ l’attente fut longue.', 'mais', ['et', 'ou'], 'Mais oppose deux idées.'), f('Elle a beaucoup travaillé, ___ elle n’a pas réussi.', 'mais', ['et', 'ou'], 'Mais oppose deux idées.')]),
 'Des mots qui ne changent jamais': (
  [C('', 'Quelle liste contient des conjonctions de coordination ?', 'mais, ou, et', ['petit, grand, joli', 'un, une, des'], 'Et, ou, mais relient.'), C('', 'Quel autre mot relie, comme et, ou, mais ?', 'donc', ['table', 'dormir'], 'Il relie deux parties de phrase.'),
   C('', 'Quel mot relie, comme et, ou, mais ?', 'car', ['maison', 'courir'], 'Il relie deux parties de phrase.'), C('', 'Quel mot ne change jamais ?', 'mais', ['petit', 'chats'], 'Un mot invariable ne change jamais.')],
  [C('', 'Quelle liste ne contient que des conjonctions de coordination ?', 'mais, ou, et, donc, car', ['et, très, mais', 'ou, bien, car'], 'Et, ou, mais, donc, or, ni, car.'), C('', 'Quel mot n’est PAS une conjonction de coordination ?', 'très', ['donc', 'ni'], 'Et, ou, mais, donc, or, ni, car.'),
   C('', 'Quel mot relie deux parties de phrase en exprimant la cause ?', 'car', ['très', 'beaucoup'], 'Il donne la cause.'), C('', 'Quel mot relie deux parties de phrase en exprimant la conséquence ?', 'donc', ['bien', 'vite'], 'Il donne la conséquence.')]),
 'Je choisis selon le sens': (
  [f2('Tu veux du lait ___ du jus ? J’ai soif, ___ pas faim.', 'ou', ['et', 'mais'], 'Ou : un choix ; mais : une opposition.'), f2('Je mets un bonnet ___ des gants, ___ j’ai encore froid.', 'et', ['ou', 'mais'], 'Et : j’ajoute ; mais : une opposition.'),
   f2('Il pleut, ___ je sors. Tu viens ___ tu restes ?', 'mais', ['et', 'ou'], 'Mais : une opposition ; ou : un choix.'), f2('Nous mangeons du pain ___ du fromage, ___ nous avons encore faim.', 'et', ['ou', 'mais'], 'Et : j’ajoute ; mais : une opposition.')],
  [f2('Prends le bus ___ le tramway, ___ ne reste pas ici.', 'ou', ['et', 'mais'], 'Ou : un choix.'), f2('Il fait froid ___ nous gardons nos manteaux, ___ nous avons chaud en marchant.', 'et', ['ou', 'mais'], 'Et : j’ajoute.'),
   f2('Elle a étudié ___ elle a réussi, ___ elle ne s’arrête pas.', 'et', ['ou', 'mais'], 'Et : j’ajoute.'), f2('Veux-tu du riz ___ des pâtes ? Je préfère le riz, ___ j’aime aussi les pâtes.', 'ou', ['et', 'mais'], 'Ou : un choix ; mais : une opposition.')]),
 'Les pièges': (
  [ph('Il fait beau, mais il fait froid.', ['Il fait beau mais, il fait froid.'], 'Une virgule avant mais.', 'Choisis la phrase bien écrite.'), ph('Je mange et je bois.', ['Je mange, et, je bois.'], 'Pas de virgule autour de et.', 'Choisis la phrase bien écrite.'),
   ph('J’ai faim, mais je n’ai rien.', ['J’ai faim mais, je n’ai rien.'], 'Une virgule avant mais.', 'Choisis la phrase bien écrite.'), ph('Tu viens ou tu restes ?', ['Tu viens, ou, tu restes ?'], 'Pas de virgule autour de ou.', 'Choisis la phrase bien écrite.')],
  [ph('Elle voulait sortir, mais il pleuvait trop fort.', ['Elle voulait sortir mais, il pleuvait trop fort.'], 'Une virgule avant mais.', 'Choisis la phrase bien écrite.'), ph('Prends un fruit ou un yaourt pour le goûter.', ['Prends un fruit, ou, un yaourt pour le goûter.'], 'Pas de virgule autour de ou.', 'Choisis la phrase bien écrite.'),
   ph('Mon frère aime lire et ma sœur préfère dessiner.', ['Mon frère aime, lire et ma sœur préfère dessiner.'], 'La virgule ne coupe pas le groupe verbal.', 'Choisis la phrase bien écrite.'), ph('Le chat dort, mais le chien surveille la maison.', ['Le chat dort mais, le chien surveille la maison.'], 'Une virgule avant mais.', 'Choisis la phrase bien écrite.')]),
}
H['H5'] = {
 'la : un déterminant': (
  [f('Je ferme ___ porte.', 'la', ['le', 'les'], 'Devant un nom féminin : la.'), f('Léa mange ___ pomme.', 'la', ['le', 'les'], 'Devant un nom féminin : la.'), f('Papa gare ___ voiture.', 'la', ['le', 'les'], 'Devant un nom féminin : la.'), f('Maman range ___ cuisine.', 'la', ['le', 'les'], 'Devant un nom féminin : la.')],
  [f('Mon frère arrose ___ pelouse du jardin chaque soir.', 'la', ['le', 'les'], 'Devant un nom féminin : la.'), f('Nous visitons ___ cathédrale de cette ville.', 'la', ['le', 'les'], 'Devant un nom féminin : la.'),
   f('Le facteur ouvre ___ boîte aux lettres.', 'la', ['le', 'les'], 'Devant un nom féminin : la.'), f('Ma grand-mère prépare ___ soupe pour le dîner.', 'la', ['le', 'les'], 'Devant un nom féminin : la.')]),
 'la : un pronom': (
  [f('Cette histoire, je ___ raconte souvent.', 'la', ['le', 'les'], 'Devant un verbe, la remplace un nom féminin.'), f('Ma voisine ? Je ___ connais bien.', 'la', ['le', 'les'], 'La remplace « ma voisine ».'), f('Ma montre ? Je ___ porte tous les jours.', 'la', ['le', 'les'], 'La remplace « ma montre ».'), f('Cette chanson, Léa ___ chante tout le temps.', 'la', ['le', 'les'], 'La remplace « cette chanson ».')],
  [f('Cette vieille photo, mon grand-père ___ regarde chaque soir.', 'la', ['le', 'les'], 'La remplace « cette vieille photo ».'), f('Ta cousine ? Nous ___ invitons ce week-end.', 'la', ['le', 'les'], 'La remplace « ta cousine ».'),
   f('La porte, il ___ ferme doucement.', 'la', ['le', 'les'], 'La remplace « la porte ».'), f('Cette valise, je ___ porte jusqu’à la gare.', 'la', ['le', 'les'], 'La remplace « cette valise ».')]),
 'c’est : cela est': (
  [ph('C’est une belle journée.', ['Cest une belle journée.', 'C’es une belle journée.'], 'C’est = cela est.'), ph('C’est mon cartable.', ['Cest mon cartable.'], 'C’est = cela est.'), ph('C’est très bon.', ['Cest très bon.'], 'C’est = cela est.'), ph('C’est ma sœur.', ['Cest ma sœur.'], 'C’est = cela est.')],
  [ph('C’est la plus belle journée de l’année.', ['Cest la plus belle journée de l’année.'], 'C’est = cela est.'), ph('C’est un livre que j’ai lu trois fois.', ['Cest un livre que j’ai lu trois fois.'], 'C’est = cela est.'),
   ph('Regarde : c’est un renard !', ['Regarde : cest un renard !'], 'C’est = cela est.'), ph('C’est exactement ce que je voulais.', ['C’es exactement ce que je voulais.'], 'C’est = cela est.')]),
 'c’est au passé : c’était': (
  [f('C’est mon cadeau. Hier, ___ mon cadeau.', 'c’était', ['c’étais', 'cétait'], 'Au passé, c’est devient c’était.'), f('C’est difficile. Hier, ___ difficile.', 'c’était', ['c’étais', 'cétait'], 'Au passé, c’est devient c’était.'),
   f('C’est lundi. Hier, ___ dimanche.', 'c’était', ['c’étais', 'cétait'], 'Au passé, c’est devient c’était.'), f('C’est amusant. Hier, ___ amusant.', 'c’était', ['c’étais', 'cétait'], 'Au passé, c’est devient c’était.')],
  [f('Aujourd’hui, c’est la fête. L’an dernier, ___ la fête aussi.', 'c’était', ['c’étais', 'cétait'], 'Au passé, c’est devient c’était.'), f('Maintenant, c’est facile. Au début, ___ très difficile.', 'c’était', ['c’étais', 'cétait'], 'Au passé, c’est devient c’était.'),
   f('Ce matin, c’est le printemps. Hier, ___ encore l’hiver.', 'c’était', ['c’étais', 'cétait'], 'Au passé, c’est devient c’était.'), f('Aujourd’hui, c’est ma sœur qui gagne. Hier, ___ moi.', 'c’était', ['c’étais', 'cétait'], 'Au passé, c’est devient c’était.')]),
 'Je choisis le bon mot': (
  [f2('Prends ___ clé : ___ celle de la cave.', 'la', ['le', 'c’est'], 'La devant un nom ; c’est = cela est.'), f2('___ un cadeau pour ma mère : je ___ cache.', 'C’est', ['La', 'Le'], 'C’est = cela est ; la devant un verbe remplace un nom féminin.'),
   f2('Ma sœur ? Je ___ vois souvent. ___ ma meilleure amie.', 'la', ['le', 'c’est'], 'La devant un verbe ; c’est = cela est.'), f2('Regarde ___ voiture : ___ celle de mon oncle.', 'la', ['le', 'c’est'], 'La devant un nom ; c’est = cela est.')],
  [f2('Cette photo, je ___ garde précieusement : ___ le souvenir de nos vacances.', 'la', ['le', 'c’est'], 'La remplace « cette photo » ; c’est = cela est.'), f2('___ la porte du fond : ouvre-___ doucement.', 'C’est', ['La', 'Le'], 'C’est = cela est ; la remplace « la porte ».'),
   f2('Ma tante ? Nous ___ visitons demain : ___ une femme très gentille.', 'la', ['le', 'c’est'], 'La remplace « ma tante » ; c’est = cela est.'), f2('Prends ___ route de gauche : ___ la plus courte.', 'la', ['le', 'c’est'], 'La devant un nom ; c’est = cela est.')]),
 'Les pièges': (
  [ph('Cette carte, je la garde.', ['Cette carte, je le garde.']), ph('C’était mon tour.', ['C’étais mon tour.']), ph('Ma lampe, je la répare.', ['Ma lampe, je le répare.']), ph('C’était une belle journée.', ['Cétait une belle journée.'])],
  [ph('Ta montre, tu la perds souvent.', ['Ta montre, tu le perds souvent.']), ph('C’était un jour de fête dans tout le village.', ['Cétait un jour de fête dans tout le village.']), ph('La maîtresse, je la rencontre demain.', ['La maîtresse, je le rencontre demain.']), ph('C’est la plus belle journée de l’année.', ['Cest la plus belle journée de l’année.'])]),
}
H['H6'] = {
 'son : à lui, à elle': (
  [f('Léa range ___ cartable.', 'son', ['ses', 'mes'], 'Une seule chose à lui ou à elle : son.'), f('Le chien cherche ___ os.', 'son', ['ses', 'mes'], 'Une seule chose : son.'), f('Mon frère lit ___ livre.', 'son', ['ses', 'mes'], 'Une seule chose : son.'), f('Ma tante ferme ___ sac.', 'son', ['ses', 'mes'], 'Une seule chose : son.')],
  [f('Le jardinier arrose ___ potager avec soin.', 'son', ['ses', 'mes'], 'Une seule chose à lui : son.'), f('Mon oncle répare ___ vieux vélo dans le garage.', 'son', ['ses', 'mes'], 'Une seule chose à lui : son.'),
   f('Le peintre nettoie ___ pinceau après le travail.', 'son', ['ses', 'mes'], 'Une seule chose à lui : son.'), f('La maîtresse corrige ___ cahier de préparation.', 'son', ['ses', 'mes'], 'Une seule chose à elle : son.')]),
 'ses : plusieurs choses': (
  [f('Léa range ___ livres.', 'ses', ['son', 'mes'], 'Plusieurs choses à lui ou à elle : ses.'), f('Le chien mange ___ croquettes.', 'ses', ['son', 'mes'], 'Plusieurs choses : ses.'), f('Papa cherche ___ clés.', 'ses', ['son', 'mes'], 'Plusieurs choses : ses.'), f('Tom lave ___ chaussures.', 'ses', ['son', 'mes'], 'Plusieurs choses : ses.')],
  [f('Le fermier nourrit ___ vaches tous les matins.', 'ses', ['son', 'mes'], 'Plusieurs choses à lui : ses.'), f('Ma voisine arrose ___ rosiers chaque soir.', 'ses', ['son', 'mes'], 'Plusieurs choses à elle : ses.'),
   f('Le musicien accorde ___ instruments avant le concert.', 'ses', ['son', 'mes'], 'Plusieurs choses à lui : ses.'), f('La maîtresse range ___ cahiers dans l’armoire.', 'ses', ['son', 'mes'], 'Plusieurs choses à elle : ses.')]),
 'mes : à moi': (
  [f('Je range ___ crayons.', 'mes', ['son', 'ses'], 'Plusieurs choses à moi : mes.'), f('J’aime ___ amis.', 'mes', ['son', 'ses'], 'Plusieurs personnes à moi : mes.'), f('Je lave ___ mains.', 'mes', ['son', 'ses'], 'Plusieurs choses à moi : mes.'), f('Je prête ___ jouets.', 'mes', ['son', 'ses'], 'Plusieurs choses à moi : mes.')],
  [f('Ce week-end, j’invite ___ cousins à la maison.', 'mes', ['son', 'ses'], 'Plusieurs personnes à moi : mes.'), f('J’ai oublié ___ lunettes chez ma grand-mère.', 'mes', ['son', 'ses'], 'Plusieurs choses à moi : mes.'),
   f('Je montre ___ dessins à toute la classe.', 'mes', ['son', 'ses'], 'Plusieurs choses à moi : mes.'), f('J’apporte ___ affaires de sport pour le match.', 'mes', ['son', 'ses'], 'Plusieurs choses à moi : mes.')]),
 'Un ou plusieurs ?': (
  [f('Tu as perdu ___ gants.', 'tes', ['ton', 'ta'], 'Plusieurs choses à toi : tes.'), f('Nous rangeons ___ affaires.', 'nos', ['notre', 'vos'], 'Plusieurs choses à nous : nos.'), f('Les élèves prennent ___ cahiers.', 'leurs', ['leur', 'ses'], 'Plusieurs choses à eux : leurs.'), f('Vous cherchez ___ clés ?', 'vos', ['votre', 'nos'], 'Plusieurs choses à vous : vos.')],
  [f('Les enfants ont rangé ___ jouets avant de dormir.', 'leurs', ['leur', 'ses'], 'Plusieurs choses à eux : leurs.'), f('Nous avons invité ___ voisins à notre fête.', 'nos', ['notre', 'vos'], 'Plusieurs personnes à nous : nos.'),
   f('Tu as oublié ___ cahier de textes à l’école.', 'ton', ['ta', 'tes'], 'Une seule chose à toi, masculin : ton.'), f('Les voisins arrosent ___ jardin tous les soirs.', 'leur', ['leurs', 'ses'], 'Une seule chose à eux : leur.')]),
 'À qui ? Combien ?': (
  [f2('Tom promène ___ chien, et moi ___ chats.', 'son', ['ses', 'mes'], 'À lui, un seul ; à moi, plusieurs.'), f2('Papa lave ___ vélo, et moi ___ patins.', 'son', ['ses', 'mes'], 'À lui, un seul ; à moi, plusieurs.'),
   f2('Léa lit ___ livre, et moi ___ bandes dessinées.', 'son', ['ses', 'mes'], 'À elle, un seul ; à moi, plusieurs.'), f2('Tom range ___ crayons, et moi ___ cahier.', 'ses', ['son', 'mes'], 'À lui, plusieurs ; à moi, un seul.')],
  [f2('Mon frère nettoie ___ chaussures, et moi ___ vélo.', 'ses', ['son', 'mes'], 'À lui, plusieurs ; à moi, un seul.'), f2('La maîtresse corrige ___ cahiers, et nous ___ exercices.', 'ses', ['son', 'mes'], 'À elle, plusieurs ; à nous, plusieurs.'),
   f2('Ma sœur range ___ jouet, et moi ___ jouets.', 'son', ['ses', 'mes'], 'À elle, un seul ; à moi, plusieurs.'), f2('Le chat mange ___ pâtée, et moi ___ céréales.', 'sa', ['ses', 'mes'], 'À lui, une seule chose féminine ; à moi, plusieurs.')]),
 'Les pièges': (
  [ph('Il porte son écharpe.', ['Il porte sa écharpe.']), ph('Elle range ses jouets.', ['Elle range ses jouet.']), ph('Léa prête son stylo.', ['Léa prête ses stylo.']), ph('J’ai rangé mes affaires.', ['J’ai rangé mes affaire.'])],
  [ph('Mon voisin lave son auto tous les samedis.', ['Mon voisin lave sa auto tous les samedis.']), ph('Les enfants ont rangé leurs jouets avant le dîner.', ['Les enfants ont rangé leurs jouet avant le dîner.']), ph('Ma tante a perdu son parapluie hier.', ['Ma tante a perdu sa parapluie hier.']), ph('J’ai invité mes amis pour mon anniversaire.', ['J’ai invité mes ami pour mon anniversaire.'])]),
}
H['H7'] = {
 'se : devant un verbe': (
  [f('Le chat ___ réveille tôt.', 'se', ['s’est'], 'Se est devant un verbe conjugué.'), f('Mon frère ___ peigne.', 'se', ['s’est'], 'Se est devant un verbe conjugué.'), f('Les enfants ___ cachent.', 'se', ['s’est'], 'Se est devant un verbe conjugué.'), f('Maman ___ repose.', 'se', ['s’est'], 'Se est devant un verbe conjugué.')],
  [f('Chaque matin, mon grand-père ___ promène dans le parc.', 'se', ['s’est'], 'Se est devant un verbe conjugué.'), f('Les oiseaux ___ posent sur le fil dès l’aube.', 'se', ['s’est'], 'Se est devant un verbe conjugué.'),
   f('Quand il fait chaud, le chien ___ couche à l’ombre.', 'se', ['s’est'], 'Se est devant un verbe conjugué.'), f('Ma sœur ___ prépare pour la fête de l’école.', 'se', ['s’est'], 'Se est devant un verbe conjugué.')]),
 'je me, tu te, il se': (
  [f('Les oiseaux ___ posent sur le fil.', 'se', ['me', 'te'], 'Avec ils : se.'), f('Je ___ lave les mains.', 'me', ['se', 'te'], 'Avec je : me.'), f('Tu ___ coiffes devant le miroir.', 'te', ['se', 'me'], 'Avec tu : te.'), f('Elle ___ réveille tôt.', 'se', ['me', 'te'], 'Avec elle : se.')],
  [f('Chaque matin, je ___ prépare avant tout le monde.', 'me', ['se', 'te'], 'Avec je : me.'), f('Pendant les vacances, tu ___ lèves toujours très tard.', 'te', ['se', 'me'], 'Avec tu : te.'),
   f('Les élèves ___ rangent dans la cour dès la sonnerie.', 'se', ['me', 'te'], 'Avec ils : se.'), f('Mon petit frère ___ cache derrière le rideau.', 'se', ['me', 'te'], 'Avec il : se.')]),
 's’est : au passé composé': (
  [f('Hier, mon frère ___ promené.', 's’est', ['se'], 'Au passé composé : s’est.'), f('Le chat ___ caché sous le lit.', 's’est', ['se'], 'Au passé composé : s’est.'), f('Ma sœur ___ coiffée.', 's’est', ['se'], 'Au passé composé : s’est.'), f('Papa ___ reposé hier.', 's’est', ['se'], 'Au passé composé : s’est.')],
  [f('Hier soir, mon grand-père ___ endormi devant la télévision.', 's’est', ['se'], 'Au passé composé : s’est.'), f('Pendant la récréation, le petit garçon ___ blessé au genou.', 's’est', ['se'], 'Au passé composé : s’est.'),
   f('La semaine dernière, ma cousine ___ perdue dans la forêt.', 's’est', ['se'], 'Au passé composé : s’est.'), f('Hier matin, le chien ___ échappé du jardin.', 's’est', ['se'], 'Au passé composé : s’est.')]),
 'se ou s’est ?': (
  [f2('Aujourd’hui, Tom ___ lève. Hier, il ___ levé tôt.', 'se', ['s’est'], 'Un verbe conjugué ? se. Un participe passé ? s’est.'), f2('Le chien ___ couche. Hier, il ___ couché tôt.', 'se', ['s’est'], 'Un verbe conjugué ? se. Un participe passé ? s’est.'),
   f2('Léa ___ est lavée ? Non, elle ___ lave maintenant.', 's’est', ['se'], 'Un participe passé ? s’est.'), f2('Mon frère ___ habille. Hier, il ___ habillé vite.', 'se', ['s’est'], 'Un verbe conjugué ? se. Un participe passé ? s’est.')],
  [f2('Chaque jour, ma sœur ___ prépare. Hier, elle ___ préparée en cinq minutes.', 'se', ['s’est'], 'Un verbe conjugué ? se. Un participe passé ? s’est.'), f2('Le vieux chat ___ réchauffe au soleil. Hier, il ___ réchauffé toute la journée.', 'se', ['s’est'], 'Un verbe conjugué ? se. Un participe passé ? s’est.'),
   f2('Demain, nous irons voir comment le village ___ transforme. Hier, il ___ transformé.', 'se', ['s’est'], 'Un verbe conjugué ? se. Un participe passé ? s’est.'), f2('Mon frère ___ est disputé avec son ami. Maintenant, ils ___ réconcilient.', 's’est', ['se'], 'Un participe passé ? s’est.')]),
 'L’accord avec s’est': (
  [v('Léa s’est ___.', 'lavée', ['lavé', 'lavés'], 'Le participe s’accorde avec le sujet : Léa, féminin.'), v('Le chien s’est ___.', 'couché', ['couchée', 'couchés'], 'Le chien, masculin singulier.'), v('Mes sœurs se sont ___.', 'reposées', ['reposé', 'reposée'], 'Mes sœurs, féminin pluriel.'), v('Mon père s’est ___.', 'rasé', ['rasée', 'rasés'], 'Mon père, masculin singulier.')],
  [v('Après la longue randonnée, ma cousine s’est ___ sur un banc.', 'assise', ['assis', 'assises'], 'Ma cousine, féminin singulier.'), v('Les deux frères se sont ___ pendant la récréation.', 'disputés', ['disputé', 'disputées'], 'Les deux frères, masculin pluriel.'),
   v('Mes amies se sont ___ au bord du lac.', 'promenées', ['promené', 'promenée'], 'Mes amies, féminin pluriel.'), v('Le petit garçon s’est ___ en courant.', 'blessé', ['blessée', 'blessés'], 'Le petit garçon, masculin singulier.')]),
 'Les pièges': (
  [ph('Elle s’est blessée.', ['Elle se est blessée.']), ph('Il se réveille tôt.', ['Il s’est réveille tôt.']), ph('Les chats se sont couchés.', ['Les chats s’est couchés.']), ph('Je me suis habillé.', ['Je me est habillé.'])],
  [ph('Mes cousines se sont perdues dans la forêt.', ['Mes cousines s’est perdues dans la forêt.']), ph('Le petit chat se lave après le repas.', ['Le petit chat s’est lave après le repas.']),
   ph('Ma sœur s’est promenée hier soir au bord du lac.', ['Ma sœur se est promenée hier soir au bord du lac.']), ph('Les enfants se sont amusés toute la journée.', ['Les enfants se est amusés toute la journée.'])]),
}
if __name__ == '__main__':
    for g in H:
        titres = [e['titre'] for e in lessons_json(g)['ecrans']]
        manque = [t for t in titres if t not in H[g]]
        assert not manque, (g, manque)
        appliquer(g, {t: H[g][t] for t in titres})
