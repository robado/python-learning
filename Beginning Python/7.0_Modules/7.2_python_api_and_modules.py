#! /usr/bin/python
# 7.2 Python API and Modules

# https://docs.python.org/3/library/index.html <- Python libraries what Python has. From here you can read what it
# has and what do they do and how they work.

# Examples

import shutil

# This module copies a file to another file
shutil.copyfile('testfile.txt', 'test')

# Some more examples...

# This one starts a simple http server at http://localhost:8000/
# If you run this in terminal with ctrl+c you can stop it but with PyCarm simple clicking the red square and it stops it
import http.server
import socketserver

PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
