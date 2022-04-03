import numpy

from smooth import double_exponential_smoothing

def getName():
    return "Yunus Arli"

def getStudentID():
    return "070190051"

def MAPE(y , y_pred):
    return round(100*numpy.nanmean(numpy.abs(y - y_pred)/numpy.abs(y)),2)


def double(x,l_zero,b_zero=0,alpha=0.3,beta=0.5,mape=False):

    if not 0<alpha<1 and 0<beta<1:
            raise ValueError("The value of alpha and beta should be between 0 and 1")

    length = len(x)
        
    forecasts = numpy.array([numpy.nan]*length)

    trend = b_zero
    level = l_zero

    for index in range(0,length-1):
        value = x[index]
        prev_level = level#
        level = alpha*value + (1-alpha)*(level+trend)#

        Yt = level
        forecasts[index+1] = Yt
        trend = beta * (level - prev_level) + (1 - beta) * trend

    if not mape:
        return forecasts
        
    return forecasts,MAPE(x,forecasts)

x = numpy.array([2.92, 0.84, 2.69, 2.42, 1.83, 1.22, 0.10, 1.32, 0.56, -0.35])
l_zero = 2
result = double_exponential_smoothing(x=x,l_zero=l_zero,mape=True)
print("Sonuc: ",result)
