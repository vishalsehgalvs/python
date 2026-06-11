# ============================================================
# COMMAND LINE ARGUMENTS IN PYTHON
# Simple to Complex, explained in plain everyday language
# ============================================================
# When you run a Python script, you can pass extra information
# directly from the terminal — like:
#   python myscript.py  hello  42  --output result.txt
# Those extra words/numbers after the script name are called
# "command line arguments". Python gives you 3 built-in ways
# to handle them. Let's go from simplest to most powerful.
# ============================================================


# ------------------------------------------------------------
# METHOD 1: sys.argv  — the most basic way
# ------------------------------------------------------------
# Think of sys.argv like a shopping receipt.
# sys.argv[0]  = the store name (the script itself)
# sys.argv[1:] = the items you bought (your actual inputs)
#
# HOW TO RUN THIS SECTION:
#   python command_line_args.py 5 10 15
# ------------------------------------------------------------

import sys

print("=" * 50)
print("METHOD 1 — sys.argv (the simple receipt approach)")
print("=" * 50)

print("Total things typed (including script name):", len(sys.argv))
print("Script name (always first)                :", sys.argv[0])
print("Your actual arguments                      :", sys.argv[1:])

# Example: add up all the numbers you passed in
# e.g. python command_line_args.py 5 10 15  → Sum = 30
if len(sys.argv) > 1:
    total = 0
    for arg in sys.argv[1:]:
        try:
            total += int(arg)       # convert text → number
        except ValueError:
            pass                    # skip anything that isn't a number
    print("Sum of all numeric arguments:", total)
else:
    print("(No arguments passed — try: python command_line_args.py 5 10 15)")


# ------------------------------------------------------------
# METHOD 2: getopt  — handling flags like -h or --help
# ------------------------------------------------------------
# Think of getopt like a vending machine with buttons.
# -h or --Help   → Press the Help button
# -m or --My_file → Press the File button
# -o result.txt  → Press Output and type what you want
#
# HOW TO RUN THIS SECTION:
#   python command_line_args.py -o result.txt
#   python command_line_args.py -h
#   python command_line_args.py -m
# ------------------------------------------------------------

import getopt

print("\n" + "=" * 50)
print("METHOD 2 — getopt (the vending machine approach)")
print("=" * 50)

args = sys.argv[1:]          # grab everything after the script name

# Define which "buttons" (options) are allowed:
# "hmo:" means:  -h  (no value needed)
#                -m  (no value needed)
#                -o  (needs a value after it, shown by the colon)
short_options = "hmo:"
long_options  = ["Help", "My_file", "Output="]   # long versions of the same buttons

try:
    arguments, leftover_values = getopt.getopt(args, short_options, long_options)

    for flag, value in arguments:
        if flag in ("-h", "--Help"):
            # User pressed the Help button
            print("Showing Help: run with -m for filename, -o <name> for output mode")

        elif flag in ("-m", "--My_file"):
            # User pressed the File button — show the script's own name
            print("File name (this script):", sys.argv[0])

        elif flag in ("-o", "--Output"):
            # User pressed Output and gave a value
            print("Output mode set to:", value)

except getopt.error as err:
    # If the user types a flag that doesn't exist, we catch it gracefully
    print("Unrecognised option:", str(err))


# ------------------------------------------------------------
# METHOD 3: argparse  — the smart, friendly way (recommended)
# ------------------------------------------------------------
# Think of argparse like a helpful receptionist.
# You tell it what options the script accepts,
# and it automatically:
#   ✔ explains them when someone types --help
#   ✔ checks the types (e.g. must be a number)
#   ✔ sets default values if nothing is passed
#   ✔ shows an error with a hint if something is wrong
#
# HOW TO RUN THESE EXAMPLES:
#   python command_line_args.py -h
#   python command_line_args.py -o Hello
#   python command_line_args.py --Output "Good morning"
# ------------------------------------------------------------

import argparse

print("\n" + "=" * 50)
print("METHOD 3 — argparse (the smart receptionist approach)")
print("=" * 50)

# Step 1: Create the receptionist (the parser)
# The description shows up when someone asks for help with -h
parser = argparse.ArgumentParser(
    description="Demo script showing how to handle command line arguments"
)

# Step 2: Tell the receptionist what to expect
# add_argument() is how you define each option the script accepts

# Optional argument:  -o  or  --Output
#   The user can pass a value after it, e.g.  -o Hello
#   If they don't pass it, args.Output will be None
parser.add_argument(
    "-o", "--Output",
    help="A message you want the script to display"
)

# Optional argument:  -n  or  --name
#   default="World" means if the user doesn't pass --name, it uses "World"
parser.add_argument(
    "-n", "--name",
    default="World",
    help="Your name (default: World)"
)

# Optional argument:  --count
#   type=int means argparse will automatically convert the text to an integer
#   and show a helpful error if the user passes something that isn't a number
parser.add_argument(
    "--count",
    type=int,
    default=1,
    help="How many times to print the greeting (default: 1)"
)

# Step 3: Let the receptionist read what was actually typed
# parse_known_args() is used here because this demo file also handles
# raw numbers for sys.argv above. In a real dedicated script you would
# just use  parser.parse_args()  and it will catch unknown arguments.
args, _ = parser.parse_known_args()

# Step 4: Use what was received
if args.Output:
    # User passed -o or --Output with a value
    print("Output message:", args.Output)

# Greet using the --name argument (falls back to "World" if not given)
greeting = f"Hello, {args.name}!"
for i in range(args.count):
    print(greeting)

print("\n(Tip: run this file with  -h  to see the full help menu)")
