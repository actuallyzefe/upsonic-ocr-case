
FROM python:3.12-slim


WORKDIR /app

#  OpenCV (required by easyocr)
RUN apt-get update && apt-get install -y \
    libgl1 \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

COPY pyproject.toml ./


# use pyproject.toml instead ?
RUN pip install --no-cache-dir \
    easyocr>=1.7.2 \
    fastapi>=0.121.1 \
    onnxruntime>=1.23.2 \
    pydantic>=2.12.4 \
    rapidocr>=3.4.2 \
    uvicorn>=0.38.0


COPY app.py ./
COPY ocr.py ./
COPY random-invoice.png ./


EXPOSE 8000


CMD ["python", "app.py"]
