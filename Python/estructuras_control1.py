"""
70 helado
20 pastel
10 flan
"""
# elif es un si no - si
stock = input(" ingrese el postre encontrado  ")
if stock ==  "helado":
    print("Recuerda comprar las cucharas desechables, por cierto, no olvides el hielo")
elif stock == "pastel":
    print("Recuerda comprar platos desechables")
elif stock == "flan":
    print("Recuerda comprar salsa de caramelo")
else:
    print("no es ningun postre de la lista")