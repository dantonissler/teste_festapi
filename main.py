from fastapi import FastAPI, Request
import uvicorn

app = FastAPI()

@app.post("/webhook")
async def webhook(req: Request):
    data = await req.json()
    print("📦 Recebido:", data)
    return {"status": "ok"}

@app.get("/")
def root():
    return {"msg": "Webhook ativo 🚀"}
