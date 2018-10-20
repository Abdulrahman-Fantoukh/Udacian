from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs

class Udacian:
    def __init__(self,name,city,enrollment,nanodegree,status):
        self.name =name
        self.city=city
        self.enrollment=enrollment
        self.nanodegree=nanodegree
        self.status=status
    def print_udacian(self):
        return self.name+" is enrolled in " + self.city+ " studying " + self.nanodegree + " in sat am with ms.lujain , he/she is " + self.status

memory = []
form = '''<!DOCTYPE html>
    <title>Message Board</title>
    <form method="POST">
        <textarea name="name" placeholder="Name"></textarea>
        <br>
        <textarea name="city" placeholder="City"></textarea>
        <br>
        <textarea name="enrollment" placeholder="Enrollment"></textarea>
        <br>
        <textarea name="nanodgree" placeholder="Nanodegree"></textarea>
        <br>
        <textarea name="status" placeholder="Status"></textarea>
        <br>
        <button type="submit">Save</button>
    </form>
    <pre>
{}
    </pre>
'''
class UdacianHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        length = int(self.headers.get('content-length',0))
        data = self.rfile.read(length).decode()
        #message = parse_qs(data)["message"][0]
        #l1 = Udacian(message[0],message[1],message[2],message[3],message[4])
        name = parse_qs(data)["name"][0]
        city = parse_qs(data)["city"][0]
        enrollment = parse_qs(data)["enrollment"][0]
        enrollment = tuple(enrollment.split(' '))
        nanadegree = parse_qs(data)["nanodegree"][0]
        status = parse_qs(data)["status"][0]
        #message = message.replace("<","&alt;")
        student = Udacian(name, city, enrollment, nanadegree, status)
        memory.append(student)
        self.send_response(303)
        self.send_header('Location','/')
        self.end_headers()

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/html; charset=utf-8')
        self.end_headers()
        mesg = form.format('\n'.join(i.print_udacian() for i in memory))
        self.wfile.write(mesg.encode())

if __name__ == '__main__':
    server_address = ('',8000)
    httpd = HTTPServer(server_address,UdacianHandler)
    httpd.serve_forever()