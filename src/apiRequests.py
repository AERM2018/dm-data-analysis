import requests
import serializers
def getImports():
    res = requests.get("http://localhost:3000/api/imports")
    return serializers.serializeImports(res.content)
