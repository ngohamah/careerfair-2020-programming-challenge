# Career_Project.py
# Ngoh Rodney Amah
# Resources used: Programming for CS by John Zelle (one of my freshman books)

'''
This function would read from a file and then generate a list of a list lines
where each line corresponds to a row in the .csv file.

The first use of the split method deals away with the newline
character leaving behind the contents of the line and an empty string.
e.g. [['Country,Country_Code,Population,Year', '']...]

The second use of the split method deals away with the commas separating
individual elements of item at index 0 of the line list(s)
'''

                                        #*****************************
                                        #        Section 1           #
                                        #*****************************
def ReadingFromFile(filename):
    infile = open(filename,'r')
    listoflines= []
    newlistoflines = []
    
    # reading each line of the file and assigning it to an empty list, listoflines.
    for line in infile:
        listoflines.append(line.split('\n'))
    
    # separating the strings at position 0 of each list of listoflines to the actual constants.
    for item in listoflines:
        for j in range(1):
    #splitting wherever there is a comma and assigning the new list generated to newlistoflines.
            newlistoflines.append(item[j].split(','))
    
    return newlistoflines

'''This function would provide an interface where the user can choose which option
   they'll like to work on and then returns the user choice.
'''
def MenuAndSelecting():
    print('This program answers questions you might need answers to: ')
    print('\n','***Options***')
    print('\n','1. Country with the highest number of infections to date (and the number of infected): ',
          '\n','2. Country with the 2nd heighest number of infections to date (and the number of infected): ',
          '\n','3. Country with the highest infection rate (ratio of number of infections to population) ',
          '\n','   to date (and infection rate): ',
          '\n','4. Overall death rate (ratio of number of deaths to number of infections) for COVID-19.',
          '\n','5. Country with the highest death rate (ratio of number of deaths to number of infections) ',
          '\n','   (and the death rate for that country): ',
          '\n','6. Countries with new infections per day on the rise (and country with the steepest increase): ', 
          '\n','7. Countries with new infections per day decreasing and the country with the steepest decrease ',
          '\n','   AND the country where the infections per day peak the earliest and when it happened for this country',
          '\n','8. Doing a data comparison with information in the file \'partial_time_series\'',
          '\n','\n','9. QUIT')
    
    print('\n','Select your option: ',end='')
    
    try:
        choice = int(input())
        if 1<=choice<=8:
            return choice
        else:
            print('\n','Incorrect option choice')
    except ValueError as message:
        message='Error: Please enter a numeric value'
        print('\n',message)
 
#calling the function
#MenuAndSelecting()  

# This function is used to create a copy of the CountryExp tab in the covid_data
# file by eliminating the redundant occurence of the countries and calculating
# the number of infected persons for every country.
def Countries_Infected_Death_Trending(filename):
    covid_data=ReadingFromFile(filename)
    CountriesInfected=[]
    NumberInfected=[]
    NumberDeath=[]
    
    total=0
    total2=0
    counter=0
    
    #These values are used below to generate a list of the the number of new cases of each country.
    accum=''
    ListRedundant=[]
    
    
    #Replacing CountryExp, the header with the name of the next country
    #and replacing NewConfCases and Newdeaths another header with 0 this would help me
    #in the loop below to count the number of infected as well as eliminate
    #the redundancy CountryExp field.
    for item1 in covid_data:
        i=0
        for item2 in covid_data:
            if i==1:
                item1[1]=item2[1]
                item1[2]='0'
                item1[3]=0
                break 
            i+=1
        break
    
    #creating a list of countries using the covid_data to avoid redundancy.
    for item1 in covid_data:
        total+=int(item1[2])
        total2+=item1[3]
        for item2 in covid_data:
            if item1[1]==item2[1]: #countries names match!
                accum+=item2[2]+','
                total+=int(item2[2])
                total2+=int(item2[3])
            if item1[1]!=item2[1]:
                ListRedundant.append(accum)
                CountriesInfected.append(item1[1])
                NumberInfected.append(total)
                NumberDeath.append(total2)
                item1=item2
                accum=item1[2]+','
                total=int(item2[2])
                total2=int(item2[3])
            counter+=1
            #checking if item2 has reached the last list of covid_data
            if counter==len(covid_data):
                CountriesInfected.append(item2[1])
                NumberInfected.append(total)
                NumberDeath.append(total2)
                ListRedundant.append(accum)
                break
        break
    
    return CountriesInfected, NumberInfected, NumberDeath,ListRedundant


