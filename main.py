# lab 6, version control

def main():
    pass


def decoder(string_pw):
    new_val_list = []
    for val in string_pw:
        val = int(val)
        val += 3
        val = str(val)
        new_val_list.append(val)
    decoded_pw = ''.join(new_val_list)
    return decoded_pw
