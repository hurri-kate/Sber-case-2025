import torch
print("PT Version:", torch.__version__)          
print(f"GPU доступен: {torch.cuda.is_available()}, {torch.cuda.get_device_name(0)}")