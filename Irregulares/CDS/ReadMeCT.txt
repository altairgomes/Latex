J/A+A/580/A76   Giant planets satellite positions catalog  (Gomes-Junior+, 2015)
Astrometric positions for 18 irregular satellites of giant planets from 23 years
of observations.
    Gomes-Junior A.R., Assafin M., Vieira Martins R., Arlot J.-E.,
    Camargo J.I.B., Braga-Ribas F., da Silva Neto D.N., Andrei A.H.,
    Dias-Oliveira A., Morgado B.E., Benedetti-Rossi G., Duchemin Y.,
    Desmars J., Lainey V., Thuillot W.
    <Astron. Astrophys. 580, A76 (2015)>
    =2015A&A...580A..76G        (SIMBAD/NED BibCode)
ADC_Keywords: Positional data - Solar system

Keywords: planets and satellites: general -
          planets and satellites: individual: Jupiter -
          planets and satellites: individual: Saturn - astrometry -

Abstract:
    The irregular satellites of the giant planets are believed to have
    been captured during the evolution of the solar system. Knowing their
    physical parameters, such as size, density and albedo is important to
    constrain where they came from and how they were captured. The best
    way to obtain these parameters are observations in situ by spacecrafts
    or from stellar occultations by the objects. Both techniques demand
    that the orbits are well known. We aimed to obtain good astrometric
    positions of irregular satellites in order to improve their orbits and
    ephemeris. We identified and reduced observations of several irregular
    satellites from three databases containing more than 8000 images
    obtained between 1992 and 2014 at three sites (Observatorio do Pico
    dos Dias, Observatoire de Haute-Provence and European Southern
    Observatory - La Silla). We used the software PRAIA (Platform for
    Reduction of Astronomical Images Automatically) to make the
    astrometric reduction of the CCD frames. The UCAC4 catalogue
    represented the International Celestial Reference System in the
    reductions. The identification of the satellites in the frames was
    done through their ephemerides as determined from the SPICE/NAIF
    kernels. Some procedures were taken to overcome missing or incomplete
    information (coordinates, date), mostly for the older images. We
    managed to obtain more than 6000 positions for 18 irregular
    satellites, being 12 of Jupiter, 4 of Saturn, 1 of Uranus (Sycorax)
    and 1 of Neptune (Nereid). For some satellites the number of obtained
    positions is more than 50% of that used in earlier orbital numerical
    integrations. Comparison of our positions with recent JPL ephemeris
    suggests the presence of systematic errors in the orbits for some of
    the irregular satellites. The most evident case was an error in the
    inclination of Carme.

Description:
    Tables contain the topocentric ICRS coordinates of the irregular
    satellites, the position error estimated from the dispersion of the
    ephemeris offsets of the night of observation, the UTC time of the
    frame's mid-exposure in julian date, the estimated magnitude, the
    filter used, the telescope origin and correspondent IAU code. The
    filters may be U, B, V, R or I following the Johnson system; C stands
    for clear (no filter used), resulting in a broader R band magnitude,
    RE for the broad-band R filter ESO#844 with λ=651.725nm and
    Δλ=162.184nm (full width at half maximum) and "un" for
    unknown filter. E, OH, PE, BC and Z stand respectively for the ESO,
    OHP (Observatoire de Haute-Provence), Perkin-Elmer, Bollen & Chivens
    and Zeiss telescopes from the Observatorio do Pico dos Dias.

File Summary:

       FileName      Lrecl  Records   Explanations

ReadMe            80        .   This file
objects.dat       29       18   List of studied satellites
tables/*          70       18   Individual catalogs of positions


See also:
   J/A+A/453/349 : CCD positions for 8 Jovian irregular satellites (Veiga, 2006)


Byte-by-byte Description of file: objects.dat

   Bytes Format Units   Label     Explanations

   1- 10  A10   ---     Name      Satellite Name
  12- 14  I3    ---     Num       IAU code for the satellite
  15- 29  A15   ---     FileName  Name of the file with positions
                                   in subdirectory tables


Byte-by-byte Description of file: tables/*

   Bytes Format Units   Label     Explanations

   2-  3  I2    h       RAh       Right ascension (J2000.0)
   5-  6  I2    min     RAm       Right ascension (J2000.0)
   8- 14  F7.4  s       RAs       Right ascension (J2000.0)
      16  A1    ---     DE-       Sign of declination
  17- 18  I2    deg     DEd       Declination (J2000.0)
  20- 21  I2    arcmin  DEm       Declination (J2000.0)
  23- 28  F6.3  arcsec  DEs       Declination (J2000.0)
  30- 33  I4    mas     e_RAs     Right ascension error at mean epoch
  35- 38  I4    mas     e_DEs     Declination error at mean epoch
  40- 55  F16.8 d       JD        Mean epoch (Julian Date) of coordinates
  57- 60  F4.1  mag     mag       Magnitude (apparent) in Filter (1)
  62- 63  A2    ---     Filt      Filter used (2)
  65- 66  A2    ---     Tel       Telescope used (3)
  68- 70  I3    ---     Site      IAU code of the site of observation

Note (1): Estimated magnitude (from PSF fitting) based on filter given in column
 Filt. The magnitude errors can be as high as 1mag; they are not photometrically
 calibrated and should be used with care.
Note (2): The filters may be U, B, V, R or I following the Johnson system;
  C stands for clear (no filter used), resulting in a broader R band magnitude,
  RE for the broad-band R filter ESO#844 with λ=651.725nm and
  Δλ=162.184nm (full width at half maximum) and
  "un" for unknown filter.
Note (3): Telescope code as follows:
     E = ESO,
    OH = OHP (Observatoire de Haute-Provence),
    PE = Perkin-Elmer telescope (Observatorio do Pico dos Dias)
    BC = Bollen & Chivens telescope (Observatorio do Pico dos Dias)
     Z = Zeiss telescope (Observatorio do Pico dos Dias)


Acknowledgements:
   Altair Ramos Gomes-Junior, altair08(at)astro.ufrj.br
(End)  A.R. Gomes-Junior [UFRJ/OV, Brazil], P. Vannier [CDS]         15-May-2015
