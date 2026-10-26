from datetime import UTC, datetime
from enum import StrEnum
from secrets import token_urlsafe

from sqlalchemy import DateTime, Enum, Float, ForeignKey, String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from mid_way.database import Base


def utc_now() -> datetime:
    return datetime.now(UTC)


def generate_public_id() -> str:
    return token_urlsafe(16)


class TravelMode(StrEnum):
    WALKING = "walking"
    BIKE = "bike"
    PUBLIC_TRANSPORT = "public_transport"
    CAR = "car"


class TimestampMixin:
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=utc_now,
        nullable=False,
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=utc_now,
        onupdate=utc_now,
        nullable=False,
    )


class GuestUser(TimestampMixin, Base):
    __tablename__ = "guest_users"

    id: Mapped[int] = mapped_column(primary_key=True)
    public_id: Mapped[str] = mapped_column(
        String(32),
        default=generate_public_id,
        unique=True,
        nullable=False,
        index=True,
    )
    display_name: Mapped[str | None] = mapped_column(String(100))

    organized_events: Mapped[list["Event"]] = relationship(
        back_populates="organizer",
        cascade="all, delete-orphan",
    )
    participations: Mapped[list["EventParticipant"]] = relationship(
        back_populates="guest_user",
        cascade="all, delete-orphan",
    )


class Event(TimestampMixin, Base):
    __tablename__ = "events"

    id: Mapped[int] = mapped_column(primary_key=True)
    public_id: Mapped[str] = mapped_column(
        String(32),
        default=generate_public_id,
        unique=True,
        nullable=False,
        index=True,
    )
    name: Mapped[str] = mapped_column(String(200), nullable=False)
    scheduled_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    city_or_area: Mapped[str | None] = mapped_column(String(200))
    place_category: Mapped[str | None] = mapped_column(String(100))
    organizer_id: Mapped[int] = mapped_column(ForeignKey("guest_users.id"), nullable=False)

    organizer: Mapped[GuestUser] = relationship(back_populates="organized_events")
    participants: Mapped[list["EventParticipant"]] = relationship(
        back_populates="event",
        cascade="all, delete-orphan",
    )


class EventParticipant(TimestampMixin, Base):
    __tablename__ = "event_participants"
    __table_args__ = (
        UniqueConstraint("event_id", "guest_user_id", name="uq_event_participant_guest"),
    )

    id: Mapped[int] = mapped_column(primary_key=True)
    event_id: Mapped[int] = mapped_column(ForeignKey("events.id"), nullable=False)
    guest_user_id: Mapped[int] = mapped_column(ForeignKey("guest_users.id"), nullable=False)
    starting_location_label: Mapped[str] = mapped_column(String(300), nullable=False)
    starting_latitude: Mapped[float | None] = mapped_column(Float)
    starting_longitude: Mapped[float | None] = mapped_column(Float)
    travel_mode: Mapped[TravelMode] = mapped_column(
        Enum(TravelMode, values_callable=lambda enum_type: [item.value for item in enum_type]),
        nullable=False,
    )

    event: Mapped[Event] = relationship(back_populates="participants")
    guest_user: Mapped[GuestUser] = relationship(back_populates="participations")
