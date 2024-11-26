"""Models for responses of api/v1/vehicle-automatization/{vin}/departure/ endpoint."""

from dataclasses import dataclass, field
from datetime import datetime
from datetime import time as datetime_time

from mashumaro import field_options
from mashumaro.mixins.orjson import DataClassORJSONMixin

from .air_conditioning import TemperatureUnit, TimerMode
from .common import Weekday


@dataclass
class TargetTemperature(DataClassORJSONMixin):
    celsius: float | None = field(default=None, metadata=field_options(alias="celsius"))
    fahrenheit: float | None = field(default=None, metadata=field_options(alias="fahrenheit"))
    unit_in_car: TemperatureUnit = field(
        default=TemperatureUnit.CELSIUS, metadata=field_options(alias="unitInCar")
    )


@dataclass
class ChargingTime(DataClassORJSONMixin):
    """Information related to DepartureTimer."""

    id: int
    enabled: bool
    start_time: datetime_time | None = field(
        default=None, metadata=field_options(alias="startTime")
    )
    end_time: datetime_time | None = field(default=None, metadata=field_options(alias="endTime"))


@dataclass
class DepartureTimer(DataClassORJSONMixin):
    """Information related to DepartureTimer."""

    id: int
    enabled: bool
    charging: bool | None = field(default=None, metadata=field_options(alias="charging"))
    climatisation: bool | None = field(default=None, metadata=field_options(alias="climatisation"))
    preferred_charging_times: list[ChargingTime] | None = field(
        default=None, metadata=field_options(alias="preferredChargingTimes")
    )
    recurring_on: list[Weekday] | None = field(
        default=None, metadata=field_options(alias="recurringOn")
    )
    target_battery_state_of_charge_in_percent: int | None = field(
        default=None, metadata=field_options(alias="targetBatteryStateOfChargeInPercent")
    )
    time: datetime_time | None = field(default=None, metadata=field_options(alias="time"))
    type: TimerMode | None = field(default=None, metadata=field_options(alias="type"))


@dataclass
class DepartureInfo(DataClassORJSONMixin):
    """Information related to Departure."""

    car_captured_timestamp: datetime | None = field(
        default=None, metadata=field_options(alias="carCapturedTimestamp")
    )
    first_occurring_timer_id: int | None = field(
        default=None, metadata=field_options(alias="firstOccurringTimerId")
    )
    minimum_battery_state_of_charge_in_percent: int | None = field(
        default=None, metadata=field_options(alias="minimumBatteryStateOfChargeInPercent")
    )
    target_temperature: TargetTemperature | None = field(
        default=None, metadata=field_options(alias="targetTemperature")
    )
    timers: list[DepartureTimer] | None = field(
        default=None, metadata=field_options(alias="timers")
    )
