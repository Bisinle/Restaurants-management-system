class Customer:
    def __init__(self, given_first_name="Hana", fam_name="Baker"):
        self._given_first_name = Customer.validate_user_input(given_first_name)
        self._fam_name = Customer.validate_user_input(fam_name)

    @staticmethod
    def validate_user_input(value1):
        if isinstance(value1, str):
            return value1

        else:
            return f" name should be a string not{type(value1)} "

    @property
    def given_name(self):
        return self._given_first_name

    @given_name.setter
    def given_name(self, value):
        self._given_first_name = Customer.validate_user_input(value)

    # family name getter  and setter
    @property
    def family_name(self):
        return self._fam_name

    @family_name.setter
    def family_name(self, value):
        self._fam_name = Customer.validate_user_input(value)

    @property
    def full_name(self):
        if isinstance(self.family_name, str) and isinstance(self.given_name, str):
            return "{} {}".format(self.family_name, self.given_name)
        else:
            return "fullname must me a string "


customer1 = Customer(78, 89)
# customer1.given_name = 90
print(customer1.given_name)
print("-------------")
print(customer1.family_name)
print("------------")
print(customer1.full_name)
# customer1.family_name = 23
