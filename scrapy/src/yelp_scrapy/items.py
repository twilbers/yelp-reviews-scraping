from scrapy import Item, Field


class BizItem(Item):

    business_name = Field()
    business_city = Field()
    business_state = Field()
    business_url = Field()
    business_zip = Field()
    business_star_rating = Field()
#     number_of_reviews = Field()
#     price = Field()
#     cuisine = Field()
#     liked_by_vegetarians = Field()
#     takes_reservations = Field()
#     delivery = Field()
#     take_out = Field()
#     accepts_credit_cards = Field()
#     accepts_apple_pay = Field()
#     accepts_google_pay = Field()
#     good_for_lunch = Field()
#     parking_garage = Field()
#     bike_parking = Field()
#     good_for_kids = Field()
#     good_for_groups = Field()
#     attire_casual = Field()
#     ambience = Field()
#     noise_level = Field()
#     alcohol_full_bar = Field()
#     outdoor_seating = Field()
#     wi_fi = Field()
#     has_tv = Field()
#     dogs_allowed = Field()
#     drive_thru = Field()
#     caters = Field()

class UserItem(Item):

    user_url = Field()
    reviewer_location = Field()
    review_text = Field()
    label = Field()
    review_date = Field()
    review_raiting = Field()
    feedback = Field()
#     check_ins = Field()
#     friends = Field()
#     review_count = Field()
#     eliet = Field()