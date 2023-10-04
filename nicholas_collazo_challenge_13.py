import re
def its_right(digits):
    return type(digits) == str and re.match(r'^\d{3}-\d{3}-\d{4}$', digits)

def checker():
    number = input("Please enter a phone number formated as follows XXX-XXX-XXXX: ").strip()
    if number.isdigit():
        return
    elif its_right(number):
        print( (number), "is a valid phone number")
    else:
        print((number), "is not a valid phone number")

if __name__ =="__main__":
    checker()