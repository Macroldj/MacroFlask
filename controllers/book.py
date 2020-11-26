from controllers import books
from models.book import Book
from ulits import myCache


@books.route("/lidejin")
def lidejin():
    resp = ""
    try:
        resp = myCache.get("lidejin")
    except Exception as e:
        print(e)
    if resp:
        return resp
    else:
        myCache.set("lidejin","lidejin")
        return "lidejin"