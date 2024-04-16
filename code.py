import sys

def fibonacci(f):
    if type(f) != int or f < 0:
        sys.stderr.write("Error: Input must be a non-negative integer.\n")
        return None
    elif f == 0 or f == 1:
        return 1
    else:
        return fibonacci(f - 1) + fibonacci(f - 2)

def main():
    
    for line in sys.stdin:

        try:
            n = int(line)
        except ValueError:
            sys.stderr.write("Error: Input must be an integer.\n")
            continue
        
        result = fibonacci(n)
        
        if result is not None:
            sys.stdout.write(str(result) + '\n')

if __name__ == "__main__":
    main()
