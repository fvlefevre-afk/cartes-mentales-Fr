#!/usr/bin/env python3
"""« Je retiens » : trois exemples sous chaque point (25/11/2026, demande de l'enseignante : « sous chaque point 3 exemples, et les enlever du texte
s'ils y sont déjà »). Réécrit CE2_PLUS, CM1_PLUS et CM2_PLUS dans index.html : chaque <li> devient
<li>TEXTE<span class="exs"><i>exemple</i><i>exemple</i><i>exemple</i></span></li>. Rejouable : un point qui a déjà son bloc « exs » n'est pas touché.
Clé = « NIVEAU|ceinture|n° du point » ; valeur = (nouveau texte ou None pour garder l'ancien, [3 exemples]).
Usage : python3 outils/retiens_exemples.py"""
import json, pathlib, re, sys

P = pathlib.Path(__file__).resolve().parent.parent / "index.html"

R = {
# ---------------- CM1 ----------------
"CM1|G1|1": (None, ["Le chat dort.", "Léa mange une pomme.", "Les enfants jouent dans la cour."]),
"CM1|G1|2": ("Le sujet peut être <b>un seul mot</b> ou <b>un groupe de mots</b>. Je le trouve avec « <b>qui est-ce qui</b>… ? ».", ["<b>Charles</b> court.", "<b>Toutes les dames du salon</b> discutent.", "<b>Mon petit chat</b> dort."]),
"CM1|G1|3": ("Le verbe dit <b>l’action</b> : je demande « qu’est-ce qu’il / elle fait ? ». Il <b>change avec le moment</b>.", ["Hier, il <b>regardait</b> la télé.", "Aujourd’hui, il <b>regarde</b> la télé.", "Demain, il <b>regardera</b> la télé."]),
"CM1|G2|1": (None, ["Léa mange une pomme. (déclarative)", "Où habites-tu ? (interrogative)", "Ferme la porte. (impérative)"]),
"CM1|G2|2": ("Deux formes : <b>affirmative</b> et <b>négative</b>. La négation <b>encadre le verbe</b> (<b>n’</b> devant une voyelle).", ["Tom <b>ne</b> chante <b>pas</b>.", "Je <b>n’</b>entends <b>rien</b>.", "Il <b>ne</b> vient <b>plus</b>."]),
"CM1|G2|3": (None, ["Quelle belle journée !", "Comme tu chantes bien !", "Ne touche pas !"]),
"CM1|G3|1": (None, ["le chat noir", "une grande maison", "mes deux frères"]),
"CM1|G3|2": (None, ["un <b>chat</b> noir", "de belles <b>fleurs</b>", "la <b>porte</b> bleue"]),
"CM1|G3|3": (None, ["un chat <b>noir</b>", "une <b>grande</b> maison", "des fleurs <b>jaunes</b>"]),
"CM1|G3|4": ("Au féminin, j’ajoute souvent <b>e</b> (parfois le mot change). Au pluriel, j’ajoute souvent <b>s</b>.", ["un ami → une ami<b>e</b>", "gros → gro<b>sse</b>", "un chat → des chat<b>s</b>"]),
"CM1|G3|5": ("Attention : pluriel en <b>x</b>, <b>-al → -aux</b> ; déjà en -s, -x, -z : pas de changement.", ["un gâteau → des gâteau<b>x</b>", "un cheval → des chev<b>aux</b>", "un pays → des pays"]),
"CM1|G4|1": (None, ["articles : <b>le, la, un, des</b>", "possessifs : <b>mon, ta, leurs</b>", "démonstratifs : <b>ce, cette, ces</b>"]),
"CM1|G4|2": ("Le <b>verbe</b> se conjugue ; le <b>pronom</b> remplace un groupe nominal.", ["Léa chante → <b>Elle</b> chante", "Les enfants jouent → <b>Ils</b> jouent", "Le chien aboie → <b>Il</b> aboie"]),
"CM1|G4|3": ("L’<b>adverbe</b> précise un verbe, un adjectif ou un autre adverbe (beaucoup finissent par <i>-ment</i>).", ["Il court <b>vite</b>.", "Elle est <b>très</b> gentille.", "Il parle <b>doucement</b>."]),
"CM1|G4|4": ("Les <b>conjonctions de coordination</b> relient : mais, ou, et, or, ni, car.", ["Je lis <b>et</b> j’écris.", "Tu veux du thé <b>ou</b> du café ?", "Il pleut, <b>mais</b> je sors."]),
"CM1|G4|5": (None, ["un grand arbre → de grands arbres (variable)", "je chante → nous chantons (variable)", "très, demain, mais, et (invariables)"]),
"CM1|G5|1": ("Le verbe <b>s’accorde avec son sujet</b>.", ["tu chant<b>es</b>", "nous chant<b>ons</b>", "ils chant<b>ent</b>"]),
"CM1|G5|2": ("Pour trouver le sujet, je <b>le remplace par un pronom</b>.", ["Les enfants (= <b>ils</b>) jouent.", "Ma sœur (= <b>elle</b>) lit.", "Le chat et le chien (= <b>ils</b>) dorment."]),
"CM1|G5|3": ("Attention aux pièges : le sujet est loin du verbe ou un petit mot est devant.", ["Le chat des voisins <b>miaule</b>.", "Je les <b>regarde</b>.", "Les élèves de la classe <b>chantent</b>."]),
"CM1|G5|4": ("Les verbes du <b>2e groupe</b> : infinitif en <b>-ir</b>, avec <b>-iss-</b> à nous, vous, ils ; <i>partir</i> n’en est pas.", ["finir → nous fin<b>iss</b>ons", "grandir → ils grand<b>iss</b>ent", "choisir → vous chois<b>iss</b>ez"]),
"CM1|G5|5": (None, ["Les oiseaux (chanter) : sujet = ils → ils chant<b>ent</b>", "Nous (finir) : nous fin<b>iss</b>ons", "Tu (jouer) : tu jou<b>es</b>"]),
"CM1|G6|1": (None, ["Léa mange <b>une pomme</b>.", "Le chat dort <b>sur le canapé</b>.", "<b>Ce matin</b>, il pleut."]),
"CM1|G6|2": ("Le <b>complément d’objet</b> complète le verbe : il se place <b>après lui</b> et on <b>ne peut pas le déplacer</b>. COD : sans préposition ; COI : avec <i>à</i> ou <i>de</i>.", ["COD : Tom lance <b>le ballon</b>.", "COI : Il parle <b>à sa mère</b>.", "COI : Elle rêve <b>de vacances</b>."]),
"CM1|G6|3": (None, ["<b>Hier</b>, j’ai joué.", "Il dort <b>dans le salon</b>.", "Elle chante <b>joyeusement</b>."]),
"CM1|G6|4": (None, ["Léa lit un livre <b>le soir</b>. → je supprime « le soir » : Léa lit un livre.", "<b>Le soir</b>, Léa lit un livre. → je déplace : la phrase reste juste.", "Léa lit <b>un livre</b>. → le complément d’objet reste après le verbe."]),
"CM1|G7|1": (None, ["Les petites filles <b>chantent</b>.", "Mon grand frère <b>dort</b>.", "Les chats noirs <b>miaulent</b>."]),
"CM1|G7|2": ("Avec <b>être</b>, le participe passé s’accorde avec le <b>sujet</b>, comme un adjectif.", ["Léa est parti<b>e</b>.", "Elles sont parti<b>es</b>.", "Tom est parti."]),
"CM1|G7|3": ("Avec <b>avoir</b>, pas d’accord avec le sujet.", ["Léa a mangé.", "Elles ont mangé.", "Nous avons chanté."]),
"CM1|G7|4": (None, ["Les filles sont arriv<b>ées</b>.", "Mon frère est part<b>i</b>.", "Les petits chats sont tomb<b>és</b>."]),
"CM1|H1|1": ("<b>avoir</b> et <b>être</b> au présent.", ["j’<b>ai</b>, tu <b>as</b>, il <b>a</b>, ils <b>ont</b>", "je <b>suis</b>, tu <b>es</b>, il <b>est</b>, ils <b>sont</b>", "Tom <b>a</b> un vélo. Tom <b>est</b> content."]),
"CM1|H1|2": ("Pour choisir : je dis la phrase avec <b>« hier »</b> ou je <b>change le sujet</b>.", ["Il a un chien → hier, il <b>avait</b> un chien", "Il est content → hier, il <b>était</b> content", "Il a faim → ils <b>ont</b> faim"]),
"CM1|H1|3": ("Le sujet me dit la personne, le sens me dit le verbe. Le sujet peut être loin ou formé de plusieurs mots.", ["Tom <b>a</b> un vélo. (avoir)", "Tom <b>est</b> content. (être)", "Léa et Tom <b>ont</b> gagné. (sujet de plusieurs mots)"]),
"CM1|H1|4": (None, ["Mes voisins <b>ont</b> un chat.", "Le chien de Léa <b>est</b> gentil.", "Elles <b>ont</b> gagné."]),
"CM1|H2|1": ("<b>on</b> est un pronom : je prouve avec <b>quelqu’un</b> ; le verbe est au singulier.", ["<b>On</b> chante. (quelqu’un chante)", "<b>On</b> finit à midi.", "<b>On</b> joue dehors."]),
"CM1|H2|2": ("<b>là</b> indique un lieu : je prouve avec <b>ici</b> ; il garde l’accent dans les mots composés.", ["Pose ton sac <b>là</b>. (ici)", "<b>Là</b>-bas, il y a un lac.", "<b>Voilà</b> mon cahier."]),
"CM1|H2|3": ("<b>où</b> indique le lieu : je prouve en répondant par un lieu ; il commence souvent une question.", ["<b>Où</b> habites-tu ?", "<b>Où</b> est mon sac ?", "La ville <b>où</b> je vis est petite."]),
"CM1|H3|1": ("<b>ce, cet, cette</b> : déterminants au singulier (<b>cet</b> devant une voyelle ou un h muet) ; <b>ces</b> : devant un nom au pluriel.", ["<b>ce</b> chien, <b>cette</b> fleur", "<b>cet</b> arbre, <b>cet</b> hôtel", "<b>ces</b> chiens, <b>ces</b> fleurs"]),
"CM1|H3|2": ("Je prouve en mettant au singulier ou au pluriel.", ["ces chiens → ce chien", "ces fleurs → cette fleur", "ces arbres → cet arbre"]),
"CM1|H3|3": ("<b>à</b> est un petit mot qui ne change jamais : je mets la phrase au passé, il ne bouge pas. En majuscule, il garde son accent.", ["Il parle <b>à</b> sa mère.", "<b>À</b> demain !", "à + le = <b>au</b> : je vais <b>au</b> parc."]),
"CM1|H4|1": ("<b>et</b> : j’ajoute.", ["du pain <b>et</b> du beurre", "Tom <b>et</b> Léa", "Je lis <b>et</b> j’écris."]),
"CM1|H4|2": ("<b>ou</b> : je choisis, je peux dire <b>ou bien</b>.", ["pile <b>ou</b> face", "du thé <b>ou</b> du café ?", "Tu viens <b>ou</b> tu restes ?"]),
"CM1|H4|3": ("<b>mais</b> : j’oppose deux idées, souvent avec une virgule avant.", ["Il pleut<b>, mais</b> je sors.", "Je veux jouer<b>, mais</b> j’ai du travail.", "Il est petit<b>, mais</b> il est fort."]),
"CM1|H4|4": (None, ["Je ne mange <b>ni</b> pain <b>ni</b> gâteau.", "Il rentre, <b>car</b> il a froid.", "Il pleuvait, <b>or</b> j’avais mon parapluie."]),
"CM1|H5|1": ("<b>la</b> devant un nom féminin est un déterminant : je dis <b>une</b> ou je mets au pluriel.", ["<b>la</b> porte → une porte, les portes", "<b>la</b> table → une table, les tables", "<b>la</b> rue → une rue, les rues"]),
"CM1|H5|2": ("<b>la</b> devant un verbe est un pronom : avec un nom masculin, je dis <b>le</b>.", ["Je <b>la</b> coiffe → Je <b>le</b> coiffe", "Il <b>la</b> regarde → Il <b>le</b> regarde", "Nous <b>la</b> cherchons → Nous <b>le</b> cherchons"]),
"CM1|H5|3": ("<b>c’est</b> = cela est : je mets au passé, <b>c’était</b> ; toujours avec une apostrophe.", ["<b>C’est</b> mon livre. → C’était mon livre.", "<b>C’est</b> facile.", "<b>C’est</b> l’heure de partir."]),
"CM1|H6|1": (None, ["Tom prend <b>son</b> vélo. (à lui)", "Léa range <b>ses</b> crayons. (plusieurs, à elle)", "Je range <b>mes</b> livres. (plusieurs, à moi)"]),
"CM1|H6|2": ("Je prouve en changeant la personne ou en mettant au singulier.", ["son vélo → mon vélo", "ses crayons → son crayon", "mes livres → mon livre"]),
"CM1|H6|3": ("Le possessif s’accorde avec le nom : un seul ou plusieurs ? Devant une voyelle, j’écris <b>son</b> même pour un nom féminin.", ["<b>son</b> amie", "<b>son</b> école", "<b>mon</b> idée"]),
"CM1|H7|1": ("<b>se</b> est devant un verbe : je prouve en changeant la personne.", ["Il <b>se</b> lève → je me lève", "Elle <b>se</b> coiffe → tu te coiffes", "Ils <b>se</b> cachent → nous nous cachons"]),
"CM1|H7|2": ("<b>s’est</b> = se + est, passé composé (je me suis levé).", ["il se lève → il <b>s’est</b> levé", "elle se coiffe → elle <b>s’est</b> coiffée", "on se lave → on <b>s’est</b> lavé"]),
"CM1|H7|3": ("Comme avec être, le participe passé s’accorde avec le sujet (au pluriel : <b>se sont</b>).", ["Tom s’est levé.", "Léa s’est levé<b>e</b>.", "Ils se sont levé<b>s</b>."]),
"CM1|C1|1": (None, ["chant + <b>e</b> : je chante", "chant + <b>ons</b> : nous chantons", "chant + <b>ent</b> : ils chantent"]),
"CM1|C1|2": ("<b>1er groupe</b> : infinitif en <i>-er</i> (sauf <i>aller</i>) ; le radical peut changer. <b>2e groupe</b> : infinitif en <i>-ir</i>, avec <i>-iss-</i> à nous, vous, ils.", ["je l<b>è</b>ve · nous l<b>e</b>vons · j’app<b>ell</b>e", "nous mang<b>e</b>ons · nous commen<b>ç</b>ons", "nous fin<b>iss</b>ons (2e groupe)"]),
"CM1|C1|3": ("<b>être, avoir</b> et les verbes à connaître.", ["<b>aller</b> : je vais, ils vont", "<b>faire</b> : vous faites, ils font", "<b>prendre</b> : il prend, nous prenons"]),
"CM1|C1|4": ("Attention aux terminaisons à connaître par cœur. Un sujet composé = <i>nous</i> ou <i>ils</i>.", ["tu v<b>eux</b>, tu p<b>eux</b>", "vous <b>êtes</b>, <b>faites</b>, <b>dites</b>", "ils <b>sont</b>, <b>ont</b>, <b>vont</b>, <b>font</b>"]),
"CM1|C2|1": ("Le <b>futur</b> dit ce qui va se passer : <b>infinitif + ai, as, a, ons, ez, ont</b>.", ["je chanter<b>ai</b>", "tu finir<b>as</b>", "nous jouer<b>ons</b>"]),
"CM1|C2|2": ("Toujours un <b>r</b> avant la terminaison : c’est la marque du futur. Parfois deux r (avec <i>pouvoir</i> et <i>voir</i>).", ["tu chante<b>r</b>as", "je pou<b>rr</b>ai (deux r)", "il ve<b>rr</b>a (deux r)"]),
"CM1|C2|3": ("Verbes en <i>-re</i> : j’enlève le e ; <i>jouer</i> : le e s’écrit.", ["prendre → je prend<b>r</b>ai", "jouer → je jou<b>e</b>rai", "lire → je li<b>r</b>ai"]),
"CM1|C2|4": ("<b>être</b>, <b>avoir</b> et les irréguliers : le radical change, les terminaisons restent.", ["être → je <b>ser</b>ai", "avoir → j’<b>aur</b>ai", "aller → j’<b>ir</b>ai"]),
"CM1|C3|1": ("L’<b>imparfait</b> parle du passé : ce qui durait, ce qui se répétait.", ["Autrefois, je jouais dehors.", "Il pleuvait toute la journée.", "Chaque matin, nous marchions."]),
"CM1|C3|2": ("Je prends le <b>radical de « nous »</b> au présent + <b>-ais, -ais, -ait, -ions, -iez, -aient</b>.", ["nous finissons → je <b>finiss</b>ais", "nous chantons → tu <b>chant</b>ais", "nous prenons → ils <b>pren</b>aient"]),
"CM1|C3|3": ("<b>être</b> est le seul qui ne suit pas la règle.", ["j’<b>étais</b>", "tu <b>étais</b>", "nous <b>étions</b>"]),
"CM1|C3|4": ("Attention : verbes en <i>-ger</i>, verbes en <i>-cer</i>, et deux i avec les verbes en <i>-ier</i>.", ["je mang<b>e</b>ais · nous mangions", "je commen<b>ç</b>ais · nous commencions", "nous cri<b>i</b>ons"]),
"CM1|C4|1": ("Le <b>passé composé</b> parle d’une action terminée : <b>avoir au présent + participe passé</b>.", ["j’<b>ai chanté</b>", "nous <b>avons fini</b>", "tu <b>as joué</b>"]),
"CM1|C4|2": ("Participe passé : 1er groupe <i>-é</i>, 2e groupe <i>-i</i>. Pour écrire <i>é</i> ou <i>er</i>, je remplace par <i>vendu</i>.", ["chanter → chant<b>é</b>", "finir → fin<b>i</b>", "Il a mang<b>é</b> : je remplace par vendu → <b>é</b>"]),
"CM1|C4|3": ("À la forme négative, <i>ne… pas</i> encadre l’auxiliaire.", ["Je <b>n’</b>ai <b>pas</b> chanté.", "Tu <b>n’</b>as <b>pas</b> fini.", "Nous <b>n’</b>avons <b>pas</b> joué."]),
"CM1|C4|4": ("Avec <b>avoir</b>, le participe passé ne s’accorde pas avec le sujet.", ["elles ont chanté", "Léa a mangé", "nous avons fini"]),
"CM1|C5|1": (None, ["Je <b>suis</b> allé au parc.", "Il <b>est</b> arrivé hier.", "Nous <b>sommes</b> partis tôt."]),
"CM1|C5|2": ("Avec <b>être</b>, le participe passé <b>s’accorde avec le sujet</b>.", ["Tom est parti.", "Léa est parti<b>e</b>.", "Ils sont parti<b>s</b>."]),
"CM1|C5|3": ("Avec <b>avoir</b>, je n’accorde pas. Les verbes avec <i>se</i> aussi se conjuguent avec être.", ["Elle est tombée.", "Elle a joué.", "Elle s’est levée."]),
"CM1|C6|1": ("Au présent, je connais : <b>aller</b>, <b>faire</b>, <b>dire</b>, <b>venir</b>, <b>pouvoir, vouloir</b>, <b>voir, prendre</b>.", ["<b>aller</b> : je vais, ils vont", "<b>faire</b> : vous faites, ils font", "<b>vouloir</b> : je veux, nous voulons"]),
"CM1|C6|2": ("Le radical change.", ["venir : je viens, nous venons, ils viennent", "prendre : je prends, nous prenons, ils prennent", "pouvoir : je peux, nous pouvons, ils peuvent"]),
"CM1|C6|3": ("Attention aux terminaisons à connaître par cœur.", ["tu pe<b>ux</b>, tu ve<b>ux</b> (avec un x)", "il pren<b>d</b> (sans t)", "vous fai<b>tes</b>, vous di<b>tes</b> · ils <b>vont</b>, ils <b>font</b>"]),
"CM1|C7|1": ("<b>Futur</b> : le radical change, la terminaison reste ; deux r à <i>pouvoir</i> et <i>voir</i>.", ["j’<b>ir</b>ai · je <b>fer</b>ai · je <b>dir</b>ai", "je <b>viendr</b>ai · je <b>voudr</b>ai · je <b>prendr</b>ai", "je pou<b>rr</b>ai · je ve<b>rr</b>ai"]),
"CM1|C7|2": ("<b>Imparfait</b> : je pars du radical de <i>nous</i>.", ["nous faisons → je <b>fais</b>ais", "nous disons → je <b>dis</b>ais", "nous prenons → il <b>pren</b>ait"]),
"CM1|C7|3": ("<b>Participe passé</b> : <i>allé, fait, dit, venu, pu, vu, voulu, pris</i>. Avec avoir ou avec être.", ["je suis <b>allé</b>", "j’ai <b>fait</b>", "il a <b>pris</b>"]),
"CM1|C7|4": ("Le présent et le passé composé se ressemblent : l’<b>auxiliaire</b> m’aide.", ["il <b>fait</b> (présent) · il <b>a fait</b> (passé composé)", "il <b>dit</b> · il <b>a dit</b>", "il <b>prend</b> · il <b>a pris</b>"]),
"CM1|V1|1": ("Le <b>mot-étiquette</b> est un mot général qui regroupe des <b>mots précis</b>.", ["fruits → pomme, poire, cerise", "animaux → chien, chat, cheval", "outils → marteau, scie, tournevis"]),
"CM1|V1|2": ("L’échelle des mots va du général au précis. Un même mot peut être précis et étiquette.", ["animal → chien → caniche", "véhicule → voiture → taxi", "animal → oiseau → mésange"]),
"CM1|V1|3": (None, ["pomme, poire, cerise → <b>fruits</b>", "carotte, poireau, radis → <b>légumes</b>", "chaise, table, lit → <b>meubles</b>"]),
"CM1|V1|4": ("Ça sert à ranger mon carnet de mots et à éviter les répétitions.", ["une pomme… le <b>fruit</b>", "mon chien… l’<b>animal</b>", "ma voiture… le <b>véhicule</b>"]),
"CM1|V2|1": ("Pour comprendre un mot inconnu : je lis <b>toute la phrase</b>, je cherche des <b>indices dans la phrase</b> et <b>dans le mot</b> (un mot caché).", ["<b>incassable</b> : je vois « casser », donc qu’on ne peut pas casser", "Il est <b>affamé</b> : il n’a rien mangé → il a très faim", "Le <b>malheureux</b> pleure : je vois « heureux » avec mal-"]),
"CM1|V2|2": (None, ["Il est <b>affamé</b> → Il a très faim : la phrase garde son sens", "Un <b>sentier</b> traverse le bois → Un petit chemin traverse le bois", "Elle est <b>ravie</b> → Elle est très contente"]),
"CM1|V2|3": (None, ["je lis la phrase suivante", "je demande à un camarade", "je cherche dans le dictionnaire"]),
"CM1|V3|1": (None, ["<b>re</b>lire : préfixe + « lire »", "chant<b>eur</b> : « chanter » + suffixe -eur", "<b>mal</b>heureux : préfixe + « heureux »"]),
"CM1|V3|2": ("Préfixes : <i>re-</i> (à nouveau), <i>dé-</i> (le contraire), <i>in-, im-, mal-</i> (pas). Suffixes : <i>-ier</i> (métier), <i>-eur, -euse</i> (qui fait), <i>-ette</i> (petit), <i>-able</i> (qu’on peut), <i>-ment</i> (manière).", ["<b>re</b>faire (à nouveau) · <b>dé</b>faire (le contraire)", "boulang<b>ier</b> · chant<b>eur</b>", "fille<b>tte</b> (petite fille) · lav<b>able</b> (qu’on peut laver)"]),
"CM1|V3|3": ("Les morceaux sont des indices pour comprendre le mot.", ["<b>in</b>cass<b>able</b> : qu’on ne peut pas casser", "<b>dé</b>coller : le contraire de coller", "<b>re</b>faire : faire à nouveau"]),
"CM1|V3|4": ("Attention : il faut un mot de base qui existe (<i>reine</i> n’est pas <i>re + ine</i>) ; on écrit <i>im-</i> devant b, p, m.", ["<b>im</b>possible (devant p)", "<b>im</b>battable (devant b)", "<b>im</b>mobile (devant m)"]),
"CM1|V4|1": ("Une <b>famille de mots</b> : des mots qui ont une <b>partie commune</b> et parlent de la même chose.", ["jardin, jardinier, jardinage", "terre, terrain, enterrer", "chant, chanter, chanteur"]),
"CM1|V4|2": ("Je fabrique des mots en ajoutant des morceaux devant ou derrière.", ["terre → terrain", "terre → enterrer", "chaud → réchauffer"]),
"CM1|V4|3": ("<b>L’intrus</b> ressemble mais ne parle pas de la même chose.", ["<b>champ</b> n’est pas de la famille de chant", "<b>mer</b> n’est pas de la famille de mère", "<b>verre</b> n’est pas de la famille de vert"]),
"CM1|V4|4": ("La famille m’aide à écrire la lettre muette.", ["lait → lai<b>t</b>ière", "galop → galo<b>p</b>er", "plomb → plom<b>b</b>erie"]),
"CM1|V5|1": ("Les <b>synonymes</b> ont le même sens, ou presque : je choisis celui qui va avec la phrase.", ["content = joyeux", "un gros rhume → un rhume fort", "joli = beau"]),
"CM1|V5|2": ("Les <b>contraires</b> ont un sens opposé ; parfois un préfixe fabrique le contraire.", ["grand ↔ petit", "heureux ↔ <b>mal</b>heureux", "possible ↔ <b>im</b>possible"]),
"CM1|V5|3": (None, ["grand (adjectif) ↔ petit (adjectif)", "rapidement (adverbe) = vite (adverbe)", "marcher (verbe) = avancer (verbe)"]),
"CM1|V5|4": ("Avec une famille de mots, je trouve le contraire de chaque mot.", ["joie ↔ tristesse", "joyeux ↔ triste", "se réjouir ↔ s’attrister"]),
"CM1|V6|1": ("Les <b>homonymes</b> se prononcent pareil mais n’ont pas le même sens.", ["la mer, ma mère, le maire", "un verre, un ver, vert", "le pain, un pin"]),
"CM1|V6|2": ("Ils s’écrivent parfois autrement, parfois pareil : le déterminant et la phrase m’aident.", ["<b>verre</b>, <b>ver</b>, <b>vert</b> (écrits autrement)", "un <b>livre</b> · une <b>livre</b> (écrits pareil)", "une <b>voie</b> · je <b>vois</b> · une <b>voix</b>"]),
"CM1|V6|3": (None, ["Je mets mon <b>verre</b> sur la table.", "Le <b>ver</b> sort de la pomme.", "Le feu est <b>vert</b>."]),
"CM1|V6|4": (None, ["homonymes : <b>mer</b> / <b>mère</b>", "synonymes : <b>content</b> / <b>joyeux</b>", "contraires : <b>grand</b> / <b>petit</b>"]),
"CM1|O1|1": ("Devant <b>m, b, p</b>, j’écris <b>m</b> ; devant les autres lettres, j’écris <b>n</b>.", ["une ja<b>m</b>be (devant b)", "un po<b>m</b>pier (devant p)", "le ve<b>n</b>tre (devant t)"]),
"CM1|O1|2": ("C’est vrai pour <i>an, en, in, on</i>.", ["la cha<b>m</b>bre", "le te<b>m</b>ps", "l’o<b>m</b>bre"]),
"CM1|O1|3": (None, ["ja<b>m</b>be : la lettre qui suit est b", "po<b>m</b>pier : la lettre qui suit est p", "ve<b>n</b>tre : la lettre qui suit est t"]),
"CM1|O1|4": ("Quelques mots font exception : on écrit <b>n</b> devant b ou m.", ["bo<b>n</b>bon", "bo<b>n</b>bonne", "néa<b>n</b>moins"]),
"CM1|O2|1": ("À la fin de beaucoup de mots, une lettre <b>ne s’entend pas</b>.", ["le lai<b>t</b>", "un galo<b>p</b>", "gran<b>d</b>"]),
"CM1|O2|2": ("La <b>famille</b> m’aide et le <b>féminin</b> aussi.", ["lait → lai<b>t</b>ier", "grand → gran<b>d</b>e", "petit → peti<b>t</b>e"]),
"CM1|O2|3": ("Je prouve : « J’écris un t à la fin de <i>chat</i>, car j’entends t dans <i>chaton</i>. »", ["chat → chaton : un <b>t</b>", "lourd → lourde : un <b>d</b>", "plomb → plomberie : un <b>b</b>"]),
"CM1|O2|4": ("Quand aucun mot ne m’aide, je mémorise.", ["le nez", "un puits", "toujours"]),
"CM1|O3|1": ("Le son « s » : <b>s</b> au début ou à côté d’une consonne ; <b>ss</b> entre deux voyelles (attention : <i>poison</i> → z) ; <b>c</b> devant e, i, y ; <b>ç</b> devant a, o, u.", ["<b>s</b>ac · pen<b>s</b>er", "poi<b>ss</b>on", "<b>c</b>erise · <b>c</b>inéma · gar<b>ç</b>on"]),
"CM1|O3|2": (None, ["<b>c</b>erise : la lettre qui suit est e → c", "gar<b>ç</b>on : la lettre qui suit est o → ç", "poi<b>ss</b>on : entre deux voyelles → ss"]),
"CM1|O4|1": ("Le son « k » : <b>c</b> devant a, o, u ou devant une consonne / à la fin du mot.", ["une <b>c</b>abane · une <b>c</b>orde · un <b>c</b>ube", "un <b>c</b>rabe", "un sa<b>c</b>"]),
"CM1|O4|2": ("<b>qu</b> devant e, i ; quelques mots à mémoriser.", ["une <b>qu</b>ille", "un ban<b>qu</b>et", "<b>qu</b>and · <b>qu</b>atre (à mémoriser)"]),
"CM1|O4|3": ("<b>k</b> est rare : je mémorise.", ["un <b>k</b>angourou", "un <b>k</b>ilo", "un <b>k</b>iwi"]),
"CM1|O5|1": ("Le son « g » : <b>g</b> devant a, o, u ou une consonne ; <b>gu</b> devant e, i.", ["une <b>g</b>are · une <b>g</b>omme · <b>g</b>rand", "une <b>gu</b>itare", "une ba<b>gu</b>e"]),
"CM1|O5|2": ("Devant e, i, y, la lettre <b>g</b> fait « j ».", ["une <b>g</b>irafe", "un <b>g</b>enou", "le <b>g</b>ymnase"]),
"CM1|O5|3": ("Pour garder le son « j » devant a, o, u : <b>ge</b>.", ["nous man<b>ge</b>ons", "un pi<b>ge</b>on", "il na<b>ge</b>ait"]),
"CM1|O6|1": ("<b>ill</b> après une voyelle ; <b>il</b> à la fin d’un mot ; <b>ille</b> après une consonne.", ["la pa<b>ill</b>e · une abe<b>ill</b>e", "le sole<b>il</b> · un réve<b>il</b>", "une f<b>ille</b> · une b<b>ille</b>"]),
"CM1|O6|2": ("<b>y</b> entre deux voyelles vaut deux i.", ["un cra<b>y</b>on → crai-ion", "un no<b>y</b>au → noi-iau", "un pa<b>y</b>sage → pai-isage"]),
"CM1|O6|3": ("Le son « oi » s’écrit souvent <b>oi</b> ; devant une voyelle : <b>oy</b>.", ["le <b>roi</b> · une v<b>oi</b>ture", "un v<b>oy</b>age", "le r<b>oy</b>aume"]),
"CM1|O8|1": ("Nom masculin : <b>-é</b> sans e, sauf quelques exceptions ; nom féminin : <b>-ée</b>.", ["un caf<b>é</b> · un bl<b>é</b>", "une id<b>ée</b> · une journ<b>ée</b>", "le mus<b>ée</b> · le lyc<b>ée</b> (exceptions)"]),
"CM1|O8|2": ("Une qualité, un état : <b>-té</b> sans e ; sauf un contenu, une action : <b>-tée</b>.", ["la san<b>té</b> · la liber<b>té</b>", "la dic<b>tée</b>", "la mon<b>tée</b>"]),
"CM1|O8|3": ("Trois noms en <b>-tié</b> à mémoriser.", ["la moi<b>tié</b>", "l’ami<b>tié</b>", "la pi<b>tié</b>"]),
"CM1|O8|4": (None, ["<b>un</b> café (masculin) → -é", "<b>une</b> idée (féminin) → -ée", "<b>la</b> santé (une qualité) → -té"]),
"CM1|O9|1": ("Après <b>a-, e-, o-</b> ou <b>com-</b> au début du mot, la consonne se <b>double</b>.", ["a<b>pp</b>eler · a<b>cc</b>ident · a<b>tt</b>endre", "e<b>ff</b>ort · o<b>ff</b>rir", "co<b>mm</b>e"]),
"CM1|O9|2": ("Quelques exceptions à mémoriser.", ["<b>a</b>près", "<b>a</b>percevoir", "l’<b>a</b>telier"]),
"CM1|O9|3": ("Un mot de la même famille m’aide.", ["a<b>pp</b>eler → un a<b>pp</b>el", "a<b>tt</b>endre → l’a<b>tt</b>ente", "o<b>ff</b>rir → une o<b>ff</b>re"]),
"CM1|O9|4": (None, ["a<b>pp</b>orter : a- au début → double p", "e<b>ff</b>acer : e- au début → double f", "co<b>mm</b>encer : com- au début → double m"]),
"CM1|O10|1": ("Un nom en [œr] : <b>-eur</b> sans e ; exceptions : <i>l’heure, la demeure, le beurre, le leurre</i>.", ["le bonh<b>eur</b>", "la coul<b>eur</b>", "la p<b>eur</b>"]),
"CM1|O10|2": ("Un nom d’agent : je pense au verbe ; au féminin : <b>-euse</b> ou <b>-trice</b>.", ["chanter → un chant<b>eur</b> · une chant<b>euse</b>", "jouer → un jou<b>eur</b> · une jou<b>euse</b>", "un ac<b>teur</b> · une ac<b>trice</b>"]),
"CM1|O10|3": ("<b>œur</b> : trois noms à mémoriser.", ["le c<b>œur</b>", "la s<b>œur</b>", "le ch<b>œur</b>"]),
"CM1|O11|1": ("<b>-tion</b> : l’écriture la plus fréquente.", ["une na<b>tion</b>", "une ac<b>tion</b>", "une solu<b>tion</b>"]),
"CM1|O11|2": ("<b>-sion</b> après une voyelle, quand j’entends « z » ; après n, r : souvent <i>-tion</i>, quelques <i>-sion</i> à mémoriser.", ["une déci<b>sion</b>", "la vi<b>sion</b>", "une atten<b>tion</b> · la ver<b>sion</b>"]),
"CM1|O11|3": ("<b>-ssion</b> entre deux voyelles, pour le son « s ».", ["une mi<b>ssion</b>", "une pa<b>ssion</b>", "une permi<b>ssion</b>"]),
"CM1|O11|4": ("Le verbe de la famille m’aide.", ["décider → une déci<b>sion</b>", "permettre → une permi<b>ssion</b>", "inventer → une inven<b>tion</b>"]),
"CM1|O12|1": ("Adverbe en <b>-ment</b> : l’adjectif au <b>féminin + -ment</b>.", ["lente → lente<b>ment</b>", "heureuse → heureuse<b>ment</b>", "douce → douce<b>ment</b>"]),
"CM1|O12|2": ("Si l’adjectif finit par une <b>voyelle</b> : j’ajoute <b>-ment</b>.", ["vrai → vrai<b>ment</b>", "poli → poli<b>ment</b>", "absolu → absolu<b>ment</b>"]),
"CM1|O12|3": ("Je cherche l’adjectif d’où vient l’adverbe.", ["rapidement : rapide", "gentiment : gentil", "joyeusement : joyeux"]),
"CM1|O12|4": ("Exceptions à mémoriser.", ["gentiment", "précisément", "énormément"]),
# ---------------- CM2 ----------------
"CM2|G1|1": ("Le <b>sujet inversé</b> : il peut être placé <b>après le verbe</b>.", ["Dans la forêt vivent <b>des loups</b>.", "Sur la table se trouve <b>un livre</b>.", "Hier sont arrivés <b>mes cousins</b>."]),
"CM2|G1|2": (None, ["Ce sont <b>des loups</b> qui vivent dans la forêt.", "C’est <b>un livre</b> qui se trouve sur la table.", "Ce sont <b>mes cousins</b> qui sont arrivés hier."]),
"CM2|G2|1": (None, ["Léa chante. (un verbe conjugué)", "Léa chante et Tom dessine. (deux verbes)", "Quand il pleut, je reste à la maison. (deux verbes)"]),
"CM2|G2|2": (None, ["Je reste ici <b>parce qu’</b>il pleut.", "Il vient <b>et</b> il s’assoit.", "<b>Si</b> tu veux, nous jouons."]),
"CM2|G2|3": (None, ["Quand tu arrives, ouvre la porte. (impérative)", "Est-ce que tu viens si je t’invite ? (interrogative)", "Je ne sors pas parce qu’il pleut. (négative)"]),
"CM2|G3|1": ("Le <b>complément du nom</b> précise le nom ; il commence souvent par <b>de, à, en</b>.", ["un pull <b>en laine</b>", "une tasse <b>à café</b>", "la maison <b>de Léa</b>"]),
"CM2|G3|2": ("L’adjectif <b>épithète</b> est collé au nom ; l’<b>attribut du sujet</b> est relié par être, sembler, devenir…", ["un chat <b>noir</b> (épithète)", "Le chat est <b>noir</b>. (attribut)", "Elle semble <b>fatiguée</b>. (attribut)"]),
"CM2|G4|1": (None, ["Il marche <b>sur</b> le trottoir.", "Je pars <b>avec</b> mon frère.", "Elle habite <b>chez</b> sa tante."]),
"CM2|G4|2": (None, ["<b>le</b> livre (déterminant)", "Je <b>le</b> lis. (pronom)", "Léa <b>les</b> range. (pronom)"]),
"CM2|G4|3": (None, ["Il <b>me</b> regarde.", "Je <b>leur</b> parle.", "Nous <b>les</b> voyons."]),
"CM2|G4|4": (None, ["Je sors <b>quand</b> il ne pleut plus.", "Il reste <b>parce qu’</b>il est malade.", "Viens <b>si</b> tu veux."]),
"CM2|G4|5": ("Le pronom complément remplace un groupe déjà écrit : son <b>antécédent</b>.", ["Le facteur apporte <b>une lettre</b>. Maman <b>la</b> lit.", "Tom a perdu <b>ses clés</b>. Il <b>les</b> cherche.", "Léa voit <b>Paul</b>. Elle <b>le</b> salue."]),
"CM2|G5|1": ("Le sujet peut être <b>après le verbe</b>, même dans une question.", ["Que disent <b>les élèves</b> ?", "Où vont <b>tes amis</b> ?", "Quand arrive <b>le train</b> ?"]),
"CM2|G5|2": ("L’<b>attribut du sujet</b> s’accorde avec le sujet.", ["Les fleurs sont <b>belles</b>.", "Mon frère est <b>content</b>.", "Mes sœurs semblent <b>fatiguées</b>."]),
"CM2|G6|1": ("Le <b>COI</b> commence par une <b>préposition</b> (à, de).", ["Je parle <b>à ma voisine</b>.", "Il se souvient <b>de ses vacances</b>.", "Elle pense <b>à son frère</b>."]),
"CM2|G6|2": (None, ["<b>Hier</b>, il a plu. (temps)", "Il dort <b>dans le salon</b>. (lieu)", "Il reste au lit <b>parce qu’il est malade</b>. (cause)"]),
"CM2|G6|3": ("L’<b>attribut du sujet</b> (avec être, sembler, devenir…) n’est pas un complément d’objet.", ["Paul est <b>un bon élève</b>.", "Léa devient <b>médecin</b>.", "Ce chat semble <b>affamé</b>."]),
"CM2|G7|1": ("La chaîne des accords va jusqu’à l’<b>attribut du sujet</b>.", ["Les petites filles sont <b>contentes</b>.", "Mes grands frères sont <b>fatigués</b>.", "La petite chienne est <b>mouillée</b>."]),
"CM2|G7|2": ("Avec <b>avoir</b>, le participe passé ne s’accorde jamais avec le sujet ; il s’accorde avec le <b>COD placé avant</b> le verbe.", ["Les pommes, Léa <b>les</b> a mangé<b>es</b>.", "Les lettres, Tom <b>les</b> a écrit<b>es</b>.", "Les fleurs que j’ai cueilli<b>es</b> sont belles."]),
"CM2|H1|1": ("Le verbe peut être <b>avant le sujet</b>, dans une question. Je prouve encore avec l’imparfait.", ["Quel âge <b>a</b> ton frère ?", "Où <b>sont</b> tes amis ?", "Combien d’élèves <b>ont</b> gagné ?"]),
"CM2|H1|2": ("<b>l’a</b> = l’ + a, <b>l’as</b> = l’ + as. Je prouve : <b>l’avait</b>, <b>tu l’avais</b>.", ["Ton cahier, Léa <b>l’a</b> rangé.", "Ta clé, tu <b>l’as</b> perdue.", "Ce film, il <b>l’a</b> vu hier."]),
"CM2|H2|1": (None, ["Je pense <b>qu’elle</b> viendra.", "Il faut <b>qu’elle</b> parte.", "Léa dit <b>qu’elle</b> a faim."]),
"CM2|H3|1": (None, ["un café <b>sans</b> sucre", "Il part <b>sans</b> sa veste.", "Elle dort <b>sans</b> bruit."]),
"CM2|H4|1": (None, ["Il pleut, <b>donc</b> je prends mon parapluie.", "J’ai faim, <b>donc</b> je mange.", "Tu es fatigué, <b>donc</b> tu te reposes."]),
"CM2|H5|1": ("<b>dont</b> remplace un groupe nominal précédé de <b>de</b> : je parle de ce livre.", ["le livre <b>dont</b> je parle", "l’ami <b>dont</b> je me souviens", "la chanson <b>dont</b> j’ai besoin"]),
"CM2|H6|1": (None, ["<b>Quelle</b> belle robe !", "<b>Quels</b> beaux livres !", "<b>Quel</b> grand arbre !"]),
"CM2|H7|1": (None, ["il <b>s’en</b> va", "Elle <b>s’en</b> souvient.", "Ils <b>s’en</b> vont."]),
"CM2|V1|1": (None, ["générique : <b>fruit</b> → spécifique : pomme", "générique : <b>animal</b> → spécifique : chien", "générique : <b>véhicule</b> → spécifique : vélo"]),
"CM2|V1|2": ("Un mot peut être spécifique et générique à la fois.", ["véhicule → voiture → cabriolet", "animal → oiseau → mésange", "meuble → siège → fauteuil"]),
"CM2|V2|1": (None, ["je cherche <b>sentier</b> : un petit chemin étroit", "je cherche <b>affamé</b> : qui a très faim", "je cherche <b>vaste</b> : très grand"]),
"CM2|V2|2": (None, ["<b>chat</b> avant <b>chien</b> (ca avant ch)", "<b>chanter</b> (v.) : produire des sons avec sa voix", "<b>grand</b> (adj.) : qui a une grande taille"]),
"CM2|V2|3": (None, ["<b>glace</b> : une glace à la fraise · la glace d’un miroir", "<b>pièce</b> : une pièce de monnaie · une pièce de la maison", "<b>feuille</b> : la feuille d’un arbre · une feuille de papier"]),
"CM2|V3|1": (None, ["<b>télé</b>phone, <b>télé</b>vision", "<b>aqua</b>rium, <b>aqua</b>tique", "<b>bio</b>logie, <b>géo</b>graphie"]),
"CM2|V3|2": (None, ["le contraire : <b>dé</b>faire, <b>in</b>visible, <b>mal</b>heureux", "à nouveau : <b>re</b>lire", "la personne : chant<b>eur</b>, pian<b>iste</b>, boulang<b>ier</b>"]),
"CM2|V4|1": ("Un mot peut être <b>simple</b>, <b>dérivé</b> ou <b>composé</b>.", ["<b>simple</b> : terre", "<b>dérivé</b> : terrain, enterrer", "<b>composé</b> : pomme de terre, porte-monnaie"]),
"CM2|V5|1": ("Le <b>champ lexical</b> : les mots qui parlent d’un même thème, de toutes les classes.", ["la mer : vague, plage, nager, salé", "la forêt : arbre, sentier, marcher, sombre", "le sport : ballon, courir, rapide, gagner"]),
"CM2|V6|1": ("Un mot <b>polysémique</b> a plusieurs sens proches.", ["la <b>tête</b> d’une personne", "la <b>tête</b> de la course", "la <b>tête</b> d’un clou"]),
"CM2|V6|2": (None, ["homonymes : le <b>verre</b> / le <b>ver</b>", "polysémie : la <b>pièce</b> (maison, monnaie)", "polysémie : une <b>feuille</b> (arbre, papier)"]),
"CM2|V6|3": ("Un mot a un <b>sens propre</b> (son sens de base) et parfois un <b>sens figuré</b> (une image).", ["<b>souffler</b> les bougies (sens propre)", "<b>souffler</b> une réponse (sens figuré)", "avoir un <b>cœur</b> d’or (sens figuré)"]),
"CM2|C1|1": ("Des <b>radicaux qui changent</b> aussi au 3e groupe.", ["pouvoir : je peux · nous pouvons · ils peuvent", "vouloir : je veux · nous voulons · ils veulent", "voir : je vois · nous voyons · ils voient"]),
"CM2|C2|1": (None, ["chante<b>r</b>ai : r = futur, ai = je", "chante<b>r</b>ons : r = futur, ons = nous", "chante<b>r</b>ont : r = futur, ont = ils"]),
"CM2|C3|1": (None, ["Il <b>faisait</b> nuit. (le décor)", "Le loup <b>entra</b>. (l’action)", "Le vent soufflait ; soudain, la porte <b>s’ouvrit</b>."]),
"CM2|C3|2": ("Passé simple du 1er groupe : je chantai, tu chantas, il chanta, nous chantâmes, vous chantâtes, ils chantèrent.", ["Il <b>marcha</b> longtemps.", "Nous <b>mangeâmes</b> vite.", "Les enfants <b>chantèrent</b>."]),
"CM2|C3|3": (None, ["Il <b>fut</b> surpris.", "Ils <b>furent</b> contents.", "Elle <b>eut</b> peur."]),
"CM2|C4|1": ("Avec avoir, le participe passé s’accorde avec le <b>COD placé avant</b> le verbe.", ["Les pommes, je <b>les</b> ai mangé<b>es</b>.", "La lettre, Léa l’a écrit<b>e</b>.", "Les chansons que nous avons chanté<b>es</b> sont belles."]),
"CM2|C4|2": ("À la forme négative, ne… pas encadre l’<b>auxiliaire</b>.", ["je <b>n’</b>ai <b>pas</b> mangé", "tu <b>n’</b>as <b>pas</b> fini", "nous <b>n’</b>avons <b>pas</b> joué"]),
"CM2|C5|1": ("Avec être, le participe s’accorde avec le sujet, même quand le sujet est <b>après le verbe</b>.", ["Hier sont arrivé<b>es</b> mes cousines.", "Sont parti<b>s</b> les derniers invités.", "Dans la cour sont tombé<b>es</b> les feuilles."]),
"CM2|O2|1": ("Des familles moins faciles : la famille m’aide à trouver la lettre muette.", ["accro<b>c</b> → accrocher", "respe<b>ct</b> → respecter", "fusi<b>l</b> → fusiller"]),
"CM2|O8|1": ("D’autres noms en <b>-tée</b>, comme au CM1.", ["une assiet<b>tée</b>", "une por<b>tée</b>", "une je<b>tée</b>"]),
"CM2|O9|1": ("Le préfixe <b>in-</b> devient <b>il-, ir-, im-</b> devant l, r, m, et la consonne <b>se double</b> ; devant n : <i>innombrable</i>.", ["<b>il</b>lisible (devant l)", "<b>ir</b>réel (devant r)", "<b>im</b>mobile (devant m)"]),
"CM2|O11|1": ("Le <b>verbe de la famille</b> décide de la fin du nom : -quer → -cation, -ter → -tion, -mettre → -mission, -der et -clure → -sion. Exception : discuter → discussion.", ["communiquer → communi<b>cation</b>", "inventer → inven<b>tion</b>", "admettre → admi<b>ssion</b>"]),
"CM2|O12|1": ("Un adjectif en <b>-ent</b> donne un adverbe en <b>-emment</b> ; un adjectif en <b>-ant</b> donne <b>-amment</b>. Les deux se prononcent [amɑ̃].", ["prudent → prud<b>emment</b>", "évident → évid<b>emment</b>", "constant → const<b>amment</b>"]),
# ---------------- CE2 ----------------
"CE2|G1|1": (None, ["Le chat dort.", "Léa mange une pomme.", "Les enfants jouent."]),
"CE2|G1|2": (None, ["Qui est-ce qui dort ? Le chat.", "Qui est-ce qui chante ? Léa.", "Qui est-ce qui court ? Les enfants."]),
"CE2|G1|3": (None, ["Le chat dort → <b>Il</b> dort.", "Léa chante → <b>Elle</b> chante.", "Les enfants jouent → <b>Ils</b> jouent."]),
"CE2|G2|1": (None, ["Il fait beau. (déclarative)", "Tu viens ? (interrogative)", "Viens ici. (impérative)"]),
"CE2|G2|2": (None, ["Je <b>ne</b> chante <b>pas</b>.", "Il <b>ne</b> pleut <b>plus</b>.", "Quel beau dessin !"]),
"CE2|G2|3": (None, ["Léa dit : « J’ai faim. »", "« Viens ! » crie Tom.", "Papa demande : « Tu es prêt ? »"]),
"CE2|G3|1": (None, ["<b>le</b> chat", "<b>une</b> grande maison", "<b>mes</b> deux amis"]),
"CE2|G3|2": ("Les accords : -e au féminin, -s au pluriel ; -x et -aux.", ["un ami → une ami<b>e</b>", "un chat → des chat<b>s</b>", "un cheval → des chev<b>aux</b>"]),
"CE2|G3|3": ("Les féminins qui s’entendent.", ["lecteur → lec<b>trice</b>", "joyeux → joy<b>euse</b>", "gentil → gentil<b>le</b>"]),
"CE2|G4|1": (None, ["un <b>chat</b> (nom)", "<b>le</b> chat (déterminant)", "il <b>chante</b> (verbe)"]),
"CE2|G4|2": ("Certains mots changent (variables), d’autres jamais (invariables).", ["variable : un petit chat → des petits chats", "variable : je chante → ils chantent", "invariable : très, bien, demain, doucement"]),
"CE2|G5|1": ("Le sujet commande le verbe.", ["il chant<b>e</b>", "tu chant<b>es</b>", "ils chant<b>ent</b>"]),
"CE2|G5|2": (None, ["Les enfants (= <b>ils</b>) jouent.", "Ma sœur (= <b>elle</b>) lit.", "Mon frère (= <b>il</b>) dort."]),
"CE2|G6|1": (None, ["<b>Le chat</b> (groupe sujet) <b>dort sur le canapé</b> (groupe verbal).", "<b>Léa</b> <b>mange une pomme</b>.", "<b>Les enfants</b> <b>jouent dans la cour</b>."]),
"CE2|G6|2": (None, ["déplacer : Hier, Léa a chanté. → Léa a chanté hier.", "supprimer : Léa mange une pomme rouge. → Léa mange une pomme.", "remplacer : Léa chante. → Elle chante."]),
"CE2|G7|1": (None, ["Les petites filles <b>chantent</b>.", "Mon grand frère <b>dort</b>.", "Les chats noirs <b>miaulent</b>."]),
"CE2|C1|1": (None, ["être : je <b>suis</b>, tu <b>es</b>", "avoir : j’<b>ai</b>, tu <b>as</b>", "chanter : je chant<b>e</b>, ils chant<b>ent</b>"]),
"CE2|C1|2": (None, ["chant + <b>e</b> : je chante", "chant + <b>ons</b> : nous chantons", "chanter : l’<b>infinitif</b>"]),
"CE2|C1|3": (None, ["je <b>vais</b> à l’école", "tu <b>fais</b> un gâteau", "ils <b>disent</b> bonjour"]),
"CE2|C2|1": ("Le futur d’<b>être</b>, d’<b>avoir</b> et du <b>1er groupe</b>.", ["je chanter<b>ai</b>", "nous chanter<b>ons</b>", "tu <b>seras</b> content"]),
"CE2|C2|2": (None, ["j’<b>irai</b>", "je <b>ferai</b>", "il <b>dira</b>"]),
"CE2|C3|1": ("L’imparfait d’<b>être</b>, d’<b>avoir</b> et du <b>1er groupe</b>.", ["je chant<b>ais</b>", "nous chant<b>ions</b>", "il <b>était</b> content"]),
"CE2|C3|2": (None, ["je <b>faisais</b>", "tu <b>disais</b>", "nous <b>allions</b>"]),
"CE2|C4|1": ("Le passé composé avec <b>avoir</b> : avoir au présent + participe passé.", ["j’<b>ai chanté</b>", "tu <b>as joué</b>", "nous <b>avons fini</b>"]),
"CE2|C5|1": ("Le passé composé avec <b>être</b> pour les verbes de déplacement.", ["je <b>suis parti</b>", "il <b>est arrivé</b>", "elles <b>sont tombées</b>"]),
"CE2|V1|1": (None, ["fruits : pomme, poire, cerise", "animaux : chien, chat, cheval", "outils : marteau, scie, pince"]),
"CE2|V2|1": (None, ["<b>incassable</b> : je vois « casser »", "<b>affamé</b> : il a très faim", "<b>sentier</b> : un petit chemin"]),
"CE2|V3|1": (None, ["<b>dé</b>faire", "<b>mal</b>heureux", "<b>re</b>faire"]),
"CE2|V3|2": (None, ["chant<b>eur</b>", "boulang<b>ier</b>", "fille<b>tte</b>"]),
"CE2|V4|1": ("Une <b>famille de mots</b> : une partie commune et un même sens.", ["port, portuaire, aéroport", "chant, chanter, chanteur", "terre, terrain, enterrer"]),
"CE2|V4|2": (None, ["jardin (nom) · jardiner (verbe)", "chant (nom) · chanter (verbe)", "port (nom) · portuaire (adjectif)"]),
"CE2|V5|1": (None, ["content = joyeux", "grand ↔ petit", "joli = beau"]),
"CE2|V5|2": ("Des mots de plus en plus forts.", ["la crainte → la peur → l’épouvante", "tiède → chaud → brûlant", "joli → beau → magnifique"]),
"CE2|V5|3": ("Les <b>niveaux de langue</b> : familier, courant, soutenu.", ["familier : une bagnole", "courant : une voiture", "soutenu : une automobile"]),
"CE2|V6|1": ("Les <b>homonymes</b> : des mots qui se disent pareil mais n’ont pas le même sens.", ["le <b>verre</b> d’eau", "le feu <b>vert</b>", "un <b>ver</b> de terre"]),
"CE2|V6|2": (None, ["Un <b>ver</b> sort de la terre.", "Je bois dans un <b>verre</b>.", "une <b>feuille</b> d’arbre · une <b>feuille</b> de papier"]),
"CE2|V6|3": ("Un mot a un <b>sens propre</b> (son sens de base) et parfois un <b>sens figuré</b> (une image).", ["<b>souffler</b> les bougies", "<b>souffler</b> une réponse", "avoir un <b>cœur</b> d’or"]),
"CE2|O1|1": ("Devant <b>m, b, p</b>, j’écris <b>m</b>.", ["une ja<b>m</b>be", "un po<b>m</b>pier", "un ta<b>m</b>bour"]),
"CE2|O2|1": ("Pour trouver la lettre muette, je cherche un mot de la même famille.", ["un chat → un chaton", "beau → beauté", "grand → grande"]),
"CE2|O3|1": (None, ["<b>s</b>ac", "poi<b>ss</b>on", "<b>c</b>erise · gar<b>ç</b>on"]),
"CE2|O4|1": (None, ["une <b>c</b>abane", "une <b>qu</b>ille", "un <b>k</b>iwi"]),
"CE2|O5|1": (None, ["une <b>g</b>are", "une <b>gu</b>itare", "une ba<b>gu</b>e"]),
"CE2|O6|1": ("<b>ill</b> après une voyelle ; le son « oi » s’écrit <b>oi</b>.", ["la pa<b>ill</b>e", "une abe<b>ill</b>e", "le <b>roi</b>"]),
}

