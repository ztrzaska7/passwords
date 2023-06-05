import random
import string
def generate_password(length=8):
    lowercase_signs=string.ascii_lowercase
    uppercase_signs=string.ascii_uppercase
    digits=string.digits
    special_signs=string.punctuation

    chars=lowercase_signs+uppercase_signs+digits+special_signs
    password="".join(random.choice(chars) for _ in range(length))
    return password
def main():
    length=int(input("Enter password's length: "))
    password=generate_password(length)
    print("Generated password is: ",password)
if __name__=='__main__':
    main()