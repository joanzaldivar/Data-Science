class Bayes(object):
    '''
    INPUT:
        prior (dict): key is the value (e.g. 4-sided die),
                      value is the probability

        likelihood_func (function): takes a new piece of data and the value and
                                    outputs the likelihood of getting that data
    '''
    def __init__(self, prior, likelihood_func):
        self.prior = prior
        self.likelihood_func = likelihood_func
        
    def normalize(self):
        '''
        INPUT: None
        OUTPUT: None

        Makes the sum of the probabilities equal 1.
        '''
        #alternate solution #1 -- this doesn't work because it recreates the prior 
        # instead of updating it
        #self.prior = {k:v/sum(self.prior.values()) for k, v in self.prior.items()}
        
        total = sum(self.prior.values())
        #print("total before normalization: {}".format(total))
        for k, v in self.prior.items():            
            self.prior[k] = self.prior[k] / total          
        #total = sum(self.prior.values())
        #print("total after normalization: {}".format(total))

    def update(self, data):
        '''
        INPUT:
            data (int or str): A single observation (data point)

        OUTPUT: None

        Conduct a bayesian update. Multiply the prior by the likelihood and
        make this the new prior.
        '''
        #alternate solution #1
        #self.prior = {k:v*self.likelyhood_func(data,k) for k, v in self.prior.items()}
        #self.normalize()
        
        #alternate solution #2
        #for die in self.prior:
        #    self.prior[die] *= self.likelihood_func(data, die)
        
        for die, prior in self.prior.items():
            #print("update die: {}, prior: {}, likelihood: {}".format(die, self.prior[die], self.likelihood_func(data, die)))
            self.prior[die] = self.prior[die] * self.likelihood_func(data, die)
            #print("updated die: {}, posterior: {}".format(die, self.prior[die]))
        self.normalize()    
        

    def print_distribution(self):
        '''
        Print the current posterior probability.
        '''
        #alternate solution #1
        #print(sorted(self.prior.items()))
        
        for die in sorted(self.prior.keys()):
            print ("die: {}, posterior: {}".format(die, self.prior[die]))