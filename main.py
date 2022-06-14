from get_color_from_pair_number import test_number_to_pair
from get_pair_number_from_color import test_pair_to_number
from user_reference_manual import print_user_reference_manual


if __name__ == '__main__':
    print_user_reference_manual()
    test_number_to_pair(4, 'White', 'Brown')
    test_number_to_pair(5, 'White', 'Slate')
    test_pair_to_number('Black', 'Orange', 12)
    test_pair_to_number('Violet', 'Slate', 25)
    test_pair_to_number('Red', 'Orange', 7)
    print('Done :)')
