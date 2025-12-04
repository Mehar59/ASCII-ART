import os
import sys
from colorama import Fore, Style, init

# Initialize colorama for cross-platform color support
init(autoreset=True)

# Hardcoded font data (from user's original file)
FONT_DATA = [
    " ***  ****   ***  ****  ***** *****  ***  *   * ***** ***** *   * *     *   * *   *  ***  ****   ***  ****   **** ***** *   * *   * *   * *   * *   * *****        ***                     ***  ***   ****  ****  *   * *****  ***  ***** ",
    "*   * *   * *   * *   * *     *     *     *   *   *      *  *  *  *     ** ** **  * *   * *   * *   * *   * *       *   *   * *   * *   *  * *   * *     *        * ***                   *   *   *       *     * *   * *     *         * *   * *   * ",
    "*   * ****  *     *   * ***   ****  *  ** *****   *      *  ***   *     * * * * * * *   * ****  *   * ****  *****   *   *   * *   * * * *   *     *     *         * * *       *****       *   *   *       *   **  ***** ****  ****      *  ***  ***** ",
    "***** *   * *   * *   * *     *     *   * *   *   *   *  *  *  *  *     *   * *  ** *   * *     *   * *  *      *   *   *   *  * *  ** **  * *    *    *          * * *              ***  *   *   *   ***       *     *     * *   *     * *   *     * ",
    "*   * ****   ***  ****  ***** *      ***  *   * *****  ***  *   * ***** *   * *   *  ***  *      ***  *   * ****    *   *****   *   *   * *   *   *   *****        ***  *****        ***   ***  ***** ***** ****      * ****   ***      *  ***      * "
]

# Character width in columns
CHAR_WIDTH = 6

# Color map for user selection
COLOR_MAP = {
    "1": Fore.RED,
    "2": Fore.GREEN,
    "3": Fore.YELLOW,
    "4": Fore.BLUE,
    "5": Fore.MAGENTA,
    "6": Fore.CYAN,
    "7": Fore.WHITE,
    "8": Style.BRIGHT + Fore.RED,
    "9": Style.BRIGHT + Fore.GREEN,
    "0": Style.BRIGHT + Fore.YELLOW,
    "R": Style.RESET_ALL
}

def clear_screen():
    """Clears the terminal screen in a cross-platform way."""
    os.system('cls' if os.name == 'nt' else 'clear')

def get_char_index(char):
    """
    Calculates the starting index for a character in the FONT_DATA string.
    (Logic preserved from original program)
    """
    char = char.upper()
    
    if 'A' <= char <= 'Z':
        return (ord(char) - ord('A')) * CHAR_WIDTH
    elif '0' <= char <= '9':
        return (ord(char) - 17) * CHAR_WIDTH
    elif char == ' ':
        return 26 * CHAR_WIDTH
    elif char == '@':
        return 27 * CHAR_WIDTH
    elif char == '_':
        return 28 * CHAR_WIDTH
    elif char == '-':
        return 29 * CHAR_WIDTH
    elif char == '.':
        return 30 * CHAR_WIDTH
    else:
        return -1

def render_ascii_art(text, color_code, prefix=""):
    """
    Generates and prints the ASCII art for the given text with the specified color.
    """
    selected_color = COLOR_MAP.get(color_code, Style.RESET_ALL)
    
    # Print the "You Entered" message with color
    print(f"\n{selected_color}{Style.BRIGHT}>> {prefix}{text}{Style.RESET_ALL}\n")
    
    # Iterate over each line of the font data
    for line in FONT_DATA:
        sys.stdout.write(selected_color)
        
        # Iterate over each character in the input text
        for char in text:
            start_index = get_char_index(char)
            
            if start_index != -1:
                char_art = line[start_index : start_index + CHAR_WIDTH]
                sys.stdout.write(char_art)
            else:
                sys.stdout.write(" " * CHAR_WIDTH)
        
        sys.stdout.write(Style.RESET_ALL + "\n")
    
    print(Style.RESET_ALL) # Final reset

def print_title_banner():
    """Prints a large, colorful ASCII art banner for the main menu."""
    title_text = "ART GEN" # Using a short, punchy title
    
    # Define a custom color sequence for the title
    title_colors = [Fore.MAGENTA, Fore.CYAN, Fore.YELLOW, Fore.GREEN, Fore.RED, Fore.BLUE, Fore.MAGENTA]
    
    print(Style.BRIGHT + Fore.WHITE + "==================================================")
    print("         ✨ Advanced Terminal Art Generator ✨")
    print("==================================================" + Style.RESET_ALL)
    
    # Render the title art with a color gradient effect
    for i, line in enumerate(FONT_DATA):
        sys.stdout.write(Style.BRIGHT)
        for j, char in enumerate(title_text):
            start_index = get_char_index(char)
            if start_index != -1:
                char_art = line[start_index : start_index + CHAR_WIDTH]
                # Apply a different color for each character
                sys.stdout.write(title_colors[j % len(title_colors)] + char_art)
            else:
                sys.stdout.write(" " * CHAR_WIDTH)
        sys.stdout.write(Style.RESET_ALL + "\n")
    
    print(Style.BRIGHT + Fore.WHITE + "==================================================" + Style.RESET_ALL)

