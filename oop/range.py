class Range:
    def __init__(self,start=0,stop=None,step=1):
        self._start = start
        self._stop = stop
        self._step = step

        if self._stop is None:
            #range(12) gibi tekli durumları düzeltmek ör=> (0,12,1) yapmak
            self._start, self._stop = 0,self._start

        #döngü en az iki kez dönmeli
        assert self._stop > 1, "The range must be greater than 1"

        #adım sayısı son sayıdan büyük olmak zorunda
        assert self._step < self._stop, "The step cannot be greater than the stop"

        #sadece pozitif range destekleniyor
        assert self._stop > self._start, "Unfortunately, we just can afford positive ranging"
        
        assert self._step != 0, "step cannot be zero"

    def __getitem__(self,index):
        assert index < len(self), "Index is out of the range"
        #sayılarımızı herhangi bir yerde depolamadık. Dolayısıyla erişim için bi förmüle ihtiyacımız var.
        #başlangıç noktasına adım*indeks ekleyerek istenen sayıyı kolayca bulabiliyoruz.
        formula = self._start + self._step*index
        return formula

    def __len__(self):
        #veri yapımızın len metodu olmadığı için class içinde bir döngü ile dönerek kendi metodumuzu oluşturuyoruz.
        length = 0
        for i in self:
            length += 1
        return length

    def __iter__(self):
        #NumIterator classındaki formülü kullanarak bir döngü oluşturduk.
        return NumIterator(self._start,self._stop,self._step)

class NumIterator:
    def __init__(self,start,stop,step):
        self._start = start
        self._stop = stop
        self._step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self._stop > self._start:
            val = self._start
            self._start += self._step
            return val
        else:
            raise StopIteration





r = Range(5,8,1)
print(r[2])