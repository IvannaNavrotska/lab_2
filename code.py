import sys

sys.stdout.write('There is what you should know if you wanna find fibonacci:\n'
                 'to have something, you have to give somethig\n'
                 'letters are cool, but not here\n'
                 "we all love negative integers, but fibonacci doesn't\n"
                 'Now you can enter you integers :) \n')

def fibonacci(f):
    if type(f) != int or f < 0:
        sys.stderr.write("Error: You know, input must be a non-negative integer \n")
        return None
    elif f == 0 or f == 1:
        return 1
    else:
        return fibonacci(f - 1) + fibonacci(f - 2)

def main():
    
    for line in sys.stdin:

        if not line.strip():
            sys.stderr.write("Error: Wait, your input cannot be empty! \n")
            sys.exit(1)

        try:
            n = int(line)
        except ValueError:
            sys.stderr.write("Error: Forget about letters! Input must be an integer \n")
            sys.exit(1)
        
        result = fibonacci(n)
        
        if result is not None:
            sys.stdout.write(str(result) + '\n')
    
    sys.exit(0)

if __name__ == "__main__":
    main()
