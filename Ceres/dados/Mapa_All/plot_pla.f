c
c programme de trace de fonctions au choix.
c
	INTEGER UNIT,JUST,AXIS
	CHARACTER*150 DEVICE,XLBL,YLBL,TOPLBL
 1000	FORMAT(A)
c
c
	write(*,*) 'tt/gf=console micro-VAX, tt/tek= console VAX, /dw= Xwindow'
	write(*,*) 'toto/ps'
	write(*,*) '/xw: fenetre temporaire'
	write(*,*) '/xserve: fenetre permanente'
	read 1000, device
	write(*,*) 'Nombre de dessins en x et y ?'
	read(*,*)  nx,ny
	unit= 20
	CALL PGBEGIN (UNIT,DEVICE,NX,NY)
	write(*,*)  'Epaisseur du trait ?'
	read(*,*)  iepai
	call pgslw(iepai)
c
	write(*,*)  '1= echelle automatique'
	write(*,*)  '0= pleine page'
c	just=0
	read(*,*)  just

  2	write(*,*)  'axis= -2, pas d''annotation'
	write(*,*)  'axis= -1, cadre seulement'
	write(*,*)  'axis=  0, cadre avec valeurs sur les axes'
	write(*,*)  'axis=  1, tirets sur les axes'
	write(*,*)  'axis=  2, trace une grille'
	write(*,*)  'axis= 10, trace axe des x en logarithmique'
	write(*,*)  'axis= 20, trace axe des y en logarithmique'
	write(*,*)  'axis= 30, trace axe des x et y en logarithmique'	
	read(*,*)  axis

	write(*,*) 'coin inf. gauche et coin sup. droit ? Taille char.?'
	write(*,*) 'Xmin, Ymin'
	write(*,*) 'Xmax, Ymax, taille'
	read(*,*) xmin,ymin
	read(*,*) xmax,ymax, char_size
	call pgsch (char_size)
	call pgenv(xmin,xmax,ymin,ymax,just,axis)
C
	write(*,*) 'LEGENDE EN X,Y ET SOMMET ?'
	READ 1000 ,XLBL
	READ 1000 ,YLBL
	READ 1000 ,TOPLBL
	CALL PGLABEL (XLBL,YLBL,TOPLBL)
	call pgsch (1.)

	write(*,*) 'afficher un tableau en grise?'
	read(*,*)  iop
	if (iop.eq.1) call gris (iepai)

	write(*,*)  'Remplir une surface delimitee par des points?'
	read(*,*)  iop
	if (iop.eq.1) call fill (xmin,ymin,xmax,ymax)
c
c trace de la courbe
c
	write(*,*)  '1= trace d''une courbe'
	write(*,*)  '2= trace de points en perspective'
	read(*,*)  iop
	if (iop.eq.1) call trace (iepai)
	if (iop.eq.2) call points (iepai)
c
c insertion d'un texte
c
	write(*,*)  'Faut-il ecrire des commentaires dans la figure ?'
	read(*,*)  iop
	if (iop.eq.1) then
		call commentaire
	endif
c
c	trace eventuel d'autres graphes
c
	write(*,*) 'Faut-il tracer d''autres graphes ?'
	read(*,*) iop
	if(iop.eq.1) go to 2
c
c Trace du monde
c
	write(*,*)  'Faut-il tracer le monde?'
	read(*,*)  iop
	if (iop.eq.1) call monde(iepai,B,alpha)
c
c Trace de la planete
c
	write(*,*)  'Faut-il tracer la planete ?'
	read(*,*)  iop
	if (iop.eq.1) call planete(iepai,B,alpha)
c
c
c
 1	CALL PGEND
	STOP
	END
c
c                         FIN PROGRAMME PRINCIPAL
c
c
c
c *************************************************************************
c
c sous programme de trace de la courbe
c
	subroutine trace (iepai)
c
	parameter (nmax=1000000)
	dimension x(nmax),y(nmax),xx(nmax),yy(nmax),xxx(2),yyy(2)
	CHARACTER*150, fichier
 1000	format(A)
c
 1	write(*,*) 'Fichier a tracer ?'
	read 1000, fichier
	write(*,*) fichier
	open (unit=22,file=fichier,status='old',form='formatted',err=1)
	write(*,*)  'Lissage sur ? points '
	read(*,*)  ipas
	ipas2= ipas/2

c	write(*,*) 'Decalage horizontal ?'
c	read(*,*)  xshift
c	write(*,*) 'Multiplication horizontale ?'
c	read(*,*)  xfac
c	write(*,*) 'Decalage vertical ?'
c	read(*,*)  yshift
c	write(*,*) 'Multiplication verticale ?'
c	read(*,*)  yfac
	xshift= 0.
	yshift= 0.
	xfac=   1.
	yfac=   1.
c
 	npt= 0
	do i= 1, nmax 
		read(22,*,end=100,err=100) x(i), y(i)
		npt= npt + 1
	enddo
 100	close(22)
	write(*,*)  npt, ' points lus'
c
	k= 0
	do i= 1+ipas2, npt-ipas2, ipas
		som= 0.
		do j= i-ipas2, i+ipas2
			som= som + y(j)
		enddo
		k= k+1
		xx(k)= x(i)*xfac	           + xshift
		yy(k)= (som/float(2*ipas2+1))*yfac + yshift
	enddo
