class Progression:
    """
        Başlangıç değeri verilen sayıların artimetik olarak ilerlemesini görmek,
        üzerinde döngüler kurmak ve base ilerleme class'ı oluşturmak.

    """
    def __init__(self,start=0):
        self._current = start


    def _advance(self):
        self._current += 1

    def __iter__(self):
        #kendi class'ımızdaki __next__() fonksiyonunu döndüreceğiz.
        return self

    def __next__(self):
        #her çağrıldıpında birer birer artarak ilerle
        if self._current is None:
            raise StopIteration
        else:
            answer = self._current
            self._advance()
            return answer

    def print_progression(self,n):
        progression = " ".join(str(next(self)) for i in range(n))
        print(progression)

class  ArithmeticProgression(Progression):
    def __init__(self,start=0,increment=1):
        super().__init__(start)
        self._increment = increment #artış sayımızı kendimiz belirleyebiliyoruz


    def _advance(self):
        #zaten varolan _advance() metodunun üzerine yazarak değiştiriyoruz.
        self._current += self._increment


class GeometricProgression(Progression):
    def __init__(self,start=1,factor=2):
        super().__init__(start)
        self._factor = factor

    def _advance(self):
        self._current *= factor

class FibonacciProgression(Progression):
    def __init__(self,start=0,prev=1):
        super().__init__(start)
        self._prev = prev

    def _advance(self):
        #fibonacci serisinde ilerleme
        self._current += self._prev
        self._current,self._prev = self._prev,self._current


if __name__ == "__main__":
    fb = FibonacciProgression(4,6)
    fb.print_progression(10)