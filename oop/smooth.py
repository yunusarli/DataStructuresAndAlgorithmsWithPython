""" 
    Double exponential smoothing algorithm in python
    owner: Yunus Arli
    mail: arli19@itu.edu.tr
    student_number:070190051 
    I wrote the codes according to the object-oriented programming approach 
    to be maintainable and readable,I hope this does not cause a problem.
"""

import numpy

class DoubleSmoothing(object):
    def __init__(self,x,l_zero,b_zero=0,alpha=0.3,beta=0.5,mape=False) -> None:
        #data (as a numpy array)
        self.x = x
        #starting point for forecast
        self.l_zero = l_zero
        #initial value of trend
        self.b_zero = b_zero
        #smoothing value for forecast
        self.alpha = alpha
        #smoothing value for trend
        self.beta = beta
        #a boolean for mape function
        self.mape = mape
    
    def __len__(self):
        #length of the array
        return self.x.shape[0]
    
    def is_valid(self) -> bool:
        """ Check alpha and beta values is valid or not. """
        return 0<self.alpha<1 and 0<self.beta<1
    
    
    def calculate_mape(self,real_values,forecast):
        real_values = real_values[1:]
        forecast = forecast[1:]#first element is None
        return round(100*numpy.nanmean(numpy.abs(real_values - forecast)/numpy.abs(real_values)),2)


    def double_exponantial_smoothing(self):
        """ 
        Calculating the double exponantial smoothing.
        formula is:
        Lt = alpha*Yt + (1-alpha)*(Lt-1(as indis) + Bt-1(as indis))
        Bt = beta*(Lt-Lt-1(as indis)) + (1-beta)*Bt-1(as indis)

        forecast:
            Yt+1(as indis) = Lt + Bt

        """
        if not self.is_valid():
            raise ValueError("The value of alpha and beta should be between 0 and 1")

        length = len(self)
        
        #at first output array has no value. Just know the lenght of the array
        forecasts = numpy.array([numpy.nan]*length)

        trend = self.b_zero
        level = self.l_zero#0

        for index in range(0,length-1):
            value = self.x[index]
            #we need to keep previous level to calculate the formula.
            prev_level = level#
            level = self.alpha*value + (1-self.alpha)*(level+trend)#

            Yt = level
            forecasts[index+1] = Yt
            trend = self.beta * (level - prev_level) + (1 - self.beta) * trend

        if not self.mape:
            return forecasts
        
        #if mape set to True, it has to be calculated
        return forecasts,self.calculate_mape(self.x,forecasts)


def getName():
    return "Yunus Arli"

def getStudentID():
    return "070190051"

def double_exponential_smoothing(x, l_zero, b_zero = 0, alpha=0.3, beta=0.5 , mape=False):
   
    instance = DoubleSmoothing(x,l_zero,b_zero,alpha,beta,mape)

    return instance.double_exponantial_smoothing()