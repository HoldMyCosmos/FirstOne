class compint:
    def __init__(self,p,r,n,t):
        self.p=p
        self.n=n
        self.t=t
        self.r=r
    def calculate(self):
        self.amt=self.p*((1+(self.r/self.n))**(self.n*self.t))
        print(self.amt)
interest=compint(2,3,2,1)
interest.calculate()