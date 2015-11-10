import os
import re

import jinja2
import webapp2
import cgi

template_dir=os.path.join(os.path.dirname(__file__), 'templates')
jinja_env=jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir),
	autoescape=True)

# The root def first removes any duplicate consonant in the word, then it removes the vowels and lastly
# it concatenates the remaining consonants, which form the root of the word.
def root(word):
	removeDuplicates= re.sub(r'([a-z])\1+', r'\1', word)
	removeVowels= re.findall(r'[^aeiou]', removeDuplicates)
	if removeVowels[0]=='t' and removeVowels[-1]=='t':
		removeVowels=removeVowels[1:-1]
	result= ''.join(removeVowels).lower()
	return result
jinja_env.globals['root']=root

def render_str(template, **params):
		t=jinja_env.get_template(template)
		return t.render(params)

class Handler(webapp2.RequestHandler):
	def render(self, template, **kw):
		self.response.out.write(render_str(template, **kw))

	def write(self, *a, **kw):
		self.response.out.write(*a, **kw)




class rootForm(Handler):

    
    def get(self):
        items=self.request.get_all('word')
        self.render('root.html', items=items)
        
	


	
	


app = webapp2.WSGIApplication([('/root', rootForm),
			    ],
			    debug=True)
		
