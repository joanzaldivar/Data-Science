# Object-oriented Bayes Dice Exercise

## Part 1

We're going to start with an example with Python.

A box contains a 4-sided die, a 6-sided die, an 8-sided die, a 12-sided die, and a 20-sided die. A die is selected at random, and the rest are destroyed.

We would like to determine which die I have selected, given only information of what I roll.

We will be implementing a `Bayes` class that is able to handle Bayesian updates in the discrete case.
A prior is defined and at each data point, a likelihood is computed and the
prior is updated to give the posterior.

**The posterior becomes the prior at the next data point.**

The starter code is provided for you in `bayes.py` and `dice.py`.

1. Write the `normalize` method. It scales the probabilities in `self.prior` so that they sum to 1. `self.prior` will be a member of your
`Bayes` class that holds the probability for each type of die.

   To normalize, you need to find the sum of all the probabilities and then divide each probability by this value, modifying them in-place.

1. Write the `update` method. It should take the result of one test, calculate the likelihood for each die and use it to calculate the posterior probability for each die. The posterior should now be your prior.

    The likelihood function should be used like this:

    ```python
    self.likelihood_func(roll, die)
    ```

    Here, `roll` means the result of one roll, and `die` means which kind of die was rolled.

    Make sure to call the `normalize` method as the final step!

1. Write the `print_distribution` method in order to print out the current prior.

    It will be easier to read if you print the values in sorted order so you'll always see them in a consistent order.

## Part 2

Now we're ready to use our code to verify our intuition about the dice problem. You'll need to run several simulations using your bayes code.

We are going to consider both a uniform prior and the unbalanced prior from above:

```
4-sided die: 8%
6-sided die: 12%
8-sided die: 16%
12-sided die: 24%
20-sided die: 40%
```

Put all the code you use to answer these questions in `dice.py` (which uses your `Bayes` class).

1. Encode info about your priors into data structures.

    ***Note: When you pass these into your `Bayes` class, you should somehow ensure that the original priors are left unchanged. Hint: `.copy()` If you do not do this, your prior and won't be usable in subsequent uses of `Bayes`.***

1. Implement the likelihood function. It should take the data (in this case a number 1-20) and the die number (4, 6, 8, 12 or 20).

1. First, let's examine the case where we only roll the die once. Say we roll a single 8.

    * What are the posteriors if we started with the uniform prior?

    * What are the posteriors if we started with the unbalanced prior?

    * How different were these two posteriors?

1. Let's say you get all this data:

    ```
    [8,2,1,2,5,8,2,4,3,7,6,5,1,6,2,5,8,8,5,3,4,2,4,3,8,
     8,7,8,8,8,5,5,1,3,8,7,8,5,2,5,1,4,1,2,1,3,1,3,1,5]
    ```

    * What are the posteriors if we started with the uniform prior?

    * What are the posteriors if we started with the unbalanced prior?

    * How different are these two posteriors?

1. With the uniform prior, which of these two sets of data leads to a more certain posterior? `[1, 1, 1, 3, 1, 2]` or `[10, 10, 10, 10, 8, 8]`
