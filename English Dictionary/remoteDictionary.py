import mysql.connector

connection = mysql.connector.connect(
    user = 'ardit700_student', 
    password = 'ardit700_student',
    host = '108.167.140.122',
    database = 'ardit700_pm1database'
)

word = input('Enter a word: ')

cursor = connection.cursor()
cursor.execute('SELECT * FROM Dictionary WHERE Expression = \'%s\'' % word)

results = cursor.fetchall()

if results:
    for result in results:
        print(result[1])
else:
    print('No word found!')
