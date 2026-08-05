# importaçôes
from openai import OpenAI
import time 

# criação do client_openai
client_openai = OpenAI(
    base_url="http://127.0.0.1:1234/v1",
    api_key="lm-studio"
)

def extrair_json(lista_de_feedbacks):
    lista_feedbacks_json = []

    for i, linha in enumerate(lista_de_feedbacks, 1):

        resposta_llm = client_openai.chat.completions.create(
            model="google/gemma-3-1b",
            messages=[
                {"role" : "system", 
                 "content": """Você é um especialista em processamento de linguagem natural (NLP), identificação de idiomas e tradução de textos para pt-BR para análise de avaliações de clientes.
                                Seu Objetivo é:
                                
                                Extrair informações da avaliação do cliente, traduzir o conteúdo para português do Brasil e classificar o sentimento.
                
                                Regras de Processamento
                                Considere que:
                                As colunas estão separadas por ,
                                A primeira coluna contém o nome do cliente.
                                A segunda coluna contém o texto da avaliação original.
                                Identifique o idioma da avaliação presente na terceira coluna.
                                Analise o sentimento predominante da avaliação e classifique utilizando apenas um dos seguintes valores:
                                "Positiva"
                                "Negativa"
                                "Neutra"
                                Traduza a avaliação para português do Brasil (pt-BR), preservando:
                                O significado original.
                                O tom emocional da mensagem.
                                Gírias, informalidades e intensidade emocional sempre que possível.
                                A intenção exata do cliente.
                                Não resuma, não interprete e não reescreva de forma mais elegante. Apenas traduza mantendo o estilo original do autor.
                                Regras de Saída:
                                Retorne exclusivamente um objeto JSON válido.
                
                                Exemplo da Estrutura JSON obrigatória:
                                {
                                    "usuario": "<nome na primeira coluna>",
                                    "resenha_original": "<somente texto original na segunda coluna>",
                                    "resenha_pt": "<somente o texto traduzido do feedback para pt-BR>",
                                    "avaliacao": "<Positiva|Negativa|Neutra>"
                                }
                
                                Restrições:
                                Não adicione explicações.
                                Não utilize markdown.
                                Não utilize blocos de código.
                                Não retorne texto fora do JSON.
                                O JSON deve ser válido e parseável."""},
                {"role" : "user", 
                 "content": f"""Receba o seguinte registro: {linha}"""}
            ],
            temperature=0.7,
            max_completion_tokens=1024,
            stream=False,
        )

        resposta_texto = resposta_llm.choices[0].message.content.replace("```json", "").replace( "```","")

        print(f"Linha {i}: {resposta_texto}")
        lista_feedbacks_json.append(resposta_texto)
        print("-" * 150)
        time.sleep(3)

    return lista_feedbacks_json