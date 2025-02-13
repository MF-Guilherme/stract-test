# Relatórios de Insights de Anúncios

Este projeto é uma API em Flask que consome dados de uma API externa para gerar relatórios de anúncios em formato CSV. Ele coleta insights de diversas plataformas de anúncios e os organiza de forma estruturada.

## Funcionalidades

- Obtenção de dados de diversas plataformas de anúncios.
- Geração de relatórios detalhados e resumidos.
- Conversão e formatação de dados para CSV.
- Tratamento de paginação para garantir que todos os dados sejam processados.

## Tecnologias Utilizadas

- **Python 3.12**
- **Flask** (Framework web)
- **Requests** (Consumo da API externa)
- **Pandas** (Manipulação e formatação de dados)
- **Dotenv** (Gerenciamento de variáveis de ambiente)

## 📂 Estrutura do Projeto

```
📁 projeto
│── 📁 app
│   │── 📄 __init__.py  # Inicializa a aplicação
│   │── 📄 config.py  # Configurações globais
│   │── 📄 routes.py  # Definição dos endpoints
│   │── 📄 services.py  # Consumo da API externa
│   │── 📄 utils.py  # Geração de relatórios em CSV
│   │── 📄 helpers.py  # Funções auxiliares
│── 📄 app.py  # Arquivo principal para execução do Flask
│── 📄 .env  # Armazena as variáveis de ambiente
│── 📄 requirements.txt  # Dependências do projeto
│── 📄 README.md  # Documentação
```

## 🔧 Configuração e Execução

### 1️⃣ Clonar o repositório
```bash
  git clone git@github.com:MF-Guilherme/stract-test.git
  cd stract-test
```

### 2️⃣ Criar e ativar o ambiente virtual
```bash
  python3 -m venv venv
  source venv/bin/activate  # Linux/macOS
  venv\Scripts\activate  # Windows
```

### 3️⃣ Instalar as dependências
```bash
  pip install -r requirements.txt
```

### 4️⃣ Configurar as variáveis de ambiente
Crie um arquivo `.env` na raiz do projeto e adicione:
```ini
API_TOKEN= o token fornecido para o teste
API_BASE_URL=https://sidebar.stract.to/api
```

### 5️⃣ Executar a aplicação
```bash
  flask run
```
A API estará rodando em: `http://127.0.0.1:5000/` ou `localhost:5000/`

## 🛠 Endpoints Disponíveis

| Método | Rota                      | Descrição |
|--------|---------------------------|-------------|
| GET    | `/`                        | Retorna as informações do desenvolvedor |
| GET    | `/{plataforma}`            | Relatório detalhado de uma plataforma |
| GET    | `/{plataforma}/resumo`     | Relatório resumido de uma plataforma |
| GET    | `/geral`                   | Relatório de todas as plataformas |
| GET    | `/geral/resumo`            | Relatório resumido de todas as plataformas |

📌 **Observação:** O parâmetro `{plataforma}` deve ser o mesmo valor presente no campo **###`value`** da resposta do endpoint externo `https://sidebar.stract.to/api/platforms`. Exemplos de valores aceitos:

```json
{
  "platforms": [
    {"text": "Google Analytics", "value": "ga4"},
    {"text": "TikTok", "value": "tiktok_insights"},
    {"text": "Facebook Ads", "value": "meta_ads"}
  ]
}
```

Por exemplo, para obter o relatório da plataforma Google Analytics (`ga4`), utilize:
```bash
curl -X GET http://127.0.0.1:5000/ga4
```

## 📜 Exemplo de Uso
Para obter o relatório geral:
```bash
curl -X GET http://127.0.0.1:5000/geral
```

## 📌 Autor
👤 **Guilherme Montenegro Ferreira**  
🔗 [LinkedIn](https://www.linkedin.com/in/guimontenegro/)  
📧 [Email](mailto:guimontenegro23@yahoo.com.br)

