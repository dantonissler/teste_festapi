from fastapi import FastAPI, Request, Body
from fastapi.responses import JSONResponse
import json
import logging
import uvicorn

logging.basicConfig(level=logging.INFO)
app = FastAPI(title="Webhook Jusbrasil")

@app.post("/webhook")
async def webhook(req: Request, data: dict = Body(...)):
    # Tenta JSON; se falhar, tenta corpo cru; se vier vazio, aceita mesmo assim
    try:
        data = await req.json()
    except Exception:
        body = await req.body()
        if body:
            try:
                data = json.loads(body.decode("utf-8", errors="ignore"))
            except Exception:
                data = body.decode("utf-8", errors="ignore")  # texto cru
        else:
            data = None  # sem corpo

    logging.info("📦 Webhook recebido: %r", data)
    return JSONResponse({"status": "ok"}, status_code=200)


@app.get("/")
def root():
    return {"msg": "Webhook ativo 🚀"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080)
