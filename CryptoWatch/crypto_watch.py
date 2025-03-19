import requests
import webbrowser
import locale

# Configurando o locale para o Brasil (isso irá utilizar a vírgula como separador de decimais)
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

# URL da API CoinGecko para obter a cotação de várias criptomoedas em Reais (BRL)
url = 'https://api.coingecko.com/api/v3/simple/price?ids=brz,bitcoin,ethereum&vs_currencies=brl'

# Fazendo a requisição GET à API
response = requests.get(url)

# Verificando o status da requisição
if response.status_code == 200:
    # Convertendo a resposta JSON em um dicionário Python
    data = response.json()

    # Formatando as cotações
    brz_price = locale.format_string('%.2f', data['brz']['brl'], grouping=True)
    bitcoin_price = locale.format_string('%.2f', data['bitcoin']['brl'], grouping=True)
    ethereum_price = locale.format_string('%.2f', data['ethereum']['brl'], grouping=True)

    # Criando o conteúdo HTML para exibir as cotações com links clicáveis
    html_content = f"""
    <html>
        <head>
            <title>Cotações de Criptomoedas</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    background-color: #f4f4f9;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    margin: 0;
                    color: #333;
                }}
                .container {{
                    background-color: #fff;
                    border-radius: 10px;
                    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
                    width: 300px;
                    padding: 20px;
                    text-align: center;
                }}
                h1 {{
                    color: #4CAF50;
                    font-size: 24px;
                    margin-bottom: 20px;
                }}
                p {{
                    font-size: 18px;
                    margin: 10px 0;
                    font-weight: bold;
                    color: #333;
                }}
                p strong {{
                    color: #4CAF50;
                }}
                .price {{
                    font-size: 22px;
                    color: #4CAF50;
                    font-weight: bold;
                }}
                a {{
                    color: #4CAF50;
                    text-decoration: none;
                }}
                a:hover {{
                    text-decoration: underline;
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Cotações de Criptomoedas</h1>
                <p><strong><a href="https://www.coingecko.com/pt/moedas/brz" target="_blank">BRZ</a>:</strong> <span class="price">R${brz_price}</span></p>
                <p><strong><a href="https://www.coingecko.com/pt/moedas/bitcoin" target="_blank">Bitcoin</a>:</strong> <span class="price">R${bitcoin_price}</span></p>
                <p><strong><a href="https://www.coingecko.com/pt/moedas/ethereum" target="_blank">Ethereum</a>:</strong> <span class="price">R${ethereum_price}</span></p>
            </div>
        </body>
    </html>
    """

    # Caminho para salvar o arquivo HTML
    file_path = "cotacoes_criptomoedas.html"

    # Salvando o HTML em um arquivo
    with open(file_path, "w") as f:
        f.write(html_content)

    # Abrindo o arquivo HTML no navegador
    webbrowser.open(file_path)

else:
    print("Erro ao obter os dados")
