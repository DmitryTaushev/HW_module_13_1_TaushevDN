import random
import threading


class NumberOperation:

    def __init__(self):
        self.random_number = []
        self.arithmetic_mean = 0
        self.sum_num = 0
    def rnd(self):
        self.random_number=[random.randint(1,100) for i in range(10)]


    def num_sum(self):
        self.sum_num = sum(self.random_number)

    def average(self):
        self.arithmetic_mean = self.sum_num/len(self.random_number)

numb_oper = NumberOperation()

thread1 = threading.Thread(target = numb_oper.rnd())
thread2 = threading.Thread(target = numb_oper.num_sum())
thread3 = threading.Thread(target = numb_oper.average())

thread1.start()
thread2.start()
thread3.start()
thread1.join()



print(f'Список чисел - {numb_oper.random_number}')
print(f'Сумма чисел - {numb_oper.sum_num}')
print(f'Среднее арифметическое - {numb_oper.arithmetic_mean}')

thread2.join()
thread3.join()