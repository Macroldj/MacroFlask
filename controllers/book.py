import redis

# from controllers import books
#
#
# @books.route("/lidejin")
# def lidejin():
#     resp = ""
#     try:
#         resp = cache.RedisCache.get("lidejin")
#     except Exception as e:
#         print(e)
#     if resp:
#         return resp
#     else:
#         cache.set("lidejin","lidejin")
#         return "lidejin"