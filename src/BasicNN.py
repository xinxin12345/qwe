import numpy as np
class BasicNN(object):
    """ Basic Neural Network

    """
    def __init__(self,node_size,input_size=0,init_parameter='random'):
        self.node_size = node_size
        self.input_size = input_size
        self.W = np.random.rand(input_size, node_size)
        self.b = np.random.rand(1,node_size)
    def set_param(self,input_size):
        self.W = np.random.rand(input_size, self.node_size)
        self.input_size = input_size
    def forward(self, input_data):

        self.pre_data = input_data
        self.data_forward = np.add(np.dot(input_data,self.W), self.b)
        return self.data_forward

    def default_func(self, A):
        return 1
    def backword(self, dZ, pre_W,func=default_func):
        """ dZ.shape=sample,node_size
        pre_W.shape = node_size,back_layer_size

        :param dZ:
        :param pre_W:
        :return:
        """
        m = dZ.shape[0]
        input_size, node_size = self.W.shape
        _, back_size = pre_W.shape
        grad_b = np.zeros((m,dZ.shape[1]))
        grad_W = np.zeros((m,input_size, node_size))
        for i in range(m):
            for j in range(node_size):
                for k in range(back_size):
                    tmp = dZ[i,j] * pre_W[j,k] * func(self, self.data_forward[i,j])
                    grad_b[i,j] += tmp
                    grad_W[i,:,j] += tmp * self.pre_data[i]

        assert grad_W.shape[1:] == (self.input_size,self.node_size)
        assert grad_b.shape[1] == 3
        return grad_W, grad_b

if __name__ == '__main__':
    nn = BasicNN(3,4)
    np.random.seed(10)
    input_data = np.random.rand(2,4)
    print('input:',input_data)
    print('param:',nn.W,nn.b)
    print('forward=',nn.forward(input_data))

    dZ = np.random.rand(2,3)
    pre_W = np.random.rand(3,1)
    print('dZ:',dZ)
    print('pre_W:',pre_W)
    back =nn.backword(dZ,pre_W)

    print('backward_W:',back[0])
    print('backward_b:',back[1])