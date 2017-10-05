from bottle import route, run, static_file
@route('/')
def main():
	#В вызове static_file() мы хотим получить файл index.html из каталога,
	#указанного в  root (в нашем случае в  '.' , текущем каталоге).
	return static_file('index.html', root='.')
run(host='localhost', port=9999)
