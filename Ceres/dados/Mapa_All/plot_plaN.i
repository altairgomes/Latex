Ceres_all.ps/cps
1 1 (pour creer .ps remplacer /xserve par file.ps/cps) [cps=color ps, sinon ps] [vps ou vcps pour portrait]
3
1
0
800  -600	   x1 y1
-800  600   1.2   taille caract.   x2 y2
\fr f\dc\u (km)
\fr g\dc\u (km)
\fr Ceres, 17 August 2010
0
0
1 (ci dessous : fort.21 pour decale, fort.51 pour limbe elliptique, fort_new.23 pour corrig)
fort.21neg
1
2           caractere (si point 2 de data 4 param, si ligne 1, 3 param)
1 1 2 3     caract, taille_car, epaiss_lin(entier), couleur
1
1           autre fichier?
fort.21mid
1
2 
1 2 15 2 
1
1           autre fichier?
fort.21err
1
2 
1 1 15 2 
1
1           autre fichier?
fort.21all
1
2 
1 1 6  4 
1
fort.51nom
1
1
1 4 14       type_ligne, epaiss_lin(entier), couleur
0
1
0 0 1.5 1 0   si commentaire : centre, taille car, couleur, angle en deg du txt - fr : font roman
\fr
1
700 00 1.5 1 0
E
1
00 500 1.5 1 0
N
1
-500 -400 5 1 205
\(2263)
1
-600 450 1 1 0
CEAMIG
1
-600 330 1 1 0
LNA
1
-600 260 1 1 0
INPE
1
-600 -150 1 1 0
UEPG
0
0
0
0                   on veut la planete
-20 10.0 0.8 30     lat pt sub-terr, angl pos N (en passant par E), phase (meridien 0), pas long-lat
-2641.5 -1212.5     offset en ksi et eta
558 -0.016          rayon aplatiss
1 1                 style, epaisseur (equateur 3x)
0
0
0
