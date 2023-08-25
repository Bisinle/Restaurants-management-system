class Customer:
    customer_instances_list = list()
    customer_count = 0

    def __init__(self, given_first_name="Hana", fam_name="Baker"):
        self._given_first_name = Customer.validate_user_input(given_first_name)
        self._fam_name = Customer.validate_user_input(fam_name)
        self.add_to_customer_instances_list(self)

    # ----------------------------------------------------------------------------------
    # method that cheks the type of the initialized variables
    @staticmethod
    def validate_user_input(value1):
        if isinstance(value1, str):
            return value1
        else:
            return f" name should be a string not{type(value1)} "

    # ----------------------------------------------------------------------------------

    # first /given name getter and setter
    @property
    def given_name(self):
        return self._given_first_name

    @given_name.setter
    def given_name(self, value):
        self._given_first_name = Customer.validate_user_input(value)

    # ----------------------------------------------------------------------------------

    # family name getter  and setter
    @property
    def family_name(self):
        return self._fam_name

    @family_name.setter
    def family_name(self, value):
        self._fam_name = Customer.validate_user_input(value)

    # ----------------------------------------------------------------------------------

    @property
    def full_name(self):
        if isinstance(self.family_name, str) and isinstance(self.given_name, str):
            return "{} {}".format(self.family_name, self.given_name)
        else:
            return "fullname must me a string "

    # ----------------------------------------------------------------------------------

    # class method that creates the instance dict and addes to the  customer_instances_list
    # and alos prevents duplicates inthe list of instances
    @classmethod
    def add_to_customer_instances_list(cls, self):
        cls.customer_List_dict = {
            "firs_name": self.given_name,
            "family_name": self.family_name,
        }
        # check for duplicate and add if there are None
        if cls.customer_List_dict not in cls.customer_instances_list:
            cls.customer_instances_list.append(cls.customer_List_dict)
        else:
            return cls.customer_instances_list

    # print the instance list in customer_instances_list
    @classmethod
    def all(cls):
        return [instances for instances in cls.customer_instances_list]

    # ----------------------------------------------------------------------------------


customer1 = Customer("Allan", "Kunta")
customer2 = Customer("Camila", "Carlos")
customer3 = Customer("Abdi", "Jalwo")

# print(Customer.customer_List[0].given_name)
print(customer1.all())
# print("----------------------")
# # customer1.given_name = 90
# print(customer1.given_name)
# print("-------------")
# print(customer1.family_name)
# print("------------")
# print(customer1.full_name)
# # customer1.family_name = 23
