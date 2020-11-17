import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates 
from IPython.display import display

data = pd.read_excel(r'C:\Users\emilie.cai\Documents\COURS\Algorithmique et Programmation\Projet\EIVP_KM_V2.xlsx')
data = data.drop(['sent_at', 'date'],axis=1)

data['dateheure'] = pd.to_datetime(data.dateheure)      #On change le type de la colonne dateheure

capteur_1 = data[data['id']==1]
capteur_2 = data[data['id']==2]
capteur_3 = data[data['id']==3]
capteur_4 = data[data['id']==4]
capteur_5 = data[data['id']==5]
capteur_6 = data[data['id']==6]

time1 = capteur_1.dateheure
time2 = capteur_2.dateheure
time3 = capteur_3.dateheure
time4 = capteur_4.dateheure
time5 = capteur_5.dateheure
time6 = capteur_6.dateheure

mdate1,Mdate1 = time1.min(),time1.max()         #date min et max pour chaque capteur
mdate2,Mdate2 = time2.min(),time2.max()
mdate3,Mdate3 = time3.min(),time3.max()
mdate4,Mdate4 = time4.min(),time4.max()
mdate5,Mdate5 = time5.min(),time5.max()
mdate6,Mdate6 = time6.min(),time6.max()

##Courbes
print('Choix des courbes ')

#Température
def CourbeTemp():
    numero = input('Saisir le numéro du capteur : ' )
    if (numero in ['1','2','3','4','5','6'])==True:
        time = []
        capteur_numero = []
        if numero == '1':  #On choisit les dates et capteurs pertinents
            time,capteur_numero = time1,capteur_1
        elif numero == '2':
            time,capteur_numero = time2,capteur_2
        elif numero == '3':
            time,capteur_numero = time3,capteur_3
        elif numero == '4':
            time,capteur_numero = time4,capteur_4
        elif numero == '5':
            time,capteur_numero = time5,capteur_5
        elif numero == '6':
            time,capteur_numero = time6,capteur_6
            
        plt.figure("Courbe de la température en fonction du temps")
        plt.plot(time,capteur_numero.temp)
        
        plt.title('Température en fonction du temps', color='r')
        plt.xlabel('Date')        
        plt.xticks(rotation='vertical') 
        #xlim(xmin, xmax)                      
        plt.ylabel('Température (°C)')

        plt.show()
    else :              #Mauvais capteur
        print('Capteur non existant')

#Bruit
def CourbeNoise():
    numero = input('Saisir le numéro du capteur : ' )
    if (numero in ['1','2','3','4','5','6'])==True:
        time = []
        capteur_numero = []
        if numero == '1':  #On choisit les dates et capteurs pertinents
            time,capteur_numero = time1,capteur_1
        elif numero == '2':
            time,capteur_numero = time2,capteur_2
        elif numero == '3':
            time,capteur_numero = time3,capteur_3
        elif numero == '4':
            time,capteur_numero = time4,capteur_4
        elif numero == '5':
            time,capteur_numero = time5,capteur_5
        elif numero == '6':
            time,capteur_numero = time6,capteur_6
            
        plt.figure("Courbe du bruit en fonction du temps")
        plt.plot(time,capteur_numero.noise)
        
        plt.title('Bruit en fonction du temps', color='r')
        plt.xlabel('Date')        
        plt.xticks(rotation='vertical') 
        #xlim(xmin, xmax)                      
        plt.ylabel('Bruit (en dB)')

        plt.show()
    else :              #Mauvais capteur                          
        print('Capteur non existant')
        
#Humidité
def CourbeHumidity():
    numero = input('Saisir le numéro du capteur : ' )
    if (numero in ['1','2','3','4','5','6'])==True:
        time = []
        capteur_numero = []
        if numero == '1':  #On choisit les dates et capteurs pertinents
            time,capteur_numero = time1,capteur_1
        elif numero == '2':
            time,capteur_numero = time2,capteur_2
        elif numero == '3':
            time,capteur_numero = time3,capteur_3
        elif numero == '4':
            time,capteur_numero = time4,capteur_4
        elif numero == '5':
            time,capteur_numero = time5,capteur_5
        elif numero == '6':
            time,capteur_numero = time6,capteur_6
            
        plt.figure("Courbe de l'humidité en fonction du temps")
        plt.plot(time,capteur_numero.humidity)
        
        plt.title('Humidité en fonction du temps', color='r')
        plt.xlabel('Date')        
        plt.xticks(rotation='vertical') 
        #xlim(xmin, xmax)                      
        plt.ylabel('Humidité (g/m3)')

        plt.show()
    else :              #Mauvais capteur
        print('Capteur non existant')
        
#Luminosité
def CourbeLum():
    numero = input('Saisir le numéro du capteur : ' )
    if (numero in ['1','2','3','4','5','6'])==True:
        time = []
        capteur_numero = []
        if numero == '1':  #On choisit les dates et capteurs pertinents
            time,capteur_numero = time1,capteur_1
        elif numero == '2':
            time,capteur_numero = time2,capteur_2
        elif numero == '3':
            time,capteur_numero = time3,capteur_3
        elif numero == '4':
            time,capteur_numero = time4,capteur_4
        elif numero == '5':
            time,capteur_numero = time5,capteur_5
        elif numero == '6':
            time,capteur_numero = time6,capteur_6
            
        plt.figure("Courbe de la luminosité en fonction du temps")
        plt.plot(time,capteur_numero.lum)
        
        plt.title('Luminosité en fonction du temps', color='r')
        plt.xlabel('Date')        
        plt.xticks(rotation='vertical') 
        #xlim(start_date, end_date)                      
        plt.ylabel('Luminosité')  #UNITE A TROUVER

        plt.show()
    else :
        print('Capteur non existant')
        
#Teneur en CO2
def CourbeCO2():
    numero = input('Saisir le numéro du capteur : ' )
    if (numero in ['1','2','3','4','5','6'])==True:
        time = []
        capteur_numero = []
        if numero == '1':  #On choisit les dates et capteurs pertinents
            time,capteur_numero = time1,capteur_1
        elif numero == '2':
            time,capteur_numero = time2,capteur_2
        elif numero == '3':
            time,capteur_numero = time3,capteur_3
        elif numero == '4':
            time,capteur_numero = time4,capteur_4
        elif numero == '5':
            time,capteur_numero = time5,capteur_5
        elif numero == '6':
            time,capteur_numero = time6,capteur_6
            
        plt.figure("Courbe de CO2 en fonction du temps")
        plt.plot(time,capteur_numero.humidity)
        
        plt.title('Teneur en fonction du temps', color='r')
        plt.xlabel('Date')        
        plt.xticks(rotation='vertical') 
        #xlim(xmin, xmax)                      
        plt.ylabel('Teneur en CO2 (ppm)')

        plt.show()
    else :              #Mauvais capteur
        print('Capteur non existant')
        