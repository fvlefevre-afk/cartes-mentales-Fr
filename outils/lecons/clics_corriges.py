"""Corrections du 09/11/2026 : exercices « Clique sur … » où plusieurs réponses étaient justes (ex. « Papa lit le journal dans le salon » : deux « le »).
Règle : toute réponse juste est marquée <…> et le nombre à trouver (n) est annoncé dans la consigne ; sinon la phrase n'a qu'une seule réponse possible."""
from niveaux_lib import *
def gn(n): return (f'Clique sur les {n} groupes nominaux.', 'Cherche les noms avec leur déterminant.')
GN2, GN3 = gn(2), gn(3)
DT1 = ('Clique sur le déterminant.', 'C’est le petit mot devant le nom.')
def dt(n): return (f'Clique sur les {n} déterminants.', 'Ce sont les petits mots devant les noms.')
NN = ('Clique sur le nom noyau du groupe sujet.', 'Le sujet est au début : qui est-ce qui… ?')
AD1 = ('Clique sur l’adjectif.', 'Il dit comment est le nom.')
AD2 = ('Clique sur les 2 adjectifs.', 'Ils disent comment est le nom.')
def k(p, a, n=None): return K(p, a[0], a[1], 'x', n)
G3 = {
 'Des mots autour d’un nom': (
  [k('<Les enfants> regardent <un vieux film> ensemble.', GN2, 2), k('<Mon voisin> cultive <de beaux légumes> patiemment.', GN2, 2),
   k('<Ma sœur> porte <une longue écharpe rouge> aujourd’hui.', GN2, 2), k('<Le petit garçon> range <ses petites voitures> soigneusement.', GN2, 2)],
  [k('<Les touristes> ont visité <un magnifique château médiéval> hier.', GN2, 2), k('<Les élèves> offrent <un joli bouquet> à <leur maîtresse>.', GN3, 3),
   k('<La jeune institutrice> raconte <une très longue histoire> calmement.', GN2, 2), k('<Mon oncle> prête <son vieux vélo rouge> à <ses deux cousins>.', GN3, 3)]),
 'Le déterminant': (
  [k('<Mes> cousins arrivent demain soir.', DT1), k('Papa lit <le> journal dans <le> salon.', dt(2), 2), k('Nous cueillons <des> pommes mûres.', DT1), k('Elle admire <cette> belle montagne.', DT1)],
  [k('Pendant <les> vacances d’été, nous irons à <la> mer.', dt(2), 2), k('<Mon> frère a lu <un> livre passionnant sur <les> volcans.', dt(3), 3),
   k('<Ces> vieilles maisons de pierre sont fragiles.', DT1), k('<Nos> voisins ont repeint <leur> maison en blanc.', dt(2), 2)]),
 'Le mot le plus important': (
  [k('Le petit <chat> noir dort doucement.', ('Clique sur le nom noyau.', 'Quel mot ne peut-on pas enlever ?')), k('Une grande <maison> blanche brille là-bas.', ('Clique sur le nom noyau.', 'Quel mot ne peut-on pas enlever ?')),
   k('Mon vieux <vélo> rouge est cassé.', ('Clique sur le nom noyau.', 'Quel mot ne peut-on pas enlever ?')), k('Les jolies <fleurs> jaunes poussent partout.', ('Clique sur le nom noyau.', 'Quel mot ne peut-on pas enlever ?'))],
  [k('Le vieux <château> abandonné domine toute la vallée depuis des siècles.', NN), k('Ces énormes <rochers> gris barrent le chemin de la montagne.', NN),
   k('Une délicieuse <odeur> de pain chaud flottait dans toute la cuisine.', NN), k('Mes deux petits <frères> jumeaux jouent dans le jardin.', NN)]),
 'Il dit comment est le nom': (
  [k('Elle porte une robe <bleue>.', AD1), k('Un <gros> nuage cache le soleil.', AD1), k('Le <vieux> pont de pierre tombe.', AD1), k('Tom mange une pomme <rouge>.', AD1)],
  [k('Au loin, on aperçoit une <immense> forêt de sapins.', AD1), k('Le chat <affamé> miaule devant sa gamelle <vide>.', AD2, 2),
   k('Mon voisin raconte toujours des histoires <extraordinaires>.', AD1), k('Ce <vieux> cheval connaît tous les chemins de la forêt.', AD1)]),
}
G4 = {
 'Le verbe se conjugue': (
  [K('[Mes cousins] (arrivent) demain.', 'Clique sur le verbe.', 'Le verbe change avec le temps et avec le sujet.', 'v'), K('[Le train] (part) à midi.', 'Clique sur le verbe.', 'Le verbe change avec le temps et avec le sujet.', 'v'),
   K('Hier, [nous] (avons mangé) des crêpes.', 'Clique sur le verbe.', 'Le verbe change avec le temps et avec le sujet.', 'v'), K('[Tu] (liras) ce livre.', 'Clique sur le verbe.', 'Le verbe change avec le temps et avec le sujet.', 'v')],
  [K('Pendant la récréation, [les élèves] (se rangent) dans la cour.', 'Clique sur le verbe.', 'Le verbe change avec le temps et avec le sujet.', 'v'), K('Demain, [ma sœur] (partira) en voyage avec ses amis.', 'Clique sur le verbe.', 'Le verbe change avec le temps et avec le sujet.', 'v'),
   K('Hier soir, [mes parents] (ont regardé) un film.', 'Clique sur le verbe.', 'Le verbe change avec le temps et avec le sujet.', 'v'), K('Chaque matin, [le boulanger] (prépare) du pain frais.', 'Clique sur le verbe.', 'Le verbe change avec le temps et avec le sujet.', 'v')]),
}
def corriger(g, patch):
    s = open(CHEMIN, encoding='utf-8').read()
    L = lessons_json(g)
    titres = [e['titre'] for e in L['ecrans']]
    m = re.search(r'const NIV_ATOI=(\{.*\});\n', s)
    NIV = json.loads(m.group(1))
    for t, (a2, a3) in patch.items():
        i = titres.index(t)
        NIV[g]['2'][i] = a2
        NIV[g]['3'][i] = a3
    s = s[:m.start(1)] + json.dumps(NIV, ensure_ascii=False) + s[m.end(1):]
    open(CHEMIN, 'w', encoding='utf-8').write(s)
    print(g, ':', len(patch), 'écrans corrigés')
if __name__ == '__main__':
    corriger('G3', G3); corriger('G4', G4)
