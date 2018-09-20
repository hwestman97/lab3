# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 13:20:35 2018

@author: Hanna
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

font = {'family': 'serif',
        'color':  'black',
        'weight': 'normal',
        'size': 20,
        }

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
            #save_file(choice, file, f)
            x = False
        elif choice == 'c':
            f, file = uppgift_c()
            #save_file(choice, file, f)
            x = False
        else:
            print('Datorn förstod inte vad du ville göra, försök igen!')

def uppgift_a():
    dictionary_xy, alpha, beta, file = calc()
    print_alphabeta(alpha, beta)
    f = plot_a(dictionary_xy, alpha, beta, file)
    return f, file

def save_file(choice, file, f):
    f.savefig('%s_%s.pdf' % (file, choice))

def print_alphabeta(alpha, beta):
    print(u'\u03B1'+ ' = '+ str(alpha))
    print(u'\u03B2'+ ' = '+ str(beta))

def plot_a(dictionary, alpha, beta, file):
    f = plt.figure()
    for key in dictionary:
        plt.scatter(key, dictionary[key], c='blue')
    labels = ['Regressionslinje', 'Datapunkter']
    plt.xlabel('x')
    plt.ylabel('y')
    x1 = min(dictionary)
    x2 = max(dictionary)
    y1 = alpha + beta*x1
    y2 = alpha + beta*x2
    plt.plot([x1,x2],[y1,y2],linewidth=3.0, c='red')
    plt.legend(labels)
    plt.title(file, fontdict=font)
    plt.show()
    return f    

def uppgift_b():
    x, y, file = b_c()
    beta, alpha = np.polyfit(x, y, 1)
    print_alphabeta(alpha, beta)
    f = plot_bc(x, y, alpha, beta, file)
    return f, file

def uppgift_c():
    x, y, file = b_c()
    beta, alpha, r_value, p_value, std_err = stats.linregress(x, y)
    print_alphabeta(alpha, beta)
    f = plot_bc(x, y, alpha, beta, file)
    return f, file

def plot_bc(x, y, alpha, beta, file):
    labels = ['Regressionslinje', 'Datapunkter']
    f = plt.figure()
    plt.scatter(x,y)
    plt.plot(x, beta * x + alpha, '-',linewidth=3.0, color='red')
    plt.xlabel('x')
    plt.ylabel('y')    
    plt.legend(labels)
    plt.title(file, fontdict=font)
    plt.show()   
    return f

def b_c():
    file = input('Vad är namnet på din fil? ')
    a = np.loadtxt(file)
    file = file[:-4]
    x = a[0:,0]
    y = a[0:,1]
    return x, y, file

def calc():
    file = input('Vad är namnet på din fil? ')    
    xy = {}
    with open(file, 'r') as f:
        for line in f:
            no_new_line = line.strip()
            new_line = no_new_line.split("\t")
            x_i = float(new_line[0])
            y_i = float(new_line[1])
            xy[x_i] = y_i
    file = file[:-4]
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
        square_y += xy[key]**2 #Uppgiften söger att man ska beräkna summan av kvadraterna av y men den används inte i programmet
    beta = (m*product_xy - sum_x*sum_y)/(m*square_x - sum_x*sum_x)
    alpha = sum_y/m - beta*sum_x/m
    return xy, alpha, beta, file

a_b_c()
