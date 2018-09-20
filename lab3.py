
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

font = {'family': 'serif',
        'color':  'black',
        'weight': 'normal',
        'size': 20,
        }

def main():
    '''
    Frågar användaren om de vill lösa problemet med bara python, alternativ A, 
    numbpy, alternativ B, eller numbpy och scipy, alternativ C.
    '''
    print('''Det här programmet tar en fil med x- och y-värden och utför en enkel 
linjär regression på punkterna. Programmet retunerar värdena på alfa och beta 
och plottar sedan en graf med både punkterna och regressionslinjen som sparas
som en pdf. Metod a använder sig av ren python, metod b av numpy och metod c 
av både numpy och scipy. Avsluta programmet genom att trycka Q.''')
    Loop = True 
    while Loop == True:
        choice = input('Vill du använda metod a, b, eller c? ')
        choice = choice.lower() #Omvandlar alla bokstäver till små bokstäver
        if choice == 'a' or choice == 'b' or choice == 'c':
            get_file(choice)
            Loop = False
        elif choice == 'q':
            Loop = False
        else:
            print('Datorn förstod inte vad du ville göra, försök igen!')

def get_file(choice):
    '''
    Skriv in ett giltigt filnamn med x- och y-värden, funktionen kollar att filen
    finns och inte är tom, anropar sedan funktionen som korresponderar till den 
    metod du valde. Till sist sparas grafen i pdf-format.
    '''
    Loop = True
    felmeddelande = '\nNågot är fel med din fil, försök igen!'
    error = (ValueError, FileNotFoundError, ZeroDivisionError, IOError, IndexError)
    #Loopen är till för att användaren ska få försöka skriva in en fil flera gånger
    #Funktionen testar också för vanliga fel med filen
    while Loop == True:
        file = input('Vad är namnet på din fil? ')
        filename = file[:-4]
        try:
            if file == 'q':
                Loop = False
            elif choice == 'a':
                    f = uppgift_a(file)
                    save_file(choice, filename, f)
                    Loop = False
            elif choice == 'b':
                    f = uppgift_b(file)
                    save_file(choice, filename, f)
                    Loop = False
            elif choice == 'c':
                    f = uppgift_c(file)
                    save_file(choice, filename, f)
                    Loop = False
        except error:
            print(felmeddelande)

def uppgift_a(file):
    '''
    Det här är metod a:s kodskelett, funktionen kallar på de nödvändiga subfunktionerna
    för att kunna gå från en fil med x- och y-värden till en graf med värden på
    alfa och beta.
    '''
    dictionary_xy, alpha, beta = calc(file)
    print_alphabeta(alpha, beta)
    f = plot_a(dictionary_xy, alpha, beta, file)
    return f

def save_file(choice, file, f):
    '''
    Den här funktionen sparar en graf till pdf-format.
    '''
    f.savefig('%s_%s.pdf' % (file, choice))

def print_alphabeta(alpha, beta):
    '''
    Den här funktionen printar ut värdena på alfa och beta.
    '''
    print(u'\u03B1'+ ' = '+ str(alpha))
    print(u'\u03B2'+ ' = '+ str(beta))

def plot_a(dictionary, alpha, beta, file):
    '''
    Plottar grafen med metod a, dvs ren python.
    '''
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

def uppgift_b(file):
    '''
    Det här är metod b:s kodskelett, funktionen kallar på de nödvändiga subfunktionerna
    för att kunna gå från en fil med x- och y-värden till en graf med värden på
    alfa och beta.
    '''    
    x, y = b_c(file)
    beta, alpha = np.polyfit(x, y, 1)
    print_alphabeta(alpha, beta)
    f = plot_bc(x, y, alpha, beta, file)
    return f

def uppgift_c(file):
    '''
    Det här är metod c:s kodskelett, funktionen kallar på de nödvändiga subfunktionerna
    för att kunna gå från en fil med x- och y-värden till en graf med värden på
    alfa och beta.
    '''    
    x, y = b_c(file)
    beta, alpha, r_value, p_value, std_err = stats.linregress(x, y)
    print_alphabeta(alpha, beta)
    f = plot_bc(x, y, alpha, beta, file)
    return f

def plot_bc(x, y, alpha, beta, file):
    '''
    Funktionen plottar en graf enligt metod b och c.
    '''
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

def b_c(file):
    '''
    Omvandlar användarens fil till två arrays som sedan retuneras.
    '''
    a = np.loadtxt(file)
    x = a[0:,0]
    y = a[0:,1]
    return x, y

def calc(file):
    '''
    Med metod a ska all summering och beräknning av inre punkter ske med ren
    python vilket är vad den här funktionen gör, sedan beräknar den alfa och
    beta, omvandlar filen till en dictionary och retunerar alfa o´ch beta.
    '''
    xy = {}
    with open(file, 'r') as f:
        for line in f:
            no_new_line = line.strip()
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
        square_y += xy[key]**2 #Uppgiften söger att man ska beräkna summan av kvadraterna av y men den används inte i programmet
    beta = (m*product_xy - sum_x*sum_y)/(m*square_x - sum_x*sum_x)
    alpha = sum_y/m - beta*sum_x/m
    return xy, alpha, beta

main()
