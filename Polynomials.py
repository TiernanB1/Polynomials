import math 

class Poly: 

    def __init__(self, coeffs1):
        self.coeffs = coeffs1
        

    def __str__(self):
       
       output = [str(self.coeffs[0])] # add first item on its own 
       
       for i in range(1, len(self.coeffs)): #loop to end of the list 
         if self.coeffs[i] < 0: # decide if negative or positive sign
            output.append(f"- {self.coeffs[i]}x^{i}")
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

       
    
 

if __name__ == "__main__":
    
    pa = Poly([1, 2, 4, 7])

    pb = Poly([1, -2, 1, 1])

    pc = pa + pb

    print(pc)




#"coeffs1 = Poly(input("enter values of coefficients").split()) # get coefficients from input "
    
# print(coeffs1)"
# coeffs1 = Poly(input("enter values of coefficients").split()) # get coefficients from input 
    
# print("why")


