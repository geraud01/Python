dias_nesse_ano = int(input("Quantos dias tem nesse ano?"))

dias_no_ano = 365
dias_no_ano_bissexto = 366
horas_no_dias = 24
minutos_no_hora = 60
segundos_no_minuto = 60

resultado = dias_no_ano * horas_no_dias * minutos_no_hora * segundos_no_minuto

ano_bissexto_resultado = dias_no_ano_bissexto * horas_no_dias * minutos_no_hora * segundos_no_minuto  

if dias_nesse_ano == 365 :
  print ("O numero de segundos desse ano é de", resultado )
else :
  print ("O numero de segundos desse ano é de", ano_bissexto_resultado)  