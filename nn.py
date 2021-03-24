import numpy, random, os
lr = 1
bias = 1
weights = [random.random(),random.random()]

def perceptron(inputuser, output):
    outputP = inputuser*weights[0]+bias*weights[1]
    outputP = 1/(1+numpy.exp(-outputP))
    if outputP >0:
        outputP = 1
    else:
        outputP = 0
    error = output - outputP
    weights[0] += error*inputuser*lr
    weights[1] += error*bias*lr

for i in range(50):
    perceptron(1,1)
    perceptron(1,0)
    perceptron(0,1)
    perceptron(0,0)

tweetin = str(input())
outputP = x*weights[0]+bias*weights[1]
if outputP > 0:
    outputP = 1
else:
    outputP = 0
print(x,"is:", outputP)
