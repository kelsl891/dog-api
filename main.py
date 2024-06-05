from controler import Get_Dog
import webbrowser

dog_array = []
#opens link automaticaly
def open_link(link):
    webbrowser.open_new_tab(link)
while True:
    # calls the api
    dog = input("Do you want dog (Yes / No): ")
    if dog == "Yes":
        dog_object = Get_Dog()
        dog_link = dog_object.dog_function()
        open_link(dog_link)

        print(dog_link)
        # asks if the image should be added to the array
        good_dog = input("Do you like the dog?: ")
        if good_dog == "Yes":
            dog_array.append(dog_link)
    else:
        break
    # asks to veiw the array
    dog_list = input("Do you want to see the dog list?: ")
    if dog_list == "Yes":
        for i in dog_array:
            print(i)