c	write(*,*)  k, ' points moyennes'
c
	write(*,*)  '1= ligne'
	write(*,*)  '2= points'
	read(*,*)  iop
	if (iop.eq.1) then
		write(*,*)  'Style de ligne, epaisseur ligne, couleur?'
		write(*,*)  '1= trait plein'
		write(*,*)  '2= tirets'
		write(*,*)  '3= mixte'
		write(*,*)  '4= pointille'
		write(*,*)  '5= tiret-point-point'
		read(*,*)  ls, iepai_line, icoul
		call pgsls(ls)
		call pgsci(icoul)
		if (iepai_line.ne.0) then 
		 call pgslw(iepai_line)
		 call pgline (k,xx,yy)
		endif
		call pgsls(1)
		call pgslw(iepai)
		call pgsci(1)
	endif
	if (iop.eq.2) then
		write(*,*)  'caracteres, taille carac, taille ligne, couleur ?'
		read(*,*)  icarac, char_size, line_size, icoul
		if (char_size.ne.0) then
		 call pgsci(icoul)
		 call pgsch (char_size)
		 call pgpoint (k,xx,yy,icarac)
		endif
		call pgsch (1.0)
		call pgsci(1)
c
c permet de tracer 2 a 2 des cordes (si k est pair)
c
c NB: on peut prendre line_size = 0 pour ne pas tracer les
c lignes entre les extremites des cordes. Il y aura un message
c d'erreur pgplot, mais le programme ne s'interrompra pas
c
		do j= 1, k-1, 2
			xxx(1)= xx(j  )
			yyy(1)= yy(j  )
			xxx(2)= xx(j+1)
			yyy(2)= yy(j+1)
			if (line_size.ne.0) then 
			 call pgsci(icoul)
			 call pgslw(line_size)
			 call pgline (2,xxx,yyy)
		 	 call pgsci(1)
			endif
			call pgslw(iepai)
		enddo
	endif
c
	write(*,*)  'Faut-il tracer un autre fichier ?'
	read(*,*)  iop
	if(iop.eq.1) go to 1
c
	return
	end
c
c
c				FIN DE TRACE
c
****************************************************************************
c
c sous-programme de trace de la planete
c
c
	subroutine planete(iepai,B,alpha)
c
	dimension xx(73),yy(73)
	pi= acos(-1.)
	rad= pi/180.
c
c parametres d'orientation du graphique
c 
	write(*,*)  'Inclinaison, angle de position, phase, intervalle? (deg)'
	read(*,*)  B_input, p, alpha_input, ipas_angle
	write(*,*)  'Corrections sur la position?'
	read(*,*) du, dv
c
c Pour avoir automatiquement B et P quand on trace une carte d'occultation
c (B et alpha sont calcules dans "monde"). On peut alors mettre, par ex.
c B= 999, P= 999
c	
	if (B_input.le.360.)     B= B_input
	if (alpha_input.le.360.) alpha= alpha_input 
c 
c dans le cas ou on trace la carte du monde, on passe automatiquement
c les valeurs de B et alpha (calcules dans monde), et on prend P= 0.
c
c	p= 0.
c	write(*,*)  'Intervalle entre les paralleles et meridiens? (deg)'
c	read(*,*)  ipas_angle
	b=  rad*b
	p= -rad*p		! ATTENTION AU CHANGEMENT DE SIGNE !
	alpha= -rad*alpha	! ATTENTION AU CHANGEMENT DE SIGNE !
c
	write(*,*) 'Rayon equatorial de la planete et ellipticite?'
	read(*,*)  r_eq, epsilon
	r_po= r_eq*( 1. - epsilon )
c
	write(*,*)  'style et epaisseur du trait?'
	write(*,*)  '1= trait plein'
	write(*,*)  '2= tirets'
	write(*,*)  '3= mixte'
	write(*,*)  '4= pointille'
	write(*,*)  '5= tiret-point-point'
	read(*,*)  ls, iepai_line
	call pgsls(ls)
	if(iepai_line.ne.0) call pgslw(iepai_line)
c
	cosb= cos(b)
	sinb= sin(b)
c
c sert pour le test de visibilite:
c
	cosbp=((r_po**2)*cosb)/sqrt((r_eq**4)*(sinb**2) + (r_po**4)*(cosb**2))
	sinbp=((r_eq**2)*sinb)/sqrt((r_eq**4)*(sinb**2) + (r_po**4)*(cosb**2))
	bp   = atan(sinbp/cosbp)
	if (cosbp.le.0.) bp= bp + pi
	write(*,*)  'Latitude maximale observable (deg):', 90. - abs(bp/rad)
c
	cosp= cos(p)
	sinp= sin(p)
	cosa= cos(alpha)
	sina= sin(alpha)
c
c trace des paralleles
c
	do 1 i= -90, 90, ipas_angle
	teta= rad*float(i)
	rp  = 1./sqrt( (cos(teta)/r_eq)**2 + (sin(teta)/r_po)**2  )
	cost= rp*cos(teta)
	sint= rp*sin(teta)
c
	l=0
	do 2 j=	0, 360, 1
	phi= rad*float(j)
	cosphi= cos(phi)
	sinphi= sin(phi)
c
c coordonnees du point courant
c
	x= cosphi*cost
	y= sinphi*cost
	z=        sint
c
c test  de visibilite du point
c
	visible= ( x*cosa + y*sina )*cosbp + z*sinbp
c
c projection sur le plan de l'observateur
c
	u=   -x*sina + y*cosa
	v= -( x*cosa + y*sina )*sinb + z*cosb
