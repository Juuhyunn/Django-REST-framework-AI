from dataclasses import dataclass


@dataclass
class Calculator(object):
    num1 : int
    num2 : int

    @property
    def num1(self): return self._num1

    @num1.setter
    def num1(self, num1): self._num1 = num1


    @property
    def num2(self): return self._num2


    @num2.setter
    def num2(self, num2): self._num2 = num2


    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num1 - self.num2

    def multiple(self):
        return self.num1 * self.num2

    def divide(self):
        return self.num1 / self.num2


@dataclass
class Contacts(object):
    # name: str
    # phone: str
    # email: str
    # address: str
    #
    # @property
    # def name(self): return self._name
    # @name.setter
    # def name(self, name): self._name = name
    # @property
    # def phone(self): return self._phone
    # @phone.setter
    # def phone(self, phone): self._phone = phone
    # @property
    # def email(self): return self._email
    # @email.setter
    # def email(self, email): self._email = email
    # @property
    # def address(self): return self._address
    # @address.setter
    # def address(self, address): self._address = address

    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def to_string(self):
        print(f'{self.name}, {self.phone}, {self.email}, {self.address}')


    def set_contact(self) -> object:
        return Contacts(input('name'), input('phone'), input('email'), input('address'))

    def get_contacts(self, ls):
        for i in ls:
            i.to_string()

    def del_contact(self, ls, name):
        for i, j in enumerate(ls):
            if name == j.name:
                del ls[i]


@dataclass
class Grade(object):
    def __init__(self, kor, eng, math):
        self.kor = kor
        self.eng = eng
        self.math = math

    def sum(self):
        return self.kor + self.eng + self.math

    def avg(self):
        return self.sum() / 3


@dataclass
class GradeWithName(object):
    def __init__(self, name):
        self.name = name
        self.scores = []

    def addScores(self, score):
        self.scores.append(score)

    def avg(self):
        return sum(self.scores) / len(self.scores)



@dataclass
class Person(object):
    def __init__(self,name,age,address):
        self.name = name
        self.age = age
        self.address = address
    def to_string(self):
        print(f'이름{self.name},나이{self.age},사는곳{self.address}')
