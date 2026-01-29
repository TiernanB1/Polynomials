

class Poly: 

    def __init__(self, coeffs1):
        self.coeffs = coeffs1
        

    def __str__(self):

      output = ""

      if self.coeffs[0] != 0: 
         output = str(self.coeffs[0]) # add first item on its own 


      if self.coeffs[1] != 0: 
         if self.coeffs[1] < 0: 
            output +=(f" - {-self.coeffs[1]}x")
         elif self.coeffs[1] > 0:
            output +=(f" + {self.coeffs[1]}x")  # add first item on its own 

      if self.coeffs[0] == 0: #decide if + is needed or not
         output=output.replace(" + ","") #replace + if not needed

      for i in range(2, len(self.coeffs)): #loop to end of the list 
         if self.coeffs[i] < 0: # decide if negative or positive sign
            output +=(f" - {-self.coeffs[i]}x^{i}")
         elif self.coeffs[i] > 0:
            output +=(f" + {self.coeffs[i]}x^{i}")     
         else: 
            pass #skip 0 terms
      
      return (output) # join into string
    
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
       for i in range(len(self.coeffs)): #loops to end of list
          self.coeffs[i] = self.coeffs[i] * i #multiplies by index
       del self.coeffs[0] #removed 0 coefficient at the start
       return Poly(self.coeffs)
    
    def antidif(self):
       new_coeff = [2] + self.coeffs #constant of integration = 2 
       for i in range(1, len(new_coeff)):   # for range of rest of coefficients
          new_coeff[i] = (self.coeffs[i - 1]/ i ) # move down place and divide by old coefficient 
       return Poly(new_coeff)
       


if __name__ == "__main__":
    
    
    #pa = Poly(list(map(int, input("enter coefficients of polynomial a: ").split())))
    #pb = Poly(list(map(int, input("enter coefficients of polynomial b: ").split())))
    pa = Poly([2, 0, 4, -1, 0, 6])
    pb = Poly([-1, -3, 0, 4.5])
    pc = (pa + pb) 
    print(pc)
    pd = pa.dif()
    print(pd)
    pe = pd.antidif()
    print(pe)
   
   
    


