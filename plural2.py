import os
import re

import jinja2
import webapp2
import cgi

template_dir=os.path.join(os.path.dirname(__file__), 'templates')
jinja_env=jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir),
	autoescape=True)
	
# This the main function that analyses the input and returns the plural form.
# Please refer to the home page of the application for an explanation of plural formation in Kabyle.
def kaPlural (word):
  if word[0]=='a':
    word= 'i' + word[1:]+'en'
    return word
  elif word[0]=='t' and word[-1]=='t':
    word='ti'+word[2:-1]+'in'
    return word
  elif word in ['isem', 'izem', 'ilef', 'ixef', 'iger', 'ifer']:
    word=word[0:2]+word[-1:]+'awen'
    return word
jinja_env.globals['kaPlural']= kaPlural     

def render_str(template, **params):
		t=jinja_env.get_template(template)
		return t.render(params)

class Handler(webapp2.RequestHandler):
	def render(self, template, **kw):
		self.response.out.write(render_str(template, **kw))

	def write(self, *a, **kw):
		self.response.out.write(*a, **kw)

	
        


class PluralForm(Handler):

   

    def get(self):
        items=self.request.get_all('word')
        self.render('plural2.html', items=items)

class WelcomePage(Handler):
    def get(self):
        self.render('home.html')

app = webapp2.WSGIApplication([('/plural2', PluralForm),
			    ('/home', WelcomePage)],
			    debug=False)
		
#('/update', UpdateHandler)
