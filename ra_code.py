# Code for Research Assistant project by Surya Roshan Mugada
from urllib import response
from cv2 import exp
import requests
import random
def get_api_draw(api_url):
    response=requests.get(api_url)
    return response

#use the api url to get the data
def make_data(no_of_draws,api_url):
    data=[]
    for i in range(no_of_draws):
        response=get_api_draw(api_url)
        if response.status_code==200:
            response_json=response.json()
            strList=response_json['body']
            strList=strList.strip('][').split(', ')
            strList=[int (x) for x in strList]
           # print(type(response_json['body']))
            data.append(strList)
        else:
            print("Api endpoint not functioning properly..")
            exit()
    return data 


# given the number of heads, identify the probability of the set of flips belonging to one of the coins
def get_prob(heads,no_of_data,theta):
    #theta[0] = probability of getting heads from coin A
    #theta[1] = probability of getting heads from coin B
    
    #using variables following mathematical notation for clarity of understanding
    p=theta[0]
    q=theta[1]

    #no of heads obtained in that particular series of 20 flips
    x=heads
    n=no_of_data
    
    p_head=pow(p,x)
    p_tail=pow((1-p),(n-x))
    
    q_head=pow(q,x)
    q_tail=pow((1-q),(n-x))

    # p*head*p_tail == p^x*(1-p)^(20-x)
    numerator_a=p_head*p_tail
    numerator_b=q_head*q_tail
    denominator=numerator_a+numerator_b

    prob_A=numerator_a/denominator
    prob_B=numerator_b/denominator

    return prob_A,prob_B

# This function is used during the e step 
# It calculates the number of heads and tails of each coin
def expectation(theta,data):
   
    #0th index is heads and 1st index is tails (despite the fact that 0 is tails and 1 is heads)
    A_flips=[0,0]
    B_flips=[0,0]
    
    for flips in data:
        heads=0
        for x in flips:
            if x==1:
                heads+=1
        
        #get probabilities of getting A or B
        prob_A,prob_B=get_prob(heads,len(data[0]),theta)
        
        #get the total number of flips associated with A and B
        A_flips[0]+=prob_A*heads
        A_flips[1]+=prob_A*(len(flips)-heads)

        B_flips[0]+=prob_B*heads
        B_flips[1]+=prob_B*(len(flips)-heads)
        
    return A_flips,B_flips        
    
#maximization function is used to update the theta values
def maximization(A_flips,B_flips):
    
    theta=[0,0]
    theta[0]=(A_flips[0]/(A_flips[0]+A_flips[1]))
    theta[1]=(B_flips[0]/(B_flips[0]+B_flips[1]))
    return theta


# start point of the em algorithm. 
# set the initial theta values, max number of iterations 
def em_algo(data):
    theta=[random.random(),random.random()]
    #theta=[0.3,0.9]
    print("initial theta=",theta)
    iters=15
    for i in range(iters):
        A_flips,B_flips=expectation(theta,data)
        theta=maximization(A_flips,B_flips)
        #if converged(theta_temp,theta):
        #    return theta
        #theta=theta_temp
        print(i,"=",theta)
        #print(theta[0]+theta[1])
    return theta

        
def calculate_em():
    no_of_draws=30
    api_url="https://24zl01u3ff.execute-api.us-west-1.amazonaws.com/beta"
    data=make_data(no_of_draws,api_url)
    #data=[[1,1,1,1,1,0,0,0,0,0],[1,1,1,1,1,1,1,1,1,0],[0,0,1,1,1,1,1,1,1,1],[1,1,1,1,0,0,0,0,0,0],[0,0,0,1,1,1,1,1,1]]
    #print(data)
    return em_algo(data)


if __name__=="__main__":
    theta=calculate_em()
    print("final",theta)

