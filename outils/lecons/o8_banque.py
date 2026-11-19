"""O8 (« Les noms en -é, -ée, -té, -tié ») : BANQUE d'exercices écrite à la main (19/11/2026). État : intégré dans index.html le 19/11/2026
(intégration : python3 o8_banque.py --integrer, relançable : repart des exercices d'origine).

Avant : 3 exercices par écran. Sources : docs/dispositif-orthographe-ce2-cm1-cm2.md (O8 : -é masculin, -ée féminin, -té qualité ou état, -tée contenu ou action, -tié : moitié, amitié, pitié ;
CM1 = découverte avec dictée et montée ; CM2 = exceptions -tée : assiettée, portée, jetée…), programme du cycle 3 (mots fréquents, régularités et formation des mots) et règle de la leçon
(« un nom masculin : -é, sauf le musée, le lycée »). Phonétique : aucun signe ([é] retiré par l'audit du 19/11/2026).
Jamais d'écriture fausse : propositions = FINS de mots (trou de lettres) ou phrases justes sur la règle ; la question « Quel nom s'écrit -tié ? » propose de vrais mots."""
H = 'hl'
ASK = 'Complète avec la bonne fin.'
def Q(p, bon, autres, hint, ask=ASK):
    return {'p': p, 'tasks': [{'choose': [bon] + autres, 'ok': 0, 'hint': hint, 'ask': ask, 'fill': H}]}
def MASC(p, hint): return Q(p, 'é', ['ée', 'er'], hint)
def FEM(p, hint): return Q(p, 'ée', ['é', 'er'], hint)
def TE(p, hint): return Q(p, 'té', ['tée', 'tié'], hint)
def TEE(p, hint): return Q(p, 'tée', ['té', 'tié'], hint)
# écran 1 : masculin -é (sauf le musée, le lycée)
MASCULIN = [MASC('un pr___', 'Le nom est masculin : un pré.'), MASC('un béb___', 'Le nom est masculin : un bébé.'), MASC('un côt___', 'Le nom est masculin : un côté.'),
            MASC('un ét___', 'Le nom est masculin : un été.'), MASC('un pât___', 'Le nom est masculin : un pâté.'), MASC('un degr___', 'Le nom est masculin : un degré.'),
            MASC('un résum___', 'Le nom est masculin : un résumé.'), MASC('un cong___', 'Le nom est masculin : un congé.'), MASC('un pass___', 'Le nom est masculin : un passé.'),
            MASC('un défil___', 'Le nom est masculin : un défilé.'),
            FEM('un mus___', 'Une exception : un musée, masculin mais avec -ée.'), FEM('un lyc___', 'Une exception : un lycée, masculin mais avec -ée.')]
# écran 2 : féminin -ée
FEMININ = [FEM('une matin___', 'Le nom est féminin : une matinée.'), FEM('la fum___', 'Le nom est féminin : la fumée.'), FEM('une poup___', 'Le nom est féminin : une poupée.'),
           FEM('une ép___', 'Le nom est féminin : une épée.'), FEM('la mar___', 'Le nom est féminin : la marée.'), FEM('une chemin___', 'Le nom est féminin : une cheminée.'),
           FEM('une entr___', 'Le nom est féminin : une entrée.'), FEM('une arriv___', 'Le nom est féminin : une arrivée.'), FEM('une all___', 'Le nom est féminin : une allée.'),
           FEM('une dur___', 'Le nom est féminin : une durée.'), FEM('une rang___', 'Le nom est féminin : une rangée.'), FEM('une travers___', 'Le nom est féminin : une traversée.')]
# écran 3 : une qualité ou un état : -té
QUALITE = [TE('la clar___', 'C’est une qualité : la clarté.'), TE('la sécuri___', 'C’est un état : la sécurité.'), TE('la difficul___', 'C’est un état : la difficulté.'),
           TE('la rapidi___', 'C’est une qualité : la rapidité.'), TE('la pauvre___', 'C’est un état : la pauvreté.'), TE('la propre___', 'C’est une qualité : la propreté.'),
           TE('la volon___', 'C’est une qualité : la volonté.'), TE('l’égali___', 'C’est un état : l’égalité.'), TE('la fier___', 'C’est une qualité : la fierté.'),
           TE('la fragili___', 'C’est une qualité : la fragilité.'), TE('la timidi___', 'C’est un état : la timidité.'), TE('la séréni___', 'C’est un état : la sérénité.')]
# écran 4 : -tée (dictée, montée) : pas de mot de plus au CM1 (le programme de la ceinture n'en voit que deux) ; les autres -tée sont au CM2
TEE_CM1 = []
# écran 5 : -tié (3 noms seulement) : questions avec de vrais mots
def TIE(ask, bon, a, b, hint):
    return {'p': '', 'tasks': [{'choose': [bon, a, b], 'ok': 0, 'hint': hint, 'ask': ask}]}
TIE_QUESTIONS = [TIE('Quel nom s’écrit -tié ?', 'la moitié', 'la santé', 'la dictée', 'Un des trois noms en -tié.'),
                 TIE('Quel nom s’écrit -tié ?', 'l’amitié', 'la bonté', 'la journée', 'Un des trois noms en -tié.'),
                 TIE('Quel nom s’écrit -tié ?', 'la pitié', 'la montée', 'la liberté', 'Un des trois noms en -tié.')]
