def decorator(func):
    def wrapper(*args, **kwargs):
        print("что то до вызова функции")
        result = func(*args, **kwargs)
        print("что то после вызова функции")
        return result
    return wrapper

@decorator
def hello():
    print("привет")

if __name__ == "__main__":
    hello()