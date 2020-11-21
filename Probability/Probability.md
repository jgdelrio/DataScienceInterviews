# Probability

### 1. Two out of three

(Data Science > Probability)

Suppose you flip a fair coin 3 times. What is the probability of getting exactly two heads?

Note: Fair coin means that every possible result has the same probability.

1. 2/3
2. 1/3
3. 3/8
4. 1/8

##### Answer:
The probability of any flip is 0.5 for both heads or tails. Total permutations is 2<sup>3</sup>

P(2h) = 1 - P(3h) - P(3t) - 2*P(2t) = 1 - (2 * 1/8) - P(2t)

Since P(2h) = P(2t) --->  2P(2h) = 1 - 2/8 --> P(2h) = 3/8



### 2. A/B Test

(Data Science > Bayes' Theorem)

Your company is running a test that is designed to compare two different versions of the company’s website.

Version A of the website is shown to 60% of users, while version B of the website is shown to the remaining 40%. 
The test shows that 8% of users who are presented with version A sign up for the company’s services, 
as compared to 4% of users who are presented with version B.

If a user signs up for the company’s services, what is the probability that she/he was presented with version A of the website?

##### Answer:

|   | A  |  B |
|---|---|---|
| Users  | 0.6  | 0.4  |
|  Conversion | 0.08  | 0.04  |

The probability of a user signing up and visiting a specific version is calculated by multiplying the chance of that site appearing by its conversion ratio.

P(vA|signup) = P(signup|vA) P(vA)  /  P(signup)
P(vA|signup) = P(signup intersecting vA) /  P(signup)

P = (0.6 * 0.08) / ( (0.6*0.08) + (0.4*0.04)) = 0.75



### 3. Second girl probability

(Data Science > Probability)

Alice has 2 kids. We know that one of them is girl. What is the probability the other kid is also a girl?
Assume there are equal probability of girl and boy.

1. 0.5
2. 0.25
3. 0.333
4. 0.75

##### Answer:
This can be resolved two ways. With boy:b and girl:g
- With the full cases: we can have... bb, bg, gb and gg but as we already know one is a girl we are left with three cases, bg, gb, and gg from which only one case has another girl, so 1/3

- Using Bayes' Theorem: P(having 2g | having at least 1) = P(having at least 1 | having 2g) P(having 2g) / P(having at least 1) = 1 * 0.25 / 0.75 = 1/3

It is worth mentioning the [Boy or Girl paradox](https://en.wikipedia.org/wiki/Boy_or_Girl_paradox). If we fix the known girl as the older, then the answer of the probability of the second being also girl would be 0.5



### 4. Probability of one even and one odd number

(Data Science > Probability)

The change of getting i when rolling a biased six-sided die is proportional to i. We roll it 2 times.
What is the probability of getting one even and one odd number?

1. 24/49
2. 1/3
3. 12/49
4. 1/4

##### Answer:
The probability of any number is proportional to itself and the total must be 1, so P(1+2+3+4+5+6) = 1

P(1)=1/21, P(2)=2/21 ... P(6)=6/21

P(odd) = (1+3+5)/21 = 3/7

P(even) = (2+4+6)/21 = 4/7

Looking at it in different ways...
- P(odd & even) = 1 - P(2odds) - P(2even) = 1 - 9/49 - 16/49 = 24/49
- P(odd & even) = P(1st odd & 2nd even) + P(1st even & 2nd odd) = 2 * (3/7 * 4/7) = 24/49



### 5. Revolver with two bullets

(Data Science > Probability)

You are playing a version of the Russian roulette where the revolver has two consecutive bullets.
Your opponent puts the two consecutive bullets in two chambers of the 6 available in the revolver.
Then he puts the revolver in his head, pulls the trigger and survive.

Now is your turn and you're given two choices:
- Put the gun straight to your head and pull the trigger
- Spin the cylinder of the revolver before putting the gun in your head and pulling the trigger

Which one do you choose and why? 

The assumptions that are not mentioned is that your objective is to survive the game 
as well as that spinning the revolver gives us a completely random result not influenced 
by the weight of the bullets or anything else. The revolver never gets jammed and never misses.


##### Answer:

The possibilities for the position of the bullets (B) are as shown in the table:

| Chamber | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| I | B | B | x | x | x | x |
| II | x | B | B | x | x | x |
| III | x | x | B | B | x | x |
| IV | x | x | x | B | B | x |
| V | x | x | x | x | B | B |
| VI | B | x | x | x | x | B |

But it doesn't matter. Let's take any of the possibilities:  x | B | B | x | x | x

The main point here to be aware off is the fact that when the opponent 
pulls the trigger and it didn't fire, there are 4 positions or possibilities in which the 
revolver may have been.

In three of those positions the next pull of the trigger will be save and only in one 
the revolver will fire. Let's call S = survival, then the probability of survival 
without spinning again the revolver is:

P(S) = 3/4 = 0.75

If I spin the revolver the probability of ending on any chamber is the same (1/6) 
and there are 2 possibilities (bullets) out of 6 of finding a bullet, or 4 possibilities out of 6 of finding an empty chamber:

P(S) = 4/6 = 0.66

So I wouldn't spin the cylinder if I were you...



### 6. Revolver variation

(Data Science > Probability)

This is a variation of the previous scenario.

Now between the 2 bullets we have 2 empty chambers. Everything else is the same as before.

Again you're given two choices:
- Put the gun straight to your head and pull the trigger
- Spin the cylinder of the revolver before putting the gun in your head and pulling the trigger

Which one do you choose and why? 


##### Answer:

Now we have the following setup:  

| Chamber | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| II | B | x | x | B | x | x |

We have 4 possible positions of the revolver when it didn't fire but as you can see 2 of those positions are repeated. 
In one position it will be safe to pull the trigger again. In the other it won't.

That means that if we don't spin:

P(S) = 1/2 = 0.5

If I spin the revolver there is equal probability of ending at any of the six chambers (1/6) and we have 2 bullets. 
As in the previous case we have 4 safe positions out of 6:

P(S) = 4/6 = 0.66

So now, even if the difference is only 16%, I would spin the cylinder of the revolver...