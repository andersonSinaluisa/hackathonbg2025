


class IncomeService:
    
    min = 100
    max = 2000
    
    
    def calculate(self,value):
        
        return (value - self.min) / (self.max - self.min)