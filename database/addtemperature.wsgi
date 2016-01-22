import sqlite3
from cgi import escape, parse_qs

def application(environ, start_response):
    connection = None
    my_response = ""
    params = parse_qs(environ['QUERY_STRING'])
    room = escape(params.get('room',[''])[0])
    temperature = escape(params.get('temperature',[''])[0])

    my_query = 'INSERT INTO temperature(roomid,temperature,datetime) VALUES(%s,%s,CURRENT_TIMESTAMP);' %(room,temperature)
    try:
        connection = sqlite3.connect('/var/www/database/temperature.db'
                                     ,isolation_level=None)
        cursor = connection.cursor()
        cursor.execute(my_query)
        query_results = cursor.fetchone()
        my_response = 'Inserted %s for room %s' % (temperature, room)
    except sqlite3.Error, e:
        my_response = "There is an error %s:" % (e)
    finally:
        connection.close()

    status = '200 OK'
    response_headers = [('Content-Type', 'text/plain'),
                        ('Content-Length', str(len(my_response)))]
    start_response(status, response_headers)
    return [my_response]
