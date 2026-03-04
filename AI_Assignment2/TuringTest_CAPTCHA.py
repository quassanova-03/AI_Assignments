import random
import string

# Generate random captcha
def generate_captcha(length=6):
    characters = string.ascii_letters + string.digits
    captcha = ''.join(random.choice(characters) for _ in range(length))
    return captcha

# Add spaces to make it harder for bots
def distort_text(text):
    distorted = " ".join(text)
    return distorted

def main():
    print("\n------ TEXT CAPTCHA VERIFICATION ------\n")

    captcha = generate_captcha()
    display = distort_text(captcha)

    print("Enter the characters shown below:\n")
    print(display)
    print()

    user_input = input("Enter CAPTCHA: ")

    if user_input == captcha:
        print("\nAccess Granted! You are human.")
    else:
        print("\nAccess Denied! CAPTCHA incorrect.")

main()