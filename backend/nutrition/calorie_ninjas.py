import requests
from rest_framework.exceptions import APIException


class CalorieNinjas:
    api_key = "gu5caHWC9n+gYMGgKVD6wA==iroL1C8u1GVOMFNR"
    api_url = r"https://api.calorieninjas.com/v1/nutrition?query="

    @classmethod
    def get_nutrition_facts(cls, query: str):
        response = requests.get(cls.api_url + query, headers={"X-Api-Key": cls.api_key})
        if response.status_code == requests.codes.ok:
            return response.json().get('items')
        else:
            raise APIException(response.text)