c (rotation de P)
	up= u*cosp - v*sinp + du
	vp= u*sinp + v*cosp + dv
c
	if(visible.gt.0.) go to 3
	l= 0
	go to 2
 3	if(l.eq.1) go to 4
	xx(1)= up 
	yy(1)= vp 
 4	xx(2)= up 
	yy(2)= vp 
	if (i.eq.0) then		! equateur plus epais
	  if(iepai_line.ne.0) call pgslw(3*iepai_line)
	endif
	if (iepai_line.ne.0) then
	   ifac= (i-90)*(i+90) 
	   if (ifac.ne.0) call pgline (2,xx,yy)	! ne pas tracer le pole
	endif
	if (iepai_line.ne.0) call pgslw(iepai_line)	! on revient a l'epaisseur courante
	xx(1)= up
	yy(1)= vp
	l= 1
 2	continue
c
 1	continue
c
c
c trace des meridiens
c 
	do 5 i= 0, 359, ipas_angle
	phi= rad*float(i)
	cosphi= cos(phi)
	sinphi= sin(phi)
c
	l=0
	do 6 j=	-90+ipas_angle, 90-ipas_angle, 1
	teta= rad*float(j)
	rp  = 1./sqrt( (cos(teta)/r_eq)**2 + (sin(teta)/r_po)**2  )
	cost= rp*cos(teta)
	sint= rp*sin(teta)
c
c coordonnees du point courant
c
	x= cosphi*cost
	y= sinphi*cost
	z=        sint
c
c test  de visibilite du point
c
	visible= ( x*cosa + y*sina )*cosbp + z*sinbp
c
c projection sur le plan de l'observateur
c
	u=   -x*sina + y*cosa
	v= -( x*cosa + y*sina )*sinb + z*cosb
c (rotation de P)
	up= u*cosp - v*sinp + du
	vp= u*sinp + v*cosp + dv
c
	if(visible.gt.0.) go to 7
	l= 0
	go to 6
 7	if(l.eq.1) go to 8
	xx(1)= up 
	yy(1)= vp 
 8	xx(2)= up 
	yy(2)= vp 
	if (i.eq.0) then		! meridien Greenwich plus epais
	  if (iepai_line.ne.0) call pgslw(3*iepai_line)
	endif
	if (iepai_line.ne.0) call pgline (2,xx,yy)
	if (iepai_line.ne.0) call pgslw(iepai_line)	! on revient a l'epaisseur courante
	xx(1)= up
	yy(1)= vp
	l= 1
 6	continue
c
 5	continue
c
c
c trace du limbe
c
c calcul du demi grand-axe apparent
c
	r_po_app= sqrt( (r_eq*sinb)**2 + (r_po*cosb)**2 )
	write(*,*)  'Rayon polaire apparent:', r_po_app
	write(*,*)  'Aplatissement apparent:', (r_eq - r_po_app)/r_eq

	k= 0
	do 9 i= 5,365,5
		phi= rad*float(i)
		rp = 1./sqrt( (cos(phi)/r_eq)**2 + (sin(phi)/r_po_app)**2  )
		xxx    = rp*cos(phi)
		yyy    = rp*sin(phi)
		k= k+1
		xx(k)= xxx*cosp - yyy*sinp + du
	        yy(k)= xxx*sinp + yyy*cosp + dv
 9	continue
c
	if (iepai_line.ne.0) call pgline (k,xx,yy)
c
	write(*,*)  '1= trace d''un cercle'
	read(*,*)  iop
	if (iop.eq.1) then
		write(*,*)  'Combien de cercles ?'
		read(*,*)  ncercle
		do i= 1, ncercle
			write(*,*)  'Rayon et centre? #', i
			read(*,*)  R, xcentre, ycentre
			call cercle (R,xcentre,ycentre,iepai)
		enddo
	endif
c
	write(*,*)  '1= trace d''anneaux'
	read(*,*)  iop
	if (iop.eq.1) then
		call anneaux (b,p,alpha,r_eq,epsilon,du,dv)
	endif
c
c
c
	call pgsls(1)
	call pgslw(iepai)		! on revient aux valeurs generales
	return
	end
c
c
c				FIN DE PLANETE
c
c *************************************************************************
c
	subroutine cercle(R,du,dv,iepai)
c
c Trace d'un cercle de rayon R
c
	dimension x(1000), y(1000)
c
	pi= 4.*atan(1.)
	rad= pi/180.
	pas= 0.5
	npt= 360/pas + 1
c
	do i= 1, npt
		phi= rad*pas*float(i-1)
		x(i)= R*cos(phi) + du
		y(i)= R*sin(phi) + dv 
	enddo
c
	write(*,*) 'Style? Epaisseur? Couleur?'
	read(*,*)  ls, iepai_line, icoul	
	call pgsls(ls)
	if (iepai_line.ne.0) then		
	  call pgslw(iepai_line)
	  call pgsci(icoul)
	  call pgline (npt,x,y)
	endif
	call pgsls(1)
	call pgslw(iepai)
	call pgsci(1)
c
c
c
	return
	end
c
c
c 				FIN DE  CERCLE
c
c ***********************************************************************
c
c sous-programme de trace d'anneaux
c
	subroutine anneaux (b,p,alpha,r_eq,epsilon,du,dv)
c
	dimension xx(72),yy(72)
c
	pi= acos(-1.)
	rad= pi/180.
	r_po= r_eq*(1.-epsilon)

