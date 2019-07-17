import utils
import request

# Verify if already have cache saved in REDIS
def verifyCache(method, url, parameters=None, data=None):
    print("[LOG] Verify Cache")
    try:
        redisConn = utils.getRedisConnection()
        keyCache = utils.convertRequestToString(method, url, parameters, data)
        
        if redisConn.exists(keyCache):
            return getCache(redisConn, method, url, parameters, data)
        else:
            return setCache(redisConn, method, url, parameters, data)
        
    except Exception as ex:
        print(ex)


# Get existing cache in REDIS
def getCache(redisConn, method, url, parameters=None, data=None):
    print("[LOG] Get existing Cache")
    try:
        keyCache = utils.convertRequestToString(method, url, parameters, data)
        print("[LOG] Redis KEY: " + keyCache)
        return redisConn.get(str(keyCache))
    except Exception as ex:
        print(ex)


# Set new cache in REDIS
def setCache(redisConn, method, url, parameters=None, data=None):
    print("[LOG] Set new Cache")
    try:
        json = callRequest(method, url, parameters, data)
        keyCache = utils.convertRequestToString(method, url, parameters, data)
        print("[LOG] Redis KEY: " + keyCache)
        redisConn.set(str(keyCache), str(json))
        redisConn.expire(keyCache, time=20)
        return redisConn.get(str(keyCache))
    except Exception as ex:
        print(ex)
    

# Choice HTTP Method to call
def callRequest(method, url, parameters=None, data=None):
    choice = switchMethod(method)
    if choice == 2:
        return str(request.post(url, parameters, data))
    elif choice == 3:
        return str(request.put(url, parameters, data))
    elif choice == 4:
        return str(request.patch(url, parameters, data))
    elif choice == 5:
        return str(request.delete(url, parameters, data))
    else:
        return str(request.get(url, parameters))


# Default method is GET
def switchMethod(argument):
    switcher = {
        1: "GET",
        2: "POST",
        3: "PUT",
        4: "PATCH",
        5: "DELETE"
    }
    return switcher.get(argument, 1)
