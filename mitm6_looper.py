import subprocess
import time

# Path to the file that contains the list of hostnames
hosts_file = 'hosts.txt'

# Other static options for mitm6
base_command = [
    'sudo', 'mitm6',
    '-d', 'domain',
    '--ignore-nofqdn',
    '-i', 'eth0'
]

# Define the wait times
wait_time_between_commands = 10 * 60  # 10 minutes
wait_time_during_command = 5 * 60      # 5 minutes

def build_command():
    """Build the mitm6 command dynamically by reading the hosts file."""
    try:
        with open(hosts_file, 'r') as file:
            hosts = [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print(f"Error: Hosts file '{hosts_file}' not found!")
        return base_command  # Fall back to base command without any allowlist

    # Add --host-allowlist for each host dynamically
    host_allowlist_args = []
    for host in hosts:
        host_allowlist_args.extend(['--host-allowlist', host])

    return base_command + host_allowlist_args

while True:
    # Build the command dynamically
    command = build_command()
    print(f"Starting mitm6 with command: {' '.join(command)}")

    # Start the process
    process = subprocess.Popen(command)

    # Wait while the command is running
    time.sleep(wait_time_during_command)

    # Terminate the process
    print("Stopping the mitm6 process.")
    process.terminate()

    try:
        process.wait(timeout=10)  # Wait for 10 seconds to terminate gracefully
    except subprocess.TimeoutExpired:
        print("mitm6 did not terminate gracefully, killing it.")
        process.kill()
        process.wait()

    # Wait before restarting
    print("Waiting 10 minutes before restarting mitm6.")
    time.sleep(wait_time_between_commands)