c	write(*,*) 'Faut-il changer les parametres angulaires ?'
c	read(*,*)  iop
c	if (iop.eq.1) then
c		write(*,*) 'Inclinaison, position et phase ? (degres)'
c		read(*,*)  ba,pa,alphaa
c		ba= rad*ba
c		pa= rad*pa
c		alphaa= rad*alphaa
c	else
c		ba= b
c		pa= p
c		alphaa= alpha
c	endif

	ba= b
	pa= p
	alphaa= alpha

	cosb= cos(ba)
	sinb= sin(ba)
	cosp= cos(pa)
	sinp= sin(pa)
	cosa= cos(alphaa)
	sina= sin(alphaa)
	r_po_app= sqrt( (r_eq*sinb)**2 + (r_po*cosb)**2 )
c
c	write(*,*) 'Anneaux ou arcs ?'
c	write(*,*) '1= anneaux'
c	write(*,*) '2= arcs'
c	read(*,*) iring
	iring= 1
	if(iring.eq.1) write(*,*) 'Nombre d''anneaux a tracer ?'
	if(iring.eq.2) write(*,*) 'Nombre d''arcs a tracer ?'
	read(*,*)  npt
c
	do 1 k= 1,npt
	write(*,*) 'Rayon de l''anneau no',k,'?'
	read(*,*)  r
c
	i1= 0
	i2= 360
	ipas= 1
	if (iring.eq.1) go to 5
	if (iring.eq.2) write(*,*) 'Azimuts de depart et de fin, pas ? (deg.)'
	read(*,*) i1,i2,ipas
 5	l= 0
	do 2 i= i1,i2,ipas
		phi= rad*float(i)
		x= r*cos(phi)
		y= r*sin(phi)
		z= 0.

		u=   -x*sina + y*cosa
		v= -( x*cosa + y*sina )*sinb + z*cosb
c
c permet de savoir si le point est au-dela du limbe APPARENT
c
		discri= (u/r_eq)**2 + (v/r_po_app)**2 - 1.
c
c projection plan du ciel (attention P a ete change de signe dans planete!)
c
		up= u*cosp - v*sinp
		vp= u*sinp + v*cosp

		if( (discri.ge.0.).or.((v*sinb).lt.0.) ) go to 3
		l=0
		go to 2
 3		if(l.eq.1) go to 4
		xx(1)= up + du
		yy(1)= vp + dv
 4		xx(2)= up + du
		yy(2)= vp + dv
		call pgline(2,xx,yy)
		xx(1)= up + du
		yy(1)= vp + dv
		l=1
 2	continue
c
 1	continue
c
c
c
	return
	end
c
c				fin de anneaux
c ***********************************************************************
c
c Sous-programme d'insertion d'un texte dans la figure. x et y sont les
c coordonnees dans l'echelle du cadre
c
c
	subroutine commentaire
c
 1000	format(a)
	CHARACTER*150 texte
c
 1	write(*,*)  'Position du texte ? Taille? Couleur? Rotation?'
	read(*,*)  x,y, char_size, icoul, angle
c
	write(*,*)  'Texte ?'
	read 1000, texte
c
	call pgsch (char_size)
c	call pgtext (x,y,texte)
	if (char_size.ne.(0.)) then 
	 call pgsci(icoul)
	 call pgptext (x,y,angle,0.,texte)
	 call pgsci(1)
	endif
	call pgsch (1.0)
c
	write(*,*)  'Autre commentaire ?'
	read(*,*)  iop
	if (iop.eq.1) go to 1
c
c
c
	return
	end
c
c				fin de commentaire
c ************************************************************************
c
c sous-programme de trace de points en perspective
c
	subroutine points(iepai)
	parameter (nptmax=10000000) 
	dimension xx(nptmax), yy(nptmax)
 1000	format(A)
	CHARACTER*150 fichier
c
	pi= acos(-1.)
	rad= pi/180.
c
c parametres d'orientation du graphique
c
	write(*,*) 'Inclinaison, angle de position, phase? (deg., 1 ligne)'
	read(*,*)  b,p,alpha
	b=  rad*b
	p= -rad*p
	alpha= rad*alpha
c
	cosb= cos(b)
	sinb= sin(b)
	cosp= cos(p)
	sinp= sin(p)
	cosa= cos(alpha)
	sina= sin(alpha)
c
 1	write(*,*) 'Fichier a tracer ?'
	read 1000, fichier
	open (unit=23,file=fichier,status='old',form='formatted',err=1)
	k= 0
	do i= 1, 200000
		read (23,*,err=2,end=2) x, y, z
		k= k + 1
		u=   -x*sina + y*cosa
		v= -( x*cosa + y*sina )*sinb + z*cosb
		xx(k)= u*cosp - v*sinp
		yy(k)= u*sinp + v*cosp
	enddo
 2	close (23)
	write (*,*) k, ' points lus'
