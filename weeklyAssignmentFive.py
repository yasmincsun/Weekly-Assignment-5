import argparse

def lineCounter(filePath, verbose):
    lineCount = 0
    with open(filePath, 'r') as weekAssFive:
        for line in weekAssFive:
            if verbose:
                print(line)
            lineCount += 1
    

    print(f"\nTotal lines in '{filePath}': {lineCount}")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("file", help = "The path to the .txt file")
    parser.add_argument("-v", "--verbose", action="store_true", default = 0)

    args = parser.parse_args()

    lineCounter(args.file, args.verbose)

if __name__ == "__main__":
    main()