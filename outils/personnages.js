/* Personnages des classes de mots (26/11/2026, demande de l'enseignante : « mes personnages sur la nature des mots apparaissent sous les mots travaillés dans la ceinture »).
   Source du bloc PERSOS-JS d'index.html : modifier ICI puis lancer  python3 outils/personnages.py  (qui recopie aussi les dessins d'origine d'outils/img/persos/).
   G3, G4 et G7 : « Je regarde », puis « Avec aide » et « Je corrige » une fois l'exercice réussi ; JAMAIS dans « Seul » (cela donnerait la réponse).
   G3 : natures calculées (natures) ; G4 et G7 : écrites phrase par phrase dans outils/personnages_phrases.txt (bloc PERSOS_PHRASES) : une phrase absente n'a pas de personnage. */
const PERSO_CEINT=['G3','G4','G7'];
const PERSO_TAGS={d:'det',n:'nom',np:'nompropre',nc:'nomcommun',a:'adj',v:'verbe',p:'pron',adv:'adv',c:'conj',pr:'prep'};
/* G4 : classes de mots montrées selon la classe de la leçon (CE2 : sans conjonction ni préposition ; CM1 : sans préposition) */
const PERSO_HORS={CE2:['conj','prep'],CM1:['prep']};
const PERSO_CL=['det','nom','adj','verbe','pron','adv','conj','prep','prel','nompropre','nomcommun'];
const PERSO_NOMS={det:'Déterminant',nom:'Nom',adj:'Adjectif',verbe:'Verbe',pron:'Pronom personnel',adv:'Adverbe',conj:'Conjonction de coordination',prep:'Préposition',prel:'Pronom relatif',nompropre:'Nom propre',nomcommun:'Nom commun'};
const persoOk=v=>typeof v==='string'&&/^data:image\/(webp|png);base64,[A-Za-z0-9+/=]+$/.test(v)&&v.length<=200000;
/* dessins choisis par l'enseignant(e) : seulement ceux qui changent ; "" = pas de personnage pour cette classe */
const persosValides=o=>{const r={};if(o&&typeof o==='object')PERSO_CL.forEach(k=>{const v=o[k];if(v===''||persoOk(v))r[k]=v;});return r;};
const persosLocaux=()=>{try{const c=JSON.parse(localStorage.getItem('francais-persos-locaux')||'null');return c&&typeof c==='object'?c:null;}catch(x){return null;}};
const persosChoisis=()=>persosValides(BROUILLON.persos||persosLocaux()||(OUVERTURE_REELLE&&OUVERTURE_REELLE.persos)||{});
const persoImg=k=>{const c=persosChoisis();return k in c?c[k]:(PERSOS_DEF[k]||'');};

