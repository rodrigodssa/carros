# 🚗 Carros Management System

[![Django](https://img.shields.io/badge/Django-5.1-092e20?style=for-the-badge&logo=django)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.x-3776ab?style=for-the-badge&logo=python)](https://www.python.org/)
[![OpenAI](https://img.shields.io/badge/OpenAI-Integrated-412991?style=for-the-badge&logo=openai)](https://openai.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

Um sistema completo de gerenciamento de inventário de veículos desenvolvido com **Django**, integrando funcionalidades modernas como geração de descrições automáticas via **Inteligência Artificial (OpenAI)** e rastreamento de estoque em tempo real.

---

## 🚀 Funcionalidades Principal

### 📝 Gestão de Veículos (CRUD Completo)
- **Cadastro e Edição:** Controle total sobre os dados dos veículos (Marca, Modelo, Ano de Fabricação, Ano do Modelo, Placa, Valor e Foto).
- **Validações Inteligentes:** Regras de negócio aplicadas via Django Forms (ex: valor mínimo de R$20.000 e ano mínimo de 1980).
- **Busca Dinâmica:** Sistema de filtragem por modelo diretamente na interface de listagem.

### 🤖 Inteligência Artificial
- **Auto-Bio:** Utiliza a API da **OpenAI** para gerar automaticamente biografias criativas para cada carro cadastrado, baseando-se no modelo, marca e ano.
- **Processamento via Signals:** A integração com a IA ocorre de forma transparente através de Django Signals (`pre_save`).

### 📊 Painel de Inventário
- **Atualização em Tempo Real:** Sempre que um carro é adicionado ou removido, o sistema atualiza automaticamente o total de veículos e o valor total do estoque (`CarInventory`).
- **Histórico de Estoque:** Rastreamento persistente para análise de crescimento do inventário.

### 🔐 Autenticação e Segurança
- **Controle de Acesso:** Áreas de criação, edição e exclusão são protegidas por login.
- **Gestão de Usuários:** Sistema completo de Registro e Login integrado.

---

## 🛠️ Tecnologias Utilizadas

- **Framework:** [Django 5.1](https://docs.djangoproject.com/en/5.1/)
- **Linguagem:** [Python 3.x](https://www.python.org/)
- **Inteligência Artificial:** [OpenAI API](https://platform.openai.com/docs/introduction)
- **Banco de Dados:** SQLite (Desenvolvimento)
- **Processamento de Imagem:** [Pillow](https://python-pillow.org/)
- **Outros:** Pydantic, HTTPX (para comunicações robustas com APIs externas).

---

## ⚙️ Como Executar o Projeto

### Pré-requisitos
- Python 3.10 ou superior instalado.
- Chave de API da OpenAI (opcional para as funções de IA).

### Passos para Instalação

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/rodrigodssa/carros.git
    cd carros
    ```

2.  **Crie e ative um ambiente virtual:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/macOS
    # venv\Scripts\activate   # Windows
    ```

3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure as variáveis de ambiente (se necessário):**
    *Crie um arquivo `.env` na raiz ou configure as variáveis para sua `OPENAI_API_KEY`.*

5.  **Execute as migrações do banco de dados:**
    ```bash
    python manage.py migrate
    ```

6.  **Crie um superusuário para acessar o Admin:**
    ```bash
    python manage.py createsuperuser
    ```

7.  **Inicie o servidor:**
    ```bash
    python manage.py runserver
    ```

O projeto estará disponível em `http://127.0.0.1:8000/`.

---

## 📁 Estrutura do Projeto

- `cars/`: App principal contendo a lógica de veículos, models, views e templates.
- `accounts/`: Gerenciamento de autenticação de usuários.
- `app/`: Configurações centrais do projeto Django.
- `templates/`: Arquivos HTML modernos e responsivos.

---

## 📄 Licença

Este projeto está sob a licença **MIT**. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

Desenvolvido por [Rodrigo](https://github.com/rodrigodssa) durante o curso Django Master.