# écran 6 : je prouve
R_M = 'Parce que c’est un nom masculin.'
R_F = 'Parce que c’est un nom féminin.'
R_Q = 'Parce que c’est une qualité ou un état.'
R_A = 'Parce que c’est une action ou un contenu.'
R_X = 'Parce que c’est une exception à mémoriser.'
R_T = 'Parce que c’est l’un des trois noms en -tié.'
def P(mot, fin, bon, a, b, hint):
    return {'p': '', 'tasks': [{'choose': [bon, a, b], 'ok': 0, 'hint': hint, 'ask': 'Pourquoi %s dans « %s » ?' % (fin, mot)}]}
PROUVE = [
 P('bébé', '-é', R_M, R_F, R_Q, 'Regarde le petit mot devant : un.'), P('soirée', '-ée', R_F, R_M, R_Q, 'Regarde le petit mot devant : une.'),
 P('clarté', '-té', R_Q, R_A, R_F, 'Une qualité, un état.'), P('musée', '-ée', R_X, R_F, R_Q, 'Un nom masculin qui s’écrit pourtant -ée.'),
 P('pré', '-é', R_M, R_F, R_Q, 'Regarde le petit mot devant : un.'), P('fumée', '-ée', R_F, R_M, R_Q, 'Regarde le petit mot devant : la.'),
 P('sécurité', '-té', R_Q, R_A, R_M, 'Un état.'), P('montée', '-tée', R_A, R_Q, R_M, 'L’action de monter.'),
 P('lycée', '-ée', R_X, R_F, R_A, 'Un nom masculin qui s’écrit pourtant -ée.'), P('pitié', '-tié', R_T, R_Q, R_A, 'Je mémorise : moitié, amitié, pitié.'),
 P('café', '-é', R_M, R_F, R_Q, 'Regarde le petit mot devant : un.'), P('timidité', '-té', R_Q, R_A, R_F, 'Un état.'),
]
CM2_EXTRA = [TEE('une je___', 'Une jetée : -tée, avec e.'), TEE('une assiet___', 'Un contenu : une assiettée, avec e.'), TEE('une pâ___', 'De la nourriture pour un animal : une pâtée, avec e.'),
             TEE('une nui___', 'Une nuit passée à l’hôtel : une nuitée, avec e.'), TEE('une pelle___', 'Le contenu d’une pelle : une pelletée, avec e.'), TEE('une po___', 'Le contenu d’un pot : une potée, avec e.')]
BANQUE = {'masc': MASCULIN, 'fem': FEMININ, 'te': QUALITE, 'tee': TEE_CM1, 'tie': TIE_QUESTIONS, 'prouve': PROUVE}
ORDRE = ['masc', 'fem', 'te', 'tee', 'tie', 'prouve']
PLUS_ORIGINE = 2
def integrer():
    import json, os, re
    chemin = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'index.html')
    s = open(chemin, encoding='utf-8').read()
    m = re.search(r'const PLUS=(\{.*\});\n', s); PLUS = json.loads(m.group(1))
    assert len(PLUS['O8']) == 6, len(PLUS['O8'])
    for k, cle in enumerate(ORDRE):
        orig = PLUS['O8'][k][:PLUS_ORIGINE]
        vus = {json.dumps(e, ensure_ascii=False) for e in orig}
        assert all(json.dumps(e, ensure_ascii=False) not in vus for e in BANQUE[cle]), ('doublon avec un exercice d’origine', cle)
        PLUS['O8'][k] = orig + BANQUE[cle]
    s = s[:m.start(1)] + json.dumps(PLUS, ensure_ascii=False) + s[m.end(1):]
    m2 = re.search(r'const CM2_PLUS=(\{.*\});\n', s); C = json.loads(m2.group(1))
    ec = C['O8']['ecrans'][0]; assert ec['titre'] == 'Les exceptions en -tée'
    base = ec['plus'][:2]
    vus = {json.dumps(e, ensure_ascii=False) for e in base + [ec['atoi']]}
    assert all(json.dumps(e, ensure_ascii=False) not in vus for e in CM2_EXTRA), 'doublon CM2'
    ec['plus'] = base + CM2_EXTRA
    s = s[:m2.start(1)] + json.dumps(C, ensure_ascii=False) + s[m2.end(1):]
    open(chemin, 'w', encoding='utf-8').write(s)
    print('O8 : exercices en plus par écran :', {k: len(v) for k, v in BANQUE.items()}, '; CM2 « -tée » :', len(CM2_EXTRA))
if __name__ == '__main__':
    import sys
    if '--integrer' in sys.argv:
        integrer(); sys.exit(0)
    for k, L in BANQUE.items():
        print('==', k, len(L))
        for e in L:
            t = e['tasks'][0]; print('  ', e['p'] or '(question)', '→', t['choose'][0], '|', t.get('ask', '') if not e['p'] else '', '|', t['hint'])
    print('== CM2 -tée', len(CM2_EXTRA))
    for e in CM2_EXTRA: print('  ', e['p'], '→', e['tasks'][0]['choose'][0], '|', e['tasks'][0]['hint'])
