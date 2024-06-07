# fastapi-tdd

Projeto de exemplo para desenvolvimento orientado a testes (TDD) com FastAPI.

## Instalação

Para instalar e configurar o ambiente de desenvolvimento, siga as etapas abaixo:

1. **Configurar a Política de Execução do PowerShell:**

```bash
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

```

2. **Instalar pyenv-win:**

```bash
Invoke-WebRequest -UseBasicParsing -Uri "https://raw.githubusercontent.com/pyenv-win/pyenv-win/master/pyenv-win/install-pyenv-win.ps1" -OutFile "./install-pyenv-win.ps1"; &"./install-pyenv-win.ps1"
```

3. **Instalar poetry**
```bash
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -
```

4. **Instalar pipx**
```bash
python -m pip install --user pipx
```

5. **Configurar Path pipx**
```bash
python -m pipx ensurepath
```

6. **Iniciar configuração poetry e inserção de dependencias**
```bash
poetry init
```

7. **Instalar dependencias**
```bash
poetry install
```

uvicorn store.main:app --reload

poetry run pre-commit install


set PRE_COMMIT_ALLOW_NO_CONFIG=1
git commit -m ":tada: feat(docs) Project Configs First Commit"
git status


poetry run pytest


poetry run python -m store.main

##


### Contribuindo
1. Faça um fork do projeto.
2. Crie uma nova branch (git checkout -b feature/nova-feature).
3. Commit suas mudanças (git commit -am 'Adicione uma nova feature').
4. Envie para a branch (git push origin feature/nova-feature).
5. Crie um novo Pull Request.
