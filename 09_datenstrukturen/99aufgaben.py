import random
numberOfExperiments=100000
numberOfStreaks = 0
for experimentNumber in range(numberOfExperiments):
    # Code that creates a list of 100 'heads' or 'tails' values.
    experiment = []
    for throw in range(100):
        #istKopf=False
        #if random.randint(0,1)==1:
        #    istKopf=True
        #experiment.append(istKopf)
        experiment.append(True if random.randint(0,1)==1 else False)
    # Code that checks if there is a streak of 6 heads or tails in a row.
    # K K Z K K K K K K K
    last_item = experiment[0]
    count = 1
    for throw in range(1,100):
        throw_value=experiment[throw]
        if throw_value == last_item:
            count = count+1
            if count==6:
                #6-streak found
                numberOfStreaks=numberOfStreaks+1
                break
        else:
            last_item=throw_value
            count=1
print('Chance of streak', 100*numberOfStreaks / numberOfExperiments, "%"),