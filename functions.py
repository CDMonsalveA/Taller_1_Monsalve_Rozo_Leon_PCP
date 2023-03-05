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