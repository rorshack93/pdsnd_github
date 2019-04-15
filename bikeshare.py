import time
import pandas as pd
import numpy as np
import datetime as dt
import calendar
from scipy import stats

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

cities = ['chicago', 'new york city', 'washington']
months = ['January', 'February', 'March', 'April', 'May', 'June']
days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    print(' ' * 40)

    # get user's city selection
    city = ''
    while city not in cities:
        city = input("Which city's bikeshare data would you like to analyze? Chicago, New York City, or Washington? ").lower()
        print(' ' * 40)

    # get user's month selection
    month = ''
    while month not in months and month != 'All':
        month = input("Which of the first 6 months would you like to analyze? (all, january, february, ... , june) ").capitalize()
        print(' ' * 40)

    # get user's day selection
    day = ''
    while day not in days and day != 'All':
        day = input("Which day of the week would you like to analyze? (all, monday, tuesday, ... sunday) ").capitalize()
        print(' ' * 40)

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
    # loads csv with the selected city into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    df = df.dropna()

    # changes the column of start times/end times into datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])

    # makes 3 new columns, m/d/y
    df['Day of Week'] = df['Start Time'].dt.strftime("%A")
    df['Month'] = df['Start Time'].dt.strftime("%B")
    df['Day'] = df['Start Time'].dt.strftime("%d,")
    df['Year'] = df['Start Time'].dt.strftime("%Y")

    # creates dataframe with specified parameters
    if month == 'All' and day == 'All':
        return df
    elif month != 'All' and day == 'All':
        df = df.loc[df['Month'] == month]
        return df
    elif month == 'All' and day != 'All':
        df = df.loc[df['Day of Week'] == day]
        return df
    else:
        df = df.loc[df['Month'] == month]
        df = df.loc[df['Day of Week'] == day]
        return df
    return df


def time_stats(df, month, day):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # if all months were selected, prints most common month
    if month == 'All':
        print('The most frequent month of travel is ' + df['Start Time'].dt.strftime("%B").mode())

    # if all days were selected, prints most common day
    if day == 'All':
        print('The most frequent day of travel is ' + df['Start Time'].dt.strftime("%A").mode())

    print('The most frequent start hour of travel is ' + df['Start Time'].dt.strftime("%H").mode())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    print('The most common start station is:')
    print(df['Start Station'].mode())

    print('The most common end station is:')
    print(df['End Station'].mode())

    print('The most frequent combination of start and end station is:')
    print((df['Start Station'] + " TO " + df['End Station']).mode())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # calculates total travel time in seconds
    t = pd.to_timedelta(df['End Time'] - df['Start Time']).astype('timedelta64[s]')
    total_trip = t.sum()
    print('The total travel time is ' + str(total_trip) + ' seconds')
<<<<<<< HEAD

||||||| merged common ancestors

=======

    # calculates the average travel time in seconds
>>>>>>> documentation
    mean_trip = t.mean()
    print('The average travel time is ' + str(mean_trip) + ' seconds')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    print('These are the counts of user types:')
    print(df['User Type'].value_counts())

    print('\n')

    if city != 'washington':
        print('These are the counts of genders:')
        print(df['Gender'].value_counts())

        print('The earliest year of birth is ' + str(df['Birth Year'].min()))
        print('The most recent year of birth is ' + str(df['Birth Year'].max()))
        print('The most common year of birth is ' + str(df['Birth Year'].mode()))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def view_raw(city):
    i = ''
    l = 5
    c = pd.read_csv(CITY_DATA[city])
    while i != 'no':
        i = input('Would you like to see the raw data for ' + city.capitalize() + '? ').lower()
        print(c.head(l))
        l = l + 5

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df , month, day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        view_raw(city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
