"""G3 (le groupe nominal) : beaucoup plus d'exercices par écran (16/11/2026, demande de l'enseignante : « les phrases utilisées en entraînement
sont trop répétitives, il en faudrait beaucoup plus »).

Chaque écran avait 4 exercices par classe (CE2 = PLUS, CM1 = NIV_ATOI[2], CM2 = NIV_ATOI[3]). Ce programme en AJOUTE `PAR_NIVEAU` (12) par écran et par classe,
fabriqués à partir de listes de noms et d'adjectifs AVEC leurs accords (genre, nombre) : chaque phrase est juste par construction.
Jamais d'écriture fausse montrée (décision du 15/11/2026) : les distracteurs des trous sont de vraies formes ou des formes cachées par le trou de lettres.
Relançable sans danger : les tableaux sont d'abord ramenés à leur taille d'origine (`TAILLE_ORIGINE`), puis complétés. Usage : python3 g3_beaucoup.py
"""
import json, os, random, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from niveaux_lib import CHEMIN

PAR_NIVEAU = 12
PLUS_ORIGINE = [3, 3, 3, 2, 4, 2, 3, 3, 3, 2, 2, 3, 2]     # exercices PLUS d'origine par écran (CE2 = 1 « atoi » + PLUS)
NIV_ORIGINE = 4
R = random.Random(303)
VOY = set('aeiouyéèêëâîïôûàh')

# ------------------------------------------------------------------ noms : (singulier, pluriel, genre) par catégorie
N = {}
def noms(cat, genre, *lst):
    for x in lst:
        sg, pl = (x if isinstance(x, tuple) else (x, x + 's'))
        N.setdefault(cat, []).append((sg, pl, genre))
noms('animal', 'm', 'chat', 'chien', 'lapin', 'renard', 'loup', 'mouton', 'cochon', 'canard', ('oiseau', 'oiseaux'), ('cheval', 'chevaux'), 'éléphant', ('ours', 'ours'), 'escargot', 'âne')
noms('animal', 'f', 'poule', 'vache', 'tortue', 'girafe', 'chèvre', 'grenouille', ('souris', 'souris'), ('brebis', 'brebis'), 'abeille', 'araignée')
noms('objet', 'm', 'livre', 'cahier', 'stylo', 'ballon', 'vélo', 'sac', ('manteau', 'manteaux'), ('chapeau', 'chapeaux'), ('bateau', 'bateaux'), 'jouet', 'camion', ('tableau', 'tableaux'), 'fauteuil', ('tapis', 'tapis'), 'parapluie', 'crayon', 'tiroir', 'panier', ('seau', 'seaux'))
noms('objet', 'f', 'robe', 'jupe', 'veste', 'valise', 'chaise', 'table', 'lampe', 'boîte', 'bouteille', 'clé', 'montre', 'trousse', 'voiture', 'moto', 'assiette', 'tasse', 'fenêtre', 'porte', 'casquette', 'chemise', 'écharpe', 'horloge', 'échelle', 'armoire', 'étagère', 'ardoise')
noms('lieu', 'm', 'jardin', 'village', ('château', 'châteaux'), 'pont', 'chemin', 'sentier', 'magasin', 'musée', 'marché', 'parc', 'champ', 'étang')
noms('lieu', 'f', 'maison', 'ville', 'forêt', 'rue', 'plage', 'montagne', 'cuisine', 'salle', 'chambre', 'rivière', 'île', 'cour')
noms('personne', 'm', 'garçon', 'voisin', 'cousin', 'boulanger', 'facteur', 'voyageur', 'ami', 'frère', 'jardinier', 'musicien')
noms('personne', 'f', 'fille', 'voisine', 'cousine', 'boulangère', 'voyageuse', 'amie', 'sœur', 'maîtresse', 'jardinière', 'musicienne')
noms('aliment', 'm', ('gâteau', 'gâteaux'), 'fromage', 'pain', 'biscuit', 'légume', ('jus', 'jus'))
noms('aliment', 'f', 'pomme', 'salade', 'soupe', 'glace', 'tarte', 'poire', 'fraise', 'banane', 'tomate', 'carotte', 'brioche', 'crêpe', 'baguette')
PORTABLE = {'livre', 'cahier', 'stylo', 'ballon', 'sac', 'manteau', 'chapeau', 'jouet', 'parapluie', 'crayon', 'panier', 'seau', 'robe', 'jupe', 'veste', 'valise', 'bouteille', 'clé', 'montre',
            'trousse', 'assiette', 'tasse', 'casquette', 'chemise', 'écharpe', 'ardoise', 'lampe', 'boîte'}
SANS_POSS = {'garçon', 'fille'}                  # « mon garçon », « ses filles » : on évite

# ------------------------------------------------------------------ adjectifs : formes, catégories de noms, place, famille, noms précis (ok)
A = {}
def adj(ms, fs, mp, fp, cats, place='post', grp='etat', ok=None):
    A[ms] = dict(f=(ms, fs, mp, fp), cats=set(cats.split()), place=place, grp=grp, ok=set(ok.split()) if ok else None)
def reg(ms, cats, place='post', grp='etat', ok=None):
    fs = ms if ms.endswith('e') else ms + 'e'
    adj(ms, fs, ms + 's', fs + 's', cats, place, grp, ok)
# couleurs
adj('blanc', 'blanche', 'blancs', 'blanches', 'animal objet lieu aliment', 'post', 'couleur', 'chat chien lapin mouton cheval ours loup canard oiseau poule vache chèvre brebis souris livre cahier sac manteau chapeau bateau jouet camion fauteuil tapis parapluie robe jupe veste valise chaise table lampe boîte bouteille trousse voiture moto assiette tasse fenêtre porte casquette chemise écharpe armoire étagère ardoise maison village château pont ville fromage pain')
reg('noir', 'animal objet', 'post', 'couleur', 'chat chien lapin mouton cheval ours loup canard oiseau livre cahier sac manteau chapeau stylo ballon vélo jouet camion fauteuil tapis parapluie crayon panier robe jupe veste valise chaise table lampe boîte bouteille trousse voiture moto casquette chemise écharpe')
reg('gris', 'animal objet lieu', 'post', 'couleur', 'chat chien lapin mouton cheval souris loup âne éléphant manteau chapeau sac tapis parapluie veste chemise écharpe casquette ville rue château pont')
reg('vert', 'animal objet lieu aliment', 'post', 'couleur', 'grenouille tortue livre cahier sac stylo ballon vélo jouet camion tapis parapluie crayon panier seau robe jupe veste valise chaise table lampe boîte bouteille trousse voiture assiette tasse écharpe chemise casquette parc jardin champ salade pomme poire')
reg('bleu', 'objet lieu', 'post', 'couleur', 'livre cahier sac stylo ballon vélo jouet camion tapis parapluie crayon panier seau robe jupe veste valise chaise table lampe boîte bouteille trousse voiture assiette tasse écharpe chemise casquette maison chambre salle cuisine')
reg('rouge', 'objet aliment', 'post', 'couleur', 'livre cahier sac stylo ballon vélo jouet camion tapis parapluie crayon panier seau robe jupe veste valise chaise table lampe boîte bouteille trousse voiture moto assiette tasse écharpe chemise casquette tomate fraise pomme')
reg('jaune', 'objet lieu aliment', 'post', 'couleur', 'livre cahier sac stylo ballon jouet camion tapis parapluie crayon panier seau robe jupe veste valise chaise table lampe boîte bouteille trousse voiture assiette tasse écharpe chemise casquette maison cuisine banane')
reg('rose', 'objet lieu', 'post', 'couleur', 'robe jupe veste valise chaise table lampe boîte trousse tasse assiette écharpe chemise casquette ballon sac chambre maison')
adj('violet', 'violette', 'violets', 'violettes', 'objet', 'post', 'couleur', 'livre cahier sac stylo ballon jouet tapis parapluie crayon panier robe jupe veste valise chaise table lampe boîte trousse tasse écharpe chemise casquette')
# tailles
for a in ('petit', 'grand'):
    reg(a, 'animal objet lieu personne', 'pre', 'taille', None)
