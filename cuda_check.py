import torch

# Check if CUDA (GPU support) is available
print("CUDA Available:", torch.cuda.is_available())

# List all available GPUs
print("Number of GPUs:", torch.cuda.device_count())

# Name of the current GPU
if torch.cuda.is_available():
    print("Current GPU:", torch.cuda.get_device_name(torch.cuda.current_device()))