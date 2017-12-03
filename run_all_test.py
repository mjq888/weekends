import unittest

if __name__ == '__main__':
    #默认测试用例加载器
    suit = unittest.defaultTestLoader.discover('./day5',pattern='*Test.py')
    #执行所有测试用例
    unittest.TextTestRunner().run(suit)
