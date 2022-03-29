# timer-decorator
Example decorator that times a function

This was useful:

<https://realpython.com/python-timer/#a-python-timer-decorator>

Sometimes, decorated functions must have correct metadata. @functools.wraps fixes exactly this issue.


Note that the wrapped function will now keep its proper name, even after being decorated. It’s good form to use @functools.wraps whenever you define a decorator. A blueprint that you can use for most of your decorators is the following:

```python
import functools

def decorator(func):
    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        # Do something before
        value = func(*args, **kwargs)
        # Do something after
        return value
    return wrapper_decorator
```

