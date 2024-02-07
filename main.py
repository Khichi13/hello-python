""" The main module. """
from functions import hello


def main():
    """ The main function. """
    hello('\n- Farooq')  # String can be inside both single or double quotes
    for i in range(0, 10):
        print(i, end=' ')
    print()


if __name__ == '__main__':
    main()
