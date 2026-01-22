import math 

class Poly: 

    def __init__(self, coeffs1, c = 2):
        self.coeffs = coeffs1
        self.c = c
        

    def __str__(self):
       
       output = [str(self.coeffs[0])] # add first item on its own 
       
       for i in range(1, len(self.coeffs)): #loop to end of the list 
         if self.coeffs[i] < 0: # decide if negative or positive sign
            output.append(f"- {-self.coeffs[i]}x^{i}")
         elif self.coeffs[i] > 0:
            output.append(f"+ {self.coeffs[i]}x^{i}")
         else: 
            pass #skip 0 terms
         
       return " ".join(output) # join into string
    
    def __add__(self, poly_b):
       return self.add(poly_b)


    def add(self, poly_b):
       new_poly = [] # new list 
       max_len = max(len(self.coeffs), len(poly_b.coeffs)) # determine max length
       for i in range(max_len):
          a = self.coeffs[i] if i < len(self.coeffs) else 0 # make sure term isnt null
          b = poly_b.coeffs[i] if i < len(poly_b.coeffs) else 0 

          new_poly.append(a + b) # append
       return Poly(new_poly)
    
    def dif(self):
       for i in range(1, len(self.coeffs)):
          self.coeffs[i] = self.coeffs[i] * i
       self.c = self.coeffs[0]
       del(self.coeffs[0])
       return Poly(self.coeffs)
    
    def antidif(self):
       new_coeff = [self.c] + self.coeffs
       for i in range(1, len(new_coeff)):
          new_coeff[i] = (self.coeffs[i - 1]/ i )
       return Poly(new_coeff)
       


if __name__ == "__main__":
    
    
    pa = Poly(list(map(int, input("enter coefficients of polynomial a: ").split())))
    pb = Poly(list(map(int, input("enter coefficients of polynomial b: ").split())))
   # pa = Poly([1, 2, 3, 4])
    #pb = Poly([4, -2, 2])
    pc = (pa + pb) 
    print(pc)
    pd = pc.dif()
    pd = pc.antidif()
    print(pd)
   
    


