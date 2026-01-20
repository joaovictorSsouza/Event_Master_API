# 🚀 Event Master API

Uma API RESTful profissional para gerenciamento de eventos, desenvolvida com **Django** e **Django REST Framework (DRF)**. Este projeto demonstra a implementação de autenticação segura, relacionamentos de banco de dados e automação de lógica de negócio.

## ✨ Funcionalidades Principais

- **🛡️ Autenticação JWT:** Sistema de login moderno utilizando JSON Web Tokens (Access e Refresh Tokens).
- **👤 Cadastro Seguro:** Serializer customizado que utiliza `create_user` para garantir que senhas sejam criptografadas (hashing) no banco de dados.
- **📅 Gestão de Eventos:** CRUD completo (Create, Read, Update, Delete) para eventos.
- **🤖 Automação de Propriedade:** Uso do método `perform_create` para vincular automaticamente o evento ao usuário logado, impedindo a manipulação manual do campo `owner`.
- **🔐 Proteção de Dados:** Campos sensíveis como `password` configurados como `write_only`.

## 🛠️ Tecnologias Utilizadas

- **Python 3.10+**
- **Django 5.x**
- **Django REST Framework**
- **Simple JWT** (Autenticação)
- **SQLite** (Banco de dados de desenvolvimento)

---

## ⚙️ Como Instalar e Rodar o Projeto

### 1. Clonar o repositório

```bash
git clone [https://https://github.com/joaovictorSsouza/Event_Master_API](https://https://github.com/joaovictorSsouza/Event_Master_API)
cd Event_Master_API
```

### 2. Configurar o ambiente virtual

```bash
python -m venv venv
# Ativar no Windows:
venv\Scripts\activate
# Ativar no Linux/Mac:
source venv/bin/activate
```

### 3. Instalar dependências

```bash
pip install -r requirements.txt
```

### 4. Preparar o Banco de Dados

```bash
python manage.py migrate
python manage.py createsuperuser
```

### 5. Iniciar o Servidor

```bash
python manage.py runserver
```

### 6. Documentação da API (EndPoints)
