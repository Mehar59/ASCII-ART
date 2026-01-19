import os
import msvcrt as msv
import sys
from colorama import Fore, Back, Style, init
init(autoreset=True)
def chooseColor():
    os.system("cls")
    print("\n\n***** SELECT TEXT COLOR *****\n")
    print("1. RED")
    print("2. GREEN")
    print("3. YELLOW")
    print("4. BLUE")
    print("5. MAGENTA")
    print("6. CYAN")
    print("\nEnter Color Number (1-6): ",end="")
    choice=msv.getch().decode()
    if choice == "1": return Fore.RED
    if choice == "2": return Fore.GREEN
    if choice == "3": return Fore.YELLOW
    if choice == "4": return Fore.BLUE
    if choice == "5": return Fore.MAGENTA
    if choice == "6": return Fore.CYAN

    print("\nInvalid color! Try again.")
    msv.getch()
    return chooseColor()


data = [
    " ***  ****   ***  ****  ***** *****  ***  *   * ***** ***** *   * *     *   * *   *  ***  ****   ***  ****   **** ***** *   * *   * *   * *   * *   * *****        ***                     ***  ***   ****  ****  *   * *****  ***  *****  ***  ***** ",
    "*   * *   * *   * *   * *     *     *     *   *   *      *  *  *  *     ** ** **  * *   * *   * *   * *   * *       *   *   * *   * *   *  * *   * *     *        * ***                   *   *   *       *     * *   * *     *         * *   * *   * ",
    "*   * ****  *     *   * ***   ****  *  ** *****   *      *  ***   *     * * * * * * *   * ****  *   * ****  *****   *   *   * *   * * * *   *     *     *         * * *       *****       *   *   *       *   **  ***** ****  ****      *  ***  ***** ",
    "***** *   * *   * *   * *     *     *   * *   *   *   *  *  *  *  *     *   * *  ** *   * *     *   * *  *      *   *   *   *  * *  ** **  * *    *    *          * * *              ***  *   *   *   ***       *     *     * *   *     * *   *     * ",
    "*   * ****   ***  ****  ***** *      ***  *   * *****  ***  *   * ***** *   * *   *  ***  *      ***  *   * ****    *   *****   *   *   * *   *   *   *****        ***  *****        ***   ***  ***** ***** ****      * ****   ***      *  ***      * "
]
sm_data = [  
    "      *               *        * *          *            *   *       *                      *                       *                                       ", 
    "  *** *      ****     *  ****  *  * ****    *     *          ****    *                ***   **** ****  *            *                           *  *        ",
    " **** ****  *      ****  *  * ****  **** *  ****         *   *   *   *   ** ** ***** *   *  *  * *  *  ****  ****  ***  *  *  *   * *   *  * *  *  *  ****  ",
    "*   * *   * *      *  *  * *   *     * *    *  *  *   *  *   ****    *   * * * *   * *   *  **** ****  *     *****  *   *  *   * *  * * *   *    *     *    ",
    " *** *****   ****  ****  ***   *    ****    *  *  *   ****   *   *   *   *   * *   *  ***   *       *  *     ****   **  ****    *   *   *  * *  *     ****  "
]





def oneCharacter():
    os.system("cls")
    color = chooseColor()
    os.system("cls")

    print("\n\n","*"*10,"ASCII ART PROJECT","*"*10,end="\n\n")
    print("\n\n","*"*10,"One Character Module","*"*10,end="\n\n")

    text = input("Enter a Character (Only One Character) -- ")
    # text = input("Enter a Character (Only One Character) -- ").upper()
    
    if len(text) != 1:
        print("\n\nPlease Enter Only One Letter -- \n\n")
        oneCharacter()
        return
    if ord(text) >= 97 and ord(text)<= 122:
        n = ((ord(text)-96)-1)*6
        for row in sm_data:
            for col in range(n, n+6):
                print(color + row[col], end="")
            print()
    else:
        n = (ord(text)-17)*6 if text.isdigit() else ((ord(text)-64)-1)*6
        for row in data:
            for col in range(n, n+6):
                print(color + row[col], end="")
            print()
    


