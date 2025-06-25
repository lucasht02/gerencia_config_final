# Restaurante Software

Uma aplicação para gerenciar cadastro de pratos, controle de estoque, processamento de pedidos e geração de relatórios de vendas, com pipeline de CI/CD completo usando Docker e GitHub Actions.

---

## 🔍 Visão Geral

Este projeto demonstra um Plano de Gerenciamento de Configuração aplicado ao “Restaurante Software”, cobrindo:

- Controle de versão (Git/GitHub) com convenções de branches e versionamento semântico  
- Estrutura de código em Python 3.12 com testes automatizados (unitário, integração e aceitação) via pytest  
- Empacotamento e execução isolada em Docker (Dockerfile e opcional Docker Compose)  
- Pipeline de CI/CD no GitHub Actions para build, testes e publicação automática de imagem Docker  

---

## 🚀 Começando

### Pré-requisitos

- Linux / Windows com WSL2  
- Python 3.12  
- Docker e Docker Compose (opcional)  
- Git  

### Instalação local

```bash
# 1. Clone o repositório
git clone git@github.com:lucasht02/restaurante-software.git
cd restaurante-software

# 2. Crie e ative um ambiente virtual
python3 -m venv venv
source venv/bin/activate

# 3. Instale dependências
pip install --upgrade pip setuptools
pip install -r requirements.txt

# 4. Para executar os testes
pytest --maxfail=1 --disable-warnings -q
