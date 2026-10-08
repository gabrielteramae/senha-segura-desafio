# Senha segura — validação sem persistir a senha

![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115.0-009688?logo=fastapi&logoColor=white)

POST que só responde se a senha passa em cinco regras. Senha aceita devolve 204 sem corpo. Senha recusada devolve 400 com a lista de todas as falhas, não só a primeira.

## Por que devolver todas as falhas

| Estratégia | Efeito |
| --- | --- |
| Percorre o dicionário `RULES` e acumula mensagens | O cliente corrige tamanho, caixa, dígito e caractere especial de uma vez. |
| Parar na primeira regra | Resposta menor; o chamador só descobre o restante na tentativa seguinte. |

Regras em `password_rules.py`: no mínimo 8 caracteres, uma maiúscula, uma minúscula, um dígito e um caractere fora de `[A-Za-z0-9]`. Não há lista de senhas vazadas, nem pontuação, nem armazenamento.

## Stack

- Python (sem versão pinada no repositório)
- FastAPI 0.115.0 e Uvicorn 0.30.6
- `unittest` da biblioteca padrão

## Estrutura

```
app/
├── main.py             # POST /validate-password
├── password_rules.py   # regras e mensagens
└── schemas.py          # PasswordRequest
tests/
└── test_password_rules.py
requirements.txt
```

## Como rodar

```bash
git clone https://github.com/gabrielteramae/senha-segura-desafio.git
cd senha-segura-desafio
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Endpoints

| Método | Rota | Resposta |
| --- | --- | --- |
| POST | `/validate-password` | Corpo `{"password":"..."}`. 204 se passar; 400 `{"errors":["..."]}` se falhar |

## Testes realizados

`tests/test_password_rules.py` usa `unittest` e cobre só a função `validate_password`: `Senha123!` não gera erro; `abc` inclui as mensagens de tamanho e de dígito. Não sobe a API e não chama o endpoint.

```bash
python -m unittest tests.test_password_rules
```

---

© 2026 Gabriel Teramae Chan
