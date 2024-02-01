import sys
import ipaddress

def split_subnet(subnet_str, new_prefix_length):
    """
    Splits a given subnet into smaller subnets of the specified prefix length.
    """
    subnet = ipaddress.ip_network(subnet_str, strict=False)

    if subnet.prefixlen >= new_prefix_length:
        return [subnet_str]  # Return the original subnet if it can't be split

    return [str(net) for net in subnet.subnets(new_prefix=new_prefix_length)]

def main():
    if len(sys.argv) != 3:
        print("Usage: python script_name.py <path_to_subnet_file> <new_prefix_length>")
        sys.exit(1)

    subnet_file_path = sys.argv[1]
    new_prefix_length = int(sys.argv[2])

    output_file_path = "output_subnets.txt"

    with open(subnet_file_path, 'r') as f:
        larger_subnets = f.read().splitlines()

    with open(output_file_path, 'w') as output_file:
        for subnet_str in larger_subnets:
            smaller_subnets = split_subnet(subnet_str, new_prefix_length)
            for small_subnet in smaller_subnets:
                output_file.write(small_subnet + '\n')

    print(f"Output written to {output_file_path}")

if __name__ == "__main__":
    main()
