from random import randint
from math import factorial
import threading


class ThreadOperation:

    def __init__(self,filepath):
        self.filepath = filepath
        self.usual_num = ['2', '3', '5', '7', '11', '13', '17', '19', '23', '29', '31', '37', '41', '43', '47', '53', '59', '61', '67', '71', '73', '79', '83', '89', '97', '101', '103', '107']
        self.factor_list = []
        self.number_usual = []
        self.random_number = []
    def filewrite(self):
        for i in range(10):
            self.random_number.append(str(randint(1,100)))
        with open(self.filepath,'w',encoding = 'utf-8') as file:
            for num in self.random_number:
                file.write(f'{num} ')
    def get_usual_num(self):
        return self.usual_num

    def open_file(self):
        with open(self.filepath, 'r', encoding = 'utf-8') as file:
            numbers = file.readline().split()
        return numbers

    def usual_num_find(self):

        for i in self.open_file():
            if i in self.usual_num:
                self.number_usual.append(i)
        with open('usual_number.txt','w',encoding = 'utf-8') as file:
            for i in self.number_usual:
                file.write(f'{i}, ')

    def factor(self):
        for i in self.open_file():
            self.factor_list.append(factorial(int(i)))
        with open('factorial_number.txt','w',encoding = 'utf-8') as file:
            for i in self.factor_list:
                file.write(f'{i}, ')



user_path = r'C:\Users\123mo\Desktop\HW_module_13_1_TaushevDN\task_2\file.txt'
thread_operation = ThreadOperation(user_path)

thread1 = threading.Thread(target = thread_operation.filewrite())
thread2 = threading.Thread(target = thread_operation.usual_num_find())
thread3 = threading.Thread(target = thread_operation.factor())

thread1.start()
thread1.join()

thread2.start()
thread3.start()

print(f'Список чисел - {thread_operation.random_number}')
print(f'Список простых чисел - {thread_operation.number_usual}')
print(f'Факториалы чисел - {thread_operation.factor_list}')

thread2.join()
thread3.join()