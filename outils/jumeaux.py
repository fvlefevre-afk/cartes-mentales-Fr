import json,re,sys,os
S=os.path.join(os.path.dirname(os.path.abspath(__file__)),'sortie')  # vérifie les leçons H2 à H7 fabriquées dans sortie/
F={ 'H2':[r'ont',r'la',r'l’a',r'l’as',r'ou',r'l\'a'],
    'H3':[r'se',r'ses',r'a',r'c’est',r's’est'],
    'H4':[r'est',r'où',r'mes'],
    'H5':[r'là',r'l’a',r'l’as',r's’est',r'ses',r'ces'],
    'H6':[r'sont',r'ces',r'mais',r'c’est',r's’est'],
    'H7':[r'ce',r'cet',r'cette',r'c’est',r'ces',r'ses']}
def strings(o):
    if isinstance(o,str): yield o
    elif isinstance(o,dict):
        for k,v in o.items():
            if k not in ('id','sec','couleur','picto','guide','fill'): yield from strings(v)
    elif isinstance(o,list):
        for v in o: yield from strings(v)
bad=0
for lid,words in F.items():
    d=json.load(open(os.path.join(S,f'{lid}.json')))
    html=open(os.path.join(S,f'{lid}map.html')).read()
    html=re.sub(r'<style>.*?</style>','',html,flags=re.S); html=re.sub(r'<[^>]+>',' ',html)
    texts=list(strings(d))+[html]
    for t in texts:
        tt=re.sub(r'[\[\](){}^~%#|*<>_]',' ',t)
        for w in words:
            for m in re.finditer(r'(?<![\wàâéèêëîïôûùç’\'])'+w+r'(?![\wàâéèêëîïôûùç’\'-])',tt,flags=re.I):
                bad+=1; print(lid,'«'+w+'»',':',tt[max(0,m.start()-40):m.end()+40].replace('\n',' '))
print('total',bad)
