import redis

# Redis Constraints
redis_host = "127.0.0.1"
redis_port = 6379
redis_password = ""

# Convert an HTTP request to string redis key
def convertRequestToString(method, url, params=None, data=None):

    strFinal = "[" + method + "]" + url
    if params is not None:
        strFinal += "|(params="
        for (key,value) in params.items():
            strFinal += "[" + str(key) + "/" + str(value) + "]"
        strFinal += ")"
    
    if data is not None and method != "GET":
        strFinal += "|(data="
        for (key,value) in data.items():
            strFinal += "[" + str(key) + "/" + str(value) + "]"
        strFinal += ")"

    return strFinal

# Get REDIS connection
def getRedisConnection():
    return redis.StrictRedis(
         host=redis_host
        ,port=redis_port
        ,password=redis_password
        ,decode_responses=True)
