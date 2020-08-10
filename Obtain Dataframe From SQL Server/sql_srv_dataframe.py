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
df.query('#ColumnName.str.contains("#Data")', engine='python')
print('Python version ' + sys.version)
print('Pandas version ' + pd.__version__) 