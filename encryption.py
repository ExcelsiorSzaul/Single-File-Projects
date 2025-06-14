
def s_to_binary(hex_string):
    binary_string = ''.join(format(int(char, 16), '04b') for char in hex_string)
    
    return binary_string

def l_shift(s, n):
    n = n % len(s)
    return s[n:] + s[:n]

def key_permutation(permutation_table, binary_string):
    new_string = ''
    shift_schedule = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]
    string_list = []

    for num in permutation_table:
        new_string = new_string + binary_string[num - 1]

    L = new_string[:28]
    R = new_string[28:]

    for each in shift_schedule:
        L = l_shift(L, each)
        R = l_shift(R, each)
        string_list.append((L, R))

    return string_list

def key_permutation2(permutation_table, strings_tuple_list):
    sub_keys = []
    for pair in strings_tuple_list:
        new_string = ''
        b_string = ''.join(pair)
        for num in permutation_table:
            new_string = new_string + b_string[num - 1]
        sub_keys.append(new_string)
    return sub_keys

def e_bit(input):
    selection_table = [
    32, 1, 2, 3, 4, 5,
    4, 5, 6, 7, 8, 9,
    8, 9, 10, 11, 12, 13,
    12, 13, 14, 15, 16, 17,
    16, 17, 18, 19, 20, 21,
    20, 21, 22, 23, 24, 25,
    24, 25, 26, 27, 28, 29,
    28, 29, 30, 31, 32, 1
    ]
    new_string = ''

    for each in selection_table:
        new_string = new_string + input[each - 1]

    return new_string

def s_boxes(string):
    S1 = [
        [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
        [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
        [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
        [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
    ]

    S2 = [
        [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
        [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
        [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
        [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]
    ]

    S3 = [
        [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
        [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
        [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
        [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]
    ]

    S4 = [
        [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
        [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
        [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
        [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]
    ]

    S5 = [
        [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
        [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
        [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
        [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]
    ]

    S6 = [
        [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
        [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
        [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
        [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]
    ]

    S7 = [
        [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
        [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
        [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
        [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]
    ]

    S8 = [
        [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
        [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
        [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
        [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]
    ]
    
    boxes = [S1, S2, S3, S4, S5, S6, S7, S8]
    Bs = [string[i:i+6] for i in range(0, len(string), 6)]
    numbers = []
    out = ''
    for i, B in enumerate(Bs):
        row_num = int(B[0] + B[5], 2)
        column_num = int(B[1:5], 2)

        num = bin(boxes[i][row_num][column_num])[2:].zfill(4)
        numbers.append(num)

    for n in numbers:
        out = out + n
    return out

def sbox_permutation(s_boxed):
    P = [
    16, 7, 20, 21, 29, 12, 
    28, 17, 1, 15, 23, 26, 
    5, 18, 31, 10, 2, 8, 24, 
    14, 32, 27, 3, 9, 19, 
    13, 30, 6, 22, 11, 4, 25
    ]
    new_string = ''

    for num in P:
        new_string = new_string + s_boxed[num - 1]
    return new_string

def f(R_string, key):
    expanded_R = e_bit(R_string)
    xor = str(bin(int(key, 2) ^ int(expanded_R, 2))[2:]).zfill(48)
    s_boxed = s_boxes(xor)
    sb_permutation = sbox_permutation(s_boxed)
    return sb_permutation

def final_permutation(binary_string):
    IP_inverse = [
    40, 8, 48, 16, 56, 24, 64, 32,
    39, 7, 47, 15, 55, 23, 63, 31,
    38, 6, 46, 14, 54, 22, 62, 30,
    37, 5, 45, 13, 53, 21, 61, 29,
    36, 4, 44, 12, 52, 20, 60, 28,
    35, 3, 43, 11, 51, 19, 59, 27,
    34, 2, 42, 10, 50, 18, 58, 26,
    33, 1, 41, 9, 49, 17, 57, 25
    ]
    new_string = ''


    for num in IP_inverse:
        new_string = new_string + binary_string[num - 1]

    return new_string

def plain_text_permutation(permutation_table, binary_string):
    new_string = ''
    for num in permutation_table:
        new_string = new_string + binary_string[num - 1]
    return new_string

def plain_text_permutation2(keys, binary_string):
    L = binary_string[:32]
    R = binary_string[32:]
    

    for key in keys:
        new_L = R
        new_R = str(bin(int(L, 2) ^ int(f(R, key), 2))[2:].zfill(32))
        R = new_R
        L = new_L

    permutated_string = new_R + new_L
    final_p = final_permutation(permutated_string)
    return final_p

def main():
    permutation_table = [
    57, 49, 41, 33, 25, 17, 9,
    1, 58, 50, 42, 34, 26, 18,
    10, 2, 59, 51, 43, 35, 27,
    19, 11, 3, 60, 52, 44, 36,
    63, 55, 47, 39, 31, 23, 15,
    7, 62, 54, 46, 38, 30, 22,
    14, 6, 61, 53, 45, 37, 29,
    21, 13, 5, 28, 20, 12, 4
    ]
    permutation_table2 = [
    14, 17, 11, 24, 1, 5, 3, 
    28, 15, 6, 21, 10, 23, 
    19, 12, 4, 26, 8, 16, 7, 
    27, 20, 13, 2, 41, 52, 31, 
    37, 47, 55, 30, 40, 51, 45, 
    33, 48, 44, 49,39, 56, 34,
    53, 46, 42, 50, 36, 29, 32
    ]
    plain_text_p_table = [
    58, 50, 42, 34, 26, 18, 10, 
    2, 60, 52, 44, 36, 28, 20, 
    12, 4, 62, 54, 46, 38, 30, 
    22, 14, 6, 64, 56, 48, 40, 
    32, 24, 16, 8, 57, 49, 41, 
    33, 25, 17, 9, 1, 59, 51, 
    43, 35, 27, 19, 11, 3, 61, 
    53, 45, 37, 29, 21, 13, 5, 
    63, 55, 47, 39, 31, 23, 15, 7
    ]

    default = None
    while default not in ('y', 'Y', 'n', 'N'):
        default = input('Would you like to use the default plain-text and key (y/n): ')
        if default in ('y', 'Y'):
            M = '0123456789ABCDEF'
            K = '133457799BBCDFF1'
        elif default in ('n', 'N'):
            M = input('Please enter a 16 digit hexadecimal number for the plain-text variable: ')
            K = input('Please enter a 16 digit hexadecimal number for the key varible: ')
        else:
            print('Invalid Input: Please type y or n (case insensitive)')
    
        if len(M) != 16 or len(K) != 16:
            default = None
            print('Invalid Input: Input must be a 16 digit hexadecimal number.')

    binary_M = s_to_binary(M)
    binary_K = s_to_binary(K)

    p1 = key_permutation(permutation_table, binary_K)
    p2 = key_permutation2(permutation_table2, p1)

    IP = plain_text_permutation(plain_text_p_table, binary_M)
    plain_text_p2 = plain_text_permutation2(p2, IP)
    hex_string = hex(int(plain_text_p2, 2))[2:].upper()
    print(f'\nEncrypted Text: {hex_string}\n')

if __name__ == '__main__':
    main()