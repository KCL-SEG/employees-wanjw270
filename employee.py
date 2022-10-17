"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, monthlyContract, hourlyContract, hour, bonusCommission, contractCommission, contractNumber):
        self.name = name
        self.monthlyContract = monthlyContract
        self.hourlyContract= hourlyContract
        self.hour = hour
        self.bonusCommission = bonusCommission
        self.contractCommission = contractCommission
        self.contractNumber = contractNumber


    def get_pay(self):
        pay = 0
        if self.monthlyContract != 0:
            pay += self.monthlyContract
        else:
            pay += self.hourlyContract * self.hour
        if self.bonusCommission != 0:
            pay += self.bonusCommission
        else:
            pay += self.contractCommission * self.contractNumber
        return pay               
        

    def __str__(self):
        str = f"{self.name} works on a "
        if self.monthlyContract != 0:
            str += f"monthly salary of {self.monthlyContract}"
        else:
            str += f"contract of {self.hour} hours at {self.hourlyContract}/hour"    
        if self.bonusCommission != 0:
            str += f" and receives a bonus commission of {self.bonusCommission}"
        elif self.contractCommission != 0:
            str += f" and receives a commission for {self.contractNumber} contract(s) at {self.contractCommission}/contract"    

        str += f". Their total pay is {self.get_pay()}."

        return str

# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', 4000, 0, 0, 0, 0, 0)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', 0, 25, 100, 0, 0, 0)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', 3000, 0, 0, 0, 200, 4)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', 0, 25, 150, 0, 220, 3)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', 2000, 0, 0, 1500, 0, 0)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', 0, 30, 120, 600, 0, 0)
