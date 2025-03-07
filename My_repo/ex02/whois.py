import sys

def main() :
    if (len(sys.argv) == 1):
        print("")
        return 
    if (len(sys.argv) > 2):
        print("more than one argument is provided")
        return
    try:
        num  = int(sys.argv[1])
    except:
        print("argument is not an integer")
    message = {
        0: "i am Zero", 
        1: "i am odd", 
        2: " i am even"
    }
    
if __name__ == "__main__" :
    main()
        