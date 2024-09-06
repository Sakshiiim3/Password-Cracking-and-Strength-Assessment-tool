import argparse
from dictionary import dictionary_attack
from strength import assess_strength

def main():
    parser = argparse.ArgumentParser(description="Password Cracking and Strength Assessment Tool")

    # Define CLI arguments
    parser.add_argument("password", type=str, help="Password to crack or assess strength")
    parser.add_argument("-c", "--crack", action="store_true", help="Perform password cracking")
    parser.add_argument("-s", "--strength", action="store_true", help="Assess password strength")

    args = parser.parse_args()

    if args.crack:
        dictionary_attack(args.password)
    elif args.strength:
        assess_strength(args.password)
    else:
        print("Error: Please specify either --crack or --strength option")

if __name__ == "__main__":
    main()
