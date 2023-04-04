import pandas as pd
import seaborn
import matplotlib.pyplot as matplot
import pdb



#Function to get filename as parameter and return 2 dataframes.
def reading_file_data(my_file):

    df1 = pd.read_csv(my_file, skiprows=4)
    df1 = df1.drop(columns=['Country Code', 'Indicator Name', 'Indicator Code'])
    df1 = df1.dropna(how='all')
    df1 = df1.set_index('Country Name')
    #Transpose of df1
    df2 = df1.T
    return df1, df2


def tool_working():

    # returning dataframes using function
    df1, df2 = reading_file_data("Data File.csv")


    # Initializing list and using describe method for summary part.
    countries_list = ['Aruba', 'Argentina', 'Belgium', 'Bangladesh', 'Bahrain', 'Zimbabwe']
    print("\nUsing describe method to print records for 2010\n")
    # pdb.set_trace()
    print(df1.loc[countries_list, '2010'].describe())

    #Plotting First Graph
    seaborn.boxplot(x='Country Name', y='2010', data=df1.loc[countries_list].reset_index())
    matplot.ylabel('CO2 emissions per capita (metric tons)')
    matplot.show()

    # Plotting Second Graph
    countries = ['Aruba', 'Argentina', 'Belgium', 'Bangladesh', 'Bahrain' , 'Zimbabwe']
    df1.loc[countries, '2009':].plot()
    matplot.ylabel('CO2 emissions (metric tons per capita)')
    matplot.show()



#tool working function
tool_working()