adj('gros', 'grosse', 'gros', 'grosses', 'animal objet aliment', 'pre', 'taille', 'chat chien lapin mouton cochon canard cheval ours escargot âne éléphant vache tortue girafe grenouille livre cahier sac ballon camion fauteuil panier seau valise boîte bouteille tasse gâteau fromage pain biscuit légume pomme poire fraise tarte brioche')
reg('énorme', 'animal objet lieu', 'pre', 'taille', 'éléphant ours cheval girafe vache cochon chien livre ballon camion fauteuil valise boîte gâteau château montagne maison ville forêt parc')
reg('minuscule', 'animal objet', 'pre', 'taille', 'souris escargot abeille araignée grenouille lapin chat jouet clé crayon stylo livre')
reg('immense', 'lieu', 'pre', 'taille', 'forêt montagne ville plage parc champ cour salle')
reg('magnifique', 'lieu objet animal', 'pre', 'taille', 'forêt montagne ville plage parc jardin maison château robe chapeau cheval oiseau')
reg('joli', 'animal objet lieu personne aliment', 'pre', 'beau', None)
reg('jeune', 'animal personne', 'pre', 'age', 'chat chien lapin cheval mouton renard loup canard garçon fille voisin voisine cousin cousine ami amie frère sœur musicien musicienne')
# tailles postposées / états : seulement avec les noms qui conviennent
adj('long', 'longue', 'longs', 'longues', 'objet lieu', 'post', 'taille', 'robe jupe manteau écharpe chemin sentier rue livre pont rivière crayon échelle')
reg('court', 'objet lieu', 'post', 'taille', 'robe jupe veste manteau chemise écharpe chemin sentier crayon')
reg('haut', 'objet lieu', 'post', 'taille', 'armoire étagère échelle fenêtre porte montagne pont')
reg('étroit', 'lieu objet', 'post', 'taille', 'rue chemin sentier pont porte fenêtre salle cuisine')
reg('large', 'lieu objet', 'post', 'taille', 'rue chemin pont rivière fenêtre porte table fauteuil chapeau')
reg('rond', 'objet', 'post', 'forme', 'assiette table ballon horloge montre tapis boîte')
reg('carré', 'objet', 'post', 'forme', 'tableau table boîte tapis ardoise fenêtre cahier')
reg('pointu', 'objet', 'post', 'forme', 'crayon chapeau')
adj('neuf', 'neuve', 'neufs', 'neuves', 'objet', 'post', 'etat', None)
reg('propre', 'objet lieu', 'post', 'etat', None); reg('sale', 'objet lieu', 'post', 'etat', None)
reg('cassé', 'objet', 'post', 'etat', 'chaise table lampe jouet vélo montre tasse assiette bouteille fenêtre ardoise stylo crayon horloge camion moto voiture valise')
reg('ouvert', 'objet lieu', 'post', 'etat', 'porte fenêtre boîte valise sac livre cahier parapluie tiroir armoire magasin musée marché parc')
reg('fermé', 'objet lieu', 'post', 'etat', 'porte fenêtre boîte valise sac livre cahier parapluie tiroir armoire magasin musée marché parc')
reg('plein', 'objet', 'post', 'etat', 'boîte valise sac panier bouteille tasse seau tiroir armoire')
reg('lourd', 'objet', 'post', 'poids', 'valise sac camion boîte panier seau table armoire fauteuil')
adj('léger', 'légère', 'légers', 'légères', 'objet aliment', 'post', 'poids', 'sac valise manteau veste robe chemise écharpe parapluie gâteau soupe')
adj('ancien', 'ancienne', 'anciens', 'anciennes', 'objet lieu', 'post', 'age', 'livre cahier tableau fauteuil tapis horloge montre armoire table chaise lampe vélo valise maison village château pont musée marché chemin')
# personnes et animaux
reg('content', 'personne', 'post', 'qualite', None); reg('fatigué', 'personne', 'post', 'qualite', None); reg('poli', 'personne', 'post', 'qualite', None); reg('bavard', 'personne', 'post', 'qualite', None)
adj('gentil', 'gentille', 'gentils', 'gentilles', 'personne animal', 'post', 'qualite', 'garçon fille voisin voisine cousin cousine ami amie frère sœur maîtresse chat chien lapin cheval mouton vache')
adj('heureux', 'heureuse', 'heureux', 'heureuses', 'personne', 'post', 'qualite', None)
adj('curieux', 'curieuse', 'curieux', 'curieuses', 'personne animal', 'post', 'qualite', 'garçon fille voisin voisine cousin cousine ami amie frère sœur chat chien lapin renard souris')
adj('courageux', 'courageuse', 'courageux', 'courageuses', 'personne', 'post', 'qualite', None)
adj('joyeux', 'joyeuse', 'joyeux', 'joyeuses', 'personne', 'post', 'qualite', None)
adj('sérieux', 'sérieuse', 'sérieux', 'sérieuses', 'personne', 'post', 'qualite', 'voisin voisine boulanger boulangère facteur voyageur voyageuse jardinier jardinière musicien musicienne maîtresse')
reg('timide', 'personne animal', 'post', 'qualite', 'garçon fille voisin voisine cousin cousine ami amie frère sœur lapin souris chat')
reg('rapide', 'animal objet', 'post', 'vitesse', 'lapin cheval renard loup chat chien souris vélo moto voiture bateau camion')
adj('doux', 'douce', 'doux', 'douces', 'animal personne objet aliment', 'post', 'qualite', 'chat lapin mouton chèvre brebis chien cheval tapis manteau écharpe fauteuil veste chemise fromage voisin voisine maîtresse')
reg('sauvage', 'animal', 'post', 'qualite', 'loup renard lapin oiseau canard ours grenouille araignée éléphant')
reg('affamé', 'animal personne', 'post', 'qualite', 'chat chien lapin loup renard cochon canard oiseau ours voyageur voyageuse garçon fille')
adj('joueur', 'joueuse', 'joueurs', 'joueuses', 'animal personne', 'post', 'qualite', 'chat chien lapin cochon âne garçon fille cousin cousine frère sœur')
adj('paresseux', 'paresseuse', 'paresseux', 'paresseuses', 'animal personne', 'post', 'qualite', 'chat chien cochon âne escargot garçon fille cousin cousine frère sœur')
reg('gourmand', 'animal personne', 'post', 'qualite', 'chat chien lapin cochon âne garçon fille cousin cousine frère sœur ami amie')
adj('peureux', 'peureuse', 'peureux', 'peureuses', 'animal personne', 'post', 'qualite', 'chat lapin souris mouton poule chèvre brebis garçon fille')
reg('fidèle', 'animal personne', 'post', 'qualite', 'chien cheval chat ami amie voisin voisine')
adj('vif', 'vive', 'vifs', 'vives', 'animal', 'post', 'qualite', 'lapin renard souris oiseau chat chien')
# lieux
reg('calme', 'lieu', 'post', 'lieu', None); reg('tranquille', 'lieu', 'post', 'lieu', None)
adj('lumineux', 'lumineuse', 'lumineux', 'lumineuses', 'lieu objet', 'post', 'lieu', 'maison salle chambre cuisine ville cour lampe horloge')
reg('ensoleillé', 'lieu', 'post', 'lieu', 'maison salle chambre cuisine ville cour plage jardin parc village')
reg('célèbre', 'lieu personne', 'post', 'lieu', 'château musée ville village pont montagne plage musicien musicienne voyageur voyageuse')
# aliments
adj('frais', 'fraîche', 'frais', 'fraîches', 'aliment', 'post', 'gout', 'salade pain fromage jus fraise poire légume carotte tomate baguette')
reg('chaud', 'aliment', 'post', 'temp', 'soupe tarte crêpe pain brioche gâteau baguette')
reg('froid', 'aliment', 'post', 'temp', 'glace jus soupe salade')
reg('sucré', 'aliment', 'post', 'gout', 'gâteau tarte brioche crêpe jus glace biscuit')
reg('salé', 'aliment', 'post', 'gout', 'biscuit fromage soupe tarte')
reg('mûr', 'aliment', 'post', 'etat', 'poire fraise banane tomate pomme')
adj('délicieux', 'délicieuse', 'délicieux', 'délicieuses', 'aliment', 'post', 'gout', None)
adj('épais', 'épaisse', 'épais', 'épaisses', 'aliment objet', 'post', 'taille', 'soupe tapis manteau livre cahier veste écharpe')
adj('bon', 'bonne', 'bons', 'bonnes', 'aliment personne', 'pre', 'gout', 'gâteau fromage pain biscuit légume jus pomme salade soupe glace tarte poire fraise banane tomate carotte brioche crêpe baguette voisin voisine cousin cousine boulanger boulangère jardinier jardinière musicien musicienne maîtresse')

