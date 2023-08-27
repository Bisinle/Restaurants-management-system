class Customer:
    customer_instances_list = list()
    review_list = []

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

    def full_name(self):
        if isinstance(self.family_name, str) and isinstance(self.given_name, str):
            return "{} {}".format(self.family_name, self.given_name)
        else:
            return "fullname must me a string "

    # ----------------------------------------------------------------------------------
    def create_customer_dict(self):
        customer_object = {
            "first_name": self.given_name,
            "family_name": self.family_name,
        }
        return customer_object

    # class method that creates the instance dict and addes to the  customer_instances_list
    # and alos prevents duplicates inthe list of instances
    @classmethod
    def add_to_customer_instances_list(cls, self):
        customer_object = cls.create_customer_dict(self)
        # check for duplicate and add if there are None
        if customer_object not in cls.customer_instances_list:
            cls.customer_instances_list.append(customer_object)
        else:
            return cls.customer_instances_list

    # print the instance list in customer_instances_list
    @classmethod
    def all(cls):
        return [instances for instances in cls.customer_instances_list]

    # ----------------------------------------------------------------------------------
    # return unique restaurants the cusomter has reviewed
    def restaurants_reviewed(self):
        from review import Review

        review_list = Review.REVIEW_LIST
        # print((Review.REVIEW_LIST))

        unique_restaurant_list = list()

        for customer in Review.REVIEW_LIST:
            if customer["full_name"] == self.full_name():
                unique_restaurant_list.append(customer["restaurant_name"])

        return (
            set(unique_restaurant_list)
            if len(unique_restaurant_list) > 0
            else f"{self.full_name()} has not given reviews "
        )

    # ----------------------------------------------------------------------------------
    #   - given a **restaurant object** and a star rating (as an integer), creates a new review and associates it with that customer and restaurant.
    def add_review(self, resaurant, rating):
        from review import Review

        new_review = Review(self, resaurant, rating)


customer3 = Customer("Abdi", "Jalwo")
# print(customer3.restaurants_reviewed())


# print(Customer.customer_List[0].given_name)
# print(customer1.all())
# print("----------------------")
# # customer1.given_name = 90
# print(customer1.given_name)
# print("-------------")
# print(customer1.family_name)
# print("------------")
# print(customer1.full_name)
# # customer1.family_name = 23
