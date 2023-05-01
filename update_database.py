import psycopg2
import pandas as pd


hostname = 'localhost'
database = 'archaeology'
username = 'dbrw'
pwd = 'dbrw'
port_id = 5432
conn = None
cur = None
    
try:
    
    conn = psycopg2.connect(
        host = hostname,
        dbname = database,
        user=username,
        password = pwd,
        port = port_id
        
    )

    cur = conn.cursor()
    df = pd.read_excel(r'update_info.xlsx')

    ##area_utm_easting_meters=478130, area_utm_northing_meters=4419430##
    
    for index, row in df.iterrows():
        temp_context_num = int(row['context_number'])
        temp_find_num = int(row['find_number'])
        temp_weight = float(row['weight'])
        temp_volume = float(row['volume'])
        cur.execute("""SELECT id FROM object.finds
                        WHERE area_utm_easting_meters=478130 AND area_utm_northing_meters=4419430
                        AND context_number = %s AND find_number = %s""" ,(temp_context_num, temp_find_num))

        result = cur.fetchall()
        
        if len(result)==0:
            print(f'No item with context_number {temp_context_num}and find_number {temp_find_num}')
        elif len(result) > 1:
            print(f'{len(result)} items with context_number {temp_context_num}and find_number {temp_find_num}')
        else:
            object_id = result[0][0]
            #cur.execute("SELECT * FROM object.finds WHERE id = %s", (object_id,))
            #result2 = cur.fetchall()
            #print(result2)
            cur.execute("UPDATE object.finds SET weight_grams = %s, volume_millimeter_cubed = %s WHERE ID = %s", (temp_weight, temp_volume, object_id))
            
        
    conn.commit()

    #get column name
    #cur.execute("select column_name from information_schema.columns where table_schema = 'object' and table_name='finds'")
    #column_names = [row[0] for row in cur]
    

except Exception as error:
    print(error)

finally:
    if cur is not None:
        cur = cur.close()
    if conn is not None:
        conn.close()
