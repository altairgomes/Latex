I/???     Catalog of satellites positions
          (Gomes-Júnior+, 2015)
================================================================================
          Astrometric positions for 18 irregular satellites of giant planets
          from 23 years of observations
          Gomes-Júnior A.R., Assafin M., Vieira Martins R., Arlot J.-E.,
          Camargo J.I.B., Braga-Ribas F., da Silva Neto D.N., Andrei A.H.,
          Dias-Oliveira A., Morgado B.E., Benedetti-Rossi G., Duchemin Y.,
          Desmars J., Lainey V., Thuillot W.
         <Astron. Astrophys. ???, ??? (2015)>
         =2015A&A...???..????
================================================================================
ADC_Keywords: Astrometry - Planets and satellites: general - Planets and
              satellites: individual: Jovian and Saturnian irregular satellites

Keywords:     Astrometry - Planets and satellites: general - Planets and
              satellites: individual: Jovian and Saturnian irregular satellites

Abstract:
The irregular satellites of the giant planets are believed to have been captured
during the evolution of the solar system. Knowing their physical parameters,
such as size, density and albedo is important to constrain where they came from
and how they were captured. The best way to obtain these parameters are
observations in situ by spacecrafts or from stellar occultations by the objects.
Both techniques demand that the orbits are well known. We aimed to obtain good
astrometric positions of irregular satellites in order to improve their orbits
and ephemeris. We identified and reduced observations of several irregular
satellites from three databases containing more than 8000 images obtained
between 1992 and 2014 at three sites (Observatório do Pico dos Dias,
Observatoire de Haute-Provence and European Southern Observatory - La Silla).
We used the software PRAIA (Platform for Reduction of Astronomical Images
Automatically) to make the astrometric reduction of the CCD frames. The UCAC4
catalogue represented the International Celestial Reference System in the
reductions. The identification of the satellites in the frames was done through
their ephemerides as determined from the SPICE/NAIF kernels. Some procedures
were taken to overcome missing or incomplete information (coordinates, date),
mostly for the older images. We managed to obtain more than 6000 positions for
18 irregular satellites, being 12 of Jupiter, 4 of Saturn, 1 of Uranus (Sycorax)
and 1 of Neptune (Nereid). For some satellites the number of obtained positions
is more than 50% of that used in earlier orbital numerical integrations.
Comparison of our positions with recent JPL ephemeris suggests the presence of
systematic errors in the orbits for some of the irregular satellites. The most
evident case was an error in the inclination of Carme.

Description:
Tables contain the topocentric ICRS coordinates of the irregular satellites,
the position error estimated from the dispersion of the ephemeris offsets of
the night of observation, the UTC time of the frame's mid-exposure in julian
date, the estimated magnitude, the filter used, the telescope origin and
correspondent IAU code. The filters may be U, B, V, R or I following the
Johnson system; C stands for clear (no filter used), resulting in a broader R
band magnitude, RE for the broad-band R filter ESO#844 with lambda = 651.725 nm
and Delta lambda = 162.184 nm (full width at half maximum) and "un" for unknown
filter. E, OH, PE, BC and Z stand respectively for the ESO, OHP (Observatoire
de Haute-Provence), Perkin-Elmer, Bollen & Chivens and Zeiss telescopes
(Observatório do Pico dos Dias).

File Summary:
--------------------------------------------------------------------------------
 FileName      Lrecl    Records    Explanations
--------------------------------------------------------------------------------
ReadMeCT.txt      80          .   This file
Albiorix.dat      70         46   Catalog of positions: Albiorix (IAU code: 626)
Ananke.dat        70        250   Catalog of positions: Ananke (IAU code: 512)
Callirrhoe.dat    70         25   Catalog of positions: Callirrhoe(IAU code:517)
Carme.dat         70        331   Catalog of positions: Carme (IAU code: 511)
Elara.dat         70        636   Catalog of positions: Elara (IAU code: 507)
Himalia.dat       70       1234   Catalog of positions: Himalia (IAU code: 506)
Leda.dat          70         98   Catalog of positions: Leda (IAU code: 513)
Lysithea.dat      70        234   Catalog of positions: Lysithea (IAU code: 510)
Megaclite.dat     70         10   Catalog of positions: Megaclite (IAU code:519)
Nereid.dat        70        902   Catalog of positions: Nereid (IAU code: 802)
Paaliaq.dat       70         11   Catalog of positions: Paaliaq (IAU code: 620)
Pasiphae.dat      70        609   Catalog of positions: Pasiphae (IAU code: 508)
Phoebe.dat        70       1787   Catalog of positions: Phoebe (IAU code: 609)
Praxidike.dat     70          2   Catalog of positions: Praxidike (IAU code:527)
Siarnaq.dat       70         76   Catalog of positions: Siarnaq (IAU code: 629)
Sinope.dat        70        221   Catalog of positions: Sinope (IAU code: 509)
Sycorax.dat       70         35   Catalog of positions: Sycorax (IAU code: 717)
Themisto.dat      70         16   Catalog of positions: Themisto (IAU code: 518)
--------------------------------------------------------------------------------

See also: ??????????????????????????????????????
          J/A+A/???/??? : Prediction tables of stellar occultations by Pluto,
          Charon, Nix and Hydra for 2008-2015 (Assafin+, 2010)

Byte-by-byte Description of file: Albiorix.dat, ... ,  Themisto.dat
--------------------------------------------------------------------------------
   Bytes Format Units   Label    Explanations
--------------------------------------------------------------------------------
   2-  3  I2    h       RAh      Right ascension (J2000.0)
   5-  6  I2    min     RAm      Right ascension (J2000.0)
   8- 14  F7.4  s       RAs      Right ascension (J2000.0)
      16  A1    ---     DE-      Sign of declination
  17- 18  I2    deg     DEd      Declination (J2000.0)
  20- 21  I2    arcmin  DEm      Declination (J2000.0)
  23- 28  F6.3  arcsec  DEs      Declination (J2000.0)
  30- 33  I4    mas     PosErr   Right ascension error at mean epoch
  35- 38  I4    mas     PosErr   Declination error at mean epoch
  40- 55  F16.8 days    JD       Mean epoch (Julian Date) of coordinates
  57- 60  F4.1  mag     ?mag     Magnitude (apparent) (1) ???
  62- 63  A2    ---     text     Filter used (2) ???
  65- 66  A2    ---     text     Telescope used (3) ???
  68- 70  I3    ---     text?    IAU code of the site of observation ???
--------------------------------------------------------------------------------
Note (1): Estimated magnitude (from PSF fitting). The magnitude errors can be as
          high as 1 mag; they are not photometrically calibrated and should be
          used with care.
Note (2): The filters may be U, B, V, R or I following the Johnson system;
          C stands for clear (no filter used), resulting in a broader R band
          magnitude, RE for the broad-band R filter ESO#844 with
          lambda = 651.725 nm and Delta lambda = 162.184 nm (full width at half
          maximum) and "un" for unknown filter.
Note (3): E, OH, PE, BC and Z stand respectively for the ESO, OHP (Observatoire
          de Haute-Provence), Perkin-Elmer, Bollen & Chivens and Zeiss telescopes
          (Observatório do Pico dos Dias).
--------------------------------------------------------------------------------

Acknowledgements: Altair Ramos Gomes-Júnior  <altair08@astro.ufrj.br>

References:
================================================================================
(End)                  Altair Ramos Gomes-Júnior [UFRJ/OV, Brazil]   12-May-2015
