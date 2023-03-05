# Info: This file contains all the functions used in the main file for processing the solutions
# Funtions for getting data from the database, and for plotting the data


#### Funciones necesarias ####



n = len(DatosTaller)
p = DatosTaller['p'].tolist()
d = DatosTaller['d'].tolist()
r = DatosTaller['r'].tolist()
SM = PCP.SingleMachine(n=n, p=p, d=d, r=r)
SM.J = DatosTaller['Nº REMISION'].tolist()
SM.LDD()
start_date = DatosTaller['FECHA'].min()
results = pd.DataFrame({'Task': SM.J,
                          'p': SM.p,
                          'd': SM.d,
                          'r': SM.r,
                          'Start': hours_to_dates(start_date,SM.S),
                          'Finish': hours_to_dates(start_date,SM.C),
                          'L': SM.L,
                          'T': SM.T,
                          'E': SM.E})
#display(resultado)
results['M']=1
results.to_excel('resultado.xlsx')
# make a gantt chart  from the dataframe results
import plotly.express as px
fig = px.timeline(results,x_start='Start',
                  x_end='Finish',
                  y='Task',
                  color='Task',
                  color_continuous_scale=["blue",
                                          "red",
                                          "green",
                                          "yellow",
                                          "grey"])
fig.show(renderer="browser")

def float_to_date(float_list: list = [], start_date: datetime.date = datetime.date.today()):
    """
    function that takes a list of floats that represent days and returns a list of dates
    and jumps the sundays in the process, so if a date happens to be a sunday it will skip it
    and add the number of days to the next day and, so at the end it will add the number of sundays
    that were skipped to the date, and also add the days, minuts and seconds
    """
    # create a list of dates
    dates = []
    # iterate over the list of floats
    for f in float_list:
        # get the number of weeks
        weeks = f // 7
        # get the number of days
        days = f - weeks
        # get the number of hours
        hours = days*24
        # get the number of minutes
        minutes = (hours - int(hours))*60
        # get the number of seconds
        seconds = (minutes - int(minutes))*60
        # create a date
        date = start_date + datetime.timedelta(days=int(f))
        # check if the date is a sunday
        if date.weekday() != 6:  # 6 is Sunday
            # add the number of days to the date
            date = date + datetime.timedelta(days=weeks)
            # add the number of hours to the date
            date = date + datetime.timedelta(hours=int(hours))
            # add the number of minutes to the date
            date = date + datetime.timedelta(minutes=int(minutes))
            # add the number of seconds to the date
            date = date + datetime.timedelta(seconds=int(seconds))
            # append the date to the list of dates
        dates.append(date)
    return dates
#    # create a list of dates
#    dates = []
#    # iterate over the list of floats
#    for f in float_list:
#        # get the number of weeks
#        weeks = f // 7
#        # get the number of days
#        days = f - weeks
#        # add the number of days to the start date
#        date = start_date + datetime.timedelta(days=int(days))
#        # if the date is a sunday add the number of weeks to the date
#        if date.weekday() == 6:  # 6 is Sunday
#            date = date + datetime.timedelta(days=weeks)
#        # append the date to the list of dates
#        dates.append(date)
#    return dates
def float_to_date_2(list, start_date):
    """"
    function that takes a list of floats that represent days and returns a list of dates
    """
    dates = []
    for f in list:
        date = start_date + datetime.timedelta(days=int(f))
        dates.append(date)
    return dates
def convert_floats_to_dates(float_list, start_date):
    dates = []
    for f in float_list:
        date = start_date + datetime.timedelta(days=int(f))
        if date.weekday() != 6:  # 6 is Sunday
            dates.append(date)
    return dates
def float_days_to_timeformat(hours):
    """
    function that takes a list of floats that represent days and returns a list of strings in the format 'HH:MM'
    """
    # create a list of strings
    timeformat = []
    # iterate over the list of floats
    for h in hours:
        # get the number of weeks
        weeks = h // 7
        # get the number of days
        days = h - weeks
        # get the number of hours
        hours = days*24
        # get the number of minutes
        minutes = (hours - int(hours))*60
        # create a string
        string = f'{int(hours)}:{int(minutes)}'
        # append the string to the list of strings
        timeformat.append(string)
    return timeformat