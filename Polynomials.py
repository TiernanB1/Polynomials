import math 

class Poly: 

    def __init__(self, coeffs1):
        self.coeffs = coeffs1
        

 #   def __str__(self):
  #      for i in range(len(self.coeffs)):
   #         return f"({self.coeffs[i]}x^{i})"

    def output(self):
        for i in range(len(self.coeffs)):
           (f"({self.coeffs[i]}x^{i})")
                 

if __name__ == "__main__":
    
    pa = Poly([1, 2, 4, 7])

    Poly.output(pa)

#"coeffs1 = Poly(input("enter values of coefficients").split()) # get coefficients from input "
    
# print(coeffs1)"
# coeffs1 = Poly(input("enter values of coefficients").split()) # get coefficients from input 
    
# print("why")