IRREG = {   # adjectifs dont le féminin change plus que « + e » : règle montrée en aide
    'gros': 'gros → grosse : deux s.', 'doux': 'doux → douce.', 'gentil': 'gentil → gentille : la consonne se double.', 'heureux': 'heureux → heureuse.',
    'neuf': 'neuf → neuve.', 'blanc': 'blanc → blanche.', 'long': 'long → longue.', 'léger': 'léger → légère.', 'frais': 'frais → fraîche.', 'vif': 'vif → vive.',
    'curieux': 'curieux → curieuse.', 'courageux': 'courageux → courageuse.', 'joyeux': 'joyeux → joyeuse.', 'sérieux': 'sérieux → sérieuse.',
    'paresseux': 'paresseux → paresseuse.', 'peureux': 'peureux → peureuse.', 'lumineux': 'lumineux → lumineuse.', 'délicieux': 'délicieux → délicieuse.',
    'ancien': 'ancien → ancienne : le n se double.', 'épais': 'épais → épaisse.', 'bon': 'bon → bonne : le n se double.', 'joueur': 'joueur → joueuse.',
    'violet': 'violet → violette : le t se double.',
}
REGULIERS = [a for a in A if a not in IRREG and not a.endswith('e')]

def compat(a, nom, cat):
    sp = A[a]
    return cat in sp['cats'] and (sp['ok'] is None or nom in sp['ok'])

# ------------------------------------------------------------------ outils de phrases
VOY = set('aeiouyéèêëâîïôûàh')
def cap(s):
    return s[0].upper() + s[1:] if s else s
def voyelle(mot):
    return mot[0].lower() in VOY
def det(kind, genre, nb, suivant):
    v = voyelle(suivant)
    if kind == 'def':
        return 'les' if nb == 'p' else ("l’" if v else ('le' if genre == 'm' else 'la'))
    if kind == 'ind':
        return 'des' if nb == 'p' else ('un' if genre == 'm' else 'une')
    if kind in ('mon', 'ton', 'son'):
        return kind[:-2] + 'es' if nb == 'p' else (kind if genre == 'm' or v else kind[:-2] + 'a')
    if kind == 'notre': return 'nos' if nb == 'p' else 'notre'
    if kind == 'votre': return 'vos' if nb == 'p' else 'votre'
    if kind == 'leur':  return 'leurs' if nb == 'p' else 'leur'
    if kind == 'ce':
        return 'ces' if nb == 'p' else ('cette' if genre == 'f' else ('cet' if v else 'ce'))
    raise ValueError(kind)
DET_S = ['def', 'ind', 'mon', 'son', 'notre', 'ce', 'leur']
DET_P = ['def', 'ind', 'mon', 'son', 'notre', 'ce', 'leur', 'votre']

def forme(a, genre, nb):
    f = A[a]['f']
    return f[(0 if genre == 'm' else 1) + (0 if nb == 's' else 2)]

