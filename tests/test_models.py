import pytest
from sqlalchemy import create_engine
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.pool import StaticPool

from mid_way.database import Base
from mid_way.models import Event, EventParticipant, GuestUser, TravelMode


@pytest.fixture
def session() -> Session:
    engine = create_engine(
        "sqlite://",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
    Base.metadata.create_all(bind=engine)
    testing_session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    with testing_session() as session:
        yield session

    Base.metadata.drop_all(bind=engine)


def test_creates_guest_organizer(session: Session) -> None:
    organizer = GuestUser(display_name="Giovanni")

    session.add(organizer)
    session.commit()
    session.refresh(organizer)

    assert organizer.id is not None
    assert organizer.public_id
    assert organizer.display_name == "Giovanni"
    assert organizer.created_at is not None
    assert organizer.updated_at is not None


def test_creates_event_owned_by_guest(session: Session) -> None:
    organizer = GuestUser(display_name="Giovanni")
    event = Event(
        name="Saturday lunch",
        city_or_area="Milan",
        place_category="restaurant",
        organizer=organizer,
    )

    session.add(event)
    session.commit()
    session.refresh(event)

    assert event.id is not None
    assert event.public_id
    assert event.organizer == organizer
    assert organizer.organized_events == [event]


def test_creates_participant_for_event_and_guest(session: Session) -> None:
    organizer = GuestUser(display_name="Organizer")
    participant_user = GuestUser(display_name="Friend")
    event = Event(name="Coffee", organizer=organizer)
    participant = EventParticipant(
        event=event,
        guest_user=participant_user,
        starting_location_label="Milano Centrale",
        starting_latitude=45.4863,
        starting_longitude=9.2035,
        travel_mode=TravelMode.PUBLIC_TRANSPORT,
    )

    session.add_all([event, participant])
    session.commit()
    session.refresh(participant)

    assert participant.id is not None
    assert participant.event == event
    assert participant.guest_user == participant_user
    assert participant.travel_mode == TravelMode.PUBLIC_TRANSPORT
    assert event.participants == [participant]
    assert participant_user.participations == [participant]


def test_prevents_duplicate_participant_for_same_event_and_guest(session: Session) -> None:
    organizer = GuestUser(display_name="Organizer")
    participant_user = GuestUser(display_name="Friend")
    event = Event(name="Coffee", organizer=organizer)
    first_participant = EventParticipant(
        event=event,
        guest_user=participant_user,
        starting_location_label="Milano Centrale",
        travel_mode=TravelMode.BIKE,
    )
    duplicate_participant = EventParticipant(
        event=event,
        guest_user=participant_user,
        starting_location_label="Porta Garibaldi",
        travel_mode=TravelMode.WALKING,
    )

    session.add_all([first_participant, duplicate_participant])

    with pytest.raises(IntegrityError):
        session.commit()


def test_generated_public_ids_are_non_empty_and_unique(session: Session) -> None:
    users = [GuestUser(display_name=f"User {index}") for index in range(10)]
    events = [Event(name=f"Event {index}", organizer=users[index]) for index in range(10)]

    session.add_all(events)
    session.commit()

    user_public_ids = {user.public_id for user in users}
    event_public_ids = {event.public_id for event in events}

    assert len(user_public_ids) == len(users)
    assert len(event_public_ids) == len(events)
    assert all(user_public_ids)
    assert all(event_public_ids)


def test_travel_modes_exclude_metro() -> None:
    assert [travel_mode.value for travel_mode in TravelMode] == [
        "walking",
        "bike",
        "public_transport",
        "car",
    ]
