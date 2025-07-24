#!/usr/bin/env python3
"""
Local test script to verify IOPaint setup
"""

import sys
import traceback

def test_imports():
    """Test if all required packages can be imported"""
    print("Testing imports...")
    
    try:
        import torch
        print(f"✓ PyTorch {torch.__version__}")
    except ImportError as e:
        print(f"✗ PyTorch import failed: {e}")
        return False
    
    try:
        import cv2
        print(f"✓ OpenCV {cv2.__version__}")
    except ImportError as e:
        print(f"✗ OpenCV import failed: {e}")
        return False
    
    try:
        import numpy as np
        print(f"✓ NumPy {np.__version__}")
    except ImportError as e:
        print(f"✗ NumPy import failed: {e}")
        return False
    
    try:
        from PIL import Image
        print(f"✓ Pillow {Image.__version__}")
    except ImportError as e:
        print(f"✗ Pillow import failed: {e}")
        return False
    
    try:
        import iopaint
        print("✓ IOPaint imported successfully")
    except ImportError as e:
        print(f"✗ IOPaint import failed: {e}")
        return False
    
    try:
        from iopaint.api import Api
        from iopaint.schema import ApiConfig, Device
        print("✓ IOPaint API components imported successfully")
    except ImportError as e:
        print(f"✗ IOPaint API import failed: {e}")
        return False
    
    return True

def test_config():
    """Test if IOPaint configuration works"""
    print("\nTesting IOPaint configuration...")
    
    try:
        from iopaint.schema import ApiConfig, Device
        
        config = ApiConfig(
            host="127.0.0.1",
            port=7860,
            model="lama",
            device=Device.cpu,
            low_mem=True,
            disable_nsfw_checker=True,
        )
        print("✓ IOPaint configuration created successfully")
        return True
    except Exception as e:
        print(f"✗ IOPaint configuration failed: {e}")
        traceback.print_exc()
        return False

def main():
    print("IOPaint Setup Test")
    print("=" * 50)
    
    if not test_imports():
        print("\n❌ Import test failed!")
        sys.exit(1)
    
    if not test_config():
        print("\n❌ Configuration test failed!")
        sys.exit(1)
    
    print("\n✅ All tests passed! IOPaint setup looks good.")
    print("\nYou can now run: python app.py")

if __name__ == "__main__":
    main()
