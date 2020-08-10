from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"
import urllib
import pandas as pd
import sys
from sqlalchemy import create_engine, MetaData, Table, select, engine
pd.set_option('display.max_rows',None)

server = #MyServerName 
database = #MyDBName 
username = #MyUserName 
password = #MyPass 
params = urllib.parse.quote_plus('DRIVER={ODBC Driver 11 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)

engine = create_engine("mssql+pyodbc:///?odbc_connect=%s" % params)

df = pd.read_sql_query("select * from #TableName", engine)
#Use line below to fetch data contained in a cell
#df_filtered = df.query('#ColumnName.str.contains("#Data")', engine='python')

#Plot Pie By Cols
colors  = ("dodgerblue","salmon", "palevioletred", "steelblue", "seagreen", "plum", "blue", "indigo", "beige", "yellow")

i = 0 #counter

for col in df: 
    sizes = df[col].value_counts()
    pie = df[col].value_counts().plot(kind='pie',colors=colors,shadow=True,autopct='%1.1f%%',startangle=30,radius=1.5,
                                      center=(0.5,0.5),textprops={'fontsize':12},frame=False,labels=None,pctdistance=.65)
    labels = sizes.index.unique()
    plt.gca().axis("equal")
    plt.title(df.columns[i],weight='bold',size=14)
    plt.subplots_adjust(left=0.0,bottom=0.1,right=0.85)
    #plt.savefig(str(df.columns[i])+'.png',dpi=100,bbox_inches='tight')
    pie.set_ylabel('')
    #plt.legend(labels, bbox_to_anchor(0.5,-.2))
    plt.legend(labels,bbox_to_anchor=(0.5, -.2),
           bbox_transform=plt.gcf().transFigure)
    i = i+1
    plt.show()

print('Python version ' + sys.version)
print('Pandas version ' + pd.__version__) 