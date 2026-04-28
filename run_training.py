import os

# Set the paths using environment variables with fallback
DATA_PATH = os.getenv('DATA_PATH', './data')
MODEL_PATH = os.getenv('MODEL_PATH', './models')

# Check if GPU is available
if os.getenv('CUDA_VISIBLE_DEVICES') is None:
    raise ValueError('No CUDA devices are visible. Please set CUDA_VISIBLE_DEVICES correctly.')

# Other code remains unchanged...