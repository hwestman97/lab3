
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

font = {'family': 'serif',
        'color':  'black',
        'weight': 'normal',
        'size': 20,
        }

errors = (ValueError, FileNotFoundError, ZeroDivisionError, IOError, IndexError, OSError)

#font och errors är globala variabler och jag har valt att ha det så
#för att de används i flera olika funktioner utan att man ändrar deras värden

def main():
    '''
    Frågar användaren om de vill lösa problemet med bara python, alternativ A, 
    numbpy, alternativ B, eller numbpy och scipy, alternativ C, och ber sedan 
    användaren skriva in en giltig fil. Ingen input eller output.
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
        if choice == 'q':
            Loop = False
        elif choice == 'a':
            file, filename = get_file()
            uppgift_a(file, choice, filename)
            Loop = False
        elif choice == 'b':
            file, filename = get_file()
            uppgift_b(file, choice, filename)
            Loop = False
        elif choice == 'c':
            file, filename = get_file()
            uppgift_c(file, choice, filename)
            Loop = False
        else:
            print('Datorn förstod inte vad du ville göra, försök igen!')

def get_file():
    '''
    Ber användaren skriva in ett filnamn, om något går fel kontrollera att 
    du skrivit in filnamn.txt Ingen input, retunerar filen och filnamnet.
    '''
    file = input('Vad är namnet på din fil? ')
    filename = file[:-4]
    return file, filename

def uppgift_a(file, choice, filename):
    '''
    Det här är metod a:s kodskelett, funktionen kallar på de nödvändiga subfunktionerna
    för att kunna gå från en fil med x- och y-värden till en graf med värden på
    alfa och beta. Som input används en fil, metoden användaren valde och filens namn.
    '''
    try:
        dictionary_xy, alpha, beta = calc_a(file)
        print_alphabeta(alpha, beta)
        f = plot_a(dictionary_xy, alpha, beta, file)
        save_file(choice, filename, f)
        return f
    except errors:
        print('\nNågot är fel med din fil!')

def save_file(choice, file, f):
    '''
    Den här funktionen sparar en graf till pdf-format. Som input används metoden
    användaren valde, en fil och grafen f, ingen output.
    '''
    f.savefig('%s_%s.pdf' % (file, choice))

def print_alphabeta(alpha, beta):
    '''
    Den här funktionen printar ut värdena på alfa och beta. Tar som input värden
    på alfa och beta, ingen output.
    '''
    print(u'\u03B1'+ ' = '+ str(alpha))
    print(u'\u03B2'+ ' = '+ str(beta))

def plot_a(dictionary, alpha, beta, file):
    '''
    Plottar grafen med metod a. Tar som input en dictionary med värden på x och
    y, värden på alfa och beta och en fil. Retunerar en graf f.
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

def uppgift_b(file, choice, filename):
    '''
    Det här är metod b:s kodskelett, funktionen kallar på de nödvändiga subfunktionerna
    för att kunna gå från en fil med x- och y-värden till en graf med värden på
    alfa och beta. Som input används en fil, den metod användaren valde och filens namn.
    Funktionen retunerar en graf f om inte filen är tom.
    '''
    try:
        alpha, beta, x, y = calc_b(file)
        print_alphabeta(alpha, beta)
        f = plot_bc(x, y, alpha, beta, file)
        save_file(choice, filename, f)
        return f
    except errors:
        print('\nNågot är fel med din fil!')

def loadtext_bc(file):
    '''
    Funktionen använder numpy för att omvandla input, en fil, till två arrays,
    x och y, som sedan retuneras.
    '''
    a = np.loadtxt(file)
    x = a[:,0]
    y = a[:,1]
    return x, y

def uppgift_c(file, choice, filename):
    '''
    Det här är metod c:s kodskelett, funktionen kallar på de nödvändiga subfunktionerna
    för att kunna gå från en fil med x- och y-värden till en graf med värden på
    alfa och beta. Som input används en fil, metoden användaren valde och 
    filens namn.
    '''
    try:
        x, y = loadtext_bc(file)
        beta, alpha, r_value, p_value, std_err = stats.linregress(x, y)
        print_alphabeta(alpha, beta)
        f = plot_bc(x, y, alpha, beta, file)
        save_file(choice, filename, f)
    except errors:
        print('\nNågot är fel med din fil!')

def plot_bc(x, y, alpha, beta, file):
    '''
    Funktionen plottar en graf enligt metod b eller c. Som input används två
    arrays, x och y, värden på alfa och beta och en fil. Funktionen retunerar sedan
    en graf f.
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

def calc_a(file):
    '''
    Tar en input, file. Med metod a ska all summering och beräkning av inre 
    punkter ske med ren python vilket är vad den här funktionen gör, sedan 
    beräknar den alfa och beta, omvandlar filen till en dictionary och 
    retunerar alfa och beta.
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
    for key in xy:
        sum_x += key
        sum_y += xy[key]
        product_xy += key*xy[key]
        square_x += key**2
    alpha, beta = alpha_beta(m, sum_x, sum_y, product_xy, square_x)
    return xy, alpha, beta

def alpha_beta(m, sum_x, sum_y, product_xy, square_x):
    '''
    Den här funktionen tar fem inputvaribler, längden av en lista med x- och y-värden,
    summan av x, summan av y, summan av producten xy och summan av kvadraterna av x.
    Funktionen returnerar sedan ett värde på alfa och beta där beta är lutningen på 
    regressionslinjen och alfa är där linjen skär y-axeln.
    '''
    beta = (m*product_xy - sum_x*sum_y)/(m*square_x - sum_x*sum_x)
    alpha = sum_y/m - beta*sum_x/m
    return alpha, beta

def calc_b(file):
    '''
    Den här funktionen hör till uppgift b, den använder numpy för att öppna filen,
    detta sker i subfunktionen loadtext_bc, men den använder vanlig python för att
    räkna ut alfa och beta. Den tar en input, file, och retunerar värden på alfa 
    och beta, och två arrays med x och y värden.
    '''
    x, y = loadtext_bc(file)
    m = len(x)
    sum_x = sum(x)
    sum_y = sum(y)
    product_xy = sum(x*y)
    square_x = sum(x**2)
    alpha, beta = alpha_beta(m, sum_x, sum_y, product_xy, square_x)
    return alpha, beta, x, y

main()
