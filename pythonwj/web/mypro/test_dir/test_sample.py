
import pyse

class YouTest(pyse.TestCase):

    def test_case(self):
        ''' a simple test case '''
        self.open("https://www.baidu.com/")
        self.type("#kw", "pyse")
        self.click("#su")
        self.assertTitle("pyse")


if __name__ == '__main__':
    pyse.main("test_sample.py", debug=True)
