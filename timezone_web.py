from flask import Flask, render_template
from pytz import timezone, all_timezones_set
from datetime import datetime

app = Flask(__name__)
time_format = '%m-%d-%Y %H:%M'
time_zone = ['Australia/Adelaide', 'US/Pacific']

def dt(location):
  time = datetime.now(timezone(location)).strftime(time_format)
  return(time)

@app.route('/')
def index():
  return render_template('index.html', Adelaide = dt(time_zone[0]), California = dt(time_zone[1]))

if __name__ == '__main__':
  app.run(debug=True)