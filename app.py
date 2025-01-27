# api/index.py
import json
from http.server import BaseHTTPRequestHandler
import urllib.parse

file_path = 'q-vercel-python.json'
with open (file_path, 'r') as file:
    data = json.load (file)

marks = dict ()
for i in range (len (data)):
    marks[data[i]['name']] =  data[i]['marks']

class handler(BaseHTTPRequestHandler):
    def do_GET (self):
        parsed_url = urllib.parse.urlparse(self.path)
        query_params = urllib.parse.parse_qs(parsed_url.query)
        names = query_params.get ('name', [])
        
        query_marks = list ()
        for n in names:
            query_marks.append (marks[n])

        self.send_response (200)
        self.send_header ('Content-type', 'application/json')
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers ()
        response = {
            "marks": query_marks,
        }
        self.wfile.write (json.dumps (response).encode ('utf-8'))
        return
