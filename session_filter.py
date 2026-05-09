from datetime import datetime


def is_active_session():

    hour = datetime.utcnow().hour

    # London session (7–11 UTC)
    london = 7 <= hour <= 11

    # New York session (13–17 UTC)
    newyork = 13 <= hour <= 17

    return london or newyork