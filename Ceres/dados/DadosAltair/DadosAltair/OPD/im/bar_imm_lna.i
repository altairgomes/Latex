-1		! -1: immersion, +1= emersion, 0: milieu de la bande
1		! reponse instrumentale
impul_lna.dat
1		! courbe de lumiere a ajuster: 
data_ratio_poly_out_CUTim
0.006		! sigma des observations	usar o polyfit
0.75      0.2	! lambda, dlambda (microns)		CONFIRMER!
343144041.66042966d0   0.06	! dist, R etoile (km)
4.		! v_perp (km/sec)            A CALCULER!!!!
1000. 0.	! largeur bande (km) et transmission   ???
100. 0.05	! duree, pas (sec)
1 0.944         ! flux hors occn, flux stellaire zero	CONFIRMER!
81450.3         ! t0 de reference (sec UT)
1 0.05         ! nombre d'heures a explorer autour de t0 et pas (sec)



81450           ! t0 de reference (sec UT)
50 0.05		! nombre d'heures a explorer autour de t0 et pas (sec)

i 81449.75
m 81450.3
f81450.85

dif 1.1s
