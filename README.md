# API CRUD com Python, PostgreSQL e RabbitMQ

Este projeto é uma API CRUD (Create, Read, Update, Delete) desenvolvida com FastAPI, PostgreSQL e RabbitMQ. A aplicação permite gerenciar tarefas e publica eventos no RabbitMQ para cada operação realizada.

## Tecnologias Utilizadas

- Python 3.11
- FastAPI
- PostgreSQL
- RabbitMQ
- SQLAlchemy
- Pydantic
- Docker e Docker Compose

## Estrutura do Projeto

```
.
├── app/
│   ├── __init__.py
│   ├── main.py           # Aplicação FastAPI
│   ├── database.py       # Configuração do PostgreSQL
│   ├── models.py         # Modelos SQLAlchemy
│   ├── schemas.py        # Schemas Pydantic
│   ├── rabbitmq.py       # Serviço RabbitMQ
│   └── consumer.py       # Consumidor de eventos RabbitMQ
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
└── README.md
```

## Como Executar

1. Clone o repositório:
```bash
git clone https://github.com/marcosvrc/python-crud-postgres-rabbitmq.git
cd python-crud-postgres-rabbitmq
```

2. Inicie os containers com Docker Compose:
```bash
docker-compose up -d
```

3. A API estará disponível em: http://localhost:8000

4. Para acessar a documentação da API: http://localhost:8000/docs

5. Para acessar o RabbitMQ Management: http://localhost:15672
   - Usuário: admin
   - Senha: admin123

## Endpoints da API

- `POST /tasks/` - Criar uma nova tarefa
- `GET /tasks/` - Listar todas as tarefas
- `GET /tasks/{task_id}` - Obter uma tarefa específica
- `PUT /tasks/{task_id}` - Atualizar uma tarefa
- `DELETE /tasks/{task_id}` - Deletar uma tarefa

## Exemplo de Payload

```json
{
  "title": "Minha Tarefa",
  "description": "Descrição da minha tarefa",
  "completed": false
}
```

## Eventos RabbitMQ

A aplicação publica os seguintes eventos no RabbitMQ:

- `task_created` - Quando uma nova tarefa é criada
- `task_updated` - Quando uma tarefa é atualizada
- `task_deleted` - Quando uma tarefa é deletada

Para consumir os eventos, execute:
```bash
python -m app.consumer
```

## Variáveis de Ambiente

O projeto utiliza as seguintes variáveis de ambiente (já configuradas no docker-compose.yml):

- `DATABASE_URL`: URL de conexão com o PostgreSQL
- `RABBITMQ_URL`: URL de conexão com o RabbitMQ

## Desenvolvimento Local

1. Crie um ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Execute a aplicação:
```bash
uvicorn app.main:app --reload
```