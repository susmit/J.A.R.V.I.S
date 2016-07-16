def sigmoid(x):
    return 1/1+np.exp(-x)


def dersig(x):
    return x*(1-x)


def wgts(i,h,o):
    weights.append(np.random.random((i+1)*(h+1)).reshape(i+1,h+1))
    weights.append(np.random.random((h+1)*o).reshape(h+1,o))


def nn(X,y,learningrate):
    X=np.array(X)
    y=np.array(y)
    activationvalues.append(sigmoid(np.dot(X,weights[0])))
    activationvalues.append(sigmoid( np.dot( activationvalues[0],weights[1] ) ) )
    #print activationvalues
    error=y-activationvalues[-1]
    deltas.append(error*dersig(activationvalues[-1]))
    deltas.append(np.dot(deltas[-1],weights[1].T)*dersig(activationvalues[0]))
    deltas.reverse()
    layer = np.atleast_2d(activationvalues[0])
    delta = np.atleast_2d(deltas[0])
    weights[0]=weights[0]+learningrate*layer.T.dot(delta)
    layer = np.atleast_2d(activationvalues[1])
    delta = np.atleast_2d(deltas[1])
    weights[1]=weights[1]+learningrate*layer.T.dot(delta)
    print weights

    
    
                                                                                      
    
        



import numpy as np
weights=[]
activationvalues=[]
deltas=[]
wgts(2,2,1)
print weights
X=[1,0,0]
y=[1]
nn(X,y,0.2)
'''activationvalues.append(sigmoid(np.dot(X,weights[0])))
activationvalues.append(sigmoid( np.dot( activationvalues[0],weights[1] ) ) )
print activationvalues,X'''
