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
    alpha, beta = calc(text)
    print(alpha)
    print(beta)
    plot1 = plotGraph(alpha + beta*x, x)
    (alpha,beta)

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

def calc(text):
    n = 0
    sum_x = 0
    sum_y = 0
    product_xy = 0
    square_x = 0
    square_y = 0
    for line in text:
        n += 1
        no_new_line = line.strip()
        new_line = no_new_line.split("\t")
        x = float(new_line[0])
        y = float(new_line[1])
        sum_x += x
        sum_y += y
        product_xy += x*y
        square_x += x**2
        square_y += y**2
    beta = (n*product_xy - sum_x*sum_y)/(n*square_x - sum_x*sum_x)
    alpha = sum_y/n - beta*sum_x/n
    return alpha, beta

def main():

    text = open_file()
    uppgift_a(text)
    
main()