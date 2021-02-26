from flask import Flask, render_template
import json
import subprocess

app = Flask(__name__)
config = json.load(open('config.json', 'r'))

@app.route('/run/<command>')
def command(command):
    p = subprocess.run(config['commands'][command], shell=True, capture_output=True)
    return render_template('result.j2', stdout=p.stdout.decode(), stderr=p.stderr.decode())    

@app.route('/')
def index():
  return render_template('commands.j2', commands = config['commands'])

if __name__ == '__main__':
  app.run(host = '0.0.0.0', port = config['port'])
  