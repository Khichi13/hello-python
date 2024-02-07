""" The main module. """
import functions as fn


def main():
    """ The main function. """
    name = input('What is your name? ')
    fn.hello(name)  # String can be inside both single or double quotes
    
    print('For Loop:')
    fn.for_loop()

    print('While Loop:')
    fn.while_loop()

    n = input('Enter a number between 0 and 10: ')

    try:
        n = int(n) # try to cast n to integer
        fn.conditions(n)
    except ValueError:
        print('Please enter a digit')

if __name__ == '__main__':
    main()
