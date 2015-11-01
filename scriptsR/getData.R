install.packages("RMySQL")
library(RMySQL)

mydb = dbConnect(MySQL(), user='root', password='lavacahacemu2', dbname='posiciones', host='localhost')

dbListTables(mydb)

dbListFields(mydb, 'posicionesgps')

rs = dbSendQuery(mydb, "select * from posicionesgps limit 10")
data = fetch(rs, n=-1)
data