class GN:
    """Un groupe nominal construit avec ses accords et des adjectifs qui conviennent au nom (une seule famille par adjectif)."""
    def __init__(self, cat=None, nb=None, avec_adj=0, kind=None, nom=None, types=None):
        self.cat = cat or R.choice(['animal', 'objet', 'lieu', 'personne', 'aliment'])
        self.nom = nom or R.choice(N[self.cat])
        self.nb = nb or R.choice(['s', 's', 'p'])
        self.sg, self.pl, self.g = self.nom
        mot = self.sg if self.nb == 's' else self.pl
        ok = [a for a in A if compat(a, self.sg, self.cat)]
        self.adjs, grp = [], set()
        for _ in range(avec_adj):
            cand = [a for a in ok if A[a]['grp'] not in grp and a not in self.adjs and not (a == 'petit' and self.sg in ('ami', 'amie'))]
            if self.adjs and any(A[x]['place'] == 'pre' for x in self.adjs):
                cand = [a for a in cand if A[a]['place'] == 'post']            # un seul adjectif devant le nom
            if not cand: break
            a = R.choice(cand); self.adjs.append(a); grp.add(A[a]['grp'])
        self.pre = [a for a in self.adjs if A[a]['place'] == 'pre'][:1]
        self.post = [a for a in self.adjs if a not in self.pre][:1]
        self.adjs = self.pre + self.post
        premier = forme(self.pre[0], self.g, self.nb) if self.pre else mot
        k = kind or R.choice(DET_S if self.nb == 's' else DET_P)
        if self.sg in SANS_POSS and k in ('mon', 'son', 'notre', 'leur', 'votre'): k = 'def'
        if self.pre and self.nb == 'p' and k == 'ind': k = 'def'                    # « de petits chats » : évité
        self.kind = k
        self.det = det(k, self.g, self.nb, premier)
        self.mot = mot
        self.afp = [forme(a, self.g, self.nb) for a in self.pre]
        self.afq = [forme(a, self.g, self.nb) for a in self.post]
    def brut(self):
        return self.det + ('' if self.det.endswith('’') else ' ') + ' '.join(self.afp + [self.mot] + self.afq)
    def redet(self, suivant, pre=False):
        """Déterminant recalculé selon le mot qui le suit (élision, « ce / cet », « des » devant un adjectif)."""
        k = self.kind
        if pre and self.nb == 'p' and k == 'ind': k = 'def'
        return det(k, self.g, self.nb, suivant)
    def texte(self, marque=None):
        sep = '' if self.det.endswith('’') else ' '
        if marque == 'gn': return '<' + self.brut() + '>'
        if marque == 'det': return '<%s>' % self.det + sep + ' '.join(self.afp + [self.mot] + self.afq)
        if marque == 'noyau': return self.det + sep + ' '.join(self.afp + ['<%s>' % self.mot] + self.afq)
        if marque == 'adj': return self.det + sep + ' '.join(['<%s>' % a for a in self.afp] + [self.mot] + ['<%s>' % a for a in self.afq])
        return self.brut()

def gn_ok(cat, nb=None, avec_adj=0, kind=None, nom=None):
    """GN dont le nombre d'adjectifs voulu a bien été obtenu (sinon on recommence)."""
    for _ in range(60):
        g = GN(cat=cat, nb=nb, avec_adj=avec_adj, kind=kind, nom=nom)
        if len(g.adjs) == avec_adj: return g
    raise RuntimeError((cat, avec_adj))

# verbes : (3e pers. singulier, pluriel, objets acceptés) ; seuls des PERSONNES agissent. Étiquettes d'objets : portable, domestique, plat, coupable, mangeable, + catégories
DOMESTIQUE = {'chat', 'chien', 'lapin', 'cheval', 'mouton', 'âne', 'chèvre', 'brebis', 'cochon'}
FERME = DOMESTIQUE | {'poule', 'vache', 'canard'}
PLAT = {'gâteau', 'soupe', 'tarte', 'salade', 'crêpe', 'brioche'}
COUPABLE = {'pain', 'gâteau', 'fromage', 'tarte', 'pomme', 'poire', 'banane', 'tomate', 'carotte', 'légume', 'baguette', 'brioche', 'biscuit'}
MANGEABLE = {x[0] for x in N['aliment']} - {'jus'}
VT = [('regarde', 'regardent', 'objet animal lieu personne', 0), ('porte', 'portent', 'portable', 0), ('ramasse', 'ramassent', 'portable', 0), ('range', 'rangent', 'portable', 0),
      ('cherche', 'cherchent', 'objet animal personne', 0), ('trouve', 'trouvent', 'objet animal', 0), ('observe', 'observent', 'animal lieu', 0), ('dessine', 'dessinent', 'animal objet lieu', 0),
      ('lave', 'lavent', 'objet', 0), ('achète', 'achètent', 'portable aliment', 0), ('caresse', 'caressent', 'domestique', 0), ('nourrit', 'nourrissent', 'ferme', 0), ('visite', 'visitent', 'lieu', 0),
      ('traverse', 'traversent', 'lieu', 0), ('admire', 'admirent', 'lieu animal objet', 0), ('répare', 'réparent', 'objet', 0), ('mange', 'mangent', 'mangeable', 0), ('prépare', 'préparent', 'plat', 0),
      ('goûte', 'goûtent', 'aliment', 0), ('coupe', 'coupent', 'coupable', 0), ('rapporte', 'rapportent', 'portable aliment', 0), ('choisit', 'choisissent', 'portable aliment', 0)]
VT = [v[:3] for v in VT]
VI = {'animal': [('dort', 'dorment', 'tranquillement'), ('court', 'courent', 'vite'), ('joue', 'jouent', 'dehors'), ('avance', 'avancent', 'lentement'), ('attend', 'attendent', 'là-bas')],
      'personne': [('arrive', 'arrivent', 'demain'), ('joue', 'jouent', 'dehors'), ('chante', 'chantent', 'souvent'), ('marche', 'marchent', 'lentement'), ('sourit', 'sourient', 'toujours')],
      'objet': [('brille', 'brillent', 'beaucoup'), ('tombe', 'tombent', 'souvent'), ('reste', 'restent', 'ici')],
      'lieu': [('se trouve', 'se trouvent', 'là-bas'), ('change', 'changent', 'souvent')],
      'aliment': [('refroidit', 'refroidissent', 'vite'), ('sent', 'sentent', 'bon'), ('attend', 'attendent', 'sur la table')]}
ADV_MILIEU = ['souvent', 'toujours', 'volontiers']
ADV_FIN = ['aujourd’hui', 'là-bas']
LIEUX_COMP = [('dans', 'jardin'), ('dans', 'cuisine'), ('dans', 'salle'), ('dans', 'cour'), ('dans', 'chambre'), ('dans', 'parc'), ('dans', 'magasin'), ('dans', 'maison'), ('dans', 'village'),
              ('dans', 'ville'), ('dans', 'forêt'), ('dans', 'rue'), ('devant', 'maison'), ('devant', 'magasin'), ('devant', 'musée'), ('devant', 'château'), ('derrière', 'maison'), ('derrière', 'château'), ('derrière', 'magasin')]

def noms_pour(tag):
    """Liste (nom, catégorie) acceptés par une étiquette d'objet."""
    if tag == 'portable': return [(x, 'objet') for x in N['objet'] if x[0] in PORTABLE]
    ens = {'domestique': DOMESTIQUE, 'ferme': FERME, 'plat': PLAT, 'coupable': COUPABLE, 'mangeable': MANGEABLE}
    if tag in ens:
        cat = 'animal' if tag in ('domestique', 'ferme') else 'aliment'
        return [(x, cat) for x in N[cat] if x[0] in ens[tag]]
    return [(x, tag) for x in N[tag]]
def objet_pour(verbe, avec_adj, nb=None):
    """GN objet d'un verbe : un nom qui convient au verbe, avec des adjectifs qui conviennent au nom."""
    L = [t for tag in verbe[2].split() for t in noms_pour(tag)]
    for _ in range(80):
        nom, cat = R.choice(L)
        try:
            return gn_ok(cat, nb=nb, avec_adj=avec_adj, nom=nom)
        except RuntimeError:
            continue
    raise RuntimeError(verbe)
def lieu_comp(avec_adj=0):
    prep, sg = R.choice(LIEUX_COMP)
    nom = [x for x in N['lieu'] if x[0] == sg][0]
    return prep, gn_ok('lieu', nb='s', avec_adj=avec_adj, nom=nom, kind=R.choice(['def', 'def', 'ind', 'mon', 'notre']))
