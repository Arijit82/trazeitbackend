from Bottle import run
from three import find_index

courses = ['History', 'Math','Physics', 'CompSci']

index = three.find_index(courses, 'Math')

print(index)

run(host='localhost', port=8080, debug=True, reloader=True)