from fastapi import FastAPI, Response
from fastapi.responses import JSONResponse
from app.schemas import PasswordRequest
from app.password_rules import validate_password

app = FastAPI(
    title="Secure Password API",
    description="Valida se uma senha atende a criterios de seguranca pre-definidos",
    version="1.0.0",
)


@app.post("/validate-password", status_code=204)
def validate(request: PasswordRequest):
    errors = validate_password(request.password)

    if errors:
        return JSONResponse(status_code=400, content={"errors": errors})

    return Response(status_code=204)
