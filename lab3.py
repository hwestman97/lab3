# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 13:20:35 2018

@author: Hanna
"""

import timeit
import matplotlib.pyplot as plt
import random

'''
If you want to compare two blocks of code / functions quickly you could do:

start_time = timeit.default_timer()
func1()
print(timeit.default_timer() - start_time)

start_time = timeit.default_timer()
func2()
print(timeit.default_timer() - start_time)
'''

def a_b_c(text):
    '''
    Prompts the user to choose if they whish to solve the problem using pure
    python, A, numbpy, B, or numbpy and scipy, C.
    '''
    x = True
    while x == True:
        choice = input('Vill du använda metod a, b, eller c? ')
        choice = choice.lower()
        if choice == 'a':
            uppgift_a(text)
            x=False
        elif choice == 'b':
            uppgift_b(text)
            x=False
        elif choice == 'c':
            uppgift_c(text)
            x=False
        else:
            print('Fel!!!!!!!!!!!!!')

def uppgift_a(text):
    dictionary_xy = x_y(text)
    alpha, beta = cal(dictionary_xy)
    print(alpha, '\n', beta)
    #plt.plot([1,2,3],[1,2,3])
    #plt.plot(*zip(*sorted(dictionary_xy.items())))
    for key in dictionary_xy:
        plt.scatter(key, dictionary_xy[key])
    plt.show()

def plotGraph(X,Y):
    fignum = random.randint(0,100)
    plt.figure(fignum)
    ### Plotting arrangements ###
    return fignum

def uppgift_b(text):
    pass

def uppgift_c(text):
    pass

def open_file():
    file = input('Vad är namnet på din fil? ')
    text = open(file, 'r')
    return text

def x_y(text):  
    n = 0
    xy = {}
    for line in text:
        n += 1
        no_new_line = line.strip()
        new_line = no_new_line.split("\t")
        x_i = float(new_line[0])
        y_i = float(new_line[1])
        xy[x_i] = y_i
    return xy

def cal(xy):
    m = len(xy)
    sum_x = 0
    sum_y = 0
    product_xy = 0
    square_x = 0
    square_y = 0     
    for key in xy:
        sum_x += key
        sum_y += xy[key]
        product_xy += key*xy[key]
        square_x += key**2
        square_y += xy[key]**2
    beta = (m*product_xy - sum_x*sum_y)/(m*square_x - sum_x*sum_x)
    alpha = sum_y/m - beta*sum_x/m
    return alpha, beta

def main():
    text = open_file()
    uppgift_a(text)
    
main()