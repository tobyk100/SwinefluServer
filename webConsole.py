from bottle import route, run, template, static_file
import csv
import parselogs

passwords_file = "testpasswords.csv"

@route('/static/:path#.+#', name='static')
def static(path):
    return static_file(path, root='static')

@route('/')
def index():
    # parse log file and write password to password.csv
    with open(passwords_file, 'rb') as csvfile:
        passwords = csv.DictReader(csvfile, delimiter=',', quotechar='|')
        logs = parselogs.parselogs()
        return template('index', passwords=passwords, logs=logs)


run(host='localhost', port=8080)