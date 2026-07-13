# API Português

## Sobre o projeto

API desenvolvida para fornecer dados de classes gramaticais da língua portuguesa para consumo em aplicações externas.

O projeto foi criado para ser utilizado por um aplicativo de flashcards, responsável por exibir notificações com conteúdos de aprendizado. A API realiza a busca dos dados armazenados no Supabase, aplica o tratamento necessário e disponibiliza as informações em um formato adequado para consumo pelo aplicativo.

## Tecnologias utilizadas

* Python
* FastAPI
* Supabase
* Pydantic
* Uvicorn

## Estrutura do projeto

A aplicação segue uma arquitetura separada por responsabilidades:

* `routes`: gerenciamento dos endpoints da API.
* `services`: regras de negócio e tratamento dos dados.
* `repositories`: comunicação com o banco de dados.
* `schemas`: modelos de entrada e saída dos dados.
* `core`: configurações e conexões externas.

## Como executar o projeto

Clone o repositório:

```bash
git clone <url-do-repositorio>
```

Entre na pasta do projeto:

```bash
cd Api_Portugues
```

Crie e ative o ambiente virtual:

```bash
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute a API:

```bash
uvicorn app.main:app --reload
```

A documentação interativa estará disponível em:

```
/docs
```

## Variáveis de ambiente

Crie um arquivo `.env` baseado no `.env.example`.

Exemplo:

```env
SUPABASE_URL=
SUPABASE_KEY=
```

## Endpoints

### Classes gramaticais

Retorna informações de uma classe gramatical tratada para consumo.

Exemplo:

```
GET /assuntos

GET /assuntos/{assunto}
```

Classes disponíveis:

* verbo
* substantivo
* adjetivo
* advérbio
* artigo
* pronome
* numeral
* preposição
* conjunção
* interjeição

## Exemplo de resposta

```json
{
  "artigo": {
    "id": 4,
    "nome": "Artigo",
    "definicao": "Palavra que acompanha o substantivo indicando gênero e número."
  }
}
```

## Integração

A API foi desenvolvida para ser consumida por aplicações mobile ou web que necessitem de conteúdos educacionais em formato de flashcards.

O fluxo da aplicação é:

1. O aplicativo solicita um conteúdo através da API.
2. A API busca os dados no Supabase.
3. Os dados são tratados conforme a necessidade do aplicativo.
4. A API retorna uma resposta pronta para exibição.
