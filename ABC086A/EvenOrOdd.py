import argparse

parser = argparse.ArgumentParser()
# required arguments:input integer A
parser.add_argument(
    "intA",
    help="Input integer",
    type=int
)
# required arguments:input integer B
parser.add_argument(
    "intB",
    help="Input integer",
    type=int
)

args = parser.parse_args()

# accumalate A and B
product = args.intA * args.intB
# remainder divided by 2
mod = product % 2
# determine if Odd or Even
if mod == 1:
    print("The product of " + str(args.intA) + " and " + str(args.intB) +
          " is " + str(product) + ".\n"
          "The product " + str(product) + " is Odd.")
elif mod == 0:
    print("The product of " + str(args.intA) + " and " + str(args.intB) +
          " is " + str(product) + ".\n"
          "The product " + str(product) + " is Even.")
else:
    print("Eroor!!")
