import os

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(title="Dada Cloud FastAPI starter")

PAGE = """
<!doctype html><html lang="ru"><head><meta charset="utf-8">
<title>Dada Cloud — FastAPI starter</title></head>
<body style="font-family:system-ui,sans-serif;max-width:640px;margin:80px auto;padding:24px;line-height:1.6">
<h1 style="font-size:40px">API работает на Dada Cloud</h1>
<p>Этот FastAPI задеплоен из GitHub в Dada Cloud — российское облако с оплатой
рублями и данными в РФ. Эндпоинт <code>/api/health</code> отдаёт JSON.</p>
<p><a href="https://cloud.dada-tuda.ru" style="color:#2563eb">cloud.dada-tuda.ru &rarr;</a></p>
</body></html>
"""


@app.get("/", response_class=HTMLResponse)
def index() -> str:
    return PAGE


@app.get("/api/health")
def health() -> dict:
    return {"status": "ok", "platform": "dada-cloud"}
