import sys 

def main():
    if (len(sys.argv) == 1):
        print("Nothing to swap")
    if (len(sys.argv) == 2):
        print(sys.argv[1][::-1])
    if (len(sys.argv) > 2):
        print(" ".join([sys.argv[1], sys.argv[2]])[::-1])
if __name__ == "__main__":
    main()
