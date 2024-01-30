import string

from aiogram.utils.markdown import hlink

from models import Event

event_template_text = '''
<b>$title</b>

Кол-во билетов: <b>$ticketCount</b>
Цена: <b>$ticketPrice</b>
Дата: <b>$ticketDate</b>

$buyTicket
'''


def format_event_date(event_date: str) -> str:
    # 2024-02-02T20:00:00.000+00:00
    month_names = [0,
                   'января',
                   'февраля',
                   'марта',
                   'апреля',
                   'мая',
                   'июня',
                   'июля',
                   'августа',
                   'сентября',
                   'октября',
                   'ноября',
                   'декабря']

    month_number = int(
        event_date.split('T')[0].split('-')[1]
    )
    day_number = int(
        event_date.split('T')[0].split('-')[-1]
    )
    hour_number = int(
        event_date.split('T')[1].split(':')[0]
    )
    minutes_number = int(
        event_date.split('T')[1].split(':')[1]
    )

    return f'{day_number:02d} {month_names[month_number]} в {hour_number:02d}:{minutes_number:02d}'


def get_event_template(event: dict) -> str:
    sales_stopped = event['salesStopped']

    import config
    template_values = {
        'title': event['title'],
        'ticketCount': 'Билетов нет' if sales_stopped else event['ticketCount'],
        'ticketPrice': 'Билетов нет' if sales_stopped else f'от {event["minPrice"]:0.0f} до {event["maxPrice"]:0.0f}',
        'ticketDate': format_event_date(event['beginDate']),
        'buyTicket': 'Билетов нет' if sales_stopped else hlink('Купить',
                                                               config.THEATRE_EVENT_URL + str(event["id"]))
    }
    return string.Template(event_template_text).safe_substitute(template_values)


def get_event_template_from_db(event: Event) -> str:
    sales_stopped = event.sales_stopped

    import config
    template_values = {
        'title': event.title,
        'ticketCount': 'Билетов нет' if sales_stopped else event.ticket_count,
        'ticketPrice': 'Билетов нет' if sales_stopped else f'от {event.min_price:0.0f} до {event.max_price:0.0f}',
        'ticketDate': event.begin_date,
        'buyTicket': 'Билетов нет' if sales_stopped else hlink('Купить',
                                                               config.THEATRE_EVENT_URL + str(event.event_id))
    }
    return string.Template(event_template_text).safe_substitute(template_values)
