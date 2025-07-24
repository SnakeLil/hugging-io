---
title: Iopaint Server
emoji: ⚡
colorFrom: yellow
colorTo: red
sdk: docker
pinned: false
license: apache-2.0
---

# IOPaint Server

A Hugging Face Space deployment of IOPaint - an AI-powered image inpainting tool.

## Features

- **Image Inpainting**: Remove unwanted objects, defects, watermarks, or people from images
- **API Access**: RESTful API endpoints for programmatic access
- **LAMA Model**: Uses the state-of-the-art LAMA model for high-quality inpainting
- **CPU Optimized**: Configured for CPU inference suitable for Hugging Face Spaces

## API Usage

### Endpoint

```
POST https://lilsnakerr-iopaint-server.hf.space/api/v1/inpaint
```

### Parameters

- `image`: The input image file (multipart/form-data)
- `mask`: The mask image file indicating areas to inpaint (multipart/form-data)

### Example using curl

```bash
curl -X POST \
  https://lilsnakerr-iopaint-server.hf.space/api/v1/inpaint \
  -F "image=@input.jpg" \
  -F "mask=@mask.png" \
  -o result.png
```

### Example using Python

```python
import requests

url = "https://lilsnakerr-iopaint-server.hf.space/api/v1/inpaint"

with open("input.jpg", "rb") as img_file, open("mask.png", "rb") as mask_file:
    files = {
        "image": img_file,
        "mask": mask_file
    }
    response = requests.post(url, files=files)

    if response.status_code == 200:
        with open("result.png", "wb") as f:
            f.write(response.content)
```

## Local Development

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Test the setup:
   ```bash
   python test_local.py
   ```

3. Run the server:
   ```bash
   python app.py
   ```

## Docker Build

```bash
docker build -t iopaint-server .
docker run -p 7860:7860 iopaint-server
```

## Notes

- The server uses CPU inference for compatibility with Hugging Face Spaces
- Low memory mode is enabled to reduce resource usage
- The LAMA model will be downloaded automatically on first run

Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference
