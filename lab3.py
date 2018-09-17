# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 13:20:35 2018

@author: Hanna
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy import stats


def a_b_c():
    '''
    Frågar användaren om de vill lösa problemet med bara python, alternativ A, 
    numbpy, alternativ B, eller numbpy och scipy, alternativ C.
    '''
    x = True
    while x == True:
        choice = input('Vill du använda metod a, b, eller c? ')
        choice = choice.lower()
        if choice == 'a':
            f, file= uppgift_a()
            save_file(choice, file, f)
            x = False
        elif choice == 'b':
            f, file = uppgift_b()
            save_file(choice, file, f)
            x = False
        elif choice == 'c':
            f, file = uppgift_c()
            save_file(choice, file, f)
            x = False
        else:
            print('Datorn förstod inte vad du ville göra, försök igen!')

def uppgift_a():
    text, file = open_file()
    dictionary_xy, alpha, beta = calc(text)
    print_alphabeta(alpha, beta)
    f = plotGraph(dictionary_xy, alpha, beta)
    return f, file

def save_file(choice, file, f):
    f.savefig('%s_%s.pdf' % (file, choice))

def print_alphabeta(alpha, beta):
    print(u'\u03B1'+ ' = '+ str(alpha))
    print(u'\u03B2'+ ' = '+ str(beta))

def plotGraph(dictionary, alpha, beta):
    f = plt.figure()
    for key in dictionary:
        plt.scatter(key, dictionary[key], c='blue')
    plt.xlabel('x')
    plt.ylabel('y')
    x1 = min(dictionary)
    x2 = max(dictionary)
    y1 = alpha + beta*x1
    y2 = alpha + beta*x2
    plt.plot([x1,x2],[y1,y2],linewidth=3.0, c='red')
    plt.show()
    return f    

def uppgift_b():
    text, file = open_file()
    x, y = b_c(text)
    beta, alpha = np.polyfit(x, y, 1)
    print_alphabeta(alpha, beta)
    f = plt.figure()
    plt.scatter(x,y)
    plt.plot(x, beta * x + alpha, '-',linewidth=3.0, color='red')
    plt.show()
    return f, file

def uppgift_c():
    text, file = open_file()
    x, y = b_c(text)
    beta, alpha, r_value, p_value, std_err = stats.linregress(x, y)
    print_alphabeta(alpha, beta)
    f = plt.figure()
    plt.scatter(x,y)
    plt.plot(x, beta * x + alpha, '-',linewidth=3.0, color='red')
    plt.show()
    return f, file

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

def calc(text):
    xy = {}
    for line in text:
        no_new_line = line.strip('\n')
        new_line = no_new_line.split("\t")
        x_i = float(new_line[0])
        y_i = float(new_line[1])
        xy[x_i] = y_i
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
    return xy, alpha, beta

def main():
    a_b_c()
    
main()
'''
open_file ska inte köras i b & c, eller iaf inte i c
rubriker och skit i graferna
slå ihop plotbestämningarna för a, b, c
skriv om open_file???
Astrids grej om random
gör dig av med listor
'''