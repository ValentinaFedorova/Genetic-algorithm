import math
import random

        
def myFunc(e):
  return e['g']


def goldsteinprice_func(x1,x2):
    return (1 + math.pow(x1+x2+1,2)*(19 - 14*x1+3*math.pow(x1,2)-14*x2+6*x1*x2+3*math.pow(x2,2)))*(30+math.pow(2*x1-3*x2,2)*(18-32*x1+12*math.pow(x1,2)+48*x2-36*x1*x2+27*math.pow(x2,2)))
#print(goldsteinprice_func(0,-1))
def mccormick_function(x1,x2):
    p = x1 - x2
    return math.sin(x1+x2) + math.pow(p,2) - 1.5*x1 + 2.5*x2 + 1

def gen_algorithm(l_lim_x1,h_lim_x1,l_lim_x2,h_lim_x2,func):
    low_limit_x1 = l_lim_x1
    high_limit_x1 = h_lim_x1
    low_limit_x2 = l_lim_x2
    high_limit_x2 = h_lim_x2

    chromosomes = []
    for i in range(0,4):
        x1=random.uniform(low_limit_x1,high_limit_x1)
        x2 = random.uniform(low_limit_x2,high_limit_x2)
        g = func(x1,x2)
        chromosomes.append({'x1':x1,'x2':x2,'g':g})
    chromosomes.sort(key=myFunc)



    cnt = 0
    minimum = chromosomes[0]['g']
    while cnt<1000000:
    

        next_generation = []

        for i in range(1,len(chromosomes)-1):
            next_generation.append({'x1':chromosomes[0]['x1'],'x2':chromosomes[i]['x2']})
            next_generation.append({'x1':chromosomes[i]['x1'],'x2':chromosomes[0]['x2']})

        next_generation[3]['x1'] = random.uniform(low_limit_x1,high_limit_x1)
        next_generation[3]['x2'] = random.uniform(low_limit_x2,high_limit_x2)
        for i in range(0,len(next_generation)):
            next_generation[i]['g'] = func(next_generation[i]['x1'],next_generation[i]['x2'])

        chromosomes = next_generation

        chromosomes.sort(key=myFunc)
     

    
        current_min = chromosomes[0]['g']
        if minimum > current_min:
            minimum = current_min

        cnt = cnt + 1 

    return(chromosomes[0]['x1'],chromosomes[0]['x2'],minimum)
    
    

result = gen_algorithm(-1.5,4,-3,4,mccormick_function)
print("Точка минимума для функции МакКормика: [",result[0]," , ",result[1],"]")
print("Значение в точке минимума: ", result[2])

result2 = gen_algorithm(-2,2,-2,2,goldsteinprice_func)
print("Точка минимума для функции Гольдман-Прайса: [",result2[0]," , ",result2[1],"]")
print("Значение в точке минимума: ", result2[2])



