from flask import session, redirect
from functools import wraps

def require_login(func):
    @wraps(func) 
    def wrap(*args, **kwargs): 
        if "username" in session:
            print('aa')
            print(session['username'])
            return func(*args, **kwargs)  
        else:
            print('a')
            return redirect('/login')
    return wrap