import subprocess
import time
import signal
import os

# Define the command and arguments
command = ['sudo', 'mitm6', '-d', 'domain.local', '-ignore-nofqdn', '-i', 'eth0']

# Define the wait time of 5 minutes in seconds
wait_time = 5 * 60

while True:
    # Start the process
    print("Starting the mitm6 command.")
    process = subprocess.Popen(command)

    # Wait for 5 minutes
    time.sleep(wait_time)

    # Terminate the process
    print("Stopping the mitm6 process.")
    process.terminate()
    
    # Give it a bit of time to terminate gracefully
    try:
        process.wait(timeout=10)  # Wait for 10 seconds for the process to terminate
    except subprocess.TimeoutExpired:
        print("mitm6 did not terminate gracefully, killing it.")
        process.kill()  # Forcefully kill the process if it didn't terminate
        process.wait()  # Now we wait again to make sure it's killed

    # Wait another 5 minutes
    print("Waiting for 5 minutes before restarting the command.")
    time.sleep(wait_time)
