class Vector:
    def __init__(self,dimension):
        self._dimension = dimension
        self._vector = [0 for i in range(dimension)]


    def __len__(self):
        return self._dimension

    def __repr__(self):
        return str(tuple(self._vector))

    def __getitem__(self,index):
        return self._vector[index]

    def __setitem__(self,index,value):
        assert index<=4 and index >= -4 , "{0} is out of the range".format(index)
        if index < 0:
            index = index*-1
        self._vector[index] = value
        return self._vector

    def __add__(self,instance):
        assert len(instance) == len(self), "{} dimension is not fit to add".format(instance)

        for index in range(len(self)):
            value = instance[index]
            self[index] += value
        return self

    def __ne__(self,instance):
        return not self == instance

    def __eq__(self,instance):
        return self._vector == instance._vector

    def __iter__(self):
        return SequenceIterator(self._vector)



class SequenceIterator:
    def __init__(self,array):
        self._array = array
        self._counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._counter < len(self._array):
            entry = self._array[self._counter]
            self._counter += 1
            return entry

        else:
            raise StopIteration()




if __name__ == "__main__":
    cc = Vector(3)
    cc[0] = 12
    ins = Vector(3)
    ins[0] = 10
    for i in cc:
        print(i)

