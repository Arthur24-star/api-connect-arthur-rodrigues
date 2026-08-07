# API Connect

## Objetivo

A API Connect é uma API REST desenvolvida em Python utilizando o framework Flask. O projeto foi criado como atividade prática da disciplina de Desenvolvimento Back-end e permite realizar operações de cadastro, consulta, atualização e remoção de usuários (CRUD).

## Tecnologias utilizadas

- Python 3
- Flask
- Git
- GitHub
- Thunder Client

## Como executar o projeto

1. Clone o repositório:

```bash
git clone https://github.com/Arthur24-star/api-connect-arthur-rodrigues.git
```

2. Acesse a pasta do projeto:

```bash
cd api-connect-arthur-rodrigues
```

3. Crie um ambiente virtual:

```bash
python -m venv venv
```

4. Ative o ambiente virtual:

Windows:

```bash
venv\Scripts\activate
```

5. Instale as dependências:

```bash
pip install -r requirements.txt
```

6. Execute a aplicação:

```bash
python app.py
```

A API será iniciada em:

```
http://127.0.0.1:5000
```

## Endpoints

### GET /usuarios <id>


Lista todos os usuários cadastrados.

### GET /usuarios/<id>

Busca um usuário pelo ID.

**Exemplo:**

```text
GET /usuarios/1
```

### POST /usuarios <id>

Cadastra um novo usuário.

**Exemplo:**

```json
{
  "nome": "Arthur",
  "email": "arthur@email.com"
}
```

### PUT /usuarios/<id>

Atualiza um usuário existente.

**Exemplo:**

```text
PUT /usuarios/1
```

```json
{
  "nome": "Novo Nome",
  "email": "novo@email.com"
}
```

### DELETE /usuarios/<id>

Remove um usuário pelo ID.

**Exemplo:**

```text
DELETE /usuarios/1
```