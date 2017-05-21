
# coding: utf-8

# In[1]:

from __future__ import division


class ComplexNumber(object):  
    
    def __init__(self, real, img):
        try:
            real = float(real)
            img = float(img)        
        except:
            print "Enter numbers. Please."
        self.real = real
        self.img = img
        
    def conjugate(self):
        return ComplexNumber(self.real, -self.img)
    
    def __repr__(self):       
        if self.img<0:
            return "%s - %si"%(self.real, -self.img)
        elif self.img==0:
            return "%s"%(self.real)
        else:
            return "%s + %si"%(self.real, self.img)

    def __add__(self, other):
        realpart = self.real + other.real
        imgpart = self.img + other.img
        return ComplexNumber(realpart, imgpart)
    
    def __sub__(self, other):
        realpart = self.real - other.real
        imgpart = self.img - other.img
        return ComplexNumber(realpart, imgpart)
    
    def __mul__(self, other):
        realpart = (self.real * other.real) - (self.img * other.img)
        imgpart = (self.img * other.real) + (other.img * self.real)
        return ComplexNumber(realpart, imgpart)


# In[2]:

a = ComplexNumber(1,-2)
b = ComplexNumber(3,4)
a*b
a.conjugate()


# In[ ]:




# In[ ]:




# In[ ]:



