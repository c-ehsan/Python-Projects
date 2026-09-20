from flask import Flask , render_template,jsonify
import json
import random
import requests
from joke_api import JokeA
class Server:
    def __init__(self):
        self.app=Flask(__name__)
        self.online_joke=JokeA(link="https://v2.jokeapi.dev/joke/any")



    def create_relative_route(self):
        @self.app.route("/")
        def home_page():
            return render_template("index.html")

        @self.app.route("/joke_Random_api")
        def create_random_joke_api():
            data=self.online_joke.get_random_joke()
            return jsonify(data)
           
                    
            
        @self.app.route("/joke_api_programming")
        def create_jokeapi_programming():
            with open("JokeDataProgramming.json","r",encoding="utf-8") as f:
                jokes=json.load(f)

            joke=random.choice(jokes)
            return jsonify(joke)

        @self.app.route("/joke_api_persian")
        def create_jokeapi_persian():
            with open("JokeDataFarsi.json","r",encoding="utf-8") as f:
                jokes=json.load(f)

            joke=random.choice(jokes)
            return jsonify(joke)
        


        
        


    def run(self):
        self.app.run("0.0.0.0",port=5000)
        


if __name__=="__main__":
    server=Server()
    server.create_relative_route()
    server.run()
