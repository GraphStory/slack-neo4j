import web
#from graph import overview
#import requests

urls = (
    '/', 'index',
    '/slack', 'slack'
)

class index:
    def GET(self):
         return "Neo4j Slack Integration"

class slack:
    def POST(self):
         data = web.data()
         text = data["text"]
         print "text "+text
         command = text.split(" ")[0]
#         if (command == "") return  overview()
#         if (command == "import") return insert()
#         if (command == "cypher") return cypher(text[7:])
         return "It works: command: "+command

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()