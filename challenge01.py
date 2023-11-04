def count_words(msg):
    words = msg.lower().split()
    contador = {}

    for word in words:
        contador[word] = contador.get(word, 0) + 1

    result = ""
    for word, frec in contador.items():
        result += word + str(frec)

    return result


msg = "gato perro perro coche Gato peRRo sol"
result = count_words(msg)
print(result)
