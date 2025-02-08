import sys
import random
from pyfiglet import Figlet

def main():
    # Initialize Figlet instance
    figlet = Figlet()

    # Check for command-line arguments
    if len(sys.argv) == 1:
        # No arguments, use random font
        font = random.choice(figlet.getFonts())
    elif len(sys.argv) == 3:
        # Two arguments, validate them
        if sys.argv[1] in ("-f", "--font"):
            font = sys.argv[2]
            if font not in figlet.getFonts():
                sys.exit("Invalid usage")
        else:
            sys.exit("Invalid usage")
    else:
        # Incorrect number of arguments
        sys.exit("Invalid usage")

    # Set the font
    figlet.setFont(font=font)

    # Prompt user for text
    text = input("Enter text: ")

    # Print the text in the selected font
    print(figlet.renderText(text))

if __name__ == "__main__":
    main()
