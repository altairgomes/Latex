#
### 
#
arquivo="Lysithea_ucac4_OHP.table"
nummin="4"
sigma="2.5"
#
### Código
#
tiramedia(){
  totalalfa="0"
  totaldelta="0"
  totalalfa2="0"
  totaldelta2="0"
  while read aa ab ac ad ae af ag ah ai aj ak al am an ao ap aq aar as at au av aw ax ay az ba;do
    totalalfa=$(calc "$totalalfa + $ac"  < /dev/null | sed 's/\~//')
    totalalfa2=$(calc "$totalalfa2 + $ac*$ac"  < /dev/null | sed 's/\~//')
    totaldelta=$(calc "$totaldelta + $ad"  < /dev/null | sed 's/\~//')
    totaldelta2=$(calc "$totaldelta2 + $ad*$ad"  < /dev/null | sed 's/\~//')
  done < $1
  numarq=$(cat $1 | wc -l)
  medalfa=$(calc "$totalalfa / $numarq"  < /dev/null | sed 's/\~//'); echo "medalfa = $medalfa"
  meddelta=$(calc "$totaldelta / $numarq"  < /dev/null | sed 's/\~//'); echo "meddelta = $meddelta"
  sigmaalfa=$(calc "sqrt(($totalalfa2 - $numarq*$medalfa*$medalfa)/($numarq -1))" < /dev/null | sed 's/\~//'); echo "sigmaalfa = $sigmaalfa"
  sigmadelta=$(calc "sqrt(($totaldelta2 - $numarq*$meddelta*$meddelta)/($numarq -1))" < /dev/null | sed 's/\~//'); echo "sigmadelta = $sigmadelta"
}
#
#
#
nlines=$(cat $arquivo | wc -l)
depois=$(echo "$nlines - 2" | bc)
head -$depois $arquivo > .aux1
antes=$(echo "$depois - 43" | bc)
tail -$antes .aux1 > .aux2
while read aa ab ac ad ae af ag ah ai aj ak al am an ao ap aq aar as at au av aw ax ay az ba;do
  if [ "$ae" -lt "$nummin" ];then
    cat $arquivo | grep "$az" >> "$arquivo"_eliminated
  else
    cat $arquivo | grep "$az" >> .aux3
  fi
done < .aux2
refazer="1"
until [ "$refazer" -eq "0" ];do
  tiramedia .aux3
  maxalfa=$(awk '$3>x{x=$3};END{print x}' .aux3); echo $maxalfa
  dataalfa=$(awk '$3>x{x=$3;data=$26};END{print data}' .aux3);echo $dataalfa
  maxdelta=$(awk '$4>x{x=$4};END{print x}' .aux3); echo $maxdelta
  datadelta=$(awk '$4>x{x=$4;data=$26};END{print data}' .aux3); echo $datadelta
  difalfa=$(calc "$maxalfa - $medalfa" < /dev/null | sed 's/\~//'); echo $difalfa
  difsigalfa=$(calc "$difalfa / $sigmaalfa" < /dev/null | sed 's/\~//'); echo $difsigalfa
  difdelta=$(calc "$maxdelta - $meddelta" < /dev/null | sed 's/\~//'); echo $difdelta
  difsigdelta=$(calc "$difdelta / $sigmadelta" < /dev/null | sed 's/\~//'); echo $difsigdelta
  if [ $(echo "$difsigalfa > $difsigdelta" | bc) -eq "1" ];then
    if [ $(echo "$difsigalfa > $sigma" | bc) -eq "1" ];then
      cat .aux3 | grep "$dataalfa" >> "$arquivo"_eliminated
      cat .aux3 | grep -v "$dataalfa" > .aux4
     echo feito
    else
      refazer="0"; echo feito1
    fi
  else
    if [ $(echo "$difsigdelta > $sigma" | bc) -eq "1" ];then
      cat .aux3 | grep "$datadelta" >> "$arquivo"_eliminated
      cat .aux3 | grep -v "$datadelta" > .aux4
    else
      refazer="0"
    fi
  fi
  mv .aux4 .aux3
done
cp .aux3 "$arquivo"_filtered
rm .aux1 .aux2 .aux3
