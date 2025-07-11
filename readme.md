# # # # About the project
# # This is the part of the case developed by Kate Dolgova (a.k.a. hedgehog), member of the Silent Guardians team in AI-hackathon being held in the MIPT 2-3 July, 2025. Includes architecture of the CNN and RNN created to solve the Sber case.

# At the moment this markdown consists of short description and tensorflow activation guide, but the project will be improved

# # # How to compile the code with TensorFlow in VS Code?

# # The sequence of actions
# Step 1
*In the Ubuntu-24.04 terminal print:*
cd /mnt/c/Users/Катюша/Desktop/Sber-case-2025 # to open your repository
code . # to open VS Code in WSL
# Step 2
*Open terminal (push Ctrl+Shift+`) in VS Code (all actions below are being conducted here). Write there the following:*
python3 -m venv ~/tf_gpu # create virtual environment (DO IT ONLY ONCE: when creating it for the first time)
source ~/tf_gpu/bin/activate # activate virtual environment (you may SKIP doing this action every time, if modify settings.json)
pwd # check the path (in exact case it should be "/mnt/c/Users/Катюша/Desktop/Sber-case-2025")
# Step 3
*Verify being in the right environment:*
In the left down corner (right below the Account & Settings icons) you should see "WSL:Ubuntu-24.04", in the right down corner (just above the date and time in your Windows 10) - "3.12.3 (tf_gpu)"
# Step 4
*Quickly check if something went wrong:*
python -c "import tensorflow as tf; \
print(f'TensorFlow: {tf.__version__}'); \
print(f'GPU доступен: {bool(tf.config.list_physical_devices(\"GPU\"))}')"
*If everything is correct, you will see the output:*
>TensorFlow: 2.19.0
>GPU доступен: True
# Step 5
*Finally run the diagnostic code:*
python gpu_test.py
*Gain the following:*
>TF Version: 2.19.0
>GPU доступен: [PhysicalDevice(name='/physical_device:GPU:0', device_type='GPU')]
*And work on your project*

# # Additional notes
# Step 2
*To make activation of the environment being automatical, find settings.json (push Ctrl+Shift+P -> type "open settings" -> choose "Preferences: Open User Settings (JSON)"), open and modify it in the certain way: into the main brackets, in the ending, add*
"terminal.integrated.profiles.linux": {
    "bash": {
      "path": "bash",
      "args": ["-c", "source ~/tf_gpu/bin/activate && exec bash"]
    }
  },
  "terminal.integrated.defaultProfile.linux": "bash"
*Then save changes and restart the VS Code*
# Step 3
*In the case VS Code doesn't see the interpreter, do the following:*
push Ctrl+Shift+P -> find "Python: Select Interpreter" ->  choose ./tf_gpu/bin/python
# Step 4
*If there is no tensorflow detected, but your environment is ale=ready activated, install it, use the following line only ONCE though:*
pip install tensorflow[and-cuda]
# Step 5
*In the other way, if tensorflow detected, but works bad, try:*
pip uninstall -y tensorflow tensorflow-gpu keras tensorflow-cuda # delete tf with buggs
pip install --no-cache-dir tensorflow[and-cuda]==2.19.0 # install cuda-suitable tf