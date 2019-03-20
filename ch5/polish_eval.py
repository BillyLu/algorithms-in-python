#coding=utf-8
'''
code 5.4
Polish notation evaluation
前最表达式求值
'''

class Polish(object):
    def __init__(self, s):
        self.s = s
        self.i = 0

    def eval(self):
        while self.s[self.i] == ' ':
            self.i += 1

        if self.s[self.i] == '+':
            self.i += 1
            return self.eval() + self.eval()
        elif self.s[self.i] == '*':
            self.i += 1
            return self.eval() * self.eval()

        num = 0
        while self.i < len(s) and self.s[self.i] >= '0' and self.s[self.i] <= '9':
            num = num * 10 + ord(self.s[self.i]) - ord('0')
            self.i += 1
        return num


if __name__ == '__main__':
    test_cases = [
        ['+ 3 4', 7],
        ['+ * 3 4 10', 22],
        ['* + 7 * * 4 6 + 8 9 5', 2075],
    ]
    for s, v in test_cases:
        r = Polish(s).eval()
        print 'result >> %s, want %d, have %d' % (v == r, v, r)

