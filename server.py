from flask import Flask, Response, render_template, request, session
import json
from subprocess import Popen, PIPE, STDOUT
from datetime import timedelta

app = Flask(__name__)
config = json.load(open('config.json', 'r'))
app.secret_key = config['secret_key']
app.permanent_session_lifetime = timedelta(days=365)
denyset = set()

def authorized():
  if not app.secret_key:
    return True
  if request.remote_addr in denyset:
    return False
  if 'authorized' in session:
    return session['authorized']
  else:
    accecpt = input(f'Accept session from {request.remote_addr}? [y,N]: ')
    if accecpt in ['y', 'Y']:
      session.permanent = True      
      session['authorized'] = True
      return True
    else:
      denyset.add(request.remote_addr)
      return False

@app.route('/run/<command>')
def run(command):
  if not authorized():
    return "Unauthorized"
  def generate():
      with Popen(config['commands'][command], shell=True, stdout=PIPE, stderr=STDOUT) as p:
        while (line := p.stdout.readline()):
          yield line
  return Response(generate(), mimetype='text/html')

@app.route('/')
def index():
  if not authorized():
    return "Unauthorized"
  return render_template('commands.j2', commands = map(lambda k: dict(name=k, cmd=config['commands'][k]) , config['commands']))

if __name__ == '__main__':
  app.run(host = config['host'], port = config['port'])
