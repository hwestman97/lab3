# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 13:20:35 2018

@author: Hanna
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

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
            x = False
        elif choice == 'b':
            uppgift_b(text)
            x = False
        elif choice == 'c':
            uppgift_c(text)
            x = False
        else:
            print('Datorn förstod inte vad du ville göra, försök igen!')

def uppgift_a(text):
    dictionary_xy = x_y(text)
    alpha, beta = calc(dictionary_xy)
    f = plotGraph(dictionary_xy, alpha, beta)
    return f

def plotGraph(dictionary, alpha, beta):
    f = plt.figure()
    for key in dictionary:
        plt.scatter(key, dictionary[key], c='darkblue')
    plt.xlabel('x')
    plt.ylabel('y')
    x1 = min(dictionary)
    x2 = max(dictionary)
    y1 = alpha + beta*x1
    y2 = alpha + beta*x2
    plt.plot([x1,x2],[y1,y2],linewidth=3.0, c='red')
    plt.show()
    return f

def uppgift_b(text):
    x, y = b_c(text)
    beta, alpha = np.polyfit(x, y, 1)
    print(u'\u03B1'+ ' = '+ str(alpha))
    print(u'\u03B2'+ ' = '+ str(beta))
    plt.scatter(x,y)
    plt.plot(x, beta * x + alpha, '-', color='red')
    plt.show()

def uppgift_c(text):
    a = np.loadtxt(text)
    x = a[0:,0]
    y = a[0:,1]
    beta, alpha, r_value, p_value, std_err = stats.linregress(x, y)
    print(u'\u03B1'+ ' = '+ str(alpha))
    print(u'\u03B2'+ ' = '+ str(beta))
    plt.scatter(x,y)
    plt.plot(x, beta * x + alpha, '-', color='red')
    plt.show()

def b_c(text):
    a = np.loadtxt(text)
    x = a[0:,0]
    y = a[0:,1]
    return x,y

def open_file():
    file = input('Vad är namnet på din fil? ')
    text = open(file, 'r')
    file = file[:-4]
    return text, file

def x_y(text):
    xy = {}
    for line in text:
        no_new_line = line.strip()
        new_line = no_new_line.split("\t")
        x_i = float(new_line[0])
        y_i = float(new_line[1])
        xy[x_i] = y_i
    return xy

def calc(xy):
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
    print(u'\u03B1'+ ' = '+ str(alpha))
    print(u'\u03B2'+ ' = '+ str(beta))
    return alpha, beta

def main():
    text, file = open_file()
    #f = 
    a_b_c(text)
    #f.savefig('%s_a.pdf' % file)
    
main()
'''
open_file ska inte köras i b & c, eller iaf inte i c
rubriker och skit i graferna
slå ihop plotbestämningarna för a, b, c
skriv om open_file???
'''