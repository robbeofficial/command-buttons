from flask import Flask, Response, render_template
import json
from subprocess import Popen, PIPE, STDOUT

app = Flask(__name__)
config = json.load(open('config.json', 'r'))

@app.route('/run/<command>')
def run(command):
    def generate():
        with Popen(config['commands'][command], shell=True, stdout=PIPE, stderr=STDOUT) as p:
          while (line := p.stdout.readline()):
            yield line
    return Response(generate(), mimetype='text/html')

@app.route('/')
def index():
  return render_template('commands.j2', commands = map(lambda k: dict(name=k, cmd=config['commands'][k]) , config['commands']))

if __name__ == '__main__':
  app.run(host = '0.0.0.0', port = config['port'])
