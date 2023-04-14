import settings

api_key = getattr(settings, "API_KEY")
print(api_key)
api_key = "abc"
print(api_key)

print(settings.API_KEY)
settings.API_KEY = "abc"
print(settings.API_KEY)

greeting_func = getattr(settings, "greeting")
greeting_func("Ali")