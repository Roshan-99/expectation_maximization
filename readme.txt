Running the code:
1) Open CMD, change to directory with python file in it.
2) Type python ra_code.py


Code explanation for Research assistant Position:
My algorithm has various functions divided so that they can modulated efficiently for customization of some parameters (such as theta value, number of iterations, data, etc)
The work flow is as follows:
1) Get the data from api through make_data function, parse it and built a list of draws (list of list of tosses).
2) Calculate the theta value by calling em_algo() and sending data from previous step as input.
3) In my implementation, I have set number of iteration as 15 and theta values are taken at random. Despite this, I have observed that as long as the theta values are not exactly same, they are convering and giving a relatively constant value for theta (sometimes interchanged).
4) In each of the iterations, expectation step and maximization step is performed.
5) In expectation step, using the data, the probability of heads for each coin is obtained by taking current theta values (obtained in previous iteration).
The probability is estimated using bernoulli formula = nCx * p^x * (1-p)^(n-x) and bayes theorem to reduce the computation (and cancelling out the constant term nCx).
6) This probability is used to obtain the number of flips for each coin.
7) Maximization is used to update the theta until convergence or max iteration. In my code, I have put condition until max iteration but observing from some test runs, the data converges pretty quickly at 6-10 iterations and reaching 14 in some worst cases.
8) Finally, output the data back to the em_algo() and display to the console.

3.1)
Obtained theta values: 
Coin 1: 68% or 0.68 (+-2%)
Coin 2: 28% or 0.28 (+-2%)

The values of the theta depends on which of the initial theta is higher. The one with higher initial theta value gets 68% and the other one gets 28%.
There is slight variation during multiple runs (due to different data from api). But the obtained mean is around the above mentioned value with a variation is +- 2%. 
This is same for all unequal values of intital theta. That is, despite difference of any amount (say 0.00001 or 0.99), it still gives the same above values. 
This is not the case when the initial theta values are exactly the same. 

3.2) 
Choices during coding:
There were many choices, which included deciding to implement using models in scikit learn or coding from scratch.
For this, I decided to do the coding from scratch since it is relatively lightweight and sufficient for this assignment (can run in any system without installing any heavy scikit learn packages).
If I had to write for a more complicated problem involving larger data and requiring graph plotting then I would have decided to pursue the path of scikit learn. Nevertheless, I have implemented another version using scikit learn locally for testing & understanding purposes.

I also had to make a choice on the number of iterations to fix or to create a function to check convergence. On testing the code with varying iteration sizes, I have noticed that it usually converges early on (6-10 iterations) and given the small data size decided to use the path of fixing iteration size to 15. 

I also had to decide on the initial theta values and on experimenting with various values, noticed that any non equal values of inital theta for this problem gave similar results. Only difference is flipping of theta values (depending on which initial theta value is larger).

Other choices included following proper naming conventions and following good programming standards so that code is modularized(can change parts of the code without affecting other parts), scalable(different data, different data size and sources) and easily customizable with various inputs.




