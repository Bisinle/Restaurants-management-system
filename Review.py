from customer import *
from Restaurant import *


class Review:
    rating_list = list()

    def __init__(self, customer, restaurant, rating):
        self._cutomer = customer
        self._restaurant = restaurant
        self._rating = Review.validate_integer(rating)

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

    @rating.setter
    def rating(self, rating_value):
        self._rating = rating_value


review1 = Review(customer1, restaurant1, 4)
review2 = Review(customer1, restaurant2, 2)

print(review1.rating)
print(review2.rating)
