from customer import *
from Restaurant import *


class Review:
    review_list = list()

    def __init__(self, customer, restaurant, rating):
        # imported function from Customer
        self._customer = Customer.create_customer_dict(customer)
        # imported functions form Restaurant
        self._restaurant = Restaurant.get_name(restaurant)
        self._rating = Review.validate_integer(rating)
        self.creat_review_object(self)

    # ----------------------------------------------------------------------------------
    # method to validate if the rating is an integer or not
    @staticmethod
    def validate_integer(rating):
        if isinstance(rating, int):
            return rating
        else:
            return "rating should be an integer"

    # ----------------------------------------------------------------------------------
    # return the rating for  rating for a restaurant
    @property
    def rating(self):
        return self._rating

    # set the rating, user can changer the raiting they gave
    @rating.setter
    def rating(self, rating_value):
        self._rating = rating_value

    # ----------------------------------------------------------------------------------
    @classmethod
    def creat_review_object(cls, self):
        first_name = self._customer["first_name"]
        family_name = self._customer["family_name"]

        review_object = {
            "first_name": first_name,
            "family_name": family_name,
            "restaurant_name": self._restaurant,
            "rating": self._rating,
        }
        Review.add_review_to_list(review_object)

    @classmethod
    def add_review_to_list(cls, object):
        if object not in cls.review_list:
            cls.review_list.append(object)
        else:
            return cls.review_list

    # ----------------------------------------------------------------------------------
    @classmethod
    def print_all_reviews(cls):
        return [review for review in cls.review_list]


review1 = Review(customer1, restaurant1, 4)
review2 = Review(customer1, restaurant2, 2)
review3 = Review(customer1, restaurant3, 5)
# print(Review.print_all_reviews())

# print(review1.rating)
# print(review2.rating)
# print(review3.rating)
