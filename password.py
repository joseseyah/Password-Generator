import random
# variables of characters and letters etc.
letters_and_numbers = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMOPQRTSUVWXYZ1234567890"
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMOPQRTSUVWXYZ1234567890!£$%&*@#?"
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMOPQRTSUVWXYZ"

characters_letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMOPQRTSUVWXYZ!£$%&*@#?"

personal_lenght = int(
    input("How many characters would you like your password to be (4-12)? "))
want_number = input("Do you wanna include numbers (y/n)? ")
want_special_characters = input(
    "Do you wanna include special characters (y/n)? ")

while True:
    if want_number.lower() == 'y':
        if want_special_characters.lower() == 'y':
            generated_passwords = random.choices(
                characters, k=personal_lenght)
            final_password = ''.join(str(x) for x in generated_passwords)
            print(final_password)
            break
        elif want_special_characters.lower() =='n':
            generated_passwords = random.choices(
                letters_and_numbers, k=personal_lenght)
            final_password = ''.join(str(x) for x in generated_passwords)
            print(final_password)
            break
        elif want_special_characters.lower() =="q":
            print("Thank you! Goodbye")
            break
    
    elif want_number.lower() == 'n':
        if want_special_characters.lower() == 'y':
            generated_passwords = random.choices(
                characters_letters, k=personal_lenght)
            final_password = ''.join(str(x) for x in generated_passwords)
            print(final_password)
            break
        elif want_special_characters.lower() =='n':
            generated_passwords = random.choices(
                letters, k=personal_lenght)
            final_password = ''.join(str(x) for x in generated_passwords)
            print(final_password)
            break
        elif want_special_characters.lower() =="q":
            print("Thank you, Goodbye!")
            break
    elif want_number.lower() =="q":
        print("Thank you, Goodbye!")
        break