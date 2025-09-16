#!/usr/bin/env python3
import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):

    def setUp(self):
        print('Running Setup...\n')
        self.first = "Churchil"
        self.last = "Okech"
        self.pay = 1200

    def tearDown(self):
        print('tearDown\n')

    def test_email(self):
        email_1 = Employee(self.first, self.last, self.pay)
        test_mail_1 = "Churchil.Okech@email.com"
        self.assertEqual(email_1.email, test_mail_1)
        email_1.first = "Peter"
        email_1.last = "Kagia"
        self.assertEqual(email_1.email, "Peter.Kagia@email.com")

    def test_fullname(self):
        first = "okech"
        last = "opiyo"
        pay = 90
        name = Employee(first, last, 90).fullname
        self.assertEqual(name, "okech opiyo")


    def test_pay(self):
        pay = Employee("dr", "fog", 30).raise_pay()
        self.assertEqual(pay, 31)
        



if __name__ == '__main__':
    unittest.main()

