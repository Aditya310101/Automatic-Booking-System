from booking.booking import Booking

with Booking(tearDown = False) as bot:
    bot.land_first_page()
    #bot.change_currency(currency='USD')
    bot.enter_destination('Goa')
    bot.dates_of_trip('2022-04-11','2022-04-16')
    bot.number_of_adults(4)
    bot.number_of_children(2)
    bot.number_of_rooms(3)

