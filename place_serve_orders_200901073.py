# -*- coding: utf-8 -*-
"""Place_Serve_Orders.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1nbU_5UJjPvFRCbLGqKHqabbH_6DNSmFW
"""

#Furqan Ali
#200901073
#BS-CS-01-B
import time
import threading
from collections import deque

class Resturant():
    def __init__(self):
        self.ord=deque()
    def Place_order (self,value):
        for i in value:
            time.sleep(0.5)
            print("Placing order: ",i)
            self.ord.appendleft(i)

    def Serve_order(self):
        for i in range(0,5):
            time.sleep(2.0)
            print("Serving order: ", self.ord.pop())

if __name__=="__main__":
    orders = ['pizza','samosa','pasta','biryani','burger']

    t = time.time()
    F=Resturant()
    th1 = threading.Thread(target=F.Place_order, args=(orders,))
    th2 = threading.Thread(target=F.Serve_order)
    th1.start()
    time.sleep(1)
    th2.start()
    th1.join()
    th2.join()
    print("Total time taking by threads is :", time.time() - t)