def sujet_personne(avec_adj, nb=None, kind=None):
    return gn_ok('personne', nb=nb, avec_adj=avec_adj, kind=kind)
def accorde(v, nb):
    return v[1] if nb == 'p' else v[0]

# ------------------------------------------------------------------ fabriques d'exercices
def K(p, ask, hint, n=None):
    t = {'click': 'x', 'ask': ask, 'hint': hint}
    if n: t['n'] = n
    return {'p': p, 'tasks': [t]}
def Cx(p, bon, mauvais, hint, ask=None, fill=None):
    t = {'choose': [bon] + list(mauvais), 'ok': 0, 'hint': hint}
    if ask: t['ask'] = ask
    if fill: t['fill'] = fill
    return {'p': p, 'tasks': [t]}

def cle(e):
    return e['p'] + '|' + e['tasks'][0].get('ask', '') + '|' + e['tasks'][0].get('choose', [''])[0]
DEJA = set()    # clés des exercices d'origine de l'écran : jamais refaits
def pool(gen, n=PAR_NIVEAU, tentatives=5000):
    """Appelle gen() jusqu'à avoir n exercices distincts."""
    vus, out = set(DEJA), []
    for _ in range(tentatives):
        try:
            e = gen()
        except RuntimeError:
            continue
        c = cle(e)
        if c in vus: continue
        vus.add(c); out.append(e)
        if len(out) == n: break
    assert len(out) == n, (gen.__name__, len(out))
    return out

def phrase(adj_s, adj_o, marque_s=None, marque_o=None, lieu=False, marque_l=None, pron=False):
    """Sujet (personne ou pronom) + verbe + objet (+ « dans / devant … » + lieu, sinon un adverbe)."""
    v = R.choice(VT)
    if lieu:
        while 'lieu' in v[2].split(): v = R.choice(VT)
    o = objet_pour(v, adj_o)
    if pron:
        pr = R.choice(['Il', 'Elle', 'Ils', 'Elles'])
        sujet = pr; nb = 'p' if pr in ('Ils', 'Elles') else 's'
    else:
        sg = sujet_personne(adj_s)
        sujet = sg.texte(marque_s); nb = sg.nb
    mots = [sujet, accorde(v, nb)]
    if lieu:
        prep, l = lieu_comp(R.choice([0, 1]))
        mots += [o.texte(marque_o), prep, l.texte(marque_l)]
    elif R.random() < 0.5:
        mots += [R.choice(ADV_MILIEU), o.texte(marque_o)]
    else:
        mots += [o.texte(marque_o), R.choice(ADV_FIN)]
    t = ' '.join(mots).replace('’ ', '’') + '.'
    return capdebut(t)
def capdebut(t):
    return '<' + cap(t[1:]) if t.startswith('<') else cap(t)

def e1(niv):   # Des mots autour d'un nom : clique sur le(s) groupe(s) nominal(aux)
    def g():
        if niv == 0:
            return K(phrase(0, R.choice([0, 1, 1]), marque_o='gn', pron=True), 'Clique sur le groupe nominal.', 'Cherche un nom avec son déterminant.')
        if niv == 1:
            return K(phrase(R.choice([0, 1]), R.choice([1, 1, 0]), 'gn', 'gn'), 'Clique sur les 2 groupes nominaux.', 'Cherche les noms avec leur déterminant.', 2)
        return K(phrase(R.choice([0, 1]), R.choice([0, 1]), 'gn', 'gn', lieu=True, marque_l='gn'), 'Clique sur les 3 groupes nominaux.', 'Cherche les noms avec leur déterminant.', 3)
    return pool(g)

def e2(niv):   # Le déterminant
    def g():
        if niv == 0:
            cat = R.choice(['animal', 'objet', 'lieu', 'aliment', 'personne'])
            o = gn_ok(cat, avec_adj=R.choice([0, 0, 1]))
            return K(o.texte('det'), 'Clique sur le déterminant.', 'C’est le petit mot devant le nom.')
        if niv == 1:
            return K(phrase(0, R.choice([0, 1]), marque_o='det', pron=True), 'Clique sur le déterminant.', 'C’est le petit mot devant le nom.')
        return K(phrase(R.choice([0, 1]), R.choice([0, 1]), 'det', 'det'), 'Clique sur les 2 déterminants.', 'Ce sont les petits mots devant les noms.', 2)
    return pool(g)

def e3(niv):   # Le mot le plus important : clique sur le nom noyau
    def g():
        cat = R.choice(['animal', 'objet', 'lieu', 'aliment', 'personne'])
        if niv == 0:
            return K(gn_ok(cat, avec_adj=2).texte('noyau'), 'Clique sur le nom noyau.', 'Quel mot ne peut-on pas enlever ?')
        if niv == 1:
            s = gn_ok(cat, avec_adj=R.choice([1, 2]))
            v = R.choice(VI[cat])
            return K(capdebut('%s %s %s.' % (s.texte('noyau'), accorde(v, s.nb), v[2])), 'Clique sur le nom noyau.', 'Quel mot ne peut-on pas enlever ?')
        s = sujet_personne(R.choice([1, 2]))
        vb = R.choice(VT); o = objet_pour(vb, 1)
        t = '%s %s %s %s.' % (s.texte('noyau'), accorde(vb, s.nb), o.brut(), R.choice(['depuis longtemps', 'chaque jour', 'avec soin', 'sans bruit', 'en silence']))
        return K(capdebut(t), 'Clique sur le nom noyau du groupe sujet.', 'Le sujet est au début : qui est-ce qui… ?')
    return pool(g)

COMPL = {'animal': ['de mon voisin', 'de ma cousine', 'de notre classe', 'de mon oncle', 'du jardin'], 'objet': ['de mon voisin', 'de ma cousine', 'de notre classe', 'de mon oncle', 'de la cuisine'],
         'lieu': ['au bord de la mer', 'près de la rivière', 'près du village', 'au bout du chemin', 'au sommet de la colline']}
def e4(niv):   # Le noyau ne s'enlève pas
    def g():
        cat = R.choice(['animal', 'objet', 'objet', 'lieu'] if niv == 2 else ['animal', 'objet', 'lieu'])
        o = gn_ok(cat, nb='s' if niv < 2 else R.choice(['s', 'p']), avec_adj=2, kind=R.choice(['ind', 'def', 'mon', 'ce']))
        t = o.brut() + (' ' + R.choice(COMPL[cat]) if niv == 2 else '')
        return Cx(t, o.mot, o.afp + o.afq, 'C’est le nom noyau.', 'Quel mot ne peut-on pas enlever ?')
    return pool(g)

def e5(niv):   # Il dit comment est le nom : clique sur l'adjectif
    def g():
        if niv == 0:
            cat = R.choice(['animal', 'objet', 'lieu', 'aliment', 'personne'])
            return K(gn_ok(cat, avec_adj=1).texte('adj'), 'Clique sur l’adjectif.', 'Il dit comment est le nom.')
        if niv == 1:
            return K(phrase(0, 1, marque_o='adj', pron=True), 'Clique sur l’adjectif.', 'Il dit comment est le nom.')
        return K(phrase(1, 1, 'adj', 'adj'), 'Clique sur les 2 adjectifs.', 'Ils disent comment sont les noms.', 2)
    return pool(g)

