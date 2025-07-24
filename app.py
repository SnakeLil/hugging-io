#!/usr/bin/env python3
"""
Simple IOPaint server launcher for Hugging Face Space
Uses IOPaint's built-in CLI to avoid dependency conflicts
"""

import subprocess
import sys
import os

def main():
    """Launch IOPaint server using the CLI"""

    # Set environment variables for better compatibility
    os.environ["PYTORCH_ENABLE_MPS_FALLBACK"] = "1"
    os.environ["ONEDNN_PRIMITIVE_CACHE_CAPACITY"] = "1"
    os.environ["LRU_CACHE_CAPACITY"] = "1"
    os.environ["TORCH_CUDNN_V8_API_LRU_CACHE_LIMIT"] = "1"

    # IOPaint CLI command
    cmd = [
        "iopaint", "start",
        "--model", "lama",
        "--host", "0.0.0.0",
        "--port", "7860",
        "--device", "cpu",
        "--low-mem",
        "--disable-nsfw-checker"
    ]

    print("Starting IOPaint server...")
    print(f"Command: {' '.join(cmd)}")

    try:
        # Run IOPaint CLI directly
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error starting IOPaint: {e}")
        sys.exit(1)
    except KeyboardInterrupt:
        print("Server stopped by user")
        sys.exit(0)

if __name__ == "__main__":
    main()