def get_color_choice():
    """Prompts the user to select a color with a cleaner, boxed presentation."""
    print(Style.BRIGHT + Fore.YELLOW + "\n" + "╔" + "═"*38 + "╗")
    print("║" + Fore.CYAN + "      🎨 COLOR PALETTE SELECTION" + Fore.YELLOW + "      ║")
    print("╠" + "═"*38 + "╣" + Style.RESET_ALL)
    
    colors = [
        (Fore.RED, "Red (Normal)", Style.BRIGHT + Fore.RED, "Red (Bright)"),
        (Fore.GREEN, "Green (Normal)", Style.BRIGHT + Fore.GREEN, "Green (Bright)"),
        (Fore.YELLOW, "Yellow (Normal)", Style.BRIGHT + Fore.YELLOW, "Yellow (Bright)"),
        (Fore.BLUE, "Blue (Normal)", None, None),
        (Fore.MAGENTA, "Magenta (Normal)", None, None),
        (Fore.CYAN, "Cyan (Normal)", None, None),
        (Fore.WHITE, "White (Normal)", None, None),
    ]
    
    # Print in two columns
    for i in range(4):
        line = Fore.YELLOW + "║ "
        
        # Column 1 (1-4)
        if i < 3:
            idx1 = i + 1
            color1, name1, bright_color, bright_name = colors[i]
            line += f"{idx1}. {color1}{name1:<15}{Style.RESET_ALL}"
            
            # Column 2 (8-0)
            idx2 = i + 8
            line += f" {Fore.YELLOW}│ {idx2}. {bright_color}{bright_name:<15}{Style.RESET_ALL}"
        elif i == 3:
            # Column 1 (4-7)
            idx1 = i + 1
            color1, name1, _, _ = colors[i]
            line += f"{idx1}. {color1}{name1:<15}{Style.RESET_ALL}"
            
            # Column 2 (R)
            line += f" {Fore.YELLOW}│ R. {Style.RESET_ALL}Reset (Default){' ':<15}"
        
        line += Fore.YELLOW + " ║"
        print(line)

    # Print remaining colors
    for i in range(4, 7):
        line = Fore.YELLOW + "║ "
        idx = i + 1
        color, name, _, _ = colors[i]
        line += f"{idx}. {color}{name:<15}{Style.RESET_ALL}"
        line += f" {' ':<20}" # Empty space for the second column
        line += Fore.YELLOW + " ║"
        print(line)

    print(Style.BRIGHT + Fore.YELLOW + "╚" + "═"*38 + "╝" + Style.RESET_ALL)
    
    while True:
        choice = input(Style.BRIGHT + Fore.GREEN + "Enter your color choice (1-9, 0, R): " + Style.RESET_ALL).upper()
        if choice in COLOR_MAP:
            return choice
        print(f"{Fore.RED}Invalid choice. Please enter a valid option.{Style.RESET_ALL}")

def one_character_module():
    """Module for generating ASCII art for a single character."""
    clear_screen()
    print(Style.BRIGHT + Fore.CYAN + "\n" + "─"*50)
    print("        [ 1 ]  SINGLE CHARACTER GENERATOR")
    print("─"*50 + Style.RESET_ALL)
    
    while True:
        text = input(Fore.YELLOW + "Enter a Character (Only One Character) >> " + Style.RESET_ALL).upper()
        if len(text) == 1:
            break
        print(f"{Fore.RED}Error: Please Enter Only One Letter/Number/Symbol.{Style.RESET_ALL}")
    
    color_choice = get_color_choice()
    render_ascii_art(text, color_choice, prefix="Character: ")

def alpha_num_words_module():
    """Module for generating ASCII art for a word/phrase (max 15 chars)."""
    clear_screen()
    print(Style.BRIGHT + Fore.CYAN + "\n" + "─"*50)
    print("        [ 2 ]  ALPHA-NUMERIC WORDS GENERATOR")
    print("─"*50 + Style.RESET_ALL)
    
    while True:
        text = input(Fore.YELLOW + "Enter String (Max 15 Characters, including spaces and symbols) >> " + Style.RESET_ALL).upper()
        if 1 <= len(text) <= 15:
            break
        print(f"{Fore.RED}Error: Please Enter a string between 1 and 15 characters.{Style.RESET_ALL}")
    
    color_choice = get_color_choice()
    render_ascii_art(text, color_choice, prefix="Text: ")

