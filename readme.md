#### About the project
## This is the part of the case developed by **Kate Dolgova** (a.k.a. *hedgehog*), member of the **Silent Guardians** team in *AI-hackathon* being held in the *MIPT 2-3 July, 2025*. 
## The repository containes architecture of the CNN and RNN created to solve the Sber case.

# Currently this README contains a short description and a TensorFlow activation guide, although the project will be expanded later.

### How to Compile & Run PyTorch & TensorFlow code in VS Code (WSL)

## The sequence of actions

# Step 1
In the Ubuntu-24.04 (WSL) terminal print:
```ruby
cd /mnt/c/Users/Катюша/Desktop/Sber-case-2025    # to open your repository
code .                                           # to open VS Code in WSL
```
# Step 2
Open terminal (push **Ctrl+Shift+`**) in VS Code (all actions below are being conducted here). Write there the following:
```ruby
python3 -m venv ~/tf_gpu       # create virtual environment (DO IT ONLY ONCE: when creating it for the first time)
source ~/tf_gpu/bin/activate   # activate virtual environment (you may SKIP doing this action every time, if you modify settings.json)
pwd                            # check the path (in exact case it should be "/mnt/c/Users/Катюша/Desktop/Sber-case-2025")
```
# Step 3
Verify being in the right environment:
In the lower left corner (right below the Account & Settings icons) you should see "WSL: Ubuntu-24.04", in the lower (for .py) or upper (for .ipynb) right corner - "3.12.3 (tf_gpu)" or "tf_gpu (Python 3.12.3)" (*status-bar*). CLick on the last one and check if "tf_gpu (Python 3.12.3) ~/tf_gpu/bin/python" is currently selected.
# Step 4
Finally run the diagnostic scripts:
```ruby
python pt_gpu_test.py
python tf_gpu_test.py
```
Expected output:
```ruby
PT Version: 2.6.0+cu124            # for your CUDA v12.4
GPU доступен: True, NVIDIA GeForce GTX 1650
TF Version: 2.18.0
GPU доступен: [PhysicalDevice(name='/physical_device:GPU:0', device_type='GPU')]
```
And work on your project

## Additional notes
# Step 2
To make activation of the environment being automatical, find **settings.json** (push Ctrl+Shift+P -> type "open settings" -> choose "Preferences: Open User Settings (JSON)"), open and modify it in the certain way: into the main brackets (exactly in the ending) add
```ruby
"terminal.integrated.profiles.linux": {
    "bash": {
      "path": "bash",
      "args": ["-c", "source ~/tf_gpu/bin/activate && exec bash"]
    }
  },
  "terminal.integrated.defaultProfile.linux": "bash"
```
Then save changes and restart the VS Code
# Step 3
In the case VS Code doesn't see the interpreter, do the following:
>push Ctrl+Shift+P -> find "Python: Select Interpreter" ->  choose ~/tf_gpu/bin/python
# Step 4
If there is no PyTorch/Tensorflow detected or your PyTorch/Tensorflow is broken try the following (only ONCE):
```ruby
# PyTorch
pip uninstall -y torch torchvision torchaudio                                                  # delete torch with buggs (the 2nd case - DO, 1st case - SKIP)
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124    # install cuda-suitable torch
#TensorFlow
pip uninstall -y tensorflow tensorflow-gpu keras tensorflow-cuda                               # delete tensorflow with buggs (the 2nd case - DO, 1st case - SKIP)
pip install --no-cache-dir tensorflow[and-cuda]==2.18.0                                        # install cuda-suitable tensorflow
```

### How to check the GPU memory usage
Open another bash here (in the VS Code terminal) and type:
```ruby
watch -n 1 nvidia-smi  # updates every second
```
OR
```ruby
pip install gpustat    # use only ONCE
gpustat -i 1           # updates evry second
```
*Then monitor the percentage, temperature and *

### Mini-check before every new session
In the WSL terminal:
```ruby
cd /mnt/c/Users/Катюша/Desktop/Sber-case-2025
code .
```
In the VS Code terminal (bash, it should be open after the previous step):
```ruby                      
source ~/tf_gpu/bin/activate
python tf_gpu_test.py        # TensorFlow GPU test
python pt_gpu_test.py        # PyTorch GPU test
```

### Verified software stack (author’s laptop, GeForce GTX 1650)

| NVIDIA Driver | CUDA     | cuDNN      | Python     | TensorFlow | PyTorch   |
| ------------- | -------- | ---------- | ---------- | ---------- | --------- |
| **576.88**    | **12.4** | **9.10.2** | **3.12.3** | **2.18.0** | **2.6.0** |