def trou(o, a):
    """GN avec un trou à la place de l'adjectif a (devant ou derrière le nom)."""
    if A[a]['place'] == 'pre':
        d = o.redet(forme(a, o.g, o.nb), pre=True)
        return d + ('' if d.endswith('’') else ' ') + '___ ' + o.mot
    d = o.redet(o.mot)
    return d + ('' if d.endswith('’') else ' ') + o.mot + ' ___'
def qui(o):
    return ('l’' + o.sg) if voyelle(o.sg) else (('le ' if o.g == 'm' else 'la ') + o.sg)
INTROS = ['Ce matin,', 'Aujourd’hui,', 'Pendant les vacances,', 'Après l’école,', 'Le dimanche,', 'Chaque semaine,']
def phrase_trou(o, a, niv, pron_pl=False):
    """Phrase autour d'un GN à trou (niv 1 : courte ; niv 2 : avec un début de phrase)."""
    v = R.choice(VT)
    while not any(o.nom[0] in [x[0][0] for x in noms_pour(tag)] for tag in v[2].split()) or 'lieu' in v[2].split() and o.cat != 'lieu': v = R.choice(VT)
    pr = R.choice(['Ils', 'Elles']) if pron_pl else R.choice(['Il', 'Elle'])
    vb = v[1] if pr in ('Ils', 'Elles') else v[0]
    fin = '.' if A[a]['place'] == 'pre' else ' .'
    gn = trou(o, a)
    if niv == 1:
        return cap('%s %s %s' % (pr, vb, gn)) + fin
    intro = R.choice(INTROS)
    return '%s %s %s %s' % (intro, pr.lower(), vb, gn) + fin
def adj_pour(o, parmi=None):
    cand = [a for a in (parmi or A) if compat(a, o.sg, o.cat) and not (a == 'petit' and o.sg in ('ami', 'amie'))]
    return R.choice(cand) if cand else None
def gn_nu(cat=None, nb=None, kind=None, exclus=()):
    c = cat or R.choice(['animal', 'objet', 'lieu', 'aliment', 'personne'])
    return GN(cat=c, nb=nb, avec_adj=0, kind=kind)

def e6(niv):   # J'enrichis le GN : complète avec l'adjectif qui convient
    def g():
        o = gn_nu(nb='s' if niv < 2 else R.choice(['s', 'p']), kind='ind' if niv == 0 else None)
        a = adj_pour(o)
        if not a: raise RuntimeError
        o.nb = o.nb
        bon = forme(a, o.g, o.nb)
        dis = [R.choice(['vite', 'doucement', 'souvent', 'toujours', 'soudain', 'lentement']), R.choice(['manger', 'dormir', 'courir', 'chanter', 'passer', 'ouvrir'])]
        p = trou(o, a) if niv == 0 else phrase_trou(o, a, niv, o.nb == 'p')
        return Cx(p, bon, dis, 'Cherche un mot qui dit comment est %s.' % qui(o), 'Complète avec l’adjectif qui convient.' if niv else None, 'pr')
    return pool(g)

def e7(niv):   # Masculin ou féminin
    def g():
        o = gn_nu(nb='s', kind=R.choice(['ind', 'mon', 'ce', 'def']))
        cand = [a for a in REGULIERS if compat(a, o.sg, o.cat)]
        if not cand: raise RuntimeError
        a = R.choice(cand)
        bon = forme(a, o.g, 's')
        dist = [x for x in dict.fromkeys(A[a]['f']) if x != bon][:2]
        hint = ('%s est féminin : j’ajoute un e.' if o.g == 'f' else '%s est masculin singulier.') % cap(o.mot)
        p = trou(o, a) if niv == 0 else phrase_trou(o, a, niv)
        return Cx(p, bon, dist, hint, None, 'pr')
    return pool(g)

def e8(niv):   # Des féminins qui changent
    def g():
        o = gn_nu(nb='s', kind=R.choice(['ind', 'mon', 'ce', 'def']))
        if o.g != 'f': raise RuntimeError
        cand = [a for a in IRREG if compat(a, o.sg, o.cat) and a not in ('long', 'bon') or (a in ('long', 'bon') and compat(a, o.sg, o.cat))]
        if not cand: raise RuntimeError
        a = R.choice(cand)
        bon, ms = A[a]['f'][1], A[a]['f'][0]
        faux = ms + 'e' if ms + 'e' not in (bon, 'fraise') else ms + 'x'
        p = trou(o, a) if niv == 0 else phrase_trou(o, a, niv)
        return Cx(p, bon, [faux, ms], IRREG[a], 'Complète avec l’adjectif au féminin.' if niv == 0 else 'Complète avec l’adjectif qui convient.', 'pr')
    return pool(g)

def e9(niv):   # Singulier ou pluriel
    def g():
        o = gn_nu(nb='p', kind=R.choice(['def', 'mon', 'ce', 'son', 'notre']))
        a = adj_pour(o)
        if not a: raise RuntimeError
        if A[a]['place'] != 'pre' and R.random() < 0.4: o = GN(cat=o.cat, nb='p', avec_adj=0, kind='ind', nom=o.nom)
        bon = forme(a, o.g, 'p')
        dist = [x for x in dict.fromkeys(A[a]['f']) if x != bon][:2]
        if len(dist) < 2: raise RuntimeError
        hint = '%s est pluriel %s.' % (cap(o.mot), 'masculin' if o.g == 'm' else 'féminin')
        p = trou(o, a) if niv == 0 else phrase_trou(o, a, niv, True)
        return Cx(p, bon, dist, hint, None, 'pr')
    return pool(g)

def e10(niv):  # Je vérifie les accords : un trou, ou une question sur le mot qui commande l'accord
    def g():
        t = R.choice(['trou', 'qui', 'pourquoi'] if niv else ['trou', 'qui'])
        o = gn_nu(kind=R.choice(['def', 'mon', 'ce', 'son', 'notre']))
        a = adj_pour(o)
        if not a: raise RuntimeError
        bon = forme(a, o.g, o.nb)
        gtxt = ('féminin' if o.g == 'f' else 'masculin') + (' pluriel' if o.nb == 'p' else ' singulier')
        o2 = GN(cat=o.cat, nb=o.nb, avec_adj=0, kind=R.choice(['def', 'mon', 'ce']), nom=o.nom)
        full = o2.det + ('' if o2.det.endswith('’') else ' ') + (bon + ' ' + o2.mot if A[a]['place'] == 'pre' else o2.mot + ' ' + bon)
        if t == 'trou':
            dist = [x for x in dict.fromkeys(A[a]['f']) if x != bon]
            if len(dist) < 2: raise RuntimeError
            p = trou(o2, a) if niv == 0 else phrase_trou(o2, a, niv, o2.nb == 'p')
            return Cx(p, bon, dist[:2], 'Le nom noyau « %s » est %s : l’adjectif s’accorde avec lui.' % (o2.mot, gtxt), 'Complète avec la bonne forme.' if niv else None, 'pr')
        if t == 'qui':
            return Cx(full, o2.mot, [o2.det, bon], 'L’adjectif prend le genre et le nombre du nom noyau.', 'Avec quel mot « %s » s’accorde-t-il ?' % bon)
        autres = [x for x in ['féminin pluriel', 'masculin pluriel', 'féminin singulier', 'masculin singulier'] if x != gtxt][:2]
        return Cx(full, 'Parce que « %s » est %s.' % (o2.mot, gtxt), ['Parce que « %s » est %s.' % (o2.mot, x) for x in autres],
                  'Je cherche le nom noyau, puis je regarde son genre et son nombre.', 'Pourquoi « %s » s’écrit-il ainsi ?' % bon)
    return pool(g)