c
	write(*,*)  '1= ligne'
	write(*,*)  '2= points'
	read(*,*)  iop
	if (iop.eq.1) then
 		write(*,*)  'Style de ligne, epaisseur ligne, couleur?'
		write(*,*)  '1= trait plein'
		write(*,*)  '2= tirets'
		write(*,*)  '3= mixte'
		write(*,*)  '4= pointille'
		write(*,*)  '5= tiret-point-point'
		read(*,*)  ls, iepai_line, icoul	
		call pgsls(ls)
		if (iepai_line.ne.0) then		
		 call pgslw(iepai_line)
		 call pgsci(icoul)
		 call pgline (k,xx,yy)		 
		endif
		call pgsls(1)
		call pgslw(iepai)
		call pgsci(1)
	endif

	if (iop.eq.2) then
		write(*,*)  'caracteres, taille, couleur?'
		read(*,*)  icarac, char_size, icoul
		call pgsch (char_size)
		if (char_size.ne.0) then
		 call pgsci(icoul)
		 call pgpoint (k,xx,yy,icarac)
		endif
	endif
	call pgsch (1.0)
	call pgsci(1)
c
	write(*,*)  'Faut-il tracer une autre fichier ?'
	read(*,*)  iop
	if (iop.eq.1) go to 1

	return
	end
c
c ********************** FIN DE POINTS **************************

	subroutine gris (iepai)
c
	parameter (imax=1001,jmax=1001) 	! dimension du tableau gris'e
	parameter (nlevel_max=100)			! nombre de lignes de niveaux
	dimension A(imax,jmax), tr(6), alev(nlevel_max)
 1000   format(A)
	CHARACTER*150 fichier

c
c Initialisation du tableau A
c
	do i= 1, imax
		do j= 1, jmax
			A(i,j)= 0.
		enddo
	enddo

	write(*,*) 'Fichier a lire?' 
	read 1000, fichier
	open (unit=23,file=fichier,status='old',form='formatted',err=1)
 1	continue		! permet de continuer si erreur fichier

	write(*,*) 'Dimension en x, en y?'
	read(*,*) idim, jdim 
	write(*,*) 'xmin, ymin, xmax, ymax?' 
	read(*,*) xmin, ymin, xmax, ymax

	pasx= (xmax-xmin)/float(idim-1)
	pasy= (ymax-ymin)/float(jdim-1)

	tr(2)= pasx
	tr(1)= xmin - tr(2)
	tr(6)= pasy
	tr(4)= ymin - tr(6)
	tr(3)= 0.
	tr(5)= 0.

	write(*,*) 'Valeur du noir, du blanc?' 
	read(*,*)  black, white
	
	do i= 1, idim
	 do j= 1, jdim
	  read (23,*,err=2,end=2) A(i,j)
	 enddo
	enddo
	close(23)
 2	continue
	
	i1= 1
	i2= idim
	j1= 1
	j2= jdim

c
c Trace du tableau en grise:
c
	call pggray (A,imax,jmax,i1,i2,j1,j2,black,white,tr)
c
c Trace des courbes de niveaux (isophotes)
c 

c Definit les niveaux a tracer, ici nlevel niveaux entre "black" et "white"

	write (*,*) 'Niveaux min et max, nombre d''isophotes, epaisseur, couleur?'
	read (*,*) alev_min, alev_max, nlevel, lw, icol
	
	do i= 1, nlevel
	 alev(i)= alev_min + float(i-1)*(alev_max-alev_min)/float(nlevel-1)
	enddo

	call pgslw (lw)
	call pgsci (icol)
	if (lw.ne.0) call pgcont (A,imax,jmax,i1,i2,j1,j2,alev,nlevel,tr) 
c
c NB. on peut tracer aussi les isophotes a partir d'un niveau donne
c Par ex. pour tracer les niveaux alev(6),...alev(10):
c call pgcont (A,imax,jmax,i1,i2,j1,j2,alev(6),5,tr)
c	
	call pgsci (1)			! retour au noir
	call pgslw (iepai)		! on revient a l'epaisseur generale

	return
	end

************************************ fin de gris ***************************

	subroutine fill (xg,yg,xd,yd)

c
c  Ce programme remplit de gris les points a l'interieur de la courbe
c  fermee f(1), g(1) .... f(i), g(i) .... f(npt), g(npt). On referme
c  la courbe par f(npt), g(npt) = f(1), g(1). D'autre part, on pose
c  f(0), g(0) = f(npt), g(npt) pour certains tests, le cas echeant.
c
c  idim, jdim: dimensions du tableau A(i,j) qui va etre affiche. Les
c  pas de la grille sont donc de Df/(idim-1) et Dg/(jdim-1), ou Df et Dg
c  sont les extensions maximales en f et g des points.
c
	parameter (idimax=501,jdimax=501) 	! dimension du tableau gris'e
	parameter (Nfich_max=10) 		! nombre max de fichiers lus
        dimension f(Nfich_max,0:10000), g(Nfich_max,0:10000)
	dimension npt(Nfich_max)
	dimension xx(1000), A(idimax,jdimax), tr(6)
	dimension xcont(10000), ycont(10000)
 1000   format(A)
        CHARACTER*150 fichier

c-------------------------------------------------------------------------------
c Lecture des fichiers
c-------------------------------------------------------------------------------
	write(*,*)  'Nombre de fichiers a lire? (< a', Nfich_max,')'
	write(*,*)  'et dimension (pixels en i et j) de la zone grisee'
	read(*,*)  Nfich, idim, jdim

c-------------------------------------------------------------------------------
c Contraste
c-------------------------------------------------------------------------------
	write(*,*)  'Contraste?'
	read(*,*)  contraste
	white= 0.
	black= 1.
c	black= 1./contraste

