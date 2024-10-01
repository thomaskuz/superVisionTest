import argparse

# Create the parser
parser = argparse.ArgumentParser(description="A simple example script")

# Add arguments
parser.add_argument('name', type=str, help='Name of the person')
parser.add_argument('--age', type=int, help='Age of the person', default=20)

# Parse the arguments
args = parser.parse_args()

# Access arguments
print(f"Hello {args.name}, you are {args.age} years old.")
