from __future__ import annotations

from enum import Enum


class CountryCode(str, Enum):
    US = "US"
    CA = "CA"
    GB = "GB"
    AU = "AU"
    DE = "DE"
    FR = "FR"


class MailType(str, Enum):
    usps_first_class = "usps_first_class"
    usps_standard = "usps_standard"


class PrintSpeed(str, Enum):
    core = "core"
    rapid = "rapid"


class PostcardSize(str, Enum):
    s4x6 = "4x6"
    s6x9 = "6x9"
    s6x11 = "6x11"


class RenderStatus(str, Enum):
    processed = "processed"
    rendered = "rendered"
    failed = "failed"
