from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import sqlite3

file = "riegoArduino.db"
table = "dataEnviroment"



class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()

        mensaje = (self.rfile.read(int(self.headers['Content-Length'])).decode())
        print(mensaje)

        var = json.loads(mensaje)["CPUtemp"]

        cursor.execute(f'''INSERT INTO {table} (temperatura) VALUES({var})''')
        conexion.commit()
        #mensaje = "<h1>deja erwasa en clase</h1>"
        #self.wfile.write(bytes(mensaje,"utf8"))

if __name__ == "__main__":
    conexion = sqlite3.connect(file)
    cursor = conexion.cursor()

    with HTTPServer(('',8000), handler) as server:
        server.serve_forever()

    

