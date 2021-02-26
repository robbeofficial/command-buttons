from flask import Flask
import json
import subprocess

app = Flask(__name__)
config = json.load(open('config.json', 'r'))

@app.route('/<command>')
def command(command):
    p = subprocess.run(config['commands'][command], shell=True, capture_output=True)    
    return f'<h1>stdout</h1><pre>{p.stdout.decode()}</pre>' + f'<h1>stderr</h1><pre>{p.stderr.decode()}</pre>'

@app.route('/')
def index():
  tags = map(lambda k: f"<button onclick=fetch('/{k}')>{k}</button>", config['commands'].keys())
  return "<br/>".join(tags)

if __name__ == '__main__':
  app.run(host = '0.0.0.0', port = config['port'])
  