c
c Initialisation du tableau A
c
	do i= 1, idimax
		do j= 1, jdimax
			A(i,j)= 0.
		enddo   
	enddo

	do k= 1, Nfich
 1       write(*,*) 'Fichier #', k,'?'
         read 1000, fichier
         open (unit=23,file=fichier,status='old',form='formatted',err=1)

	 npt(k)= 0
	 nmax= 10000
	 do i= 1, nmax
		read (23,*,err=2,end=2) f(k,i), g(k,i)
		npt(k)= npt(k) + 1
	 enddo
 2	 continue
	 close(23)
	if (npt(k).eq.nmax) write(*,*)
     *  'ATTENTION: tous les points ne sont pas lus!'

c-------------------------------------------------------------------------------
c Calcul des min et max en f et g (taille de la boite)
c-------------------------------------------------------------------------------
	 f(k,0)=     f(k,npt(k))
	 g(k,0)=     g(k,npt(k))
	 f(k,npt(k)+1)= f(k,1)
	 g(k,npt(k)+1)= g(k,1)

	enddo

	xmin= f(1,1)
	xmax= f(1,1)
	ymin= g(1,1)
	ymax= g(1,1)
	do k= 1, Nfich
		do i= 2, npt(k)
			if (f(k,i).le.xmin) xmin= f(k,i)
			if (f(k,i).ge.xmax) xmax= f(k,i)
			if (g(k,i).le.ymin) ymin= g(k,i)
			if (g(k,i).ge.ymax) ymax= g(k,i)
		enddo
	enddo
c-------------------------------------------------------------------------------
c Calcul des min et max du cadre
c-------------------------------------------------------------------------------
	if (xg.lt.xd) then
		xcadre_min= xg
		xcadre_max= xd
	endif
	if (xg.gt.xd) then
		xcadre_min= xd
		xcadre_max= xg
	endif
	if (yg.lt.yd) then
		ycadre_min= yg
		ycadre_max= yd
	endif
	if (yg.gt.yd) then
		ycadre_min= yd
		ycadre_max= yg
	endif
	delta_x= xcadre_max - xcadre_min
	delta_y= ycadre_max - ycadre_min

c-------------------------------------------------------------------------------
c Calcul de l'intersection de la boite des donnees et du cadre
c-------------------------------------------------------------------------------
	epsilon= 0.01
	if (xmin.lt.xcadre_min) xmin= xcadre_min + epsilon*delta_x
	if (xmax.gt.xcadre_max) xmax= xcadre_max - epsilon*delta_x
	if (ymin.lt.ycadre_min) ymin= ycadre_min + epsilon*delta_y
	if (ymax.gt.ycadre_max) ymax= ycadre_max - epsilon*delta_y

	if (xmin.gt.xmax) return ! la boite est a l'exterieur du cadre
	if (ymin.gt.ymax) return ! la boite est a l'exterieur du cadre

	pasx= (xmax-xmin)/float(idim-1)
	pasy= (ymax-ymin)/float(jdim-1)

	tr(2)= pasx
	tr(1)= xmin - tr(2)
	tr(6)= pasy
	tr(4)= ymin - tr(6)
	tr(3)= 0.
	tr(5)= 0.

c-------------------------------------------------------------------------------
c On balaie en x et y pour determiner les points a l'interieur de la surface
c-------------------------------------------------------------------------------
	do kf= 1, Nfich			! explore les fichiers un par un

	do j= 1, jdim
		y= ymin + float(j-1)*pasy
		k= 0

c-------------------------------------------------------------------------------
c On cherche les segments qui ont une intersection avec y= cste
c-------------------------------------------------------------------------------
		do i= 1, npt(kf)
		  fac= ( y-g(kf,i) )*( y-g(kf,i+1) )
		  denom= g(kf,i+1)-g(kf,i)	     ! evite les segments horizontaux
		  if ((fac.le.0.).and.(denom.ne.0.)) then
		   k= k+1
		   xx(k)= f(kf,i) + ((f(kf,i+1)-f(kf,i))/denom)*(y-g(kf,i))
		  endif
		enddo

c-------------------------------------------------------------------------------
c On balaie en x (y=cste), pour chercher les points internes
c-------------------------------------------------------------------------------
		do i= 1, idim
		  x= xmin + float(i-1)*pasx
		  prod= 1.
		  do L= 1, k
		    prod= sgn(x-xx(L))*prod
		  enddo

		  if (prod.le.0.) then
			A(i,j)= contraste + A(i,j) ! point interne
		  else
			A(i,j)=        0. + A(i,j) ! point externe
		  endif

		enddo			! fin balayage en x
	enddo				! fin balayage en y

	enddo				! fin de la boucle sur les fichiers

	i1= 1
	i2= idim
	j1= 1
	j2= jdim

	call pggray (A,idimax,jdimax,i1,i2,j1,j2,black,white,tr)

c
c On trace le contour de chaque fichier
c
	do k= 1, Nfich
		do i= 1, npt(k)+1
			xcont(i)= f(k,i-1)
			ycont(i)= g(k,i-1)
		enddo
c		call pgline (npt(k)+1,xcont,ycont)
	enddo

	return
	end

************************************ fin de fill ***************************

	function sgn(x)

	if (x.lt.0.) sgn= -1.
	if (x.eq.0.) sgn=  0.
	if (x.gt.0.) sgn=  1.

	return
	end
************************************ fin de sgn  ***************************
c
c Sous-programme de calcul du Jour Julien.
c
c	Entree: jj/mm/aa (date).
c	Sortie: ajd (jour julien),
c		hs (temps sideral a 00 T.U. du jour).
c
	subroutine ajulien(jj,mm,aa,heure, ajd,hs,hsh)
