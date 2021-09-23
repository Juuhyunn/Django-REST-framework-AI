import unittest
from models_oop import Calculator, Contacts, Grade, GradeWithName, Person

class TestCalculator(unittest.TestCase):
    def test_add(self):
        instance = Calculator()
        instance.num1 = 10
        instance.num2 = 7
        res = instance.add()
        print(f'My Expected Value is {res}')
        self.assertEqual(res, 17)

    def test_subtract(self):
        instance = Calculator()
        instance.num1 = 10
        instance.num2 = 7
        res = instance.subtract()
        print(f'My Expected Value is {res}')
        self.assertEqual(res, 3)

    def test_multiple(self):
        instance = Calculator()
        instance.num1 = 10
        instance.num2 = 7
        res = instance.multiple()
        print(f'My Expected Value is {res}')
        self.assertEqual(res, 70)

    def test_divide(self):
        instance = Calculator()
        instance.num1 = 10
        instance.num2 = 2
        res = instance.divide()
        print(f'My Expected Value is {res}')
        self.assertEqual(res, 5)

class TestContacts(unittest.TestCase):
    def test_contacts(self):
        instance = Contacts('','','','')
        a = instance.set_contact('안주땡', '010', '지메일', '서울')
        b = instance.set_contact('주주주', '111', '네이버', '부산')
        # instance.name='안주땡'
        # instance.phone = '010'
        # instance.email = '지메일'
        # instance.address = ''
        ls = []
        ls.append(a)
        ls.append(b)
        a.get_contacts(ls[0])
        instance.del_contact(ls, '안주땡')
        print(f'My Expected Value is {ls}')






    def test_get_contacts(self, ls):
        for i in ls:
            i.to_string()

    def test_del_contact(self, ls, name):
        for i, j in enumerate(ls):
            if name == j.name:
                del ls[i]

if __name__ == '__main__':
    unittest.main()