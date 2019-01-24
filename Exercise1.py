#%% [markdown]
# Write a shutting down program:
# 
# First, def a function, shut_down, that takes one argument s.
# Then, if the shut_down function receives an s equal to "yes",
# it should return "Shutting down" Alternatively,
# elif s is equal to "no", then the function should 
# return "Shutdown aborted". Finally, if shut_down gets anything other than those inputs,
# the function should return "Sorry".

#%%
def shut_down(s):
    if s=="yes":
        return "shutting down"
    elif s == "no":
        return "Shutdown aborted"
    else:
        return "sorry"
shut_down("yes")

#%% [markdown]
# Define a function called hotel_cost with one argument nights as input.
# The hotel costs $140 per night.
# So, the function hotel_cost should return 140 * nights.

#%%
def hotel_cost(nights):
    cost =140
    return nights * cost
hotel_cost(4)

#%% [markdown]
# Define a function called plane_ride_cost that takes a string, city, as input.
# The function should return a different price depending on the location, similar to the code example above.
# Below are the valid destinations and their corresponding round-trip prices.
# "Charlotte": 183
# "Tampa": 220
# "Pittsburgh": 222
# "Los Angeles": 475

#%%
def plane_ride_cost(city):
    if city is "Charlotte":
        return 183
    elif city is "Tampa":
        return 220
    elif city is "Pittsburgh":
        return 222
    elif city is "Los Angeles" :
        return 475
plane_ride_cost("Tampa")

#%% [markdown]
# -Below your existing code, define a function called rental_car_cost with an argument called days. Calculate the cost of renting the car: Every day you rent the car costs $40.(cost=40*days) if you rent the car for 7 or more days, you get $50 off your total(cost-=50). Alternatively (elif), if you rent the car for 3 or more days, you get $20 off your total. You cannot get both of the above discounts. Return that cost. -Then, define a function called trip_cost that takes two arguments, city and days. Like the example above, have your function return the sum of calling the rental_car_cost(days), hotel_cost(days), and plane_ride_cost(city) functions.

#%%
def rental_car_cost(days):
    cost = 40 * days
    if days >= 7:
        return cost - 50
    elif days >= 3:
        return cost - 20
    else:
        return cost

rental_car_cost(10)


#%%
def trip_cost(city,days):
    return rental_car_cost(days) + hotel_cost(nights) + plane_ride_cost(city)


    


