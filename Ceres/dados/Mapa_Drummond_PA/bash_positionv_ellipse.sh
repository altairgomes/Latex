#nedit ellipse_fit.i positionv.i plot_* fort.53 &
rm -f fort.66
./positionv < positionv_err.i > out_poserr
cp fort.21 fort.21err
./positionv < positionv_mid.i > out_posmid
cp fort.21 fort.21mid
#./positionv < positionv_mid_err.i > out_posmid_err
#cp fort.21 fort.21mid_err
#./positionv < positionv_neg.i > out_posneg
#cp fort.21 fort.21neg
./positionv < positionv_all.i > out_posall
cp fort.21 fort.21all
./positionv < positionv.i > out_positionv
cp fort.21 fort.21nom
./ellipse_fit < ellipse_fit.i > out_ellipse2
cp fort.51 fort.51nom
#read ok
#plot_data < plot_data_lat.i
#plot_pla < plot_pla.i

