# -*- coding: utf-8 -*-
from chaoslib.types import Configuration, Secrets

__all__ = ["empty_probe"]


def empty_probe(
    configuration: Configuration = None, secrets: Secrets = None
) -> bool:
    return True
