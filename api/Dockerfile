FROM python:3.11

WORKDIR /app

COPY main.py /app

RUN pip install --no-cache-dir fastapi uvicorn motor

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
