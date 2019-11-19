import time
import pandas as pd

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

    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        try:
            city = input('Please select a city to explore: (chicago, new york city, washington) \n').lower()
            if city in ['chicago', 'new york city', 'washington']: break
        except:
            print('Please enter a valid city: chicago, new york city, washington \n')
        continue

    # get user filter options
    while True:
        try:
            filter_opts = input('\n Would you like to filter the data by day, month or both? Type "none" for no filter. \n').lower()
            if filter_opts in ['day', 'month', 'both', 'none']: break
        except:
            print('Please enter a valid response: (day, month, both, none) \n')
        continue

    if filter_opts == 'day':
          while True:
                # get user input for day of week (all, monday, tuesday, ... sunday)
                try:
                    day = input('Please selected your prefered day: (monday, tuesday, ... sunday) \n').lower()
                    month = 'all'
                    if day in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']: break
                except:
                    print('Please enter a valid day: (monday, tuesday, ... sunday) \n')
                continue

    elif filter_opts == 'month':
            while True:
                # get user input for month (all, january, february, ... , june)
                try:
                    month = input('Please selected your prefered month: (january, february, ... , june) \n').lower()
                    day = 'all'
                    if month in ['january', 'february', 'march', 'april', 'may', 'june']: break
                except:
                    print('Please enter a valid month: (january, february, ... , june) \n')
                continue

    elif filter_opts == 'both':
            while True:
                # get user input for month (all, january, february, ... , june)
                try:
                    month = input('Please selected your prefered month: (january, february, ... , june) \n').lower()
                    if month in ['january', 'february', 'march', 'april', 'may', 'june']: break
                except:
                    print('Please enter a valid month: (january, february, ... , june) \n')
                continue

            while True:
          # get user input for day of week (all, monday, tuesday, ... sunday)
                try:
                   day = input('Please selected your prefered day: (monday, tuesday, ... sunday) \n').lower()
                   if day in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']: break
                except:
                 print('Please enter a valid day: (monday, tuesday, ... sunday) \n')
                continue
    else:
         month = 'all'
         day = 'all'
    print('-'*40)
    return city, month, day

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

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

    # extract hour Start Time to create an hour column
    df['hour'] = df['Start Time'].dt.hour

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.weekday_name


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
        df = df[df['day'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    month = months[df['month'].mode()[0] -1]
    print('The most common month is: {} \n'.format(month.title()))

    # display the most common day of week
    print('The most common day of week is: {} \n'.format( df['day'].mode()[0]))

    # display the most common start hour
    print('The most common start hour is: {} \n'.format( df['hour'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print('The most commonly used start station: {}'.format(df['Start Station'].value_counts().idxmax()))

    # display most commonly used end station
    print('The most commonly used end station: {}'.format(df['End Station'].value_counts().idxmax()))

    # display most frequent combination of start station and end station trip
    station_pairs = df['Start Station'] + "_" + df['End Station']
    popular_pair = station_pairs.value_counts().idxmax()
    print('The most frequent trip is from \n{} \nto \n{}.'.format(popular_pair.split("_")[0], popular_pair.split("_")[1]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print('\nThe total travel time was: {}'.format(df['Trip Duration'].sum()))

    # display mean travel time
    print('\nThe average travel time was: {}'.format(df['Trip Duration'].mean()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print('\nDistribution of users:\n')
    print(user_types)

    # Display counts of gender
    if 'Gender' in df.columns:
        gender_types = df['Gender'].value_counts()
        print('\nDistribution of gender:\n')
        print(gender_types)

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        print('\nThe earliest year of birth was {}'.format(df['Birth Year'].min()))
        print('\nThe most recent year of birth was {}.'.format(df['Birth Year'].max()))
        print('\nThe most common year of birth was {}.'.format(df['Birth Year'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
        """Displays raw data on bikeshare upon users request."""
    inp = input('Do you want to see the raw data? Yes or No \n')
    row_num = 0

    while True:
        if inp.lower() != 'no':
            print(df.iloc[row_num: row_num + 5])
            row_num += 5
            inp = input('\nWould you like to see more raw data? Yes or No \n')
        else:
            break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)
        restart = input('\nWould you like to restart? Enter yes or no:\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
