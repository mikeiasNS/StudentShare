import web
import json
from teste import restaurants
          
urls = (
	'/raimundo', 'hello'
)
app = web.application(urls, globals())
  
class hello:        
    def GET(self):
        return restaurants()
  
if __name__ == "__main__":
	app.run()