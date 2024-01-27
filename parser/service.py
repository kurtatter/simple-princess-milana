import requests
from bs4 import BeautifulSoup
import json

import config


class TheatreParser:
    def __get_new_key(self):
        theatre15_text = requests.get(config.THEATRE_URL).text
        soup = BeautifulSoup(
            theatre15_text,
            'lxml'
        )

        buy_button = soup.find('a', {'class': 'red_button'}).first()
        return buy_button['data-radario-widget-key']

    def get_events(self) -> dict:
        data = {
            'key': config.RADARIO_QUERY_KEY,
            'page': 0,
            'pageSize': 1000,
            'allowEventGrouping': False
        }
        events_response = requests.get(
            config.RADARIO_QUERY_URL,
            data
        )
        if events_response.status_code == 404:
            data['key'] = self.__get_new_key()
            events_response = requests.get(
                config.RADARIO_QUERY_URL,
                data
            )
        print(events_response.json())
        return events_response.json()

    def save_to_file(self, filename: str = 'events') -> None:
        with open(filename+'.json', 'w') as file_json:
            json.dump(self.get_events(), file_json)


TheatreParser().get_events()