c
c
	implicit real*8 (a-h,o-z)
	dimension nj(12)
	integer*4 aa
c
c Nombre de jours dans chaque mois
c
	nj(1)=  31
	nj(2)=  28
	if( mod(aa,4  ).eq.0 ) nj(2)=  29 ! annees bissextiles normales
	if( mod(aa,100).eq.0 ) nj(2)=  28 ! les siecles ne sont pas bissextiles
	if( mod(aa,400).eq.0 ) nj(2)=  29 ! les 4-siecles sont bissextiles
	nj(3)=  31
	nj(4)=  30
	nj(5)=  31
	nj(6)=  30
	nj(7)=  31
	nj(8)=  31
	nj(9)=  30
	nj(10)= 31
	nj(11)= 30
	nj(12)= 31
c
c Nombre de jour ecoules depuis le 1 er janvier 1950 (00 h T.U.) au 1 er 
c janvier de l'annee "aa" (00 h T.U.).
c
	jd= 0
c
c Annee 1950
c
	if (aa.eq.1950) jd= 0
c
c Annees apres 1950
c
	if (aa.gt.1950) then 
	 do i= 1950, aa-1
	  nbrj= 365
	  if( mod(i,4  ).eq.0 ) nbrj= 366 ! annees bissextiles normales
	  if( mod(i,100).eq.0 ) nbrj= 365 ! les siecles ne sont pas bissextiles
	  if( mod(i,400).eq.0 ) nbrj= 366 ! les 4-siecles sont bissextiles
	  jd= jd + nbrj
	 enddo
	endif
c
c Annees avant 1950
c
	if (aa.lt.1950) then 
	 do i= aa, 1949
	  nbrj= -365
	  if( mod(i,4  ).eq.0 ) nbrj= -366 ! annees bissextiles normales
	  if( mod(i,100).eq.0 ) nbrj= -365 ! les siecles ne sont pas bissextiles
	  if( mod(i,400).eq.0 ) nbrj= -366 ! les 4-siecles sont bissextiles
	  jd= jd + nbrj
	 enddo
	endif
c
c Nombre de jours ecoules depuis le 1 er janvier 1950 (00 h T.U.) jusqu'au
c jour "jj mm aa" (00 h T.U.).
c
	do 2 i= 1, mm-1
 2	jd= jd + nj(i)
c
	jd= jd + jj - 1
c
c Jour Julien au jour "jj mm aa" a 00 h T.U.
c
	ajd= dfloat(jd) + 2433282.5
c
c Heure siderale au jour "jj mm aa" a 00 h T.U.
c On prend pour reference l'heure siderale au 1 er janvier 1985 a 00 h T.U.
c ---> changee pour le 1er janvier 2000 a 00h TU le 7 aout 2006
c
	rapp= 0.99726956633602776
c	ihhs0= 6
c	mms0=  42
c	secs0= 21.9674
	ihhs0= 6		! from JPL Horizons
	mms0=  39
	secs0= 51.8041	
	
	ts0= ( 3600.*dfloat(ihhs0) + 60.*dfloat(mms0) + secs0 )/3600.
c
c Heure siderale a 0h du jour, a Greenwich
c
c	djd= ajd - 2446066.5
	djd= ajd - 2451544.5
	hs= djd/rapp
	unite= 1.
	hs= dmod(hs,unite)
	hs= hs*24. + ts0
	unite= 24.
	hs= dmod(hs,unite)
	if (hs.lt.0.) hs= hs + 24.
c
c Heure siderale l'heure courante "heure" a Greenwich
c
	hsh= hs + heure/rapp
	hsh= dmod(hsh,unite)
	if (hsh.lt.0.) hsh= hsh + 24.
c
c
c
	return
	end
c
c
c			FIN DE AJULIEN
c
c
c **********************************************************************
c
      subroutine dms(heure, ihh,imn,sec)
c
c	ce sous-programme transforme l'heure decimale
c	'heure' en heure, minute, seconde: ihh:imn:sec.
c
      implicit real*8 (a-h,o-z)
c
      ihh= int(heure)
      amn= (heure - dfloat(ihh))*60.
      imn= int(amn)
      sec= (amn - dfloat(imn))*60.
c
	if(heure.lt.0.and.ihh.ne.0) then
		imn= iabs(imn)
		sec= dabs(sec)
	endif
c
c
c
      return
      end
c
c				FIN DE DMS
c
c ************************************************************************

	subroutine monde(iepai,lat_s,lon_s)

	dimension x(1000),y(1000)
	CHARACTER*150, fichier
	real*4 lon, lat, lon_s, lat_s
	real*8 ajd, heure,hs,hsh,sss
	integer*4 aa
 1000	format(A)
	pi=  acos(-1.e0)
	rad= pi/180.e0
	R=   6378.
c
 	write(*,*) 'Fichier contenant le monde?'
	read 1000, fichier
	open (unit=22,file=fichier,status='old',form='formatted',err=1)
	go to 2
