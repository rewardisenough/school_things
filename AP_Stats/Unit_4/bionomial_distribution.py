import math
#Binomial distribution

def bionomial_dist():
  # applies to both single and cumulative probability
  
  random_variable = input('What is the random variable?: ')
  success = input('What is the success outcome: ')
  failure = input('What is the failure outcome: ')
  
  is_independent = input('Are the trials independent? Yes or no: ')
  
  if(is_independent == 'no'):
    print('Sorry the trials has to be independent. Terminating...')
    return 

  fixed_trials = int(input('What is the fixed number of trials?: '))

  prob_of_success = float(input(f'What is the probability of {success} occuring?: '))
    
  
  # Ask if single or cumulative probability
  type = input('Do you want to calculate single or cumulative probability?: ')
  if(type=='single'):
    num_of_success = int(input(f'Out of {fixed_trials}, how many times of success do you expect?: '))
    combination_formula =(math.factorial(fixed_trials))/(math.factorial(num_of_success)*(math.factorial(fixed_trials-num_of_success)))
    probability = combination_formula * math.pow(prob_of_success,num_of_success) * math.pow(1-prob_of_success,fixed_trials-num_of_success)
    
    rounded_prob = round(probability,4)
    print(f"The probability that {num_of_success} trials of {fixed_trials} trials will become {success} is {rounded_prob}")


  if(type=='cumulative'):
    up_or_below = input('at_least? or up to that?')
    
    if(up_or_below=='at_least'):
      num_of_success = int(input(f'Out of {fixed_trials}?, how many times of success is at least going to occur?: '))
      
    if(up_or_below=='up to that'):
      num_of_success = int(input(f'Out of {fixed_trials}?, how many times of success is it going to occur up to?: '))
      
    probability = 0 # defined probability outside of loop.
      
    for i in range(num_of_success): # cdf can only take values of <=
      combination_formula = (math.factorial(fixed_trials))/(math.factorial(i)*(math.factorial(fixed_trials-i)))
      
      probability += combination_formula * math.pow(prob_of_success,i) * math.pow(1-prob_of_success,fixed_trials-i)

    
    # output for either at_least or up to that.  
    if(up_or_below=="at_least"):
      probability = 1 - probability
      rounded_prob = round(probability,4)
      print(f"The probability that at least {num_of_success} trials of {fixed_trials} trials will become {success} is {rounded_prob}")
    else:
      rounded_prob = round(probability,4)
      print(f"The probability that up to {num_of_success} trials of {fixed_trials} trials will become {success} is {rounded_prob}")
  


