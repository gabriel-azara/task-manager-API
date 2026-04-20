# API de Tarefas com FastAPI

Uma API REST simples de lista de tarefas (To-Do list) desenvolvida com **FastAPI** e **Pydantic**. Os dados são armazenados localmente em memória durante a execução do servidor.

## 🚀 Como rodar o projeto

Siga os passos abaixo para subir a aplicação na sua máquina local (MacOS / Linux):

### 1. Acesse o diretório do projeto
Abra o seu terminal de preferência e navegue até a pasta do projeto:
```bash
cd projeto-tarefas
```

### 2. Ative o Ambiente Virtual (venv)
O projeto conta com um ambiente virtual (`venv`) configurado. Para ativá-lo, utilize o comando:
```bash
source venv/bin/activate
```

### 3. Instale as Dependências
Com o ambiente virtual ativado, instale as bibliotecas necessárias que estão no arquivo `requirements.txt`:
```bash
pip install -r requirements.txt
```

### 4. Rode o Servidor
Com tudo instalado e ativado, inicie o servidor de desenvolvimento do Uvicorn:
```bash
uvicorn main:app --reload
```

A flag `--reload` é muito útil durante o desenvolvimento, pois o servidor reinicia automaticamente assim que você salva qualquer modificação no código.

## 📚 Acessando a Documentação

Uma das grandes vantagens do FastAPI é que ele gera a documentação interativa da sua API automaticamente. Com o servidor rodando, acesse no seu navegador:

- **Swagger UI (Recomendado):** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc:** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

Pela interface interativa do Swagger (`/docs`), você consegue enviar requisições (`GET`, `POST`, `PUT`, `DELETE`) para testar a sua API em tempo real direto pela tela, sem precisar de outras ferramentas extras.

## 🔗 Endpoints da API

A API conta atualmente com as seguintes rotas:

| Método   | Endpoint           | Descrição                                              |
| :------- | :----------------- | :----------------------------------------------------- |
| `GET`    | `/`                | Rota raiz, retorna uma verificação de boas-vindas.     |
| `GET`    | `/tasks`           | Retorna a lista contendo todas as tarefas.             |
| `POST`   | `/tasks`           | Cria e salva uma nova tarefa (Requer `{ "title": ... }`). |
| `PUT`    | `/tasks/{task_id}` | Atualiza uma tarefa pelo seu ID marcando-a como concluída. |
| `DELETE` | `/tasks/{task_id}` | Deleta definitivamente uma tarefa pelo seu ID.         |


## 🌐 Deploy na Render

A aplicação foi deployada na plataforma **Render**.

- **Link da API:** https://task-manager-api-bgsn.onrender.com
- **Documentação (Swagger UI):** https://task-manager-api-bgsn.onrender.com/docs