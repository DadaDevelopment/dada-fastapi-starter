# FastAPI starter for Dada Cloud

[![Deploy to Dada Cloud](https://img.shields.io/badge/Deploy%20to-Dada%20Cloud-2563eb?style=for-the-badge)](https://cloud.dada-tuda.ru/deploy?repo=DadaDevelopment/dada-fastapi-starter&utm_source=github_template&utm_campaign=fastapi)

Минимальный шаблон FastAPI, готовый к деплою из GitHub в **[Dada Cloud](https://cloud.dada-tuda.ru)** — российское облако для разработчиков.

## Зачем это нужно

Хостить Python-API за рубежом стало неудобно: Heroku убил бесплатный тариф, зарубежные карты не проходят. Dada Cloud — деплой прямо из GitHub, оплата рублями, данные в России (152-ФЗ). Есть бесплатный тариф.

## Как задеплоить

1. Нажми **Use this template → Create a new repository** (или форкни репозиторий).
2. Зарегистрируйся на [cloud.dada-tuda.ru](https://cloud.dada-tuda.ru/deploy?repo=DadaDevelopment/dada-fastapi-starter&utm_source=github_template&utm_campaign=fastapi).
3. Подключи свой GitHub, выбери этот репозиторий — Dada соберёт образ по `Dockerfile` и выдаст HTTPS-домен.
4. Каждый `git push` пересобирает приложение автоматически.

## Эндпоинты

- `GET /` — HTML-страница.
- `GET /api/health` — `{"status": "ok", "platform": "dada-cloud"}`.

## Локальный запуск

```bash
pip install -r requirements.txt
uvicorn main:app --reload
# http://localhost:8000
```

## Лицензия

MIT — используй как хочешь.
