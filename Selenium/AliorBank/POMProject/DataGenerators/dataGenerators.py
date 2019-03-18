import string
import random
from rstr import xeger


class DataGenerators():

    def generateEmailAddress(self):
        email = xeger(r'[a-zA-Z0-9-]{7}@[a-zA-Z0-9-]{3}\.com')
        print("Generated email is " + email)
        return email

    def generateFirstName(self):
        length = random.randint(1, 15)
        firstName = ''.join(random.choices(string.ascii_letters, k=length))
        print("Generated first name is " + firstName)
        return firstName

    def generateLastName(self):
        length = random.randint(1, 100)
        lastName = ''.join(random.choices(string.ascii_letters, k=length))
        print("Generated last name is " + lastName)
        return lastName