def Task1():
    countries,infected,Nd,Lr=Countries_Infected_Death_Trending('covid_data.csv')
    #checking for the highest
    for i in range(len(infected)):
        c=0
        for j in range(len(infected)):
            if infected[i]>infected[j]:
                c+=1  
        if c==len(infected)-1: #minus 1 because the country that records the highest number of infected 
                                # has an amount greater than all other countries except itself
            print('\n','{0} is the country with the highest number of infections'.format(countries[i].upper()),
                  'with a recorded amount of {:,}'.format(infected[i]),'people')            
            return 

#Task1()
def Task2():
    countries,infected,Nd,Lr=Countries_Infected_Death_Trending('covid_data.csv')
    #checking for the second highest
    for i in range(len(infected)):
        c=0
        for j in range(len(infected)):
            if infected[i]>infected[j]:
                c+=1  
        if c==len(infected)-2: #minus 2 because the country that records the second highest number of infected 
                                # has an amount second to the highest only.
            print('\n','{0} is the country with the second highest number of infections'.format(countries[i].upper()),
                  'with a recorded amount of {:,}'.format(infected[i]),'people')            
            return 

#Task2()

#This function is designed to capture a list containing the countries found 'population_data.csv' file
#and also capture the population of these respective countries. 
def CountriesAndPopulation(filename):
    population=ReadingFromFile(filename)
    AllCountries = []
    Population= []
    i=0
    for item in population:
        #This condition discards the header elements of the file
        if i>0:
            AllCountries.append(item[0])
            Population.append(item[2])
        i+=1
        
    return AllCountries, Population

#This function would compute the InfectionRates, which is the ration of the number infected to the
#population of the given country and then return a list containing these infection rates.
def Homonize():
    #calling the CountriesAndPopulation function with an argument which returns two values,
    AllCountries,Population=CountriesAndPopulation('population_data.csv')
    
    #calling the CountriesAndInfected funtion with an argument which returns two values as well.
    CountriesInfected,NumberInfected,Nd,Lr=Countries_Infected_Death_Trending('covid_data.csv')
    
    #Since not all countries may be found in the CountriesInfected list, it is important to start by 
    #deriving a new list containing the intersection of countries found in the AllCountries and
    #CountriesInfected list and their corresponding populations
    #I-for intersection
    Ipopulation = [] 
    Icountries = []
    Inumberinfected=[]
    
    #countries that were either entered wrongly or are not present in the list of
    #AllCountries
    
    CountryWithError=[]
    CWEIndex=[]
    
    for country1 in CountriesInfected:
        i=0
        for country2 in AllCountries:
            #By doing Icountries, Ipopulation, and Inumberinfected succinctly, I am guaranteed that their indices correspond
            #to each other.
            if country1==country2:
                Icountries.append(country1)
                Ipopulation.append(Population[i])
                break
                
            i+=1
    
    #determining countries which appear in the 'covid_data.csv' file but not in the
    #'population_data.csv' file
    k=0
    for country1 in CountriesInfected:
        j=0
        for country2 in Icountries:
            if country1!=country2:
                j+=1
        if j==len(Icountries):
            CountryWithError.append(country1)
            CWEIndex.append(k)
        k+=1
            
    return Icountries,Ipopulation,CountryWithError,CWEIndex

#InfectionRates()

#Determining the country with the highest rate of infection.
def Task3():
    countries,population,country_error,country_error_index=Homonize()
    CountriesInfected,NumberInfected,Nd,Lr=Countries_Infected_Death_Trending('covid_data.csv')
    
    #Rates denotes the infection rate, currently empty
    Rates = []
    #Computing ratios
    i=0 #since both list have items that correspond to each other, a single counter can be used
        #for this iteration.

    for i in range(len(population)):
        try:
            
            #This loop eliminate the indices of the various elements of CountryWithError from taking
            #up the population and NumberInfected values of other values in the list.
            for j in range(len(country_error_index)):
                if i==country_error_index[j]:
                    break
                else:
                    Rates.append(round((int(NumberInfected[i])/int(population[i])),20))
        except ZeroDivisionError as message:
            message='A country with a population of zero has crashed the program'
            print(message)
        i+=1
    #Comparing ratios for the greatest
    for i in range(len(Rates)):
        c=len(Rates)
        for j in range(len(Rates)):
            if Rates[i]>Rates[j]:
                c-=1
        if c==1:
           print('\n','{0} is the country with the highest infection rate of {1}'.format(countries[i].upper(),Rates[i]))
        i+=0
        
    print('\n','NOTICE!',
          '\n','Based on the information you provided on both the \'covid_data.csv\' and ',
               'the \'population_data.csv\' files, one or more     countries in the \'covid_data.csv\'',
               'is/are not found in the \'population_data.csv\' as shown below:')
    for item in country_error:
        print('-',item)
    
