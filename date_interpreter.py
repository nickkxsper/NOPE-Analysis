import datetime

def interpret_datestr(nope):
    nope['Datetime'] = ''
    nope['Date'] = ''
    nope['Time'] = ''
    nope['Year'] = ''
    nope['Month'] = ''
    nope['Day'] = ''
    nope['Hour'] = ''
    nope['Minute'] = ''

    # If you don't want certain columns added, just comment out the command below (ie: if you only need the datetime object and don't care about the date, day, hour, etc columns, then you can comment all commands except for the datetime one)

    for index, row in nope.iterrows():
        nope.at[index, 'Date'] = datetime.datetime.strptime(nope.iloc[index]['Human Time'], '%Y-%m-%d %H:%M:%S').date()
        nope.at[index, 'Time'] = datetime.datetime.strptime(nope.iloc[index]['Human Time'], '%Y-%m-%d %H:%M:%S').time()
        nope.at[index, 'Datetime'] = datetime.datetime.strptime(nope.iloc[index]['Human Time'], '%Y-%m-%d %H:%M:%S')
        nope.at[index, 'Year'] = datetime.datetime.strptime(nope.iloc[index]['Human Time'], '%Y-%m-%d %H:%M:%S').year
        nope.at[index, 'Month'] = datetime.datetime.strptime(nope.iloc[index]['Human Time'], '%Y-%m-%d %H:%M:%S').month
        nope.at[index, 'Day'] = datetime.datetime.strptime(nope.iloc[index]['Human Time'], '%Y-%m-%d %H:%M:%S').day
        nope.at[index, 'Hour'] = datetime.datetime.strptime(nope.iloc[index]['Human Time'], '%Y-%m-%d %H:%M:%S').hour
        nope.at[index, 'Minute'] = datetime.datetime.strptime(nope.iloc[index]['Human Time'],
                                                              '%Y-%m-%d %H:%M:%S').minute