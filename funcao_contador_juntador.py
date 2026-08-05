def contador_juntador(lista_dicionarios):
    contador_positivas = 0
    contador_negativas = 0
    contador_neutras = 0
    lista_dicionarios_str = []

    for dicionario in lista_dicionarios:
        if dicionario['avaliacao'] == "Positiva":
            contador_positivas += 1
        elif dicionario['avaliacao'] == "Negativa":
            contador_negativas += 1
        else:
            contador_neutras += 1

        lista_dicionarios_str.append(str(dicionario))

    textos_unidos = "||||".join(lista_dicionarios_str)

    return contador_positivas, contador_negativas, contador_neutras, textos_unidos
