import threading
import time
import spacy


class CreateResponse:
    '''
    this class will create a response for the user response given to it using
    detecity and ml_detectcity functions.
    '''

    def detectcity(self, user_response, city_list):
        detected_cities = list()
        # time.sleep(1)
        user_response_words = user_response.split(" ")
        for word in user_response_words:
            if word.lower() in city_list:
                detected_cities.append(word.lower())
                print("CITY DETECTED")
        if not len(detected_cities):
            for city in city_list:
                if city.lower() in user_response.lower():
                    print("CITY DETECTED")
                    if city.lower() not in detected_cities:
                        detected_cities.append(city.lower())

        if not len(detected_cities):
            print("City not found, using ml for detecting")
            response = self.ml_detectcity(user_response, city_list, detected_cities)
            print(response)

        else:
            print(detected_cities)

    def ml_detectcity(self, user_response, city_list, detected_cities):
        nlp = spacy.load('en_core_web_lg')
        extract_places = nlp(user_response)

        for ent in extract_places.ents:
            if ent.label_ == "GPE":
                # if ent.text.lower() in city_list:
                #     print(ent.text)
                detected_cities.append(ent.text.lower())
        return detected_cities


    def __init__(self, response, city_list):
        thread_fun = threading.Thread(target=self.detectcity(response, city_list))
        thread_fun.start()


# response ="Iliveinjalgaon"
# response =
response = "I live in Jaipur"

city_list = ["jalgaon", "mumbai", "Nagpur","PUNE"]

CreateResponse(response, city_list)
# CreateResponse(response, city_list)
# CreateResponse(response, city_list)
# CreateResponse(response, city_list)

