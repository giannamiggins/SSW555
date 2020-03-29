# This is our test file
import unittest
from Sprint02 import *
from Sprint01 import *
from Sprint03 import *
from Dan_Bianchini_User_Stories import *
from Jacob_Senkewicz_User_Stories import *

#format sample
    #def test_US##(self):
        #for indi in (families or individuals):
            #self.assertEquals(call your function, the return when it passes, indi)
#example output:
    #======================================================================
    #FAIL: test_US15_test (__main__.Sprint02Test)
    #----------------------------------------------------------------------
    #Traceback (most recent call last):
    #File "c:/Users/gmigg/Documents/SSW555/SSW555/AllTests.py", line 8, in test_US15_test
        #self.assertEquals(US15_child_max(indi, families), None, indi)
    #AssertionError: 'ERROR: too many kids' != None : @F15@

#IF YOU DONT GET THAT, IT DOESNT WORK

class Test(unittest.TestCase):
    def test_US15(self):
        for indi in families:
            self.assertEqual(US15_child_max(indi, families), None, indi)
    def test_US14(self):
        for indi in families:
            self.assertEqual(US14_quintuplets(indi, families), None, indi)
    def test_US34(self):
        for indi in individuals:
            self.assertEqual(US34_age_difference(indi, individuals), None, indi)
    def test_US21(self):
        for indi in families:
            self.assertEqual(US21_correct_gender(indi, families, individuals), None, indi)
    def test_US07(self):
        for indi in individuals:
            self.assertEqual(US07_check150(indi, individuals), None, indi)
    def test_US06(self):
        for indi in individuals:
            self.assertEqual(US06_divorce_before_death(indi, individuals), None, indi)
    def test_US29(self):
        for indi in individuals:
            self.assertEqual(US29_the_deceased(indi, individuals), None, indi)
    def test_US16(self):
        for indi in individuals:
            self.assertEqual(US16_get_last_names(indi,individuals), None, indi)
    def US18_automated_test(self):
        for indi in individuals:
            self.assertEqual(US18_siblings_should_not_marry(indi,individual,families), indi)
    def test_US02(self):
        for indi in individuals:
            self.assertEqual(US02_born_after_married(indi, individuals), None, indi)
    def test_US03(self):
        for indi in individuals:
            self.assertEqual(US03_death_before_birth(indi, individuals), None, indi)
    def test_US08(self):
        for indi in individuals:
            self.assertEqual(US08_born_before_parents_married(indi, individuals, families), None, indi)
    def test_US12(self):
        for indi in individuals:
            self.assertEqual(US12_parents_too_old(indi, individuals, families), None, indi)

if __name__ == '__main__':
    #this calls the automatic tests
    unittest.main()
