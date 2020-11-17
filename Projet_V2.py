# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 12:02:38 2020

@author: emilie.cai
"""
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates 
from IPython.display import display

data = pd.read_excel(r'C:\Users\emilie.cai\Documents\COURS\Algorithmique et Programmation\Projet\EIVP_KM_V2.xlsx')

data['sent_at'] = pd.to_datetime(data.sent_at)      #On change le type de la colonne

capteur_1 = data[data['id']==1]
capteur_2 = data[data['id']==2]
capteur_3 = data[data['id']==3]
capteur_4 = data[data['id']==4]
capteur_5 = data[data['id']==5]
capteur_6 = data[data['id']==6]

time1 = capteur_1.sent_at                       #Date et heure pour chaque capteur
time2 = capteur_2.sent_at
time3 = capteur_3.sent_at
time4 = capteur_4.sent_at
time5 = capteur_5.sent_at
time6 = capteur_6.sent_at


##FONCTIONS STATISTIQUES

def maximum(L):
    max = L[0]
    for k in range(1,len(L)):
        if L[k]>max:
           max = L[k]
    return(max)

def minimum(L):
    min = L[0]
    for k in range(1,len(L)):
        if L[k]<min:
            min = L[k]
    return(min)

def moyenne(L):
    s=0
    n=len(L)
    for k in range(n):
        s+=L[k]
    return(s/n)
    
def variance(L):
    m = moyenne(L)
    A=[]
    for k in range(len(L)):
        A.append((L[k]-m)**2)
    return moyenne(A)

def ecart_type(L):
    return variance(L)**0.5


def Fusion(L1,L2) :
    LF=[ ]
    while len(L1)>0 and len(L2)>0 :
        if L1[0]<L2[0] :
            LF.append(L1.pop(0))
        else :
            LF.append(L2.pop(0))
    return LF+L1+L2

def TriFusion(L) :
    if len(L)<=1 :
        return L
    else :
        n=len(L)//2
        L1=TriFusion(L[0 : n])
        L2=TriFusion(L[n : len(L)])
        return Fusion(L1,L2)

def mediane(L):
    L = TriFusion(L)
    n= len(L)
    if n < 1:
        return None
    if n % 2 == 0 :
        return ( L[(n-1)//2] + L[(n+1)//2] ) / 2.0
    else:
        return L[(n-1)//2]


##date min et max pour chaque capteur

mdate1,Mdate1 = minimum(time1.tolist()),maximum(time1.tolist())        
mdate2,Mdate2 = minimum(time2.tolist()),maximum(time2.tolist())        
mdate3,Mdate3 = minimum(time3.tolist()),maximum(time3.tolist())         
mdate4,Mdate4 = minimum(time4.tolist()),maximum(time4.tolist())      
mdate5,Mdate5 = minimum(time5.tolist()),maximum(time5.tolist())      
mdate6,Mdate6 = minimum(time6.tolist()),maximum(time6.tolist())   


##Courbes

def Courbe():
    variable = input('Choisir Température, Bruit, Luminosité, CO2 ou Humidité : ')
    
    if variable not in ['Température','Bruit','Luminosité', 'CO2', 'Humidité'] :
            return("La variable choisie n'existe pas...")
    
    
    numero = input('Saisir le numéro du capteur : ' )
    
    if (numero in ['1','2','3','4','5','6'])==True:
        time = []
        capteur_numero = []
        
        #Changer le UTC +02:00    J'ai mis Europe/Paris par défaut
        
        start_date = pd.to_datetime(input('Saisir date début AAAA-MM-JJ : ')).tz_localize('CET')
        end_date = pd.to_datetime(input('Saisir date fin AAAA-MM-JJ : ')).tz_localize('CET')
        
        #On choisit les dates et capteurs pertinents
        
        if numero == '1':  
            time,capteur_numero,date_max,date_min = time1,capteur_1,Mdate1,mdate1
        elif numero == '2':
            time,capteur_numero,date_max,date_min = time2,capteur_2,Mdate2,mdate2
        elif numero == '3':
            time,capteur_numero,date_max,date_min = time3,capteur_3,Mdate3,mdate3
        elif numero == '4':
            time,capteur_numero,date_max,date_min = time4,capteur_4,Mdate4,mdate4
        elif numero == '5':
            time,capteur_numero,date_max,date_min = time5,capteur_5,Mdate5,mdate5
        elif numero == '6':
            time,capteur_numero,date_max,date_min = time6,capteur_6,Mdate6,mdate6
        
       # Problème
        if start_date<date_min or end_date>date_max :
            return('Dates non valides')
        
            
        if variable == 'Température':
            plt.figure("Courbe de la température en fonction du temps")
            plt.plot(time,capteur_numero.temp)
            
            plt.title('Température en fonction du temps', color='r')
            plt.xlabel('Date')        
            plt.xticks(rotation='vertical') 
            plt.xlim(start_date, end_date)                       
            plt.ylabel('Température (°C)')
            plt.show()
            
        elif variable == 'Bruit' :
            plt.figure("Courbe du bruit en fonction du temps")
            plt.plot(time,capteur_numero.noise)
            
            plt.title('Bruit en fonction du temps', color='r')
            plt.xlabel('Date')        
            plt.xticks(rotation='vertical') 
            plt.xlim(start_date, end_date)                      
            plt.ylabel('Bruit (en dBA)')
            plt.show()
            
        elif variable == 'Luminosité' :
            plt.figure("Courbe de la luminosité en fonction du temps")
            plt.plot(time,capteur_numero.lum)
            
            plt.title('Luminosité en fonction du temps', color='r')
            plt.xlabel('Date')        
            plt.xticks(rotation='vertical') 
            plt.xlim(start_date, end_date)                       
            plt.ylabel('Luminosité (en lux)')
            plt.show()
        
        elif variable == 'CO2' :
            plt.figure("Courbe de CO2 en fonction du temps")
            plt.plot(time,capteur_numero.humidity)
                
            plt.title('Teneur en fonction du temps', color='r')
            plt.xlabel('Date')        
            plt.xticks(rotation='vertical') 
            plt.xlim(start_date, end_date)                       
            plt.ylabel('Teneur en CO2 (ppm)')
            plt.show()
        
        elif variable == 'Humidité' :
            plt.figure("Courbe de l'humidité en fonction du temps")
            plt.plot(time,capteur_numero.humidity)
            
            plt.title('Humidité relative en fonction du temps', color='r')
            plt.xlabel('Date')        
            plt.xticks(rotation='vertical') 
            plt.xlim(start_date, end_date)                       
            plt.ylabel('Humidité relative (en %)')
            plt.show()
        else :
            return("La variable choisie n'existe pas...")
 
    else :              #Mauvais capteur
        return('Capteur non existant')

##DISPLAY STATISTIQUES
def displayStats(L,start_date,end_date):
    
    
