from bottle import route, run, template
import csv
import parselogs

passwords_file = "testpasswords.csv"

@route('/')
def index():
    with open(passwords_file, 'rb') as csvfile:
        passwords = csv.DictReader(csvfile, delimiter=',', quotechar='|')
        logs = parselogs.parselogs()
        return template('index', passwords=passwords, logs=logs)

@route('/passwords')
def passwords():
    with open(passwords_file, 'rb') as csvfile:
        passwords = csv.DictReader(csvfile, delimiter=',', quotechar='|')
        return template('password_template', passwords=passwords)

run(host='localhost', port=8080)