CIBLES = {"CE2": "CE2_PLUS", "CM1": "CM1_PLUS", "CM2": "CM2_PLUS"}


def reecrire(niv, k, html, vus):
    n = [0]

    def f(m):
        n[0] += 1
        li = m.group(1)
        if 'class="exs"' in li:
            vus.append((niv, k, n[0], "déjà fait"))
            return m.group(0)
        cle = f"{niv}|{k}|{n[0]}"
        if cle not in R:
            vus.append((niv, k, n[0], "MANQUE"))
            return m.group(0)
        texte, ex = R[cle]
        assert len(ex) == 3, cle
        vus.append((niv, k, n[0], "ok"))
        return "<li>" + (li if texte is None else texte) + '<span class="exs">' + "".join(f"<i>{e}</i>" for e in ex) + "</span></li>"
    return re.sub(r"<li>(.*?)</li>", f, html, flags=re.S)


def main():
    lignes = P.read_text(encoding="utf-8").split("\n")
    vus = []
    for niv, nom in CIBLES.items():
        i = next(i for i, l in enumerate(lignes) if l.startswith(f"const {nom}="))
        l = lignes[i]
        fin = l.rindex("};") + 1
        data = json.loads(l[len(f"const {nom}="):fin])
        for k, v in data.items():
            if isinstance(v, str):
                data[k] = reecrire(niv, k, v, vus)
            else:
                v["html"] = reecrire(niv, k, v.get("html", ""), vus)
        lignes[i] = f"const {nom}=" + json.dumps(data, ensure_ascii=False) + l[fin:]
    manques = [x for x in vus if x[3] == "MANQUE"]
    if manques:
        print("MANQUE :", manques)
        sys.exit(1)
    P.write_text("\n".join(lignes), encoding="utf-8")
    print(sum(1 for x in vus if x[3] == "ok"), "points réécrits,", sum(1 for x in vus if x[3] == "déjà fait"), "déjà faits.")


main()
