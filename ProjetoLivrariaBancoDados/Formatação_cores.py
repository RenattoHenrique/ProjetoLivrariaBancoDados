BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
LIGHT_GRAY = '\033[37m'
DARK_GRAY = '\033[90m'
BRIGHT_RED = '\033[91m'
BRIGHT_GREEN = '\033[92m'
BRIGHT_YELLOW = '\033[93m'
BRIGHT_BLUE = '\033[94m'
BRIGHT_MAGENTA = '\033[95m'
BRIGHT_CYAN = '\033[96m'
WHITE = '\033[97m'

RESET = '\033[0m'

def printColored(s:str, color:str = WHITE, end="\n"): print(color + s + RESET, end=end)

def printBlack(s:str, end="\n"):			printColored(s,BLACK, end=end)
def printRed(s:str, end="\n"):				printColored(s,RED, end=end)
def printGreen(s:str, end="\n"):			printColored(s,GREEN, end=end)
def printYellow(s:str, end="\n"):			printColored(s,YELLOW, end=end)
def printBlue(s:str, end="\n"):				printColored(s,BLUE, end=end)
def printMagenta(s:str, end="\n"):			printColored(s,MAGENTA, end=end)
def printCyan(s:str, end="\n"):				printColored(s,CYAN, end=end)
def printLightGray(s:str, end="\n"):		printColored(s,LIGHT_GRAY, end=end)
def printDarkGray(s:str, end="\n"):			printColored(s,DARK_GRAY, end=end)
def printBrightRed(s:str, end="\n"):		printColored(s,BRIGHT_RED, end=end)
def printBrightGreen(s:str, end="\n"):		printColored(s,BRIGHT_GREEN, end=end)
def printBrightYellow(s:str, end="\n"):		printColored(s,BRIGHT_YELLOW, end=end)
def printBrightBlue(s:str, end="\n"):		printColored(s,BRIGHT_BLUE, end=end)
def printBrightMagenta(s:str, end="\n"):	printColored(s,BRIGHT_MAGENTA, end=end)
def printBrightCyan(s:str, end="\n"):		printColored(s,BRIGHT_CYAN, end=end)

class Moeda:
    def formatar(valor):
        return f"R${valor:,.2f}".replace(",", ".")