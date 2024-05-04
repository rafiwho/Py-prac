class test:
    def __init__(self,test_list):
        self.test_list = test_list

class sub_test(test):
    def __init__(self, test_list):
        super().__init__(test_list)
    def print_(self):
        for i in self.test_list:
            print(i)

lst = [1,2,3,4]


test_1 = sub_test(lst)
test_1.print_()