def alphaNumWords():
    os.system("cls")
    color = chooseColor()
    os.system("cls")

    print("\n\n","*"*10,"ASCII ART PROJECT","*"*10,end="\n\n")
    print("\n\n","*"*10,"Alpha Numeric Words Module","*"*10,end="\n\n")

    text = input("Enter String (Only <= 15 Character) -- ")

    if not (1 <= len(text) <= 15):
        print("\n\nPlease Enter Only <=15 Characters\n")
        alphaNumWords()
        return


    for row_index in range(5):
        for ch in text:

            
            if 'a' <= ch <= 'z':
                n = ((ord(ch) - 96) - 1) * 6
                source = sm_data

            
            elif ch.isdigit():
                n = (ord(ch) - 17) * 6
                source = data

           
            elif 'A' <= ch <= 'Z':
                n = ((ord(ch) - 64) - 1) * 6
                source = data

            else:
                
                print(" " * 6, end="")
                continue

            for col in range(n, n+6):
                print(color + source[row_index][col], end="")

        print()



def alphaRange():
    os.system("cls")
    color = chooseColor()
    os.system("cls")

    print("\n\n","*"*10,"ASCII ART PROJECT","*"*10,end="\n\n")
    print("\n\n","*"*10,"Alpha Range Module","*"*10,end="\n\n")

    text = input("Enter Range in Format (A-D or a-d) -- ")

    if len(text) != 3 or text[1] != '-':
        print("\n\nPlease Enter Valid Range -- \n\n")
        alphaRange()
        return

    start_ch = text[0]
    end_ch   = text[2]

    if start_ch > end_ch:
        print("\n\nRange must be in sequence -- \n\n")
        alphaRange()
        return

    
    for row_index in range(5):
        for ch in range(ord(start_ch), ord(end_ch) + 1):

            c = chr(ch)

            if 'a' <= c <= 'z':
                n = ((ord(c) - 96) - 1) * 6
                source = sm_data

            elif 'A' <= c <= 'Z':
                n = ((ord(c) - 64) - 1) * 6
                source = data

            else:
                print(" " * 6, end="")
                continue

            for col in range(n, n+6):
                print(color + source[row_index][col], end="")

        print()


def onlyAlpha():
    os.system("cls")
    color = chooseColor()
    os.system("cls")

    print("\n\n","*"*10,"ASCII ART PROJECT","*"*10,end="\n\n")
    print("\n\n","*"*10,"Only Alphabets Module","*"*10,end="\n\n")

    text = input("Enter Alphabets Only (<= 15) -- ")

    if not text.isalpha() or len(text) > 15:
        print("\n\nPlease Enter Only Alphabets (Max 15)\n")
        onlyAlpha()
        return

    for row_index in range(5):
        for ch in text:

            if 'a' <= ch <= 'z':
                n = ((ord(ch) - 96) - 1) * 6
                source = sm_data

            elif 'A' <= ch <= 'Z':
                n = ((ord(ch) - 64) - 1) * 6
                source = data

            else:
                print(" " * 6, end="")
                continue

            for col in range(n, n+6):
                print(color + source[row_index][col], end="")

        print()


def onlyNum():
    os.system("cls")
    color = chooseColor()
    sys.stdin.flush()
    os.system("cls")

    print("\n\n","*"*10,"ASCII ART PROJECT","*"*10,end="\n\n")
    print("\n\n","*"*10,"Only Numbers Module","*"*10,end="\n\n")

    text = input("Enter Numbers Only (<= 15) -- ")

    if not text.isdigit():
        print("\n\nPlease Enter Only Digits -- \n\n")
        onlyNum()
        return

    for row in data:
        for ch in text:
            n = (ord(ch)-17)*6
            for col in range(n, n+6):
                print(color + row[col], end="")
        print()


def mainUI():
    os.system("cls")
    print("\n\n","*"*10,"ASCII ART PROJECT","*"*10,end="\n\n")
    print("OPTIONS -- \n\n")
    print("1. One Character")
    print("2. Words (Maximum 15 Letters)")
    print("3. Range (A-D)")
    print("4. Only Alphabets")
    print("5. Only Numbers")
    print("6. Exit")
    print("\n\nEnter Your Choice -- ",end="")

    ch = msv.getch().decode()

    if ch == "1": oneCharacter()
    elif ch == "2": alphaNumWords()
    elif ch == "3": alphaRange()
    elif ch == "4": onlyAlpha()
    elif ch == "5": onlyNum()
    elif ch == "6": return

    print("\n\nDo you want to continue Project? Press Y else any key...")
    if msv.getch().decode().lower() == "y":
        mainUI()

mainUI()

