import sys
from os import path

MAJ = 2
MIN = 7

runtime_version_pass = sys.version_info[:2] == (MAJ, MIN)
env_version_pass =  not path.isfile(r'env\scripts\pip{0}.{1}.exe'.format(MAJ, MIN))
env_tag_pass =  not path.isfile(r'env\azure.env.python-{0}.{1}.txt'.format(MAJ, MIN))
test_pass = runtime_version_pass and env_version_pass and env_tag_pass

def wsgi_app(environ, start_response):
    status = '200 OK'
    response_headers = [('Content-type', 'text/plain')]
    start_response(status, response_headers)
    response_body = 'SUCCESS' if test_pass else 'FAILURE'
    yield response_body.encode()

if __name__ == '__main__':
    from wsgiref.simple_server import make_server

    httpd = make_server('localhost', 5555, wsgi_app)
    httpd.serve_forever()
