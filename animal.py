import sys

def duck():
    print('Quack!')

def dog():
    print('Woof!')

def default():
    print('hello')

def cat():
    print('Meowwwwwwwwwwwwwwwwwwwwwww')

def main():
    if len(sys.argv) == 1:
        print('Hello')
    elif sys.argv[1] == 'cat':
        cat()
    elif sys.argv[1] == 'dog':
        dog()
    else:
        print('Hello!')

if __name__ == '__main__':
    main()
