from timeit import default_timer as timer


def timefunc(func):
    def wrapper(*args, **kwargs):
        start = timer()
        result = func(*args, **kwargs)
        end = timer()
        print(f'{func.__name__} took {end - start} seconds')
        return result
    return wrapper