#Task3()

#Determining the overall death rate for COVID-19 
def Task4():
    CountriesInfected,NumberInfected,NumberDeath,Lr=Countries_Infected_Death_Trending('covid_data.csv')
    
    total_infected=0
    total_death=0
    
    #computing the total number of individuals who are infected.
    for item in NumberInfected:
        total_infected+=int(item)
    for item in NumberDeath:
        total_death+=int(item)
    
    #computing the deathrate which is the ratio of the number death to the number infected
    DeathRate = round((total_death/total_infected),10)
    
    print('The death rate (ratio of number of deaths to number of infections) for COVID-19 so far is: ',DeathRate)
    
#Task4()

#determining the country with the highest death rate.
def Task5():
    CountriesInfected,NumberInfected,NumberDeath,Lr=Countries_Infected_Death_Trending('covid_data.csv')
    
    DeathRate=[]
    
    for i in range(len(NumberDeath)):
        try:
            DeathRate.append(round(int(NumberDeath[i])/int(NumberInfected[i]),15))
        except ZeroDivisionError as message:
            message='Error, one of the countries in your list wasn\'t infected by the disease therefore, an error occured in parsing the deathrate.'
            print(message)
    for i in range(len(DeathRate)):
        counter=0
        for j in range(len(DeathRate)):
            if DeathRate[i]>DeathRate[j]:
                counter+=1
        if counter==len(DeathRate)-1:
            print('\n','{0} is the country with the highest death rate recorded at {1}'.format(CountriesInfected[i],DeathRate[i]))
            
            
def Trending(): #modified Countries_Infected_Death() function
    CountriesInfected,NumberInfected,NumberDeath,ListRedundant=Countries_Infected_Death_Trending('covid_data.csv')
    
    NewListRedundant = []
    
    for item in ListRedundant:
        NewListRedundant.append(item.split(','))
    
    #----------------< Determining positive trend >---------------------------------------------------#
    #In evaluating the positive trend, I imagine that during the first half of a 7day period (a week)
    #the total number of infected must be less than total number during the second half.
    #For example suppose we assume that on the 1st day the population is 0, then increasing daily by 1, until 
    #day 7 when the population is 6. We would have that, sumLowerQuarter = 0+1+2+3=6, sumUpperQuarter=4+5+6=15
    #Difference= sumLowerQuarter-sumUpperQuarter = -9
    #Hence I deduce that for any list of number infected in a seven day period, the Difference must be less than -9
    #for a positive trend to be seen
        
    #----------------< Determining negative trend >---------------------------------------------------#
    #Difference = 15-6=9
    #Also, I deduce that for any list of number infected in a seven day period, the Difference must be greater than 9
    
    i=0 # i would be used in the future for indexing purposes.
    #This loop computes the number of infected in 7days (week) of each month and assigns the value to TAmt
    
    #List of Difference for increasing Trend
    Difference=[] #this list would be used to store the difference of the sumUpperQuarter-SumLowerQuarter of all the countries
                            #given
    
    for i in range(len(NewListRedundant)):
        total=0
        s_total=0
        counter=0
        s_counter=0 #Special counter would be used to determine the upper and lower quarters.
        upperquarter=0
        lowerquarter=0
        for j in range(len(NewListRedundant[i])):
            #since 7 is an odd number, to completely split it into equal halves,
            #I eliminate the third item from being added during iteration
            if NewListRedundant[i][j]!='':
                if j!=3:
                    s_total+=int(NewListRedundant[i][j])
                if s_counter==3:
                    upperquarter=s_total
                    s_total=0
                if s_counter==7:
                    lowerquarter=s_total
                    
                if counter==7: #condition checking if 7th day has reached.
                    Difference.append(lowerquarter-upperquarter)
                    break
            s_counter+=1
            counter+=1
            if counter==len(NewListRedundant[i]):
                Difference.append(lowerquarter-upperquarter)
                break
        

    return Difference

#determining countries with an increasing daily trend in the number of infected.
def Task6():
    Difference=Trending()
    CountriesInfected,NumberInfected,NumberDeath,ListRedundant=Countries_Infected_Death_Trending('covid_data.csv')
    
    #printing countries
    print('\n','The list of countries with an increasing trend in the number of new cases infected is as follows: ','\n')
    for i in range(len(Difference)):
        if Difference[i]<-9:
            print(' '+CountriesInfected[i],end=',')
    
