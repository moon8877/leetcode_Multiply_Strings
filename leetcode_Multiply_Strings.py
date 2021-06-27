class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        def ToInt(string):
            length = len(string)
            digit = length - 1
            count = 0
            for i in range(length):
                count = count + (ord(string[i])-48)*pow(10,digit)
                digit = digit - 1
            return count
        a = ToInt(num1)
        b = ToInt(num2)
        return str(a*b)