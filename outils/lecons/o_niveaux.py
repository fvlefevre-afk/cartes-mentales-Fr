from niveaux_lib import *
MN = 'Complète : m ou n ?'; LT = 'Complète avec la bonne lettre.'; LS = 'Complète avec les bonnes lettres.'; MUET = 'Quelle lettre muette faut-il écrire ?'
def L(p, bon, mal, ask, h): return C(p, ask, bon, mal, h, 'hl')
def mn(p, bon): return L(p, bon, ['n' if bon == 'm' else 'm'], MN, 'Devant m, b, p : m. Devant les autres lettres : n.')
def mu(p, bon, mal): return L(p, bon, mal, MUET, 'Je cherche un mot de la même famille ou le féminin : j’entends la lettre.')
def pq(q, bon, mal): return C('', q, bon, mal, 'Je regarde la lettre qui suit.')
def bien(bon, mal, q='Quel mot est bien écrit ?'): return C('', q, bon, mal, 'Je mémorise ces mots.')
def lt(p, bon, mal, h='Je regarde la lettre qui suit.'): return L(p, bon, mal, LT, h)
def ls(p, bon, mal, h='Je regarde la lettre qui suit.'): return L(p, bon, mal, LS, h)
def ml(m, bon, mal): return C('', f'Quelle lettre est muette dans « {m} » ?', bon, mal, 'La lettre muette ne s’entend pas à la fin du mot.')
def mem(q, bon, mal): return C('', q, bon, mal, 'Quand un mot de la famille m’aide, je l’utilise ; sinon, je mémorise.')
O = {}
O['O1'] = {
 'La règle': ([mn('une cha___bre', 'm'), mn('un ti___bre', 'm'), mn('une la___pe', 'm'), mn('un po___pier', 'm')],
  [mn('Pour mon anniversaire, j’ai reçu un livre sur les no___bres.', 'm'), mn('Mon oncle est po___pier.', 'm'), mn('Elle a cassé la ja___be de sa poupée.', 'm'), mn('Le chat se glisse sous la ra___pe.', 'm')]),
 'Devant m aussi': ([mn('un i___meuble', 'm'), mn('e___mener', 'm'), mn('i___mense', 'm'), mn('e___mêler', 'm')],
  [mn('Cet i___meuble a dix étages.', 'm'), mn('Je vais e___mener mon petit frère à l’école.', 'm'), mn('Cette fusée est i___mense et blanche.', 'm'), mn('Ils se sont e___mêlés dans la conversation.', 'm')]),
 'Ailleurs : n': ([mn('un e___fant', 'n'), mn('une ba___que', 'n'), mn('il cha___te', 'n'), mn('un po___t', 'n')],
  [mn('Mon grand-père se promène dans la mo___tagne.', 'n'), mn('Nous attendons le pri___temps avec impatience.', 'n'), mn('Ils ont acheté un pa___talon rouge.', 'n'), mn('Le bébé est déjà e___dormi.', 'n')]),
 'Tous ces sons': ([mn('co___pter', 'm'), mn('le pri___temps', 'n'), mn('une tro___pette', 'm'), mn('du li___ge', 'n')],
  [mn('Le musicien joue de la tro___pette.', 'm'), mn('Mon grand-père co___te des histoires drôles.', 'n'), mn('Mon cousin travaille dans un ca___ping.', 'm'), mn('Il aime se promener dans la ca___pagne.', 'm')]),
 'Je prouve': ([pq('Pourquoi « lampe » s’écrit-il avec m ?', 'Parce qu’après, il y a un p.', ['Parce que le mot est court.', 'Parce que c’est un nom.']), pq('Pourquoi « tente » s’écrit-il avec n ?', 'Après, il y a un t : ce n’est ni m, ni b, ni p.', ['Parce que c’est un nom.', 'Parce que le mot finit par e.']),
   pq('Pourquoi « jambe » s’écrit-il avec m ?', 'Parce qu’après, il y a un b.', ['Parce que c’est un nom.', 'Parce que le mot est court.']), pq('Pourquoi « danser » s’écrit-il avec n ?', 'Après, il y a un s : ce n’est ni m, ni b, ni p.', ['Parce que c’est un verbe.', 'Parce que le mot finit par r.'])],
  [pq('Pourquoi « symbole » s’écrit-il avec m ?', 'Parce qu’après, il y a un b.', ['Parce que c’est un nom.', 'Parce qu’il y a un y.']), pq('Pourquoi « conduire » s’écrit-il avec n ?', 'Après, il y a un d : ce n’est ni m, ni b, ni p.', ['Parce que c’est un verbe.', 'Parce qu’il y a un u.']),
   pq('Pourquoi « immense » s’écrit-il avec mm ?', 'Parce qu’après le m, il y a aussi un m.', ['Parce que c’est un adjectif.', 'Parce que le mot est long.']), pq('Pourquoi « important » s’écrit-il avec m puis n ?', 'Le premier est devant p ; le second devant t.', ['Parce que c’est un adjectif.', 'Parce que le mot est long.'])]),
 'Attention !': ([bien('un champignon', ['un chanpignon']), bien('une ambulance', ['une anbulance']), bien('un bonbon', ['un bombon']), bien('un tambour', ['un tanbour'])],
  [bien('une trompette', ['une tronpette']), bien('néanmoins', ['néammoins']), bien('un champion', ['un chanpion']), bien('un bonbon', ['un bombon'])]),
}
O['O2'] = {
 'Une lettre muette': ([ml('grand', 'd', ['r', 'g']), ml('petit', 't', ['p', 'e']), ml('lourd', 'd', ['l', 'o']), ml('sport', 't', ['s', 'p'])],
  [ml('tabac', 'c', ['t', 'b']), ml('sirop', 'p', ['s', 'r']), ml('lézard', 'd', ['l', 'z']), ml('rempart', 't', ['r', 'm'])]),
 'La famille m’aide': ([mu('le froi___', 'd', ['t', 's']), mu('un lou___', 'p', ['t', 'd']), mu('le chan___', 't', ['d', 's']), mu('un dra___', 'p', ['t', 'd'])],
  [mu('Le renar___ rôde près du poulailler.', 'd', ['t', 's']), mu('Ce chemin est très lon___.', 'g', ['c', 't']), mu('Le spor___ m’aide à rester en forme.', 't', ['d', 's']), mu('Pose ton cam___ dans la clairière.', 'p', ['t', 'd'])]),
 'Des familles de mots': ([mu('un accor___', 'd', ['t', 's']), mu('le ven___', 't', ['d', 's']), mu('le blan___', 'c', ['t', 'k']), mu('un regar___', 'd', ['t', 's'])],
  [mu('Je range mes cahiers dans mon sa___.', 'c', ['t', 'k']), mu('Le gran___ arbre du jardin est très vieux.', 'd', ['t', 's']), mu('Mon père a acheté un nouveau tapi___.', 's', ['t', 'x']), mu('L’oiseau construit son ni___.', 'd', ['t', 's'])]),
 'Le féminin m’aide': ([mu('un garçon for___', 't', ['d', 's']), mu('un pantalon gri___', 's', ['t', 'x']), mu('un chemin lon___', 'g', ['c', 't']), mu('un enfant peti___', 't', ['d', 's'])],
  [mu('Ce garçon est très gran___.', 'd', ['t', 's']), mu('Ce chemin est très lon___ pour les enfants.', 'g', ['c', 't']), mu('Mon frère est un peu bavar___.', 'd', ['t', 's']), mu('Ce ballon est bien ron___.', 'd', ['t', 's'])]),
 'Je prouve': ([C('', 'Pourquoi « grand » finit-il par d ?', 'Parce que j’entends d dans « grande ».', ['Parce que tous les mots finissent par d.', 'Parce que c’est un adjectif.'], 'Je cherche le féminin.'), C('', 'Pourquoi « petit » finit-il par t ?', 'Parce que j’entends t dans « petite ».', ['Parce que le mot est court.', 'Parce que c’est un nom.'], 'Je cherche le féminin.'),
   C('', 'Pourquoi « lourd » finit-il par d ?', 'Parce que j’entends d dans « lourde ».', ['Parce que c’est un nom.', 'Parce que le mot est court.'], 'Je cherche le féminin.'), C('', 'Pourquoi « froid » finit-il par d ?', 'Parce que j’entends d dans « froideur ».', ['Parce que c’est un nom.', 'Parce qu’il y a un r avant.'], 'Je cherche un mot de la même famille.')],
  [C('', 'Pourquoi « éclat » finit-il par t ?', 'Parce que j’entends t dans « éclater ».', ['Parce que c’est un verbe.', 'Parce que le mot est court.'], 'Je cherche un mot de la même famille.'), C('', 'Pourquoi « tapis » finit-il par s ?', 'Parce que j’entends s dans « tapisser ».', ['Parce que c’est un adjectif.', 'Parce que le mot est long.'], 'Je cherche un mot de la même famille.'),
   C('', 'Pourquoi « galop » finit-il par p ?', 'Parce que j’entends p dans « galoper ».', ['Parce que c’est un adjectif.', 'Parce que le mot est court.'], 'Je cherche un mot de la même famille.'), C('', 'Pourquoi « sirop » finit-il par p ?', 'Parce que j’entends p dans « siroter ».', ['Parce que c’est un verbe.', 'Parce qu’il y a un r avant.'], 'Je cherche un mot de la même famille.')]),
 'Je mémorise': ([mem('Pour écrire « nez », que fais-je ?', 'Je le mémorise.', ['Je cherche le féminin.', 'J’ajoute toujours un e.']), mem('Pour trouver la fin de « petit », que fais-je ?', 'Je pense au féminin : petite.', ['J’écris toujours un s.', 'Je le mémorise sans réfléchir.']),
   mem('Pour trouver la fin de « galop », que fais-je ?', 'Je cherche un mot de la même famille : galoper.', ['J’écris toujours un s.', 'Je n’écris rien.']), mem('Pour écrire « riz », que fais-je ?', 'Je le mémorise.', ['Je cherche le féminin.', 'J’ajoute toujours un e.'])],
  [mem('Pour trouver la fin de « lézard », que fais-je ?', 'Je cherche un mot de la même famille.', ['J’écris toujours un t.', 'Je ne cherche rien.']), mem('Pour écrire « nez » ou « riz », que fais-je ?', 'Je les mémorise : aucun mot ne m’aide.', ['Je cherche le féminin.', 'J’écris toujours s.']),
   mem('Pour trouver la fin de « froid », que fais-je ?', 'Je pense à « froideur ».', ['J’écris toujours un t.', 'Je mémorise sans réfléchir.']), mem('Pour trouver la fin de « lourd », que fais-je ?', 'Je pense au féminin : lourde.', ['J’écris toujours un t.', 'Je mémorise sans réfléchir.'])]),
}
O['O3'] = {
 'J’écris s': ([lt('un ___ac', 's', ['ss', 'c']), lt('le ___oleil', 's', ['ss', 'c']), lt('pen___er', 's', ['ss', 'ç']), lt('la ___alade', 's', ['ss', 'c'])],
  [lt('Mon frère a mangé une ___oupe très chaude.', 's', ['ss', 'c']), lt('Nous allons ___auter à la corde.', 's', ['ss', 'ç']), lt('Elle a perdu son ___ac dans le bus.', 's', ['ss', 'c']), lt('Il faut pen___er à fermer la porte.', 's', ['ss', 'ç'])]),
 'J’écris ss': ([lt('une ta___e', 'ss', ['s', 'c']), lt('un poi___on', 'ss', ['s', 'ç']), lt('une cai___e', 'ss', ['s', 'c']), lt('un fo___é', 'ss', ['s', 'ç'])],
  [lt('Le pa___age était étroit entre les rochers.', 'ss', ['s', 'c']), lt('Elle boit son thé dans une jolie ta___e.', 'ss', ['s', 'c']), lt('Les poi___ons nagent dans la rivière.', 'ss', ['s', 'c']), lt('La ma___e de neige s’est détachée.', 'ss', ['s', 'ç'])]),
 'J’écris c': ([lt('une ___erise', 'c', ['ç', 'ss']), lt('un ___ygne', 'c', ['ç', 'ss']), lt('une ___ité', 'c', ['ç', 'ss']), lt('la ___ire', 'c', ['ç', 'ss'])],
  [lt('Le ___erf traverse la clairière au lever du jour.', 'c', ['ç', 'ss']), lt('Nous avons mangé une glace à la ___erise.', 'c', ['ç', 'ss']), lt('Le ___ygne glisse doucement sur le lac.', 'c', ['ç', 'ss']), lt('La ___ire de la bougie coule lentement.', 'c', ['ç', 'ss'])]),
 'J’écris ç': ([lt('un ma___on', 'ç', ['c', 'ss']), lt('une fa___ade', 'ç', ['c', 'ss']), lt('un gar___on', 'ç', ['c', 'ss']), lt('un re___u', 'ç', ['c', 'ss'])],
  [lt('Le ma___on construit un mur de pierre.', 'ç', ['c', 'ss']), lt('La fa___ade de l’église est très ancienne.', 'ç', ['c', 'ss']), lt('Le petit gar___on dessine un bateau.', 'ç', ['c', 'ss']), lt('Il a gardé le re___u de son achat.', 'ç', ['c', 'ss'])]),
 'La cédille dans les verbes': ([lt('nous lan___ons', 'ç', ['c', 'ss']), lt('nous for___ons', 'ç', ['c', 'ss']), lt('il avan___ait', 'ç', ['c', 'ss']), lt('vous commen___ez', 'c', ['ç', 'ss'])],
  [lt('Nous commen___ons la leçon.', 'ç', ['c', 'ss']), lt('Les élèves avan___aient lentement dans le couloir.', 'ç', ['c', 'ss']), lt('Il lan___ait le ballon très loin.', 'ç', ['c', 'ss']), lt('Vous plac___ez les chaises autour de la table.', 'ç', ['c', 'ss'])] if False else
  [lt('Nous commen___ons la leçon.', 'ç', ['c', 'ss']), lt('Les élèves avan___aient lentement dans le couloir.', 'ç', ['c', 'ss']), lt('Il lan___ait le ballon très loin.', 'ç', ['c', 'ss']), lt('Vous commen___ez à comprendre.', 'c', ['ç', 'ss'])]),
 'Je prouve': ([pq('Pourquoi une cédille dans « garçon » ?', 'Parce qu’après le c, il y a un o.', ['Parce que c’est la fin du mot.', 'Parce que c’est un nom.']), pq('Pourquoi deux s dans « tasse » ?', 'Le s est entre deux voyelles : avec un seul s, j’entendrais z.', ['Parce que c’est un objet.', 'Parce que le mot est long.']),
   pq('Pourquoi c dans « cerise » ?', 'Parce qu’après le c, il y a un e : c fait « s ».', ['Parce que c’est un fruit.', 'Parce que c’est le début du mot.']), pq('Pourquoi pas de cédille dans « cinéma » ?', 'Parce qu’après le c, il y a un i.', ['Parce que c’est un lieu.', 'Parce que le mot est long.'])],
  [pq('Pourquoi une cédille dans « maçon » ?', 'Parce qu’après le c, il y a un o : sans cédille, je lirais « k ».', ['Parce que c’est un métier.', 'Parce que le mot est court.']), pq('Pourquoi deux s dans « poisson » ?', 'Le s est entre deux voyelles : avec un seul s, j’entendrais z.', ['Parce que c’est un animal.', 'Parce que le mot est long.']),
   pq('Pourquoi pas de cédille dans « cygne » ?', 'Parce qu’après le c, il y a un y : c fait « s ».', ['Parce que c’est un oiseau.', 'Parce que c’est le début du mot.']), pq('Pourquoi une cédille dans « nous commençons » ?', 'Parce qu’après le c, il y a un o : je garde le son « s ».', ['Parce que c’est un verbe.', 'Parce que le mot est long.'])]),
}
O['O4'] = {
 'J’écris c': ([lt('un ___adeau', 'c', ['qu', 'k']), lt('un ___outeau', 'c', ['qu', 'k']), lt('la ___arotte', 'c', ['qu', 'k']), lt('une ___ulotte', 'c', ['qu', 'k'])],
  [lt('Le ___anard nage sur l’étang.', 'c', ['qu', 'k']), lt('Elle a mis une ___ravate rouge.', 'c', ['qu', 'k']), lt('Papa coupe le pain avec un ___outeau.', 'c', ['qu', 'k']), lt('Ma grand-mère cuisine une ___arotte râpée.', 'c', ['qu', 'k'])]),
 'Devant une consonne': ([lt('un ___rapaud', 'c', ['qu', 'k']), lt('une ___laque', 'c', ['qu', 'k']), lt('une a___tion', 'c', ['qu', 'k']), lt('un ___rayon', 'c', ['qu', 'k'])],
  [lt('Le ___rapaud saute dans la mare.', 'c', ['qu', 'k']), lt('Nous avons une grande ___lasse au deuxième étage.', 'c', ['qu', 'k']), lt('Le roi a prononcé un dis___ours.' if False else 'Le ___roissant est encore chaud.', 'c', ['qu', 'k']), lt('Ce gentil garçon a fait une bonne a___tion.', 'c', ['qu', 'k'])]),
 'J’écris qu': ([lt('une ___ête', 'qu', ['c', 'k']), lt('un mas___e', 'qu', ['c', 'k']), lt('une ___estion', 'qu', ['c', 'k']), lt('un bou___et', 'qu', ['c', 'k'])],
  [lt('Le lutin porte un mas___e en carton.', 'qu', ['c', 'k']), lt('Elle pose une ___estion à la maîtresse.', 'qu', ['c', 'k']), lt('Je lui ai offert un bou___et de fleurs.', 'qu', ['c', 'k']), lt('Le chevalier part en ___ête du trésor.', 'qu', ['c', 'k'])]),
 'Des mots à mémoriser': ([bien('quarante', ['carante', 'karante']), bien('quatorze', ['catorze', 'katorze']), bien('quatre', ['catre', 'katre']), bien('pourquoi', ['pourcoi', 'pourkoi'])],
  [bien('quarante', ['carante', 'karante']), bien('quatorze', ['catorze', 'katorze']), bien('quelqu’un', ['celqu’un', 'kelqu’un']), bien('quatre-vingts', ['catre-vingts', 'katre-vingts'])]),
 'J’écris k': ([bien('un kangourou', ['un cangourou', 'un quangourou']), bien('un kilomètre', ['un cilomètre', 'un quilomètre']), bien('un kiwi', ['un quiwi', 'un ciwi']), bien('un kimono', ['un quimono', 'un cimono'])],
  [bien('un kilogramme', ['un cilogramme', 'un quilogramme']), bien('un koala', ['un coala', 'un quoala']), bien('un kayak', ['un cayak', 'un quayak']), bien('un ketchup', ['un cetchup', 'un quetchup'])]),
 'Je prouve': ([pq('Pourquoi qu dans « quille » ?', 'Parce qu’après, il y a un i : c devant i ferait « s ».', ['Parce que c’est le début du mot.', 'Parce que c’est un jeu.']), pq('Pourquoi c dans « cube » ?', 'Parce qu’après, il y a un u.', ['Parce que le mot est court.', 'Parce que c’est un nom.']),
   pq('Pourquoi qu dans « masque » ?', 'Parce qu’après, il y a un e : c devant e ferait « s ».', ['Parce que c’est un objet.', 'Parce que le mot est court.']), pq('Pourquoi c dans « carotte » ?', 'Parce qu’après, il y a un a.', ['Parce que c’est un légume.', 'Parce que c’est le début du mot.'])],
  [pq('Pourquoi qu dans « banquet » ?', 'Parce qu’après, il y a un e.', ['Parce qu’il y a un n avant.', 'Parce que c’est un repas.']), pq('Pourquoi c dans « couteau » ?', 'Parce qu’après, il y a un o.', ['Parce que c’est un objet.', 'Parce que le mot est long.']),
   pq('Pourquoi qu dans « quête » ?', 'Parce qu’après, il y a un ê : c devant ê ferait « s ».', ['Parce que c’est un nom.', 'Parce que le mot est court.']), pq('Pourquoi c dans « classe » ?', 'Parce qu’après le c, il y a une consonne : l.', ['Parce que c’est un nom.', 'Parce que le mot est long.'])]),
}
O['O5'] = {
 'J’écris g': ([lt('un ___ant', 'g', ['gu', 'ge']), lt('une ___ourde', 'g', ['gu', 'ge']), lt('un ___arçon', 'g', ['gu', 'ge']), lt('un ___rand', 'g', ['gu', 'ge'])],
  [lt('Le ___orille se balance dans l’arbre.', 'g', ['gu', 'ge']), lt('Elle remplit sa ___ourde d’eau fraîche.', 'g', ['gu', 'ge']), lt('Les ___ants de laine protègent du froid.', 'g', ['gu', 'ge']), lt('Un ___rand sapin trône au milieu du salon.', 'g', ['gu', 'ge'])]),
 'J’écris gu': ([lt('une ba___e', 'gu', ['g', 'ge']), lt('un ___ide', 'gu', ['g', 'ge']), lt('une ___itare', 'gu', ['g', 'ge']), lt('une fi___e', 'gu', ['g', 'ge'])],
  [lt('Elle porte une jolie ba___e à son doigt.', 'gu', ['g', 'ge']), lt('Le ___ide nous montre le chemin.', 'gu', ['g', 'ge']), lt('Mon frère joue de la ___itare.', 'gu', ['g', 'ge']), lt('Ma grand-mère cueille une fi___e mûre.', 'gu', ['g', 'ge'])]),
 'g fait « j »': ([C('', 'Dans « gilet », le g se prononce…', '« j » comme dans « jardin »', ['« g » comme dans « gare »'], 'Devant e, i, y : g fait « j ».'), C('', 'Dans « gomme », le g se prononce…', '« g » comme dans « gare »', ['« j » comme dans « jardin »'], 'Devant a, o, u : g fait « g ».'),
   C('', 'Dans « gymnaste », le g se prononce…', '« j » comme dans « jardin »', ['« g » comme dans « gare »'], 'Devant e, i, y : g fait « j ».'), C('', 'Dans « gourde », le g se prononce…', '« g » comme dans « gare »', ['« j » comme dans « jardin »'], 'Devant a, o, u : g fait « g ».')],
  [C('', 'Dans « girouette », le g se prononce…', '« j » comme dans « jardin »', ['« g » comme dans « gare »'], 'Devant e, i, y : g fait « j ».'), C('', 'Dans « gorge », le premier g se prononce…', '« g » comme dans « gare »', ['« j » comme dans « jardin »'], 'Devant o : g fait « g » ; devant e : g fait « j ».'),
   C('', 'Dans « gymnase », le g se prononce…', '« j » comme dans « jardin »', ['« g » comme dans « gare »'], 'Devant y : g fait « j ».'), C('', 'Dans « légume », le g se prononce…', '« g » comme dans « gare »', ['« j » comme dans « jardin »'], 'Devant u : g fait « g ».')]),
 'J’écris ge': ([lt('nous nei___ons', 'ge', ['g', 'gu']), lt('nous man___ons', 'ge', ['g', 'gu']), lt('un pi___on', 'ge', ['g', 'gu']), lt('un plon___on', 'ge', ['g', 'gu'])],
  [lt('Nous man___ons des fruits à midi.', 'ge', ['g', 'gu']), lt('Un pi___on se pose sur le toit.', 'ge', ['g', 'gu']), lt('Le plon___on du sauveteur était parfait.', 'ge', ['g', 'gu']), lt('Nous nei___ons le trottoir devant la maison.', 'ge', ['g', 'gu'])]),
 'Je prouve': ([pq('Pourquoi un u dans « guitare » ?', 'Sans u, g devant i ferait « j ».', ['Parce que c’est un instrument.', 'Parce que le u s’entend.']), pq('Pourquoi ge dans « pigeon » ?', 'Après, il y a o : sans e, je lirais « g ».', ['Parce que c’est un oiseau.', 'Parce que le mot est long.']),
   pq('Pourquoi g seul dans « gare » ?', 'Parce qu’après, il y a un a.', ['Parce que c’est le début du mot.', 'Parce que c’est un nom.']), pq('Pourquoi gu dans « bague » ?', 'Sans u, g devant e ferait « j ».', ['Parce que c’est un bijou.', 'Parce que le mot est court.'])],
  [pq('Pourquoi ge dans « mangeons » ?', 'Parce qu’après, il y a o : je garde le son « j ».', ['Parce que c’est un verbe.', 'Parce que le mot est long.']), pq('Pourquoi gu dans « figue » ?', 'Sans u, g devant e ferait « j ».', ['Parce que c’est un fruit.', 'Parce que le mot est court.']),
   pq('Pourquoi g seul dans « gomme » ?', 'Parce qu’après, il y a un o.', ['Parce que c’est un objet.', 'Parce que le mot est court.']), pq('Pourquoi ge dans « plongeon » ?', 'Après, il y a o : sans e, je lirais « g ».', ['Parce que c’est un sport.', 'Parce que le mot est long.'])]),
}
O['O6'] = {
 'ill après une voyelle': ([ls('une feu___e', 'ill', ['y', 'oy']), ls('une pa___e', 'ill', ['y', 'oy']), ls('une boute___e', 'ill', ['y', 'oy']), ls('une grenou___e', 'ill', ['y', 'oy'])],
  [ls('Une feu___e tombe de l’arbre.', 'ill', ['y', 'oy']), ls('Le fermier dort dans la pa___e.', 'ill', ['y', 'oy']), ls('Le jardinier arrose avec une boute___e.', 'ill', ['y', 'oy']), ls('La grenou___e saute dans la mare.', 'ill', ['y', 'oy'])]),
 'À la fin : il': ([ls('un écureu___', 'il', ['ille', 'y']), ls('un fauteu___', 'il', ['ille', 'y']), ls('un trava___', 'il', ['ille', 'y']), ls('un réve___', 'il', ['ille', 'y'])],
  [ls('Un écureu___ grimpe dans le chêne.', 'il', ['ille', 'y']), ls('Mon grand-père s’assoit dans son fauteu___.', 'il', ['ille', 'y']), ls('Le réve___ sonne à sept heures.', 'il', ['ille', 'y']), ls('Cet ouvrier fait un beau trava___.', 'il', ['ille', 'y'])]),
 'ille': ([ls('une fam___', 'ille', ['y', 'il']), ls('une gr___', 'ille', ['y', 'il']), ls('une f___', 'ille', ['y', 'il']), ls('une v___', 'ille', ['y', 'il'])],
  [ls('Ma fam___ part en vacances demain.', 'ille', ['y', 'il']), ls('La gr___ du jardin est fermée.', 'ille', ['y', 'il']), ls('Cette petite f___ dessine un chat.', 'ille', ['y', 'il']), ls('Nous habitons dans une grande v___.', 'ille', ['y', 'il'])]),
 'y = deux i': ([lt('un tu___au', 'y', ['ill', 'i']), lt('un cra___on', 'y', ['ill', 'i']), lt('un pa___san', 'y', ['ill', 'i']), lt('un ra___on', 'y', ['ill', 'i'])],
  [lt('Un tu___au traverse le mur de la cuisine.', 'y', ['ill', 'i']), lt('Le pa___san travaille dans son champ.', 'y', ['ill', 'i']), lt('Elle dessine avec un cra___on bleu.', 'y', ['ill', 'i']), lt('Un ra___on de soleil entre par la fenêtre.', 'y', ['ill', 'i'])]),
 'oi': ([ls('une ét___le', 'oi', ['oy', 'ill']), ls('le m___s de mai', 'oi', ['oy', 'y']), ls('une p___re', 'oi', ['oy', 'ill']), ls('un r___', 'oi', ['oy', 'ill'])],
  [ls('Une ét___le brille dans le ciel.', 'oi', ['oy', 'ill']), ls('Nous partons en vacances au m___s de juillet.', 'oi', ['oy', 'y']), ls('Elle mange une p___re juteuse.', 'oi', ['oy', 'ill']), ls('Le r___ porte une couronne dorée.', 'oi', ['oy', 'ill'])]),
 'oy': ([ls('il v___age', 'oy', ['oi', 'ill']), ls('il se n___ait', 'oy', ['oi', 'ill']), ls('un r___aume', 'oy', ['oi', 'ill']), ls('un cit___en', 'oy', ['oi', 'ill'])],
  [ls('Mes parents v___agent chaque été.', 'oy', ['oi', 'ill']), ls('Le r___aume était entouré de montagnes.', 'oy', ['oi', 'ill']), ls('Le vieux marin n___ait ses souvenirs dans l’océan.', 'oy', ['oi', 'ill']), ls('Chaque cit___en doit respecter la loi.', 'oy', ['oi', 'ill'])]),
 'Je prouve': ([pq('Pourquoi oy dans « voyage » ?', 'Parce qu’après, il y a une voyelle : oy = oi + i.', ['Parce que c’est un nom.', 'Parce que le mot est long.']), pq('Pourquoi un y dans « tuyau » ?', 'Parce que y entre deux voyelles vaut deux i.', ['Parce que c’est un objet.', 'Parce que le y ne s’entend pas.']),
   pq('Pourquoi ill dans « feuille » ?', 'Parce qu’avant, il y a une voyelle : eu.', ['Parce que c’est un mot court.', 'Parce que c’est une plante.']), pq('Pourquoi ille dans « famille » ?', 'Parce qu’avant, il y a une consonne : m.', ['Parce que c’est un nom.', 'Parce que le mot est long.'])],
  [pq('Pourquoi oy dans « royaume » ?', 'Parce qu’après, il y a une voyelle : oy = oi + i.', ['Parce que c’est un nom.', 'Parce que le mot est long.']), pq('Pourquoi un y dans « crayon » ?', 'Parce que y entre deux voyelles vaut deux i.', ['Parce que c’est un objet.', 'Parce que le y ne s’entend pas.']),
   pq('Pourquoi ill dans « paille » ?', 'Parce qu’avant, il y a une voyelle : a.', ['Parce que c’est un mot court.', 'Parce que c’est un animal.']), pq('Pourquoi oi dans « étoile » ?', 'Parce qu’après, il y a une consonne : l, pas une voyelle.', ['Parce que c’est un astre.', 'Parce que le mot est long.'])]),
}
if __name__ == '__main__':
    for g in O:
        titres = [e['titre'] for e in lessons_json(g)['ecrans']]
        manque = [t for t in titres if t not in O[g]]
        assert not manque, (g, manque)
        appliquer(g, {t: O[g][t] for t in titres})
