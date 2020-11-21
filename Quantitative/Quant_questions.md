# Quant Questions:

### 1. Pirates Puzzle

We have 5 pirates of different ages that have a treasure of 100 gold coins.

On their ship, they decide to split the treasure by using this scheme:

- The oldest pirate proposes how to share the coins, and ALL pirates (including the oldest) vote for or against it.

- If 50% or more of the pirates vote for it, then the coins will be shared that way. 

- Otherwise, the pirate proposing the scheme will be thrown overboard, and the process is repeated with the pirates that remain.

**Considerations**: 

Pirates tend to be a bloodthirsty bunch, so if a pirate would get the same number of coins if he voted for or against 
a proposal, he will vote against so that the pirate who proposed the plan will be thrown overboard.

Assuming that these pirates are intelligent, rational, greedy, and do not wish to die, 
(and good at math for pirates)... what will happen?


#### Solution:

The oldest pirate will propose a split in (98, 0, 1, 0, 1), in other words the oldest pirate gets 98 coins, 
the middle pirate gets 1 coin and the youngest gets 1 coin.

Let us name the pirates (from oldest to youngest): Alex, Billy, Colin, Duncan and Eddie.

Working backwards:

- 2 Pirates: The oldest splits the coins (100, 0) He gives himself all the gold and his vote (50%) is enough to ensure the deal.

- 3 Pirates: Split proposed is (99, 0, 1). The youngest will accept this deal (just 1 coin), 
because he knows that if he rejects the deal there will be only two pirates left, and he gets nothing.

- 4 Pirates: The oldest splits the coins (99, 0, 1, 0). By the same reasoning as before, the one receiving 
one coin will support the deal. No coin is wasted on the following pirate as the following knows that by 
rejecting the proposal, he can pocket 99 coins once the oldest is thrown overboard. 
And no coin goes here to the youngest as the youngest knows as well that if he rejects the proposal, 
he will receive a coin in the next round anyway.

- 5 Pirates: The split is (98, 0, 1, 0, 1). By alternating between the pirates (0, 1) he is assured of a deal 
as the pirates receiving one coin in this deal would have received nothing in the next round.



### 2. Clock Angle

If you look at a clock and the time is 12:15, what is the angle between the hour and the minute hand?


#### Solution:

At 12:15 the angle is slightly less than 1/4. The reason is because the hour hand needs to move 
from 12 to 1 over the course of an hour. So it would have moved 1/4 of the space between 12 and 1.

The full 'clock' is 360 degrees, each hour is 30 degrees and it has moved 1/4, 
so the hour hand has moved 7.5 degrees.

The minute hand has moved 1/4 of 360 degrees, so that is 90 degrees.

So the angle between the two hands is 82.5 degrees



### 3. Three switches

You’re standing at three light switches at the bottom of the stairs to the attic. 
Each one corresponds to one of three lights in the attic, but you cannot see the lights 
from where you stand. You can turn the switches on and off and leave them in any position. 

How can you identify which switch corresponds to which light bulb 
if you are only allowed one trip upstairs?


#### Solution:

If you turn on the first 2 switches and left them on a few minutes, you can switch one off and go to check.

The switch on goes with the light on.

The switch that you just turn off goes with the light bulb that is off but still warm.

The switch that was never on goes with the light bulb that is off and cold.



### 4. Double the average speed

A car travels a distance of 60 miles at an average speed of 30 mph. 
How fast would the car have to travel for the same 60 mile distance home 
to average 60 mph over the entire trip?


#### Solution:

This is a tricky question as it is impossible.

The first trip took 2 hours (60 miles / 30 mph). 

In order to get the average to 60 mph over the entire trip 
you would have to travel the 120 miles (go and return) in 2 hours... 
which were already used in the first trip.



### 5. Thought process

There are many variants of this.
- Calculate the number of windows in London.
- How many kilos of chocolate were sold in UK the last year.
- How many mobile phones there are in UK.
- ...


#### Solution:

The important aspect of this problem is the approach and the logic applied to calculate the estimation.

Start by looking at the total population, divide the population into relevant age groups or families. 
Estimate consuming habits across the previous groups before adding all up to get the total market size.

Include other factors that have impact in the estimation. Ratio of offices vs residential areas, 
seasonal impacts on consumption like Valentine's Day or Halloween, etc...



### 6. Four liters

Get exactly four liters if you have only two containers, one of 5 liters and one of 3 liters.


#### Solution:

First fill the 5 liters and then pour the water from the 5 liters to the 3 liters.

You are left with 2 liters in the 5 liters container.

Empty the 3 liters and put in the 2 liters left in the other container.

Fill again the 5 liters, and pour water from the 5 liters into the 3 liter container till we fill it. 
As there is only volume for 1 liter, we will have 4 liters left.




