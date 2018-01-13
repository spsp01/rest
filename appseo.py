from flask import Flask, request, render_template
from flask_restful import Resource, Api
import requests
from bs4 import BeautifulSoup

class CustomFlask(Flask):
  jinja_options = Flask.jinja_options.copy()
  jinja_options.update(dict(
    block_start_string='(%',
    block_end_string='%)',
    variable_start_string='((',
    variable_end_string='))',
    comment_start_string='(#',
    comment_end_string='#)',
  ))

app = CustomFlask(__name__)

api = Api(app)

#Main page
@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/titleinfo")
def titleinfo():
    return render_template('titleinfo.html')

@app.route("/querytest")
def querytest():
    return render_template('querytest.html')

@app.route("/pageinfo")
def pageinfo():
    return render_template('pageinfo.html')

@app.route("/descriptioninfo")
def descriptioninfo():
    return render_template('descriptioninfo.html')

@app.route("/h1info")
def h1info():
    return render_template('h1info.html')

@app.route("/canonicalinfo")
def canonicalinfo():
    return render_template('canonicalinfo.html')

@app.route("/linksinfo")
def linksinfo():
    return render_template('linksinfo.html')

def bs_req(url):
    result = requests.get(url)
    c = result.content
    soup = BeautifulSoup(c, "html5lib")
    return soup

def get_url(self):
    #get json from
    data = request.get_json()
    url = data['url']
    return url

def desc():
    pass

class H1(Resource):
    def get(self):
         return {'message': "Otrzymasz h1 po wysłaniu zapytania POST"}
    def post(self):
        url = get_url(self)
        soup = bs_req(url)
        h1=''
        if soup.select('h1') != []:
            h1 = soup.select('h1')[0].text.strip()
        h1_len = len(h1)
        return {'url': url, 'h1': h1, 'length': h1_len }

api.add_resource(H1, '/h1')
#Page title reader
class Title(Resource):
    def get(self):
         return {'message': "Otrzymasz tytuł strony po wysłaniu zapytania POST"}
    def post(self):
        url = get_url(self)
        soup = bs_req(url)
        title = str(soup.title.get_text())
        title_length = len(title)
        return {'url': url,'title' : title, 'length': title_length}

api.add_resource(Title, '/title')

#Page description reader
class Description(Resource):
    def get(self):
         return {'message': "Otrzymasz tytuł strony po wysłaniu zapytania POST"}
    def post(self):
        url = get_url(self)
        soup = bs_req(url)
        description = ''
        if soup.find_all(attrs={"name":"description"}) != []:
             description = str(soup.find_all(attrs={"name":"description"})[0]['content'])
        desc_length = len(description)
        return {'url': url, 'description': description, 'length': desc_length }

api.add_resource(Description, '/description')


#Page info
class Info(Resource):
    def get(self):
         return {'message': "Otrzymasz tytuł strony po wysłaniu zapytania POST"}
    def post(self):
        url = get_url(self)
        soup = bs_req(url)
        description = ''
        if soup.find_all(attrs={"name":"description"}) != []:
            description = str(soup.find_all(attrs={"name":"description"})[0]['content'])
        desc_length = len(description)
        title = str(soup.title.get_text())
        title_length = len(title)
        h1= ''
        if soup.select('h1') != []:
            h1 = soup.select('h1')[0].text.strip()
        canonical = ''
        if soup.findAll('link', rel='canonical') != []:
            canonical = str(soup.findAll('link', rel='canonical')[0]['href'])
        alink = soup.select('a')
        number_href_link =(len(alink))
        scripts = ''
        if  soup.select('script') != []:
            scripts = len(soup.select('script'))
        images = ''
        if soup.select('img') != []:
            images = len(soup.select('img'))

        print(images)

        return {'url': url,'title' : title, 'title-length': title_length, 'description': description,
                'desc-length': desc_length,'h1': h1, 'href links': number_href_link, 'canonical': canonical,
                'scripts': scripts, 'images': images }

api.add_resource(Info, '/info')


if __name__ == '__main__':
   app.run(debug=True)