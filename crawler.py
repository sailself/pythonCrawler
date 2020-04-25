import pg8000
import datetime

connection = pg8000.connect('kevin', password='kev', database='python_learn')
# connection.run('''CREATE TABLE "test"
# (
#     "url" character varying NOT NULL,
#     "price" numeric,
#     "time" timestamp,
#     "name" character varying,
#     PRIMARY KEY (url)
# )''')
# connection.commit()
datetime.datetime.now
timestamp = datetime.datetime.now()
print('timestamp: ',timestamp)
connection.run("INSERT INTO test VALUES ('test2', 1009990.1, '%s', 'test')" % timestamp)

for row in connection.run('SELECT * FROM test'):
    print(row)

connection.commit()

