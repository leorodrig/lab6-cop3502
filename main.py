# lab 6, version control

def main():
    # print menu
    print("""
    Menu
    -------------
    1. Encode
    2. Decode
    3. Quit""")
    # user input and functions
    running = True
    while running:
        user_input = int(input("Please enter an option: "))
        if user_input == 1:
            encoded_pw = input("Please enter your password to encode: ")
            # add encode function here
        elif user_input == 2:
            encoded_pw = input("Please enter your password to decode: ")
            if len(encoded_pw) != 8:
                quit()
            password = decoder(encoded_pw)





        else:
            quit()


def decoder(string_pw):
    new_val_list = []
    for val in string_pw:
        val = int(val)
        val -= 3
        val = str(val)
        new_val_list.append(val)
    decoded_pw = ''.join(new_val_list)
    return decoded_pw

if __name__ == "__main__":

