subscribers = dict()


def subscribe(event_name: str, fun):
    if not event_name in subscribers:
        subscribers[event_name] = []
    subscribers[event_name].append(fun)
    print(f'Subscribed to {event_name}')


def call_event(event_name, *args, **kwargs):
    if event_name not in subscribers:
        print(f'Event {event_name} does not exist.')
        return
    for fun in subscribers[event_name]:
        fun(*args, **kwargs)