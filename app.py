import os
from pathlib import Path
from fastapi import FastAPI
from iopaint.api import Api
from iopaint.schema import ApiConfig, Device

# Set environment variables for Hugging Face Space
os.environ["PYTORCH_ENABLE_MPS_FALLBACK"] = "1"
os.environ["ONEDNN_PRIMITIVE_CACHE_CAPACITY"] = "1"
os.environ["LRU_CACHE_CAPACITY"] = "1"
os.environ["TORCH_CUDNN_V8_API_LRU_CACHE_LIMIT"] = "1"

# Initialize FastAPI app
app = FastAPI(title="IOPaint API Server", version="1.0.0")

# Configure IOPaint API
api_config = ApiConfig(
    host="0.0.0.0",
    port=7860,
    inbrowser=False,
    model="lama",  # Use LAMA model for inpainting
    device=Device.cpu,  # Use CPU for Hugging Face Space
    low_mem=True,  # Enable low memory mode
    no_half=False,
    cpu_offload=False,
    disable_nsfw_checker=True,  # Disable NSFW checker for API usage
    local_files_only=False,
    cpu_textencoder=False,
    input=None,
    mask_dir=None,
    output_dir=None,
    quality=100,
    enable_interactive_seg=False,
    enable_remove_bg=False,
    enable_anime_seg=False,
    enable_realesrgan=False,
    enable_gfpgan=False,
    enable_restoreformer=False,
)

# Initialize IOPaint API
iopaint_api = Api(app, api_config)

if __name__ == "__main__":
    # Launch the IOPaint API server
    iopaint_api.launch()

