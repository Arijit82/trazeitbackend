from bottle import route, run
import abc as a
import two as t

@route ('/demo', method=['GET'])
def demo():
    return ('now in demo file!')


run(host='localhost', port=8080, debug=True, reloader=True)
