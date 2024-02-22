nota1Flt = float(input('Ingrese la nota 1 -> ')) * 0.20
nota2Flt = float(input('Ingrese la nota 2 -> ')) * 0.30
nota3Flt = float(input('Ingrese la nota 3 -> ')) * 0.40
nota4Flt = float(input('Ingrese la nota 4 -> ')) * 0.10

definitivaFlt = (nota1Flt * 0.20) + (nota2Flt * 0.30) + (nota3Flt * 0.40) + (nota4Flt * 0.10) / 4
if definitivaFlt >= 3.5:
    print('Haz aprobado')
else:
    print ('Haz reprobado')
print('Su nota definitiva es: ',definitivaFlt)