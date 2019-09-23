from flask import Flask, request, jsonify
import blinkt
import json
import os
import subprocess

app = Flask(__name__)

def restart():
    cmd = 'pkill -f --signal SIGQUIT app.py'
    os.system(cmd)
    blinkt.clear()
    blinkt.show()
    
    subprocess.call(['python ' '~/support-offsite/app.py'], shell=True)

@app.route('/update', methods=['POST'])
def update_script():
    data = json.loads(request.data)
    print(data['commits'][0])
    print('New version available. Pulling from master.')

    cmd = 'cd support-offsite/ && git pull origin master'
    os.system(cmd)

    restart()

    resp = jsonify(success=True)
    return resp

if __name__ == '__main__':
    app.run()