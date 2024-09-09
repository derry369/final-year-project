import subprocess
import time

def run_script(script_path):
    try:
        print(f"Running the script: {script_path}")
        subprocess.check_call(["python3", script_path])
        print("Script executed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error running script: {e}")

def main():
    script_path = 'capture_udp.py'  # Replace with the path to your existing script
    interval = 5  # Time in seconds to wait before running the script again

    # Initial run of the script
    run_script(script_path)

    # Loop to run the script again after the interval
    while True:
        print(f"Waiting for {interval} seconds before running the script again...")
        time.sleep(interval)
        run_script(script_path)

if __name__ == "__main__":
    main()
