import cacheController

#################################################################################
# URL    |  https://ptsv2.com is a site to create Get/Post test servers easily  #
# you can change JSON from server here: https://ptsv2.com/t/2mdha-1563080296    #
#                                                                               #
# params |  is a optional parameters to send in request                         #
# data   |  is a optional data to send in request                               #
# method |  can be "GET", "POST", "PUT", "PATCH" OR "DELETE". "GET" is default  #
#################################################################################

url = "https://ptsv2.com/t/2mdha-1563080296/post"

params = {'parameter1':'value1', 'parameter2':'value2'}
data = {'data1': True}
method = "GET"

result = cacheController.verifyCache("GET", url, params, data)

print("\n * Result from request:\n \t " + result + "\n")
