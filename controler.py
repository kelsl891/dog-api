import requests

class Get_Dog():
    #really cool comment
    def dog_function(self):
        url = "https://random.dog/woof.json"
        response = requests.get(url)
        # confirm that the api works
        if response.status_code == 200:
            posts = response.json()
            return posts['url']
        else:
            print("It failed")

dog = Get_Dog()
print(dog.dog_function())