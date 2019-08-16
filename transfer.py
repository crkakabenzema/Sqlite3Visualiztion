import sqlite3

con = sqlite3.connect(r'C:\Users\ASUS\Desktop\project\QtSql+Sqlite3\1.db')

cur = con.cursor()

cur.execute("select name from sqlite_master where type='table'")
tab_name = cur.fetchall()
tab_name = [line[0] for line in tab_name]
print(tab_name)

col_names = []
for line in tab_name:
    cur.execute('pragma table_info({})'.format(line))
    col_name = cur.fetchall()
    col_name = [x[1] for x in col_name]
    col_names.append(col_name)
    col_name = tuple(col_name)
print(col_names)

cur.execute('SELECT * FROM {}'.format(str(tab_name).replace("'","")))

res = cur.fetchall()

for line in res:
    print(line)
    
ftxt = open(r'C:\Users\ASUS\Desktop\project\QtSql+Sqlite3\1.html',mode='w')

def fw(str):
    ftxt.write(str)
    ftxt.write('\n')

fw('<html>')
fw('<head>')
fw('<meta charset="utf-8">')
fw('<link href="table.css" rel="stylesheet" type="text/css">')
fw('</head>')
fw('<body>')
fw('<h1>')
fw('Table'+ str(tab_name).replace("'",""))
fw('</h1>')
fw('<table>')
fw('<thead>')
fw('<tr>')
for line in range(len(col_name)):
    fw("<th scope='col'>")
    fw(str(col_name[line]))
    fw('</th>')
fw('</tr>')
fw('</thead>')
fw('<tbody>')
for i in range(len(res)):
    fw('<tr>')
    fw("<th scope='row'>")
    fw(str(res[i][0]))
    fw('</th>')
    for j in range(1,(len(res[i]))):
        fw('<td>')
        fw(str(res[i][j]))
        fw('</td>')
    fw('</tr>')
fw('</tbody>')
fw('</table>')
fw('</body>')
fw('</html>')
ftxt.close()
