diam.f	       > calcula o diametro da estrela
bar.f          > calcula a difracao, chi2, para um evento em 'barra' (oc total)
plot_data.f    >  monta a curva de luz e plota os modelos
polyfit.f      >  calcula o rms e um polinomio sobre os dados 
ellipse_fit.f  >  calcula o ajuste de uma elipse
plot_pla.f     >  plota o objeto e as cordas
positionv.f    >  calcula a posicao das cordas e a posicao do corpo para o plot_pla.
implu_site.dat >  resposta instrumental. (metade do tempo de exposicao) ????
t_ratio_site.dat > tempo TU em segundos e razao de fluxo


diam.f	       > calcula o diametro da estrela
Para isto sera necessario as magnitudes B, V e K da estrela, bem como da distancia em quilometros do
objeto (jpl).

polyfit.f      >  calcula o rms e um polinomio sobre os dados 
Ajusta um polinomio de ate quarto grau à dados. Fornecendo os intervalos para os calculos (fora do
evento ou durante o evento), ele fornece como
saida os dados teoricos para os intervalos, a diferenca entre os dados e o polinomio e a razao entre os
dados e o polinomio, esto é util caso queira normalizar os dados à 1.
É interessante plotar a curva com o polinomio para verificar o juste, usar plot_data.f


bar.f          > calcula a difracao, chi2, para um evento em 'barra' (oc total)
Para uma melhor estimativa do instante de queda, lanca-se o este progrma [bar < bar_imm_lna.i >
bar_imm_opd_out] com o numero de pontos a serem explorados no enrono do instante estimado t0. É interessante ver o resultado graficamente com plot_data_chi2.i. 
Por fim, com o bar e so um ponoto a explorar, obtem-se o ajuste para a imersao/emersao do evento.


