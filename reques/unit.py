#! /usr/bin/env python
# coding = utf-8
import unittest
#help(unittest)
import  requests
def c(a,b):
    return a+b
c(3,5)
d = 'hello world'
class TestAdd(unittest.TestCase):
  '''
    def setUp(self):
        print('before login')#每个用例运行前都运行这块内容
    def tearDown(self):
        print('after') #每个运行后
    '''
@classmethod
def setUpClass(cls):#只运行一次
    cls.s = requests.session()

    def testAdd(self):
        b = c(1,2)
        self.assertEqual((1+1),2)
        self.assertEqual(b,3)
        self.assertIn('he',d)
        self.s.get()
    #unittest.skip('i just do not this')
    def Test_1(self):
        self.assertEqual(1+3,5)
if __name__=="__main__":
    unittest.main()
