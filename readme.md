## Installation & Running with Docker

### Build the Docker image

```bash
docker build -t upsonic-ocr-case .
```

### Run the container

```bash
docker run -p 8000:8000 upsonic-ocr-case
```

The API will be available at `http://localhost:8000`

## API Usage

### Process OCR

**Endpoint:** `POST /ocr`

**Request Body:**

```json
{
  "ocr_strategy": "easy_ocr",
  "backup_strategy": "rapid_ocr"
}
```

## Improvments

I could have setup aws s3 for files
