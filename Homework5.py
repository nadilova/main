class Customer:
    def __init__(self, id, name, lname, age):
        self.identidication = id
        self.name = name
        self.last_name = lname
        self.person_age = age

    def buy(self):
        return "I buy goods and services."


class Hotel_customer(Customer):
    def __init__(self, id, name, lname, age, email):
        super().__init__(id, name, lname, age)
        self.__email = email

    def book(self):
        return 'I book hotels.'

    def get_email(self):
        return f"The cliant's email is {self.__email}"

    def set_email(self, n_email):
        self.__email = n_email


customer_1 = Customer(1, 'Nur', 'Adil', 45)
customer_2 = Customer(2, 'Ail', 'Leidel', 9)
print(customer_1.buy())
print(customer_1.__dict__)
print(customer_2.__dict__)

hcustomer1 = Hotel_customer(3, 'Or', 'Adil', 33, 'or.adil@gmail.com')
print(hcustomer1.buy())
print(hcustomer1.book())
print(hcustomer1.__dict__)
print(f'the email of the customer is {hcustomer1.get_email()}')
hcustomer1.set_email("adilova@mail.ru")
print(hcustomer1.__dict__)
