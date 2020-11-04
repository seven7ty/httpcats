# -*- coding: utf-8 -*-

"""
MIT License

Copyright (c) 2020-2020 itsmewulf

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""

from enum import Enum
from requests import get

BASE_URL: str = "https://http.cat/"


class InvalidCat(ValueError):
    pass


class StatusCode(Enum):
    """:class:`Enum` representing all status codes in http.cat"""
    CONTINUE: int = 100
    SWITCHING_PROTOCOLS: int = 101
    PROCESSING: int = 102
    OK: int = 200
    SUCCESS: int = 200
    CREATED: int = 201
    ACCEPTED: int = 202
    NO_CONTENT: int = 204
    PARTIAL_CONTENT: int = 206
    MULTI_STATUS: int = 207
    MULTIPLE_CHOICES: int = 300
    MOVED_PERMANENTLY: int = 301
    FOUND: int = 302
    SEE_OTHER: int = 303
    NOT_MODIFIED: int = 304
    USE_PROXY: int = 305
    TEMPORARY_REDIRECT: int = 307
    BAD_REQUEST: int = 400
    UNAUTHORIZED: int = 401
    PAYMENT_REQUIRED: int = 402
    FORBIDDEN: int = 403
    NOT_FOUND: int = 404
    METHOD_NOT_ALLOWED: int = 405
    NOT_ACCEPTABLE: int = 406
    REQUEST_TIMEOUT: int = 408
    CONFLICT: int = 409
    GONE: int = 410
    LENGTH_REQUIRED: int = 411
    PRECONDITION_FAILED: int = 412
    PAYLOAD_TOO_LARGE: int = 413
    REQUEST_URI_TOO_LONG: int = 414
    UNSUPPORTED_MEDIA_TYPE: int = 415
    REQUEST_RANGE_NOT_SATISFIABLE: int = 416
    EXPECTATION_FAILED: int = 417
    IM_A_TEAPOT: int = 418
    ENHANCE_YOUR_CALM: int = 420
    MISDIRECTED_REQUEST: int = 421
    UNPROCESSABLE_ENTITY: int = 422
    LOCKED: int = 423
    FAILED_DEPENDENCY: int = 424
    UNORDERED_COLLECTION: int = 425
    UPGRADE_REQUIRED: int = 426
    TOO_MANY_REQUESTS: int = 429
    REQUEST_HEADER_FIELDS_TOO_LARGE: int = 431
    NO_RESPONSE: int = 444
    BLOCKED_BY_WINDOWS_PARENTAL_CONTROLS: int = 450
    UNAVAILABLE_FOR_LEGAL_REASONS: int = 451
    CLIENT_CLOSED_REQUEST: int = 499
    INTERNAL_SERVER_ERROR: int = 500
    NOT_IMPLEMENTED: int = 501
    BAD_GATEWAY: int = 502
    SERVICE_UNAVAILABLE: int = 503
    GATEWAY_TIMEOUT: int = 504
    VARIANT_ALSO_NEGOTIATES: int = 506
    INSUFFICIENT_STORAGE: int = 507
    LOOP_DETECTED: int = 508
    BANDWIDTH_LIMIT_EXCEEDED: int = 509
    NOT_EXTENDED: int = 510
    NETWORK_AUTHENTICATION_REQUIRED: int = 511
    NETWORK_CONNECT_TIMEOUT_ERROR: int = 599


class HTTPCat:
    """:class:`object` representing an HTTP Cat

    Attributes
    ------------
    code: :class:`int`
        Status Code associated with this :class:`HTTPCat`
    name: :class:`str`
        Status Code Name associated with this :class:`HTTPCat`
    url: :class:`str`
        The URL associated with this :class:`HTTPCat`
    image: :class:`bytes`
        The image bytes associated with this :class:`HTTPCat`
    """

    def __init__(self, code: int, name: str, url: str, image: bytes):
        self.code: int = code
        self.name: str = name
        self.url: str = url
        self.image: bytes = image

    def __int__(self) -> int:
        return self.code

    def __str__(self) -> str:
        return self.name

    def __bytes__(self) -> bytes:
        return self.image


def _make_valid_name(name: str) -> str:
    """Make a normal string into one that can be used to get an Enum

    Parameters
    -----------
    name: [:class:`str`]
        The status code name to make a valid :class:`StatusCode`

    Returns
    ---------
    :class:`str`
        The name that can be used to get a :class:`StatusCode`
    """

    return name.replace(" ", "_").upper()


def _pretty(name: str) -> str:
    """Make :class:`StatusCode` name pretty again

    Parameters
    -----------
    name: [:class:`str`]
        The status code name to make pretty

    Returns
    ---------
    :class:`str`
        The pretty name for the status code name given
    """

    return name.replace("_", " ").lower().title()


def cat_by_code(code: int) -> HTTPCat:
    """Get an HTTP Cat by status code

    Parameters
    -----------
    code: [:class:`int`]
        The status code to search for.

    Returns
    ---------
    :class:`HTTPCat`
        The HTTPCat object containing a name, code, URL and image bytes for the cat.
    """

    try:
        cat_enum: Enum = StatusCode(code)
        url: str = BASE_URL + str(cat_enum.value)
        return HTTPCat(int(code), _pretty(cat_enum.name), url, get(url).content)
    except ValueError:  # Couldn't get the status code
        raise InvalidCat(f"{code} is not a valid status code")


def cat_by_name(name: str) -> HTTPCat:
    """Get an HTTP Cat by status code name

    Parameters
    -----------
    name: [:class:`str`]
        The status code name to search for.

    Returns
    ---------
    :class:`HTTPCat`
        The HTTPCat object containing a name, code, URL and image bytes for the cat.
    """

    try:
        name: str = _make_valid_name(name)
        cat_enum: Enum = StatusCode[name]
        url: str = BASE_URL + str(cat_enum.value)
        return HTTPCat(cat_enum.value, _pretty(cat_enum.name), url, get(url).content)
    except ValueError:  # Couldn't get the status code name
        raise InvalidCat(f"{name} is not a valid status code name")
