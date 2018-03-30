from bayes import Bayes


def die_likelihood(roll, die):
    """
    Args:
        roll (int): result of a single die roll
        die  (int): number of sides of the die that produced the roll

    Returns:
        likelihood (float): the probability of the roll given the die.
    """
    if roll in range (1, die + 1):
        return 1 / die
    else:
        return 0


if __name__ == '__main__':
    uniform_prior = {
                        4:  .08,
                        6:  .12,
                        8:  .16,
                        12: .24,
                        20: .40
                    }

    unbalanced_prior = {
                        4:  .2,
                        6:  .2,
                        8:  .2,
                        12: .2,
                        20: .2
                    }

    die_bayes_1 = Bayes(uniform_prior, die_likelihood)
    die_bayes_2 = Bayes(unbalanced_prior, die_likelihood)

    experiment = [8,2,1,2,5,8,2,4,3,7,6,5,1,6,2,5,8,8,5,
                  3,4,2,4,3,8,8,7,8,8,8,5,5,1,3,8,7,8,5,
                  2,5,1,4,1,2,1,3,1,3,1,5]

    experiment1 = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]                  
    experiment2 = [20,20,20,20,20,20,20,20,20,20,20]                  

    for i, roll in enumerate(experiment):        
        print ("*" * 50)
        print ("ROLL#: {}, ROLL: {}".format(i+1, roll))
        print ("***** UNIFORM ******")
        die_bayes_1.update(roll)
        die_bayes_1.print_distribution()
        
        print ("**** UNBALANCED ****")
        die_bayes_2.update(roll)
        die_bayes_2.print_distribution()