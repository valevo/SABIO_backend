from time import time
import glob
from tqdm import tqdm

import pandas as pd
import numpy as np

import pyodbc

server = 'tcp:azuredfserv.database.windows.net' 
database = 'Azuredf' 
username = 'Demouser' 
password = 'Knxdde#77' 
driver='{ODBC Driver 17 for SQL Server}'


def table_to_DataFrame(connection, table_name, keys=None, until=None, random_n=None):
    
    keys = "*" if not keys else ",".join(keys)
    if not until:
        until = ""
    until = f"TOP {until}" if until else ""
    sample = f"TABLESAMPLE ({random_n} ROWS)" if random_n else ""
    query = f"SELECT {until} {keys} FROM {table_name} {sample};"
    print(query)
    df = pd.read_sql(query, connection)
    return df


def connect_to_DB():
    return pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)



with connect_to_DB() as conn:
    q  = "SELECT t.name, t.modify_date FROM sys.tables t"
    tables = pd.read_sql(q, conn)
    tables = tables[tables.name != "Person"]
    
    
    
with connect_to_DB() as conn:
    for tbl_name in tqdm(tables.name):
        cur_tbl = table_to_DataFrame(conn, tbl_name, 
                                     keys=None, until=None)
        cur_tbl.to_csv(f"tables/{tbl_name}.csv.gz", index=False)
        
        
        
        