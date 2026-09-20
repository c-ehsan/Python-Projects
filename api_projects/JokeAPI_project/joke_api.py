from base import Joke
import requests
from Elapsed_timer import ElapsedTimerFunction

elasped_time=ElapsedTimerFunction()
class JokeA(Joke):
    @elasped_time
    def __init__(self, link):
        super().__init__(link)
    def get_random_joke(self):
        request=requests.get(f"{self._link}")
        data=request.json()
        try:
            if data["type"]=="single":
                return {
                    "joke":data["joke"],
                    "answer":"",
                    "category":data["category"]
                }


            elif data["type"]=="twopart":
                return {
                    "joke":data["setup"],
                    "answer":data["delivery"],
                    "category":data["category"]
                }
        except KeyError as e:
            return f"Error:{str(e)}"
        

    


class JokeB(Joke):
    def __init__(self, link):
        super().__init__(link)
    @elasped_time
    def get_random_joke(self):
        request=requests.get(f"{self._link}")
        data=request.json()
        return f"Joke\n{data["joke"]} {data["answer"]}"
    
    


        
        


class JokeC(Joke):
    def __init__(self, link):
        super().__init__(link)
    @elasped_time
    def get_random_joke(self):
        request=requests.get(f"{self._link}")
        data=request.json()
        return f"Joke\n{data["joke"]} {data["answer"]}"


if __name__=="__main__":
    joke=JokeB(link=f"http://127.0.0.1:5000/joke_api_persian")
    print(joke.get_random_joke())