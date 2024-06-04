
cadenaIntroducida = input("Por favore introdusca una bolude cualquiera (Que sean frases perfavore amore mio): ")
listaCadena = cadenaIntroducida.split()
print(f"El chavón dijo {len(listaCadena)} palabras")
print(f"Por lo que tardará {len(listaCadena) / 2} segundos en decir la frase")

if (len(listaCadena) / 2 > 60):
    print("Pará animal, demasiado largo boludo")

daltoTiempo = (len(listaCadena) / 2) * 70 / 100
print(f"Dalto tardaría {daltoTiempo} en decir la frase")
