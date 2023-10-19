#Generates a list of all possible username and password combinations based on two inputs. Inputs include a list of usernames and passwords. It will output them in the following format : username password. This facilitates attacks utilizing Metasploit. 
import argparse

def generate_combinations(user_file, password_file, output_file):
    # Read usernames and passwords from respective files
    with open(user_file, 'r') as ufile:
        users = [line.strip() for line in ufile.readlines()]
    
    with open(password_file, 'r') as pfile:
        passwords = [line.strip() for line in pfile.readlines()]
    
    # Generate combinations
    with open(output_file, 'w') as ofile:
        for user in users:
            for password in passwords:
                ofile.write(f"{user} {password}\n")

def main():
    parser = argparse.ArgumentParser(description="Generate combinations of usernames and passwords.")
    parser.add_argument("-u", "--users", required=True, help="Path to the file containing usernames.")
    parser.add_argument("-p", "--passwords", required=True, help="Path to the file containing passwords.")
    parser.add_argument("-o", "--output", default="output.txt", help="Path for the output file. Defaults to 'output.txt'.")
    
    args = parser.parse_args()
    
    generate_combinations(args.users, args.passwords, args.output)
    print(f"Combinations saved to {args.output}")

if __name__ == "__main__":
    main()
