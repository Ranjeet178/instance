import sys
import random
import time
import json


def Ec2pi_estimator(eR,q,rid):
    start = time.time()
    
    values=[]    
    shots = eR
    incircle = 0
    for i in range(1, shots+1):
        random1 = random.uniform(-1.0, 1.0)  
        random2 = random.uniform(-1.0, 1.0)  
        if( ( random1*random1 + random2*random2 ) < 1 ):
            incircle += 1
        if i % q == 0:
            values.append([incircle,i,rid])
    elapsed_time = time.time() - start
    return str({
        "values":values,
        "elapsed_time": elapsed_time,
    })



