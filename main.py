# Desafio Final (usando uma IDE):
# 1-Carregar um arquivo .txt, onde cada linha será um elemento de uma lista do Python
# 2-Mandá-la ao modelo que você está rodando localmente para extrair, em formato JSON, onde cada item terá "usuario", "resenha original", "resenha_pt", "avaliacao" (Positiva, Negativa, Neutra)
# 3-Transformar a resposta do modelo em uma lista de dicionários Python
# 4-Criar uma função que, dada uma lista de dicionários, percorre a lista faz 2 coisas:
# a) conta a quantidade de avaliações positivas, negativas e neutras,
# b) une cada item dessa lista em uma variável do tipo string com algum separador.
# Ao final, retorna ambas as coisas.

# importações:
from funcao_classificadora import extrair_json
from funcao_contador_juntador import contador_juntador
import pandas as pd

nomes_colunas = ["ID", "Nome", "Resenhas"]

# leitura e separação da base de dados
df_feedbacks_csv = pd.read_csv("Resenhas_App_ChatGPT.txt", sep="$", header= None, names=nomes_colunas)

# separação do df
lista_linhas = df_feedbacks_csv[["Nome", "Resenhas"]].values.tolist()

feedbacks_classificados_json = extrair_json(lista_linhas)

pos, neg, neu, textos = contador_juntador(feedbacks_classificados_json)

print(f"Positivas: {pos}")
print(f"Negativas: {neg}")
print(f"Neutras: {neu}")
print(textos)