/* ---- natures des mots de G3 : listes relues sur toutes les phrases de la leçon (test : python3 outils/tester_personnages.py) ---- */
const mots_=s=>new Set(s.split(' '));
const NAT_DET=mots_('le la les l’ un une des mon ma mes ton ta tes son sa ses notre nos votre vos leur leurs ce cet cette ces du au aux quel quelle quels quelles plusieurs chaque deux trois quelques');
const NAT_PROPRES=mots_('léa hugo maya tom nina léo samir sacha amsterdam rome venise loire bretagne france');
const NAT_ADJ=mots_('hantée rapide rapides fleuri mignon violente violent solide escarpé mystérieux dorée étroit ouverte ouvert fermé fermée fermés fermées courte vive vif violettes violette peureuse célèbre célèbres abandonné affamé aimable ancien ancienne anciens anciennes beau beaux bel belle belles blanc blanche blanches blancs bleu bleue bleus bleues blond blonde blondes blonds bon bonne bonnes bons botanique bouclés brun brune bruns brunes calme calmes carré carrée carrés carrées cassé centenaire chaud chaude chauds chaudes cher chère chers chères content contente contents contentes courageux courageuse courageuses curieux curieuse curieuses délicieux délicieuse délicieuses dernier dernière différents différentes dorés dorées doux douce douces drôle drôles droite énorme énormes entier entière épais épaisse épaisses équestre extraordinaire extraordinaires fatigué fatiguée ferrée fragile fragiles frais fraîche fraîches froid froide froids froides gentil gentille gentils gentilles grand grande grands grandes gris grise grises gros grosse grosses haut haute hauts hautes heureux heureuse heureuses immense immenses important importante importantes jaune jaunes jaunis jeune jeunes joli jolie jolis jolies joyeux joyeuse joyeuses jumeaux jumelles léger légère légers légères long longue longs longues lourd lourde lourds lourdes lumineux lumineuse lumineuses magnifique magnifiques médiéval migrateurs mûr mûre mûrs mûres neuf neuve neufs neuves noir noire noirs noires nombreux nombreuses nouveau nouvel nouvelle nouveaux nouvelles paresseux paresseuse paresseuses passionnant passionnante passionnants passionnantes pédagogique petit petite petits petites plein pleine pleins pleines poussiéreux premier première puissants rieuses rond ronde ronds rondes rose roses rouge rouges sérieux sérieuse sérieuses sinueuse sombre sombres sucré sucrée sucrés sucrées sympathique sympathiques tendre tendres timide timides transparent troué usé vert verte verts vertes velues vide vides vieux vieil vieille vieilles');
const NAT_NOM=mots_('plombier serpent facteur désert président flotte conductrice clé affaires ami amie amis amies amir amiral amiraux animal animaux anim anneau anneaux anniversaire araignées arbre arbres arc-en-ciel armoire armée assiette assiettes associations atelier bal ballon ballons bals banc banque barbe barque barrière bateau bateaux besoin blanc bocal bocaux boc boîte boîtes bol bonbon bonbons bord bottes boulanger bouquet bouteille bras brebis brise bureau bureaux bus cabane cadeau cadeaux café cahier cahiers caillou camions can canal canaux capitale cardinal cardinaux cardin carottes cartable carte casquette cave centre chambre chameau chameaux chanson chansons chanteur chanteuse chapeau chapeaux chapelle chariot chat chats chatte chaussettes chaussure chaussures chemin chemins chemise chevaux cheval chev cheveux cheveu chien chiens chocolat château châteaux chêne ciel ciels classe coffre coiffeuse conducteurs confiture coquillages corde corps couleurs cour cours cousin cousine cousins couteau couteaux couverture crayon crayons croix crème crêpe cuir cuisine cuisinier cérémonie côte dame danger danseuse danseuses dessin doigts drapeau drapeaux eau écharpe éclats école élève élèves éléphant enfant enfants équipe équipes escargots étage étagère étagères été falaise femme fenêtre fer ferme fermier feuilles filet filets fille filles film fleur fleurs foin fond forgeron forêt fraises français france froid fruit fruits frère frères fête gamelle garçon gaz girafe girafes glace glands graines grand-mère grand-père grands-parents grenier gâteau gâteaux guitare haie herbe heure heures histoire histoires hiver horloge hérisson héron hôpital hôpitaux hôpit institutrice jardin jeu jeux journal journaux journ jouets jour jupe jus lac laine lait lampes lapin lapins lecteur lectrice lettre leçon lieu lieux limonade lit livre livres local locaux loc lumière lunettes légumes magicien main maison maisons malades maman manteau manteaux marchande marché marin maréchal maréchaux maréch match matin maîtres maîtresse mer midi minéral minéraux minér monde montagne montre moto mouette moutons murs musicien musée mère métal métaux mét navire neige neveu neveux nez noix nuage nuages nuit odeur oiseau oiseaux ombre oncle or orage ordres outils pain panier panneau panneaux papa pape parc parents pastèque pays pêcheur pêcheurs père photo pierre pierres placard plage plante plat pluie plume poire poires pomme pommes pont port porte portes portail poules poussière pré prix printemps pull quai quartier rail rails randonneur recette renard repas rideau rideaux rival rivaux riv rivière robe robes rochers roman romans ronde rose roses rosiers route routes rue ruisseau ruisseaux réponse sable sac sacs salade salle salon sapins sentier sign signal signaux siècles société soir soleil sommet son sortie soupe soupes sourire souris spectacle statue stylo sœur sœurs table tableau tableaux tante tapis tarte tartes tasse taureau taureaux temps tempête tiroir toile toit tortue tour touristes train travail travaux tribunal tribunaux tribun troupeau troupeaux trousse tulipes tuyau tuyaux vacances vache vagues valise vallée vase vent verger verre verres veste village villages ville villes vitrail vitraux vitrine voie voisin voisine voisines voisins voiture voitures voix volcans volets voyage voyageurs végétal végétaux végét vélo vœux vœu yeux zoo écharpes goûter');
const NAT_ADV=mots_('très bien vraiment');
const NAT_LIEN=mots_('de d’ à en');
const natBas=m=>m.toLowerCase().replace(/'/g,'’');
/* mots d'une phrase (« l’ » et « d’ » à part) avec leur place dans le texte */
const natDecouper=txt=>{const r=[],re=/[A-Za-zÀ-ÖØ-öø-ÿœŒ]+(?:-[A-Za-zÀ-ÖØ-öø-ÿœŒ]+)*[’']?|___|[.!?;:()«»→·\/,]/g;let m;
  while((m=re.exec(txt))){const brut=m[0];r.push({m:natBas(brut),brut,d:m.index,f:m.index+brut.length,mot:/^[A-Za-zÀ-ÖØ-öø-ÿœŒ]/.test(brut)});}return r;};
/* nature de chaque mot : 'det', 'nom', 'adj' ou '' (aucun personnage). Un mot n'est un nom qu'à une place de nom (« la porte » oui, « elle porte » non). */
function natures(txt){
  const T=natDecouper(txt), R=T.map(()=>'');
  const suite=i=>{let j=i+1;while(T[j]&&(NAT_ADV.has(T[j].m)||T[j].m==='deux'||T[j].m==='trois'))j++;return T[j];};
  const gn=x=>!!x&&(x.m==='___'||NAT_NOM.has(x.m)||NAT_ADJ.has(x.m)||NAT_PROPRES.has(x.m));
  const avant=i=>{let j=i-1;while(j>=0&&NAT_ADV.has(T[j].m))j--;return j;};
  T.forEach((x,i)=>{ if(!x.mot) return; const m=x.m, j=avant(i), p=j>=0?T[j]:null, pn=j>=0?R[j]:'';
    if(m==='long'&&p&&p.m==='le'&&/^(du|de|des)$/.test((T[i+1]||{}).m||'')){R[j]='';return;}   /* « le long de » */
    const debut=!p||(!p.mot&&p.m!=='___');
    if(NAT_PROPRES.has(m)){R[i]='nom';return;}
    if(NAT_DET.has(m)&&(gn(suite(i))||(T.length===1))){R[i]='det';return;}
    if((m==='de'||m==='d’')){const s=T[i+1],s2=T[i+2];if(s&&NAT_ADJ.has(s.m)&&gn(s2))R[i]='det';return;}
    if(m==='flotte'&&pn!=='det') return;   /* « une barque flotte » : verbe */
    const placeNom=debut||pn==='det'||pn==='adj'||(p&&(NAT_LIEN.has(p.m)||p.m==='___'));
    if(m==='blanc'&&p&&p.m==='en'){R[i]='nom';return;}
    if((m==='bon')&&p&&/^(sent|sentent)$/.test(p.m)) return;
    if(NAT_NOM.has(m)&&NAT_ADJ.has(m)){ const s=T[i+1]; R[i]=(placeNom&&!(s&&NAT_NOM.has(s.m))&&!(pn==='nom'))?'nom':'adj'; if(pn==='adj'&&p&&!(NAT_NOM.has(p.m)))R[i]=(s&&NAT_NOM.has(s.m))?'adj':'nom'; return; }
    if(NAT_ADJ.has(m)){R[i]='adj';return;}
    if(NAT_NOM.has(m)&&placeNom){R[i]='nom';return;}
  });
  return T.map((x,i)=>({mot:x.brut,d:x.d,f:x.f,n:x.mot?R[i]:''}));
}

/* G4, G7 : place de chaque mot d'après la phrase écrite dans la table */
const lettre_=c=>!!c&&/[A-Za-zÀ-ÖØ-öø-ÿœŒ]/.test(c);
function naturesEcrites(txt,ceinture,niveau){
  const plat=txt.replace(/\s/g,' '), ligne=(PERSOS_PHRASES[ceinture]||{})[plat.replace(/ +/g,' ').trim()]; if(!ligne) return [];
  const hors=ceinture==='G4'?(PERSO_HORS[niveau]||[]):[], r=[]; let pos=0;
  ligne.split(' ').forEach(item=>{ const k=item.lastIndexOf(':'); let m=item.slice(0,k); const n=PERSO_TAGS[item.slice(k+1)], libre=m[0]==='~'; m=m.replace('~','').replace(/_/g,' ');
    let d=plat.indexOf(m,pos);
    while(d>=0&&!libre&&(lettre_(plat[d-1])||(!m.endsWith('’')&&lettre_(plat[d+m.length])))) d=plat.indexOf(m,d+1);
    if(d<0) return; pos=d+m.length; if(n&&!hors.includes(n)) r.push({d,f:d+m.length,n}); });
  return r;
}

/* ---- affichage : chaque mot reconnu prend la couleur de sa classe et son personnage dessous ---- */
function persoEmballer(racine,noeudD,offD,noeudF,offF,cl,img){
  let a=noeudD,b=noeudF;
  if(offF<b.data.length) b.splitText(offF);
  if(offD>0){const suite=a.splitText(offD); if(b===a) b=suite; a=suite;}
  let C=a.parentNode; while(!C.contains(b)) C=C.parentNode;
  while(a.parentNode!==C) a=a.parentNode;
  while(b.parentNode!==C) b=b.parentNode;
  /* le mot occupe seul son repère (entouré, étiquette…) : le personnage se place sous le repère entier */
  const texte=()=>{let s='';for(let n=a;n;n=n.nextSibling){s+=n.textContent;if(n===b)break;}return s;};
  while(C!==racine&&C.parentNode&&C.tagName==='SPAN'&&C.textContent.trim()===texte().trim()){a=b=C;C=C.parentNode;}
  const w=document.createElement('span'),t=document.createElement('span'),i=document.createElement('img');
  w.className='mp mp-'+cl; t.className='mp-t'; i.src=img; i.alt=PERSO_NOMS[cl]; i.title=PERSO_NOMS[cl];
  C.insertBefore(w,a); for(let n=a;n;){const s=n===b?null:n.nextSibling;t.appendChild(n);n=s;} w.append(t,i);
}
function persosPoser(el,ceinture,niveau){
  if(!el||!PERSO_CEINT.includes(ceinture)||el.querySelector('.mp')) return;
  const blocs=el.querySelector('.cumul')?[...el.querySelectorAll('.cumul.cur')]:[el];
  blocs.forEach(bloc=>{
    const w=document.createTreeWalker(bloc,NodeFilter.SHOW_TEXT,{acceptNode:n=>n.parentElement.closest('small,.sr-only')?NodeFilter.FILTER_REJECT:NodeFilter.FILTER_ACCEPT});
    let txt='';const P=[];while(w.nextNode()){const n=w.currentNode;P.push([txt.length,n]);txt+=n.data;}
    const ou=(pos,fin)=>{for(let k=P.length-1;k>=0;k--){const [d,n]=P[k];if(fin?d<pos:d<=pos)return [n,pos-d];}return null;};
    (ceinture==='G3'?natures(txt):naturesEcrites(txt,ceinture,niveau||'CM1')).filter(x=>x.n&&persoImg(x.n)).reverse().forEach(x=>{const d=ou(x.d),f=ou(x.f,true);if(d&&f)persoEmballer(bloc,d[0],d[1],f[0],f[1],x.n,persoImg(x.n));});
  });
  if(el.querySelector('.mp')) el.classList.add('avec-persos');
}
function persosRetirer(el){if(el)el.classList.remove('avec-persos');}
