import random
import string

def generate_password(length=8):
    lowercase_letters=string.ascii_lowercase
    uppercase_letters=string.ascii_uppercase
    digits=string.digits
    special_chars=string.punctuation

    chars=lowercase_letters+uppercase_letters+digits+special_chars

    password=''.join(random.choice(chars) for _ in range(length))
    return password
def main():
    length=int(input("Get password's length: "))
    password=generate_password(length)
    print("The password generated is: ",password)
if __name__ == '__main__':
    main()
    