#Task6()

#determining the country with the steepest increase
def Task6i():
    #Based on Task6, the country with the highest number of infected in 7days has the steepest increase
    #--------------------------
    #copied from Task6,
    
    Difference=Trending()
    CountriesInfected,NumberInfected,NumberDeath,ListRedundant=Countries_Infected_Death_Trending('covid_data.csv')
    amounts=[]
    countries=[]
    
    #Determining difference amounts
    for i in range(len(Difference)):
        if Difference[i]<-9:
            amounts.append(Difference[i])
            countries.append(CountriesInfected[i])
    #comparing amounts   
    for i in range(len(amounts)):
        counter=1
        for j in range(len(amounts)):
            if amounts[i]<amounts[j]:#comparing total number infected of on country with that of the others.
                counter+=1
        if counter==len(amounts):
            print('\n','\n')
            print('{0} is the country with the steepest increase'.format(countries[i].upper()))
            break
#Task6i()

#determining countries with a decreasing daily trend in the number of infected.
def Task7():
    Difference=Trending()
    CountriesInfected,NumberInfected,NumberDeath,ListRedundant=Countries_Infected_Death_Trending('covid_data.csv')
    
    #printing countries
    print('\n','The list of countries with an increasing trend in the number of new cases infected is as follows: ','\n')
    for i in range(len(Difference)):
        if Difference[i]>9:
            print(' '+CountriesInfected[i],end=',')
        
#Task7()
            
#determining the country with the steepest decrease
def Task7i():    
    Difference=Trending()
    CountriesInfected,NumberInfected,NumberDeath,ListRedundant=Countries_Infected_Death_Trending('covid_data.csv')
    amounts=[]
    countries=[]
    
    #Determining difference amounts
    for i in range(len(Difference)):
        if Difference[i]>9:
            amounts.append(Difference[i])
            countries.append(CountriesInfected[i])
            
    #comparing amounts   
    for i in range(len(amounts)):
        counter=1
        for j in range(len(amounts)):
            if amounts[i]>amounts[j]:#comparing total number infected of on country with that of the others.
                counter+=1
        if counter==len(amounts):
            print('\n','\n')
            print('{0} is the country with the steepest decrease'.format(countries[i].upper()))
            break

#Task7i()

def Task7ii():
    print('Not done yet')
    
                                        #*****************************
                                        #        Section 2           #
                                        #*****************************

#doing data comparison
def Task8():
    CountriesInfected,NumberInfected,NumberDeath,ListRedundant=Countries_Infected_Death_Trending('covid_data.csv')
    CD=ReadingFromFile('covid_data.csv')

    #Reading from the Partial Time Series File
    PTS=ReadingFromFile('partial_time_series.csv')
    newitem1=''
    newPTS=[]
    newlistRed=[]
    
    #Generating a list where each list of newly confirmed infected cases
    #of a particular country in covid_data.csv file is an item in the
    #list, newlistRed.
    
    for item in ListRedundant:
        newlistRed.append(item.split(','))
        
    #converting list items to integers
    for item in newlistRed:
        for i in range(len(item)-1):
            item[i]=int(item[i])
            
    #Value one has a problem, it needs to be fixed.
    for item1 in PTS:
        for i in range(len(item1)):
            newitem1+=item1[i][3:] 
            
    for i in range(len(PTS)):
        for j in range(len(PTS[i])):
            if i!=0:
                newPTS.append(int(PTS[i][j]))
    
    cPTS=newPTS
    #comparison
    for num01 in newPTS:
        for item in newlistRed:
            c=0
            j=0
            k=0
            for num1 in item:
                if num01==num1:
                    c+=1
                    j+=1
                    num01=cPTS[j]
                    k+=0
                    continue
                else:
                    break
                
                
        break
    
    if c==len(newPTS):
        print('The country this data belongs to is {0} and the start date is {1}'.format(CD[k][1],CD[k][0]))
    else:
        print('The data does not match any country data')
                
#Task11()
    
    
def main():
    choice=MenuAndSelecting()
    while choice!=9:
        if choice==1:
            Task1()
        elif choice==2:
            Task2()
        elif choice==3:
            Task3()
        elif choice==4:
            Task4()
        elif choice==5:
            Task5()
        elif choice==6:
            Task6()
            Task6i()
        elif choice==7:
            Task7()
            Task7i()
        elif choice==8:
            Task8()
        
        print()
        try:
            choice=int(input('Select another option: '))
        except:
            print('You have enter an incorrect value')
        
main()  
    
    
    
    
    
    
    
    
    
    
    
    
    
    
