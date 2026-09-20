import time
class ElapsedTimerFunction:
    def __call__(self,func):
        def wrapper(*args,**kwargs):
            start_time=time.time()
            func(*args ,**kwargs)
            end_time=time.time()

            print(f"Elapsed Timer result:{end_time - start_time} seconds")
            return func(*args , **kwargs)
        return wrapper
        

