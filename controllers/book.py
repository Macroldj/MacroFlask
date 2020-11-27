from controllers import books
from models.book import Book
from ulits import myCache


@books.route("/test")
def test():
    resp = ""
    try:
        resp = myCache.get("test")
    except Exception as e:
        print(e)
    if resp:
        return resp
    else:
        myCache.set("test", "test")
        return "test"