def alpha_range_module():
    """Module for generating ASCII art for a range of characters (e.g., A-D)."""
    clear_screen()
    print(Style.BRIGHT + Fore.CYAN + "\n" + "─"*50)
    print("        [ 3 ]  ALPHABET RANGE GENERATOR")
    print("─"*50 + Style.RESET_ALL)
    
    while True:
        text = input(Fore.YELLOW + "Enter Range in Sequence (e.g., A-D). Max 15 characters in range. >> " + Style.RESET_ALL).upper()
        
        if len(text) == 3 and text[1] == '-' and 'A' <= text[0] <= 'Z' and 'A' <= text[2] <= 'Z':
            start_char = text[0]
            end_char = text[2]
            
            if start_char > end_char:
                print(f"{Fore.RED}Error: Start character must be before or the same as the end character (in sequence).{Style.RESET_ALL}")
                continue
            
            range_len = ord(end_char) - ord(start_char) + 1
            if range_len > 15:
                print(f"{Fore.RED}Error: The range is too large. Maximum 15 characters allowed.{Style.RESET_ALL}")
                continue
            
            # Construct the full string from the range
            full_text = "".join([chr(i) for i in range(ord(start_char), ord(end_char) + 1)])
            break
        
        print(f"{Fore.RED}Error: Please enter a valid range format (e.g., A-D).{Style.RESET_ALL}")

    color_choice = get_color_choice()
    render_ascii_art(full_text, color_choice, prefix=f"Range ({text}): ")

def only_alpha_module():
    """Module for generating ASCII art for alphabetic characters only."""
    clear_screen()
    print(Style.BRIGHT + Fore.CYAN + "\n" + "─"*50)
    print("        [ 4 ]  ALPHABETS ONLY GENERATOR")
    print("─"*50 + Style.RESET_ALL)
    
    while True:
        text = input(Fore.YELLOW + "Enter String (Only Alphabets, Max 15 Characters) >> " + Style.RESET_ALL).upper()
        if 1 <= len(text) <= 15 and text.isalpha():
            break
        print(f"{Fore.RED}Error: Please enter 1 to 15 alphabetic characters only.{Style.RESET_ALL}")
    
    color_choice = get_color_choice()
    render_ascii_art(text, color_choice, prefix="Text: ")

def only_num_module():
    """Module for generating ASCII art for numeric characters only."""
    clear_screen()
    print(Style.BRIGHT + Fore.CYAN + "\n" + "─"*50)
    print("        [ 5 ]  NUMBERS ONLY GENERATOR")
    print("─"*50 + Style.RESET_ALL)
    
    while True:
        text = input(Fore.YELLOW + "Enter String (Only Numbers, Max 15 Characters) >> " + Style.RESET_ALL).upper()
        if 1 <= len(text) <= 15 and text.isnumeric():
            break
        print(f"{Fore.RED}Error: Please enter 1 to 15 numeric characters only.{Style.RESET_ALL}")
    
    color_choice = get_color_choice()
    render_ascii_art(text, color_choice, prefix="Text: ")

def main_ui():
    """Main user interface loop."""
    while True:
        clear_screen()
        print_title_banner()
        
        print(Style.BRIGHT + Fore.WHITE + "\n" + "╔" + "═"*48 + "╗")
        print("║" + Fore.YELLOW + "  SELECT A MODE TO GENERATE YOUR TERMINAL ART:" + Fore.WHITE + "   ║")
        print("╠" + "═"*48 + "╣")
        print(f"║ {Fore.GREEN}1. Single Character{Fore.WHITE:<32}║")
        print(f"║ {Fore.GREEN}2. Alpha-Numeric Words{Fore.WHITE:<27}║")
        print(f"║ {Fore.GREEN}3. Alphabet Range (e.g., A-D){Fore.WHITE:<20}║")
        print(f"║ {Fore.GREEN}4. Alphabets Only{Fore.WHITE:<34}║")
        print(f"║ {Fore.GREEN}5. Numbers Only{Fore.WHITE:<36}║")
        print("╠" + "═"*48 + "╣")
        print(f"║ {Fore.RED}6. Exit Program{Fore.WHITE:<36}║")
        print("╚" + "═"*48 + "╝" + Style.RESET_ALL)
        
        choice = input(Style.BRIGHT + Fore.MAGENTA + "\n[INPUT] Enter Your Choice (1-6): " + Style.RESET_ALL).strip()
        
        if choice == "1":
            one_character_module()
        elif choice == "2":
            alpha_num_words_module()
        elif choice == "3":
            alpha_range_module()
        elif choice == "4":
            only_alpha_module()
        elif choice == "5":
            only_num_module()
        elif choice == "6":
            clear_screen()
            print(Fore.GREEN + Style.BRIGHT + "\nThank you for using the ASCII Art Generator! Goodbye." + Style.RESET_ALL)
            break
        else:
            print(f"{Fore.RED}Invalid choice. Please enter a number between 1 and 6.{Style.RESET_ALL}")
            input("Press Enter to continue...")
            continue
        
        # Continuation prompt
        print("\n" + Style.BRIGHT + Fore.WHITE + "─"*50)
        cont = input(Fore.CYAN + "Do you want to generate more art? (y/Y to continue, any other key to exit): " + Style.RESET_ALL).upper()
        if cont != "Y":
            clear_screen()
            print(Fore.GREEN + Style.BRIGHT + "\nThank you for using the ASCII Art Generator! Goodbye." + Style.RESET_ALL)
            break

if __name__ == "__main__":
    main_ui()
