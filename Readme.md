Deadly Control - Rabies Edition
A fun family game where the only way of controlling a rabies outbreak is by killing neighbours dogs!
Mungo ma mbwa is the Dog God, the master of ceremony aka activity coordinator for the family-friendly (no animals were killed during the making of this) game ‘Deadly Control’.

In the Sukuma village of Maishamambwa there was an unfortunate incident in the middle of the night in early Sept 2022. A strange hyena arrived from neighbouring village Mbwehakali that was showing signs of a strange disease (a bit like rabies but not quite - Gurdeep is on the case with her MinION ready to share the new sequences that can help us to identify this scary emerging infectious disease!). The sick dog ran around without direction biting dogs that were roaming in the village. You are all members of the community in Maishamambwa and dog keeping is very common. Tonight several of the dogs that were bitten developed this deadly rabies-like illness.

The objective of the game is to control this deadly disease, which is possible to do by killing off all infected dogs. If there is a full-blown pandemic all dogs in the community die (or are killed), and the winner is the last standing dog. Alternatively, if the community controls the disease, all those with dogs remaining are winners and the person with the most dogs is the overall winner of the game and saviour of Maishamambwa.

Random stuff to be parameterised:
`B` - number of bites per sick dog per night
`H` - probability of sick dogs dying each night (going to heaven)
`T` - probability of a dog becoming sick after a bite

Game parameters:
`d_0` - starting number of dogs, `z` * number of players
`r_0` - number of sick dogs in the population at the beginning of the game
`k` - number of dogs to be culled by the community each turn. For instance being top `k` choices from a democratic vote.

Rules:
During the day you are a household that contains `z` dogs, each represented by a playing card:
**Red** represents a rabid(?) sick and infectious dog
**black** a healthy dog. 
Players don't have to show how many dogs they have (cards can be stacked). 
Mungo ma mbwa deals cards to all players.

Everyone checks their cards
Night begins and everyone closes their eyes and lies down on the table.
Mungo ma mbwa asks the sick dogs to awaken. During the night if a player has one or more cards in **red** they have to play each of the sick (rabid) dogs in their household. The players are called by Mungo to bite `b` dogs in the community. Any healthy dogs can be bitten, including ones in that player’s own household (and ones that have already been bitten by other sick dogs).
Mungo keeps a tally and location of the total dogs that are bitten.
Day breaks.
Mungo tells the households at dawn if and how many of their dogs have been bitten, and cards for those dogs are held/put face up so everyone can see which households have bitten dogs and how many.
Community gathering
The community votes to cull any `k` selected dogs. Those can be either bite victims or any other suspected rabid dogs. If a player has multiple face-down cards and is voted to have one of them culled, they need to shuffle cards and reveal the top one which is taken by Mungo to dog heaven (thanks to RDT we know if it was or wasn't rabid :) )
Night begins, everyone closes their eyes.
a. Mungo takes `h` sick dogs to dog heaven, taking those cards out of the game.
b. Out of bitten dogs `t` dogs develop the illness: Mungo takes all the bitten dogs cards, shuffles in `t` red/rabies cards, and deals them to the affected households, all the cards are held face down.
Return back to point 1.




