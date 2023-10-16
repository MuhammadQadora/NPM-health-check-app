import datetime,requests,os,dateutil.parser,time
from flask import request,url_for,make_response,jsonify,Flask


app = Flask(__name__)

# github_token = os.environ['git-token']
t1 = time.perf_counter()
npmjs_url= 'https://registry.npmjs.org'


def time_difference(time):
    time_obj = dateutil.parser.parse(time)
    date = datetime.datetime.now(datetime.timezone.utc) - time_obj
    return date.days

def last_commit(url):
    response = requests.get(url=url)
    data = response.json()
    date = data[0].get('commit',{})['author']['date']
    return date

def main(data):
    name = data
    response = requests.get(url=f'{npmjs_url}/{data}')
    data = response.json()
    maintainers = len(data.get('maintainers',[]))
    last_version = time_difference(data.get('time',[])['modified'])
    github_url = 'https://api.github.com/repos' + data.get('repository',{})['url'].split('com')[1].split('.')[0] + '/commits'
    lastCommit = time_difference(last_commit(github_url))
    if last_version <= 30 and maintainers >= 2 and lastCommit <= 14:
        return f"{name} is healthy"
    else:
        return f"{name} is not healthy"
    


@app.route('/healthy',methods=['GET','POST'])
def healthy():
    if request.method == 'POST':
        data = request.get_json()
        finalResult = []
        for package in data['packages']:
            result = main(package)
            finalResult.append(result)
        response = make_response(jsonify({"results":finalResult}))
        return response
            


app.run(debug=True,port=4000,host='0.0.0.0')