1	write(*,*) 'Le fichier contenant le monde n''a pas pu etre ouvert!!!!'
2	continue

	write(*,*)  'Date? (jj mm aa)'
	read(*,*)  jj, mm, aa
	write(*,*)  'Heure? (UT, hh mn sec)'
	read(*,*)  ihh, imn, sec
	heure= dfloat(ihh) + dfloat(imn)/60.d0 + sec/3600.d0

	call ajulien(jj,mm,aa,heure, ajd,hs,hsh)
	call dms(hs, ihh,imn,sss)
	write(*,*)  'Jour julien a Oh et temps sideral a Greenwich:'
	write(*,*)  ajd, ihh, imn, sss
	call dms(hsh, ihh,imn,sss)
	write(*,*)  'Heure siderale a Greenwich a l''heure courante:'
	write(*,*)  ihh, imn, sss

	write(*,*)  'Coordonnees du jour de la direction d''observation?'
	write(*,*)  'hh   mn  sec'
	write(*,*)  'deg amn asec'
	read(*,*)  ihh, imn, sec
	alpha= dfloat(ihh) +  dfloat( imn)/60.d0 +  sec/3600.d0
	lon_s= alpha - hsh
	lon_s= lon_s*15.0

	read(*,*)  ideg, iamn, asec
	if (ideg.lt.0) then
		iamn= -iamn
		asec= -asec
	endif
	if (ideg.eq.0) then
		write(*,*)  'ATTENTION! degre nul'
	endif
	lat_s= float(ideg) + float(iamn)/60.e0 + asec/3600.e0
	cos_lat= cos(lat_s*rad)
	sin_lat= sin(lat_s*rad)

	write(*,*)  'Longitude et latitude sub-terrestre (deg):'
	write(*,*)  '(longitude positive vers l''est)'
	write(*,*)  lon_s, lat_s

	nmax= 120000
	do j= 1, nmax
		read (22,*,end=99,err=99) ibloc, npt
		do i= 1, npt
			read(22,*,end=99,err=99) ix, iy
			lon= (float(ix)/90. - lon_s)*rad
			lat= (float(iy)/90.        )*rad
			xx= sin(lon)*cos(lat)
			yy=          sin(lat)
			zz= cos(lon)*cos(lat)
			yyy= -zz*sin_lat + yy*cos_lat
			zzz=  zz*cos_lat + yy*sin_lat
			x(i)= -R*xx ! signe - pour question d'orientation
			y(i)=  R*yyy
		enddo
		if(zzz.ge.0.) then
			call pgline (npt,x,y)
		endif
	enddo
 99	continue
	close (22)

	npt= 0
	do i= 1, 361
		phi= float(i)*rad
		x(i)= R*cos(phi)
		y(i)= R*sin(phi)
		npt= npt + 1
	enddo
	call pgline (npt,x,y)

	write(*,*)  'Tracer les cercles d''iso-elevation?'
	read(*,*)  iop
	if (iop.eq.1) then
		call pgsci(3)				! en vert
		call pgsls(1)				! ligne continue
		do k= 10, 90, 10
			elev= float(k)*rad
			R_elev= R*cos(elev)
			npt= 0
			do i= 1, 361
				phi= float(i)*rad
				x(i)= R_elev*cos(phi)
				y(i)= R_elev*sin(phi)
				npt= npt + 1
			enddo
			call pgline (npt,x,y)
		enddo
		call pgsls(1)				! retour defaut 
		call pgsci(1)				! retour defaut
	endif

	write(*,*)  'Faut-il tracer des sites particuliers?'
	read(*,*)  iop
	if (iop.eq.1) then
 	  write(*,*) 'Fichier contenant les coordonnes des sites?'
	  write(*,*) '(Lat= deg:mn:sec N, long= deg:mn:sec positive W)'
	  write(*,*) 'Attention, noter -01 -55 -23.1 une coord. negative'
	  read 1000, fichier
	  open (unit=23,file=fichier,status='old',form='formatted',err=97)
	  go to 96
 97	  write(*,*) 'Le fichier contenant les sites n''a pas pu etre ouvert!!!!'
 96	  write(*,*)  'Caracteres a tracer, taille, couleur?'
	  read(*,*)  icarac, char_size, icoul

	  nsite= 0
	  do i= 1, 1000
		read(23,*,end=98,err=98) ideg_lat, mn_lat, sec_lat
	        lat= float(ideg_lat) + float(mn_lat)/60. + sec_lat/3600.
		lat= lat*rad
		read(23,*,end=98,err=98) ideg_lon, mn_lon, sec_lon
		read(23,*,end=98,err=98) altitude
		read(23,*,end=98,err=98) ih_imm, imn_imm, sec_imm
		read(23,*,end=98,err=98) ih_eme, imn_eme, sec_eme
		read(23,*,end=98,err=98)
		lon= float(ideg_lon) + float(mn_lon)/60. + sec_lon/3600.
		lon= -lon     ! attention, mes longitude augmentent vers
			      ! l'ouest, contrairement a la carte du monde
		lon= (lon - lon_s)*rad
		xx= sin(lon)*cos(lat)
		yy=          sin(lat)
		zz= cos(lon)*cos(lat)
		yyy= -zz*sin_lat + yy*cos_lat
		zzz=  zz*cos_lat + yy*sin_lat
		x(1)= -R*xx    ! signe - pour question d'orientation
		y(1)=  R*yyy
		call pgsch (char_size)	
		call pgsci(icoul)
		if (zzz.ge.0.) call pgpoint (1,x,y,icarac)
		call pgsch (1.0)
		call pgsci(1)
		nsite= nsite + 1
	  enddo
  98      continue
	  close(23)
	  write(*,*)  nsite, ' sites portes sur la carte'
	endif
	
	return 
	end
************************************ fin de monde **************************	






