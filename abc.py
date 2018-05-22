from bottle import route

@route ('/abc', method=['GET'])
def abc():
	return ('now in abc.py file!')
