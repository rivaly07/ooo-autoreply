"""Compose the auto-reply from explicit voice and structure fragments."""

from .fragments import ASK, COMEBACK, PLACE, RELIEF


def build_reply() -> str:
    return f"{PLACE[0]} {RELIEF[0]} {ASK[0]} {COMEBACK[0]}"
