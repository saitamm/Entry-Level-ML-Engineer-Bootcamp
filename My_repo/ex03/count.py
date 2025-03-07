import sys
import string

def text_analyzer(str):
    """
    this function count charecters of string and parse them to upper and lower , punctuation mark and space
    """
    print("-", "The text contains ",sum(1 for char in str if char), "printable character(s):")
    print("-",sum(1 for char in str if char.isupper()), "upper letter(s)")
    print("-", sum(1 for char in str if char.islower()), "lower letter(s)")
    print("-", sum(1 for char in str if char in string.punctuation), "punctuation mark(s)")
    print("-", sum(1 for char in str if char.isspace()), "space(s)")
def main():
    if (len(sys.argv) == 2):
        try:
            str = string(sys.argv[1])
        except:
            print("is not string")
            return 
        text_analyzer(sys.argv[1])
if __name__ == "__main__" :
    main()
