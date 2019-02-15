import random

random.seed(42) # define a seed to ensure we get the same result every time

print(random.random()) # creates random

print(random.randrange(0, 100)) # returns an integer between [1-99]


list_of_ten = [i for i in range(10)] # create a simple list
print(list_of_ten)

random.shuffle(list_of_ten) # shuffles the list
print(list_of_ten)

my_fav_number = random.choice(list_of_ten) # picks a random element
print(f"my favourite number is {my_fav_number}")

samples_range = range(10)
my_samples = random.sample(samples_range, 5) # creates 5 samples without duplicates
print(my_samples)

my_samples = [random.choice(samples_range) for _ in range(5)] # creates 5 samples with possible duplicates
print(my_samples)