# def get_speed(length:int,time:int):
#     speed = length / time
#     return speed

# def test_get_speed():
#     assert get_speed(10,5) == 2.0
#     assert get_speed(15,5) == 3.0
#     assert get_speed(5,5) == 1.0
#     assert get_speed(5,1) == 5.0
#     assert get_speed(5,2) == 2.5


# if __name__ == "__main__":
    
#     try:
#         test_get_speed()
#         print("Succes {}".format(test_get_speed))
#     except Exception as e:
#         print('Failed: {} => {}: {}'.format(test_get_speed, type(e), e))









# import unittest
# import pytest


# def count_index(hight : float, weight : float) -> float:
#     return (weight / ((hight / 100)**2))

# def test_count_index():
#     assert count_index(170,70) == 24.221453287197235
#     assert count_index(170,10) != 24.22
#     assert count_index(180,80) == 24.691358024691358


# class UserTestCase(unittest.TestCase):
#     def test_1(self):
#         self.assertEqual(count_index(170,70),24.221453287197235)

#     def test_2(self):
#         self.assertNotEqual(count_index(160,60),60)

#     def test_3(self):
#         self.assertEqual(count_index(180,80),24.691358024691358)


#     def test_divizeon_zero(self):
#         with self.assertRaises(ZeroDivisionError):
#             count_index(0,89)

#     @unittest.skip
#     def test_skip(self):
#         self.assertEqual(1,4)

#     @unittest.expectedFailure
#     def test_failed(self):
#         self.assertEqual(count_index(60,555),22)

# def test_1():
#     assert count_index(170,70) == 24.2214532877235, "Not enquel"

# @pytest.mark.parametrize("a, b, rezult",[
#     (170,70,24.221453287197235),
#     (180,80,24.6913580246913583)

# ])
# def testparametrize(a, b, rezult):
#     assert count_index(a,b) == rezult

# def test_1():
#     assert count_index(170,70) != 24.2214532877235, "Not enquel"

# # if __name__ == "__main__":
#     # try:
#     #     test_count_index()
#     #     print("Succes - {}".format(test_count_index))
    
#     # except Exception as e:
#     #     print(f" failed : {test_count_index} -> {type(e)}:{e}")
#     # unittest.main()

    

import unittest
class Student:
    def __init__(self, name:str, lastname:str, age:int, average_mark:float):
        self.name = name
        self.lastname = lastname
        self.age = age
        self.average_mark = average_mark

stud1 = Student("Vasyl","Hetim",5,6.5)
stud2 = Student("Vlas","Hetim",6,"6.5")
# stud3 = Student("LGsg","Hetim",5,"6.5")
# stud4 = Student("SGGG","Hetim","","6.5")
# stud5 = Student("Vasyl","Hetim",6","6.5")
# stud6 = Student("Vasyl","Hetim",6","6.5")
# stud7 = Student("Vasyl","Hetim",","6.5")
# stud8 = Student("Vasyl","Hetim",6","6.5")
# stud9 = Student("Vasyl","Hetim",6","6.5")
# stud10 = Student("Vasyl","Hetim"16","6.5")

class Test_Student(unittest.TestCase):

    def test_age(self):
        self.assertLess(1,stud1.age)

    @unittest.expectedFailure
    def test_mark_is_float(self):
        self.assertIsInstance(stud2.average_mark,float)

unittest.main() 