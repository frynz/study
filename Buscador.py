import requests
from bs4 import BeautifulSoup

def buscar_resposta(pergunta):
    try:
        # URL do mecanismo de busca do DuckDuckGo
        url = f"https://duckduckgo.com/html/?q={pergunta}"
        
        # Cabeçalho de agente de usuário (user-agent)
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
        }
        
        # Realiza a solicitação HTTP com o cabeçalho de agente de usuário
        response = requests.get(url, headers=headers)
        
        # Verifica se a solicitação foi bem-sucedida
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Extrai os títulos e URLs dos resultados da pesquisa
            resultados = soup.find_all('div', class_='result')
            
            for i, resultado in enumerate(resultados, start=1):
                title = resultado.find('a', class_='result__a')
                link = resultado.find('a', class_='result__url')
                
                if title and link:
                    print(f"Resultado {i}:")
                    print("Título:", title.text)
                    print("URL:", link['href'])
                    print("\n")
        else:
            print("A solicitação falhou. Status code:", response.status_code)
    except Exception as e:
        print("Ocorreu um erro ao buscar a resposta:", str(e))

if __name__ == "__main__":
    pergunta = input("Digite sua pergunta: ")
    buscar_resposta(pergunta)
