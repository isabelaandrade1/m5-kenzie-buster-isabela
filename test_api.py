import requests

# URL da API para listar filmes
url = "http://127.0.0.1:8000/api/movies/"

# Substitua o token pelo seu token de acesso gerado
headers = {
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ..."
}

# Requisição GET para listar os filmes
response = requests.get(url, headers=headers)

# Imprimir o resultado
print(response.status_code)
print(response.json())
