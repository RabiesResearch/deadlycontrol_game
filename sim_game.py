# import seaborn as sns
# import matplotlib.pyplot as plt

import numpy as np
from numpy.random import default_rng

rng = default_rng()

# Let's define a half-time of the game which is where 50% of games end in Rabies killing all the
T = 8
#`B` - number of bites per rabid dog per night
# number_of_players = 13
# nb_p = 0.35
# prob_bitten_dog_gets_rabies = 0.35
# prob_rabid_dog_dies = 0.5
# number_to_kill = 2

# number_of_players = 7
# nb_p = 0.35
# prob_bitten_dog_gets_rabies = 0.35
# prob_rabid_dog_dies = 0.5
# number_to_kill = 1

number_of_players = 16
starting_number_of_dogs_per_player = 2
nb_n = 1
nb_p = 0.45
prob_bitten_dog_gets_rabies = 0.5
prob_rabid_dog_dies = 0.3
number_to_kill = 3

total_end = []
rabid_end = []

for jjj in range(5000):
    number_of_rabid_dogs = 4
    total_dogs = number_of_players * starting_number_of_dogs_per_player

    #let's see what happens
    for iii in range(T):
        #first night dogs bite
        bitten = rng.negative_binomial(nb_n, nb_p, number_of_rabid_dogs).sum()
        # print(f'rabid dogs left {number_of_rabid_dogs}')
        # print(f'bitten number is {bitten}')
        #community kills dogs,
        #lets assume bitten dogos are twice as likely to be put down? nope?
        #probability is proportional to number of dogs nope?
        if total_dogs < number_to_kill:
            total_end.append(0)
            rabid_end.append(0)
            break

        if number_of_rabid_dogs==0:
            total_end.append(total_dogs)
            rabid_end.append(0)
            break

        killed = rng.integers(0,total_dogs, number_to_kill)
        total_dogs = total_dogs - len(killed)
        new_bitten = bitten
        for kkk in killed:
            if kkk < bitten:
                new_bitten = new_bitten -1
        # print(number_of_rabid_dogs)
        new_number_of_rabid_dogs = number_of_rabid_dogs
        for kkk in killed:
            if (kkk >= bitten) and (kkk < number_of_rabid_dogs):
                new_number_of_rabid_dogs = new_number_of_rabid_dogs -1


        bitten = new_bitten
        number_of_rabid_dogs = new_number_of_rabid_dogs

        if number_of_rabid_dogs < 1:
            total_end.append(total_dogs)
            rabid_end.append(0)
            break

        #dogs with rabies die
        dead_rabid = rng.binomial(number_of_rabid_dogs, prob_rabid_dog_dies)
        number_of_rabid_dogs = number_of_rabid_dogs - dead_rabid
        total_dogs = total_dogs - dead_rabid

        #some of the bitten dogs develop rabies
        number_of_rabid_dogs =  number_of_rabid_dogs + rng.binomial(number_of_rabid_dogs,prob_bitten_dog_gets_rabies)
        # print(f'total_dogs is {total_dogs}')
        # print(f'number_of_rabid_dogs is {number_of_rabid_dogs}')
        if iii == T-1: #last iteration
            total_end.append(total_dogs)
            rabid_end.append(number_of_rabid_dogs)

rabid_end_bool = list(map(lambda x: 1 if x >0 else 0, rabid_end))
total_end_bool = list(map(lambda x: 0 if x >0 else 1, total_end))

rabid_end_bool = np.add(rabid_end_bool,total_end_bool) # rabies win if they kill all dogs or if there are rabid dogs left after 8 (T) turns
print(sum(rabid_end_bool)/len(rabid_end_bool))
print(len(rabid_end_bool))

# a = sns.histplot(total_end,kde=True)
# # a.savefig('a.png')
# plt.title('total left')
# plt.show()


# b = sns.displot(rabid_end, kind='hist')

# plt.title('rabid left')
# plt.show()
# b.savefig('b.png')
