from tensorflow.keras import backend as K
from tensorflow.keras.layers import Layer


class Periodic1DPadding(Layer):
    """Add a periodic padding to the output of a layer
    # Arguments
        padding_size: tuple giving the padding size (left, right)
    # Output Shape
        input_shape+left+right
    """


    def __init__ (self, padding_size, **kwargs):
        super(Periodic1DPadding, self).__init__(**kwargs)
        if isinstance(padding_size, int):
            padding_size = (padding_size, padding_size)
        self.padding_size = tuple(padding_size)

    def compute_output_shape( self, input_shape ):
        space = input_shape[1:-1]
        if len(space) != 1:
            raise ValueError ('Input shape should be 1D with channel at last')
        new_dim = space[0] + np.sum(self.padding_size)
        return (input_shape[0],new_dim,input_shape[-1])



    def build( self , input_shape):
        super(Periodic1DPadding,self).build(input_shape)

    def call( self, inputs ):
        vleft, vright = self.padding_size
        leftborder = inputs[:, -vleft:, :]
        rigthborder = inputs[:, :vright, :]
        return K.concatenate([leftborder, inputs, rigthborder], axis=-2)