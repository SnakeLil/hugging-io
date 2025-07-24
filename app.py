import subprocess

if __name__ == "__main__":
    cmd = "iopaint start --model lama --host 0.0.0.0 --port 7860"
    # start subprocess using cmd
    subprocess.run(cmd, shell=True)