# ---- écrans de pluriels : (singulier, pluriel, phrase courte, phrase longue) ; le mot cherché est remplacé par ___
PL_X = [
 ('bateau', 'bateaux', 'eau', 'Les ___ naviguent sur la mer.', 'Au port, les pêcheurs préparent leurs ___ avant de partir en mer.'),
 ('château', 'châteaux', 'eau', 'Nous visitons des ___ en Bretagne.', 'Pendant les vacances, nous avons visité plusieurs ___ au bord de la Loire.'),
 ('gâteau', 'gâteaux', 'eau', 'Maman prépare deux ___ au chocolat.', 'Pour la fête de l’école, les parents ont préparé de délicieux ___ pour tous les enfants.'),
 ('manteau', 'manteaux', 'eau', 'Ils enfilent leurs ___ pour sortir.', 'En hiver, tous les élèves portent de gros ___ pour aller dans la cour.'),
 ('chapeau', 'chapeaux', 'eau', 'Les clowns lancent leurs ___ en l’air.', 'Sur la plage, les touristes portent de grands ___ pour se protéger du soleil.'),
 ('tableau', 'tableaux', 'eau', 'Le musée expose de beaux ___ .', 'Dans la grande salle du musée, on peut admirer de célèbres ___ de peintres connus.'),
 ('couteau', 'couteaux', 'eau', 'Le cuisinier aiguise ses ___ .', 'Avant de commencer la recette, le cuisinier range tous ses ___ sur la table.'),
 ('oiseau', 'oiseaux', 'eau', 'Les ___ chantent dans l’arbre.', 'Au printemps, les ___ construisent leurs nids dans les arbres du jardin.'),
 ('cadeau', 'cadeaux', 'eau', 'Les enfants ouvrent leurs ___ .', 'Pour son anniversaire, Zoé a reçu de très jolis ___ de la part de ses amis.'),
 ('ruisseau', 'ruisseaux', 'eau', 'Les ___ descendent de la montagne.', 'Au printemps, la neige fond et de petits ___ coulent à travers la vallée.'),
 ('rideau', 'rideaux', 'eau', 'Maman lave les ___ du salon.', 'Dans la salle de classe, on ferme les ___ quand le soleil éblouit les élèves.'),
 ('bureau', 'bureaux', 'eau', 'Les ___ de la classe sont alignés.', 'Dans l’école, les ___ des maîtres sont situés au premier étage.'),
 ('panneau', 'panneaux', 'eau', 'Les ___ indiquent la direction.', 'Le long de la route, de grands ___ préviennent les conducteurs du danger.'),
 ('drapeau', 'drapeaux', 'eau', 'Les ___ flottent dans le vent.', 'Pendant la cérémonie, les enfants agitent de petits ___ aux couleurs de la France.'),
 ('anneau', 'anneaux', 'eau', 'Elle porte deux ___ aux doigts.', 'Le magicien a sorti de son chapeau trois ___ dorés qu’il a fait tourner.'),
 ('troupeau', 'troupeaux', 'eau', 'Le berger garde ses ___ .', 'Dans la montagne, plusieurs ___ de moutons broutent l’herbe tendre.'),
 ('chameau', 'chameaux', 'eau', 'Les ___ traversent le désert.', 'Dans le désert, les voyageurs avancent lentement sur leurs ___ pendant des heures.'),
 ('taureau', 'taureaux', 'eau', 'Les ___ sont dans le pré.', 'Dans cette ferme, le fermier garde deux puissants ___ derrière la barrière.'),
 ('cheveu', 'cheveux', 'eu', 'Elle a de longs ___ blonds.', 'Avant le spectacle, la coiffeuse brosse soigneusement les ___ des petites danseuses.'),
 ('jeu', 'jeux', 'eu', 'Nous jouons à des ___ de société.', 'Le soir, toute la famille se réunit autour de la table pour jouer à des ___ de cartes.'),
 ('feu', 'feux', 'eu', 'Les pompiers éteignent les ___ .', 'Pendant la fête nationale, de magnifiques ___ d’artifice éclairent tout le ciel.'),
 ('neveu', 'neveux', 'eu', 'Mes ___ viennent dîner demain.', 'Pour les vacances, ma tante invite tous ses ___ à passer une semaine chez elle.'),
 ('vœu', 'vœux', 'eu', 'Il écrit ses ___ sur une carte.', 'À la fin de l’année, le maire présente ses meilleurs ___ à tous les habitants.'),
 ('lieu', 'lieux', 'eu', 'Nous visitons des ___ célèbres.', 'Pendant notre voyage, nous avons découvert de nombreux ___ chargés d’histoire.'),
 ('tuyau', 'tuyaux', 'au', 'Le plombier change les ___ .', 'Dans la cave, de vieux ___ en métal passent le long des murs.'),
]
PL_AUX = [
 ('cheval', 'chevaux', 'Les ___ galopent dans le pré.', 'Au centre équestre, les enfants brossent les ___ avant la leçon.'),
 ('animal', 'animaux', 'Les ___ du zoo mangent à midi.', 'Dans la ferme pédagogique, les enfants nourrissent tous les ___ avec du foin.'),
 ('journal', 'journaux', 'Papa achète deux ___ .', 'Chaque matin, mon grand-père lit les ___ avec une tasse de café.'),
 ('hôpital', 'hôpitaux', 'Cette ville a trois ___ .', 'Dans les grandes villes, il y a plusieurs ___ pour soigner les malades.'),
 ('canal', 'canaux', 'Les ___ de Venise sont célèbres.', 'À Amsterdam, de nombreux ___ traversent la ville et les bateaux y circulent.'),
 ('signal', 'signaux', 'Les ___ clignotent dans la nuit.', 'Sur la voie ferrée, de grands ___ lumineux avertissent les conducteurs de train.'),
 ('bocal', 'bocaux', 'Maman range les ___ de confiture.', 'Dans la cave, nous avons rangé tous les ___ de confiture sur les étagères.'),
 ('tribunal', 'tribunaux', 'Il y a deux ___ dans cette ville.', 'Dans la capitale, plusieurs ___ jugent des affaires importantes chaque jour.'),
 ('métal', 'métaux', 'Le fer et l’or sont des ___ .', 'Dans l’atelier, le forgeron travaille différents ___ pour fabriquer des outils.'),
 ('local', 'locaux', 'L’école utilise plusieurs ___ .', 'Dans le quartier, de nouveaux ___ ont été construits pour les associations.'),
 ('végétal', 'végétaux', 'Les ___ ont besoin d’eau et de lumière.', 'Dans le jardin botanique, on peut observer des ___ venus du monde entier.'),
 ('rival', 'rivaux', 'Les deux équipes sont des ___ .', 'Pendant le match, les ___ se sont serré la main avant de commencer à jouer.'),
 ('amiral', 'amiraux', 'Les ___ dirigent la flotte.', 'Sur le grand navire, les ___ étudient la carte avant de donner leurs ordres.'),
 ('cardinal', 'cardinaux', 'Les ___ se réunissent à Rome.', 'À Rome, les ___ se rassemblent dans la chapelle pour choisir le nouveau pape.'),
 ('maréchal', 'maréchaux', 'Les ___ de l’armée défilent.', 'Pendant la cérémonie, les ___ de l’armée défilent devant le président.'),
]
PL_INV = [
 ('souris', 'Les ___ grises courent dans le grenier.', 'Pendant la nuit, des ___ viennent grignoter les restes de fromage dans la cuisine.'),
 ('tapis', 'Nous roulons les ___ du salon.', 'Avant la fête, nous avons secoué tous les ___ du grand salon dans le jardin.'),
 ('bras', 'Les nageurs lèvent les ___ .', 'Après la course, les sportifs lèvent les ___ pour saluer le public.'),
 ('repas', 'Nous préparons deux ___ par jour.', 'Pendant le camp, les enfants ont préparé tous les ___ avec l’aide des animateurs.'),
 ('pays', 'Je connais trois ___ d’Europe.', 'Pendant ses voyages, mon oncle a visité de nombreux ___ sur plusieurs continents.'),
 ('cours', 'Les ___ commencent à huit heures.', 'Le lundi, les élèves suivent plusieurs ___ importants avant la récréation de dix heures.'),
 ('bois', 'Nous traversons deux ___ .', 'Pendant la promenade, nous avons traversé de grands ___ remplis de champignons.'),
 ('corps', 'Les ___ des danseurs sont souples.', 'Après de longs entraînements, les ___ des athlètes sont devenus très forts.'),
 ('dos', 'Les élèves portent leurs sacs sur les ___ .', 'Après la randonnée, tous les marcheurs avaient mal aux ___ à cause des lourds sacs.'),
 ('fils', 'Les deux ___ du boulanger l’aident.', 'Dans cette famille, les ___ travaillent avec leur père à la boulangerie.'),
 ('jus', 'Nous buvons des ___ de fruits.', 'Au petit déjeuner, ma mère prépare toujours plusieurs ___ de fruits frais.'),
 ('nez', 'Les clowns ont des ___ rouges.', 'Pendant le spectacle, tous les clowns portaient de gros ___ rouges.'),
 ('gaz', 'Ces ___ sont dangereux.', 'Dans l’usine, de nombreux ___ circulent dans des tuyaux très surveillés.'),
 ('voix', 'Nous écoutons des ___ douces.', 'Dans la forêt, on entend des ___ lointaines qui chantent.'),
 ('prix', 'Les ___ sont affichés.', 'Au marché, les ___ des fruits changent selon les saisons.'),
 ('noix', 'Les écureuils cachent des ___ .', 'À l’automne, les écureuils ramassent des ___ qu’ils enterrent pour l’hiver.'),
 ('croix', 'Le médecin dessine deux ___ .', 'Sur la carte, le pirate a tracé plusieurs ___ rouges pour marquer les cachettes.'),
 ('puits', 'Il y a deux ___ dans le village.', 'Dans ce vieux village, plusieurs ___ servent encore à arroser les jardins.'),
]
def melanger(liste):
    L = liste[:]; R.shuffle(L)
    return L
