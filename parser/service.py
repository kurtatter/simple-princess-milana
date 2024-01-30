from typing import List

import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime

import config
from models import Event

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine("sqlite:///" + config.THEATRE_DB_PATH)
Session = sessionmaker(bind=engine)
session = Session()


class TheatreParser:
    def __get_new_key(self):
        theatre15_text = requests.get(config.THEATRE_URL).text
        soup = BeautifulSoup(
            theatre15_text,
            'lxml'
        )

        buy_button = soup.find('a', {'class': 'red_button'}).first()
        return buy_button['data-radario-widget-key']

    def get_events_json(self) -> dict:
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
        return events_response.json()

    def save_to_file(self, filename: str = 'events') -> None:
        with open(filename+'.json', 'w') as file_json:
            json.dump(self.get_events_json(), file_json)

    def write_events_to_db(self) -> None:
        events: dict = self.get_events_json()['events']

        db_events = session.query(Event).all()
        revision_count = 0

        if len(db_events) > 0:
            last_event = db_events[-1]
            revision_count = last_event.revision + 1

        for event in events:
            session.add(Event(
                event_id=event.get('id'),
                title=event.get('title'),
                min_price=event.get('minPrice'),
                max_price=event.get('maxPrice'),
                ticket_count=event.get('ticketCount'),
                begin_date=datetime.strptime(event.get('beginDate'), '%Y-%m-%dT%H:%M:%S.%f%z'),
                end_date=datetime.strptime(event.get('endDate'), '%Y-%m-%dT%H:%M:%S.%f%z'),
                poster_image_url=event['posterImage']['url'],
                sales_stopped=event.get('salesStopped'),
                ended=event.get('ended'),
                revision=revision_count
            ))
        session.commit()

    def get_new_events(self) -> List:
        events: List[dict] = self.get_events_json()['events']
        db_events = session.query(Event).all()

        if len(db_events) > 0:
            last_revision_number = db_events[-1].revision
            last_events = session.query(Event).filter(Event.revision == last_revision_number).all()

            last_events_ids = set(
                [event.event_id for event in last_events]
            )

            new_events_ids = set(
                [event['id'] for event in events]
            )

            new_events = new_events_ids - last_events_ids
            new_events_from_db = []
            self.write_events_to_db()

            if len(new_events) > 0:
                for new_event_id in new_events:
                    new_events_from_db.append(
                        session.query(Event).filter(Event.event_id == new_event_id).first()
                    )
                return new_events_from_db
        self.write_events_to_db()
        return []

