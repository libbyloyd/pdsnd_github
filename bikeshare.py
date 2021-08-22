#Consulted another students github page as a reference: https://github.com/beingjainparas/Udacity-Explore_US_Bikeshare_Data/blob/master/bikeshare_2.py


import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    cities = ('chicago', 'new york city', 'washington')
    while True:
        city = input("Which city would you like to explore? Chicago, New York City, or Washington DC?: ").lower()
        if city in cities:
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    months = ('all','january', 'february', 'march', 'april', 'may', 'june')
    month = input("Please enter a month between January and June to view an analysis from. For all months, please enter 'all': ")


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ('all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday')
    day = input("Please enter a day of the week (Monday - Sunday) you would like to preform your analysis on. For all days, please enter 'all': ")

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
        # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
    
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_popular_month = df['month'].mode()[0]
    print("The most common month to travel is: ", most_popular_month)

    # TO DO: display the most common day of week
    most_popular_day = df['day_of_week'].mode()[0]
    print("The most common day to travel is: " + most_popular_day)

    # TO DO: display the most common start hour
    most_popular_hour = df['hour'].mode()[0]
    print("The most popular hour to travel is: ", most_popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    return df


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_popular_start_station = df['Start Station'].mode()[0]
    print("The most popular Start Station is: " + most_popular_start_station)

    # TO DO: display most commonly used end station
    most_popular_end_station = df['End Station'].mode()[0]
    print("The most popular End Station is: " + most_popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    most_popular_station_combo = (df['Start Station'] + " & " + df['End Station']).mode()[0]
    print("The most popular Start & End Station Combo is: " + most_popular_station_combo)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("The total travel time for this month and day was: ", total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("The average travel time for this month and day was: ", mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("The breakdown of user type is as follows: \n", user_types)

    # TO DO: Display counts of gender
    if city == 'chicago.csv' or city =='new_york_city.csv':
        gender_types = df['Gender'].value_counts()
        print("The breakdown of user gender is as follows: \n", gender_types)

    # TO DO: Display earliest, most recent, and most common year of birth
        min_birth_year = df['Birth Year'].min()
        print("The oldest individual to ride during this time period was born in: ", min_birth_year)
    
        max_birth_year = df['Birth Year'].max()
        print("The youngest individual to ride during this time period was born in: ", max_birth_year)
    
        avg_birth_year = df['Birth Year'].mode()[0]
        print("The most common year of birth for this time period's riders was: ", avg_birth_year)
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_data(df):
    print(df.head())
    i = 0
    while True:
        data = input("Would you like to see more data?")
        if data == 'no':
            return
        i = i + 5
        print(df.iloc[i:i+5])
    
    
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        
        while True:
            data = input("Would you like to see the data? yes or no?: ")
            if data == 'no':
                break
            display_data(df)
            break

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
