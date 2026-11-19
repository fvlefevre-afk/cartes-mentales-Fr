"""O7 (CE2, « e, é, è, ê : accent ou pas ») : BANQUE d'exercices écrite à la main (19/11/2026). Intégration : `python3 o7_banque.py --integrer`
(relançable : repart des exercices d'origine) ; `python3 o7_banque.py` : liste et contrôles (banque_o.py).

Sources : docs/dispositif-orthographe-ce2-cm1-cm2.md (O7 au CE2 seulement, dictées : père, terre, fenêtre, forêt), annexe du cycle 2 (mots fréquents,
accents), règle de la leçon (é quand on entend é ; e sans accent devant deux consonnes ou une consonne finale ; è devant une consonne puis un e muet ;
è devant s à la fin de quelques mots ; ê à mémoriser). Mots du CE2 ; aucun mot qui contredit la règle de l'écran (chèvre, fièvre : è devant deux consonnes).
Aucun signe phonétique dans les ajouts (« le son é » au lieu de [é])."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from banque_o import Q, C, main
ASK = 'Complète avec la bonne lettre.'
def EA(p, mot): return Q(p, 'é', ['e', 'è'], 'J’entends le son é : %s.' % mot, ASK)
ECRAN_EAIGU = [EA('une ___toile', 'une étoile'), EA('une ___ponge', 'une éponge'), EA('un ___cureuil', 'un écureuil'), EA('une ___charpe', 'une écharpe'),
               EA('une ___pée', 'une épée'), EA('le caf___', 'le café'), EA('une f___e', 'une fée'), EA('un d___', 'un dé'),
               EA('une cl___', 'une clé'), EA('une id___e', 'une idée'), EA('un m___decin', 'un médecin'), EA('le march___', 'le marché')]
def E2(p, cc): return Q(p, 'e', ['é', 'è'], 'Deux consonnes suivent : %s.' % cc, ASK)
def EF(p): return Q(p, 'e', ['é', 'è'], 'Une consonne à la fin du mot.', ASK)
ECRAN_E = [EF('la m___r'), EF('un ch___f'), EF('le f___r'), EF('av___c'),
           E2('une assi___tte', 'tt'), E2('une v___ste', 'st'), E2('une s___rviette', 'rv'), E2('le d___ssert', 'ss'),
           E2('une l___ttre', 'tt'), E2('un m___rle', 'rl'), E2('une p___lle', 'll'), E2('un ins___cte', 'ct')]
def EG(p, c): return Q(p, 'è', ['e', 'é'], 'Une consonne puis un e muet : %s + e.' % c, ASK)
ECRAN_EGRAVE = [EG('le p___re', 'r'), EG('le fr___re', 'r'), EG('une pi___ce', 'c'), EG('une cuill___re', 'r'), EG('une sorci___re', 'r'),
                EG('la mati___re', 'r'), EG('un probl___me', 'm'), EG('un po___me', 'm'), EG('un si___ge', 'g'), EG('un mod___le', 'l'),
                EG('le coll___ge', 'g'), EG('la cr___me', 'm')]
def ES(p, mot): return Q(p, 'è', ['e', 'é'], 'Un mot à mémoriser : %s.' % mot, ASK)
QS = 'Quel mot finit par è devant s ?'
ECRAN_ES = [ES('tr___s bien', 'très'), ES('apr___s le repas', 'après'), ES('tout pr___s', 'près'), ES('aupr___s de lui', 'auprès'),
            ES('Il l’a fait expr___s.', 'exprès'), ES('un proc___s', 'un procès'),
            C(QS, 'très', 'tes', 'trop', 'Un mot à mémoriser.'), C(QS, 'après', 'avec', 'assez', 'Un mot à mémoriser.'),
            C(QS, 'le progrès', 'le prix', 'le repas', 'Un mot à mémoriser.')]
def EC(p, mot): return Q(p, 'ê', ['e', 'è'], 'Un mot avec ê : je mémorise %s.' % mot, ASK)
ECRAN_ECIRC = [EC('une b___te', 'la bête'), EC('une fen___tre', 'la fenêtre'), EC('une temp___te', 'la tempête'), EC('une cr___pe', 'la crêpe'),
               EC('un r___ve', 'le rêve'), EC('une gu___pe', 'la guêpe'), EC('un ch___ne', 'le chêne'), EC('la p___che', 'la pêche'),
               EC('m___me', 'même'), EC('pr___t', 'prêt'), EC('un arr___t', 'un arrêt'), EC('une b___tise', 'une bêtise')]
R_FIN, R_MUET, R_E, R_MEM = 'Parce qu’une consonne termine le mot.', 'Parce qu’il y a une consonne puis un e muet.', 'Parce que j’entends le son é.', 'Parce que c’est un mot à mémoriser.'
R_N, R_C, R_L = 'Parce que c’est un nom.', 'Parce que le mot est court.', 'Parce que le mot est long.'
def R2(cc): return 'Parce qu’il y a deux consonnes après : %s.' % cc
def P(lettre, mot, bon, a, b, hint): return C('Pourquoi %s dans « %s » ?' % (lettre, mot), bon, a, b, hint)
ECRAN_PROUVE = [P('e sans accent', 'lettre', R2('tt'), R_N, R_L, 'Regarde ce qui suit.'), P('e sans accent', 'vestes', R2('st'), R_MEM, R_C, 'Regarde ce qui suit.'),
                P('e sans accent', 'mer', R_FIN, R_MUET, R_N, 'Regarde la fin du mot.'), P('e sans accent', 'chef', R_FIN, R_MUET, R_L, 'Regarde la fin du mot.'),
                P('è', 'père', R_MUET, R2('rr'), R_C, 'Regarde ce qui suit.'), P('è', 'pièce', R_MUET, R_FIN, R_N, 'Regarde ce qui suit.'),
                P('è', 'problème', R_MUET, R_FIN, R_L, 'Regarde ce qui suit.'), P('é', 'étoile', R_E, R2('st'), R_N, 'Écoute le son.'),
                P('é', 'café', R_E, R_MUET, R_C, 'Écoute le son.'), P('ê', 'fenêtre', R_MEM, R_FIN, R_C, 'Je mémorise.'),
                P('ê', 'rêve', R_MEM, R_FIN, R_L, 'Je mémorise.'), P('è', 'très', R_MEM, R_E, R_L, 'Un mot à mémoriser : è devant s.')]
BANQUE = {'eaigu': ECRAN_EAIGU, 'e': ECRAN_E, 'egrave': ECRAN_EGRAVE, 'es': ECRAN_ES, 'ecirc': ECRAN_ECIRC, 'prouve': ECRAN_PROUVE}
ORDRE = ['eaigu', 'e', 'egrave', 'es', 'ecirc', 'prouve']
ORIGINE = [2, 2, 2, 2, 2, 2]
if __name__ == '__main__':
    main('O7-CE2', BANQUE, ORDRE, ORIGINE)
