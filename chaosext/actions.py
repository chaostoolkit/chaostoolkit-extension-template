# -*- coding: utf-8 -*-
from chaoslib.types import Configuration, Secrets

__all__ = ["empty_action"]


def empty_action(
    configuration: Configuration = None, secrets: Secrets = None
) -> None:
    return None
