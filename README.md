# 🚗 Carros — Sistema de Gestão de Inventário de Veículos

[![Django](https://img.shields.io/badge/Django-5.1.15-092e20?style=for-the-badge&logo=django)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.12-3776ab?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![OpenAI](https://img.shields.io/badge/OpenAI-gpt--3.5--turbo-412991?style=for-the-badge&logo=openai&logoColor=white)](https://platform.openai.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

Aplicação web em **Django** para gestão de inventário de veículos, com **CRUD completo**, autenticação de usuários, geração automática de descrições de venda via **OpenAI** e um painel de inventário que se atualiza em tempo real a cada movimentação de estoque.

---

## ✨ Funcionalidades

### 📝 Gestão de Veículos (CRUD)
- Cadastro, edição, detalhamento e exclusão de veículos: **marca, modelo, ano de fabricação, ano do modelo, placa, valor, foto e biografia**.
- **Busca dinâmica** por modelo direto na listagem (`?search=`).
- **Validações de negócio** via Django Forms — valor mínimo de **R$ 20.000** e ano de fabricação mínimo.

### 🤖 Descrição por Inteligência Artificial
- Geração automática de uma **descrição de venda** para cada carro usando a API da **OpenAI** (`gpt-3.5-turbo`), a partir de marca, modelo e ano.
- Disparada de forma transparente por um **signal `pre_save`** — só é gerada quando o campo `bio` está vazio.
- **Degradação segura:** se a `OPENAI_API_KEY` não estiver configurada ou a API falhar, o sistema grava uma descrição padrão em vez de quebrar o cadastro.

### 📊 Painel de Inventário
- O modelo `CarInventory` registra **quantidade total de veículos** e **valor total do estoque** a cada criação ou remoção de carro (signals `post_save` / `post_delete`).
- Histórico persistente e ordenado por data, permitindo acompanhar a evolução do estoque.

### 🔐 Autenticação e Segurança
- Registro, login e logout de usuários.
- As rotas de **criação, edição e exclusão** exigem login (`@login_required`).

---

## 🛠️ Stack

| Camada | Tecnologia |
|---|---|
| Framework | Django 5.1.15 |
| Linguagem | Python 3.12 |
| Banco de dados | SQLite (desenvolvimento) |
| IA | OpenAI API (`gpt-3.5-turbo`) |
| Imagens | Pillow |
| Configuração | python-dotenv |
| HTTP / dados | httpx, httpcore, pydantic |

> **Segurança:** as dependências são fixadas em versões sem vulnerabilidades conhecidas (auditadas com `pip-audit`). Reaudite após qualquer alteração no `requirements.txt`.

---

## 🗺️ Rotas

| Método | Rota | Descrição | Acesso |
|---|---|---|---|
| GET | `/cars/` | Listagem de veículos (com busca) | Público |
| GET | `/car/<pk>/` | Detalhe do veículo | Público |
| GET/POST | `/new_car/` | Novo veículo | Autenticado |
| GET/POST | `/car/<pk>/update/` | Editar veículo | Autenticado |
| GET/POST | `/car/<pk>/delete/` | Excluir veículo | Autenticado |
| GET/POST | `/register/`, `/login/`, `/logout/` | Autenticação | Público |
| — | `/admin/` | Django Admin | Superusuário |

---

## ⚙️ Como Executar

### Pré-requisitos
- **Python 3.12** (mínimo 3.9, por conta do Pillow 12).
- Chave da API da OpenAI *(opcional — sem ela, as descrições usam um texto padrão)*.

### Passo a passo

```bash
# 1. Clonar o repositório
git clone https://github.com/rodrigodssa/carros.git
cd carros

# 2. Criar e ativar o ambiente virtual
python -m venv venv
source venv/bin/activate        # Linux/macOS
# venv\Scripts\activate         # Windows

# 3. Instalar as dependências
pip install -r requirements.txt

# 4. Configurar variáveis de ambiente (ver seção abaixo)
cp .env.example .env            # e edite com suas chaves

# 5. Aplicar as migrações
python manage.py migrate

# 6. Criar um superusuário (acesso ao Admin)
python manage.py createsuperuser

# 7. Iniciar o servidor
python manage.py runserver
```

Acesse **http://127.0.0.1:8000/cars/**.

### Variáveis de Ambiente

O projeto carrega um arquivo `.env` na raiz via `python-dotenv`. Use o `.env.example` como base:

```env
# Django
SECRET_KEY=sua-secret-key
DEBUG=True

# OpenAI
OPENAI_API_KEY=sua_chave_aqui
```

> Sem a `OPENAI_API_KEY`, o cadastro de veículos continua funcionando normalmente — apenas a descrição por IA é substituída por um texto padrão. **Nunca** versione o seu `.env` real.

---

## 📁 Estrutura do Projeto

```
carros/
├── app/                # Configurações do projeto Django (settings, urls, wsgi/asgi)
├── accounts/           # Autenticação: registro, login e logout
├── cars/               # App principal
│   ├── models.py       # Brand, Car, CarInventory
│   ├── views.py        # Class-Based Views (List, Create, Detail, Update, Delete)
│   ├── forms.py        # CarModelForm com validações de negócio
│   ├── signals.py      # IA (pre_save) + atualização de inventário (post_save/post_delete)
│   └── migrations/
├── openai_api/         # Cliente da OpenAI para geração de descrições
├── manage.py
└── requirements.txt
```

---

## 🧩 Modelos de Dados

- **`Brand`** — marca do veículo (`name`).
- **`Car`** — veículo (`model`, `brand`, `factory_year`, `model_year`, `plate`, `value`, `photo`, `bio`).
- **`CarInventory`** — snapshot do estoque (`cars_count`, `cars_value`, `created_at`), gerado automaticamente a cada mudança.

---

## 📄 Licença

Distribuído sob a licença **MIT**. Consulte o arquivo [LICENSE](LICENSE) para mais detalhes.

---

Desenvolvido por **[Rodrigo](https://github.com/rodrigodssa)** durante o curso Django Master.
