class Employee:
    percent_raise = 1.05

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay


    @property
    def email(self):
        email = "{}.{}@email.com".format(self.first, self.last)
        return email


    @property
    def fullname(self):
        name = "{} {}".format(self.first, self.last)
        return name

    
    def raise_pay(self):
        raised_pay = int(self.percent_raise * self.pay)
        return raised_pay