def remplir(items):
    """Garde les PAR_NIVEAU premiers exercices qui ne sont pas déjà dans l'écran."""
    out, vus = [], set(DEJA)
    for e in items:
        c = cle(e)
        if c in vus: continue
        vus.add(c); out.append(e)
        if len(out) == PAR_NIVEAU: break
    assert len(out) == PAR_NIVEAU, len(out)
    return out

def e11(niv):
    ph = {'eau': 'Les mots en -eau prennent un x au pluriel.', 'eu': 'Les mots en -eu prennent un x au pluriel.', 'au': 'Les mots en -au prennent un x au pluriel.'}
    return remplir([Cx('un %s → des ___' % sg if niv == 0 else (court if niv == 1 else long_), pl, [sg + 's', sg], ph[f], None, 'circ') for sg, pl, f, court, long_ in melanger(PL_X)])

def e12(niv):
    return remplir([Cx('un %s → des ___' % sg if niv == 0 else (court if niv == 1 else long_), pl, [sg[:-2] + 'als', pl + 's'], '-al devient -aux.', 'Complète avec le nom au pluriel.', 'circ')
                    for sg, pl, court, long_ in melanger(PL_AUX)])

def e13(niv):
    def faux(w): return [x for x in dict.fromkeys([w + 's', w + ('x' if w[-1] != 'x' else 'z')]) if x != w]
    return remplir([Cx('un %s → des ___' % w if niv == 0 else (court if niv == 1 else long_), w, faux(w), '%s finit déjà par %s.' % (cap(w), w[-1]), None, 'circ') for w, court, long_ in melanger(PL_INV)])

ECRANS = [e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12, e13]

def main():
    s = open(CHEMIN, encoding='utf-8').read()
    mp = re.search(r'const PLUS=(\{.*\});\n', s); PLUS = json.loads(mp.group(1))
    mn = re.search(r'const NIV_ATOI=(\{.*\});\n', s); NIV = json.loads(mn.group(1))
    assert len(PLUS['G3']) == 13 and len(NIV['G3']['2']) == 13
    for k, fn in enumerate(ECRANS):
        for niv in (0, 1, 2):
            R.seed(1000 * k + 10 * niv + 7)
            orig = (PLUS['G3'][k][:PLUS_ORIGINE[k]] if niv == 0 else NIV['G3'][str(niv + 1)][k][:NIV_ORIGINE])
            DEJA.clear(); DEJA.update(cle(e) for e in orig)
            nouv = fn(niv)
            if niv == 0:
                PLUS['G3'][k] = PLUS['G3'][k][:PLUS_ORIGINE[k]] + nouv
            else:
                NIV['G3'][str(niv + 1)][k] = NIV['G3'][str(niv + 1)][k][:NIV_ORIGINE] + nouv
    s = s[:mp.start(1)] + json.dumps(PLUS, ensure_ascii=False) + s[mp.end(1):]
    mn = re.search(r'const NIV_ATOI=(\{.*\});\n', s)
    s = s[:mn.start(1)] + json.dumps(NIV, ensure_ascii=False) + s[mn.end(1):]
    open(CHEMIN, 'w', encoding='utf-8').write(s)
    print('G3 : +%d exercices par écran et par classe (CE2, CM1, CM2).' % PAR_NIVEAU)

if __name__ == '__main__':
    main()
