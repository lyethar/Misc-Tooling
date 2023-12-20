import subprocess
import time
import signal

# Define the command and arguments
command = ['sudo', 'mitm6', '-d', 'domain', '-ignore-nofqdn', '-i', 'eth0']

# Define the wait time of 10 minutes in seconds
wait_time_between_commands = 10 * 60
wait_time_during_command = 5 * 60

while True:
    # Start the process
    print("Starting the mitm6 command.")
    process = subprocess.Popen(command)

    # Wait for 5 minutes while the command is running
    time.sleep(wait_time_during_command)

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

    # Wait for 10 minutes before restarting the command
    print("Waiting for 10 minutes before restarting the command.")
    time.sleep(wait_time_between_commands)
