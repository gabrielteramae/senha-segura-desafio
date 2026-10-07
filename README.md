# Secure Password API

![Python](https://img.shields.io/badge/Python-3.11-3776AB?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115-009688?logo=fastapi&logoColor=white)

Solução para o desafio [`backend-br/desafios/secure-password`](https://github.com/backend-br/desafios/blob/master/secure-password/PROBLEM.md): validar se uma senha é considerada segura com base em critérios pré-definidos.

## Regras de validação

| Critério                     | Regra                                      |
|--------------------------------|-----------------------------------------------|
| Tamanho mínimo                    | Pelo menos 8 caracteres                          |
| Letra maiúscula                     | Pelo menos 1                                       |
| Letra minúscula                       | Pelo menos 1                                        |
| Dígito numérico                        | Pelo menos 1                                         |
| Caractere especial                       | Pelo menos 1 (ex: `!@#$%`)                            |

> **Nota:** a senha de exemplo no `PROBLEM.md` (`vYQIYxO&p$yfI^r`) não contém nenhum dígito, então ela mesma falharia na validação de "pelo menos um dígito numérico" — o JSON de exemplo do desafio ilustra apenas o formato da requisição/resposta, não uma senha necessariamente válida segundo os Requisitos.

## Stack

- **FastAPI** para a API REST
- **Pydantic** para validação de entrada
- Motor de regras isolado em `password_rules.py`, sem dependência de framework — cada critério é uma função pura, fácil de testar e estender

## Estrutura

```
app/
├── main.py            # endpoint POST /validate-password
├── schemas.py           # request/response (Pydantic)
└── password_rules.py      # regras de validacao, puras e testaveis
```

## Como rodar

```bash
git clone https://github.com/gabrielteramae/senha-segura-desafio.git
cd senha-segura-desafio
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8003
```

## Endpoint

```
POST /validate-password
```

**Senha válida**
```bash
curl -i -X POST http://localhost:8003/validate-password \
  -H "Content-Type: application/json" \
  -d '{"password":"Abcd1@fg"}'
```
```
HTTP/1.1 204 No Content
```

**Senha inválida**
```bash
curl -X POST http://localhost:8003/validate-password \
  -H "Content-Type: application/json" \
  -d '{"password":"abc"}'
```
```json
{
  "errors": [
    "A senha deve possuir pelo menos 8 caracteres",
    "A senha deve conter pelo menos uma letra maiuscula",
    "A senha deve conter pelo menos um digito numerico",
    "A senha deve conter pelo menos um caractere especial"
  ]
}
```

---

© 2026 Gabriel Teramae Chan
