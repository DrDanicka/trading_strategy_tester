import glob
import os
import subprocess
import sys
import matplotlib.pyplot as plt

def create_loss_curve(path: str):
    train_loss = []
    val_loss = []

    with open(path, 'r') as f:
        for line in f:
            if "Train loss" in line:
                train_loss.append(float(line.split("Train loss")[-1].strip().split(',')[0].strip()))
            if "Val loss" in line:
                val_loss.append(float(line.split("Val loss")[-1].strip().split(',')[0].strip()))


    # Training loss every 10 iters
    train_iters = [i * 10 for i in range(1, len(train_loss) + 1)]

    # Validation loss every 20 iters
    steps_per_eval = 20
    val_iters = [1] + [i for i in range(steps_per_eval, steps_per_eval * len(val_loss), steps_per_eval)]

    # Plot
    name = path.split('/')[-1].split('.')[0]
    param = name.split('_')[-1]
    plt.figure(figsize=(10, 10))
    plt.plot(train_iters, train_loss, label="Train Loss", marker='o')
    plt.plot(val_iters, val_loss, label="Validation Loss", marker='x')
    plt.xlabel("Iteration")
    plt.ylabel("Loss")
    plt.title(f"Training & Validation Loss Curves for {'all fields' if param == 'all' else f'parameter {param}'}")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(f"loss_curves/{name}.png")

def run_command(cmd, log_file=None):
    print(f">>> Running: {' '.join(cmd)}")

    if log_file:
        with open(log_file, "w") as log:
            process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
            for line in process.stdout:
                print(line, end='')  # Print to stdout
                log.write(line)  # Write to log file
            process.wait()
    else:
        # Just stream directly to terminal
        process = subprocess.Popen(cmd)
        process.wait()

    if process.returncode != 0:
        print(f"Command failed: {' '.join(cmd)}")
        sys.exit(process.returncode)

def single_model_train(model, data, learning_rate, iters, fine_tune_type, name, skip_training=False):
    # Step 1: Train
    if not skip_training:
        run_command([
            "mlx_lm.lora",
            "--model", model,
            "--train",
            "--data", data,
            "--learning-rate", str(learning_rate),
            "--iters", str(iters),
            "--fine-tune-type", fine_tune_type,
            "--steps-per-eval", "20",
            "--adapter-path", f"./adapters/adapters_{name}",
        ], log_file=f"logs/{name}.log")

        # Step 2: Create loss_curve
        create_loss_curve(f"logs/{name}.log")

        # Step 3: Fuse + GGUF
        run_command([
            "mlx_lm.fuse",
            "--model", model,
            "--save-path", "./fused_model",
            "--adapter-path", f"./adapters/adapters_{name}",
            "--de-quantize"
        ])

        # Step 4: Convert to GGUF using script
        run_command([
            "python3", "llama.cpp/convert_hf_to_gguf.py",
            "./fused_model",
            "--outfile", f"./fused_model/{name}.gguf",
            "--no-lazy",
            "--verbose"
        ])

    # Step 5: Modelfile
    file_to_read = 'modelfiles/Modelfile_llama3' if model.startswith('meta-llama') else 'modelfiles/Modelfile_qwen'

    with open(file_to_read, 'r') as f:
        modelfile = f.read()
        modelfile = f"FROM ../fused_model/{name}.gguf\n" + modelfile
    with open('modelfiles/Modelfile', 'w') as f:
        f.write(modelfile)

    # Step 6: Ollama create
    run_command(["ollama", "create", name, "-f", "./modelfiles/Modelfile"])
    print(f"Done: {name}")

    # Step 7: Clean up
    for file in glob.glob("fused_model/*.safetensors"):
        os.remove(file)
