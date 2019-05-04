import os
import re
import sys
dir_path = os.path.dirname(os.path.realpath(__file__))
idx = [m.start() for m in re.finditer('/', dir_path)]
sys.path.append(dir_path[0:idx[-1]])


from redis.client import Redis, StrictRedis
from redis.connection import (
    BlockingConnectionPool,
    ConnectionPool,
    Connection,
    SSLConnection,
    UnixDomainSocketConnection
)
from redis.utils import from_url
from redis.exceptions import (
    AuthenticationError,
    BusyLoadingError,
    ConnectionError,
    DataError,
    InvalidResponse,
    PubSubError,
    ReadOnlyError,
    RedisError,
    ResponseError,
    TimeoutError,
    WatchError
)


def int_or_str(value):
    try:
        return int(value)
    except ValueError:
        return value


__version__ = '3.2.1'
VERSION = tuple(map(int_or_str, __version__.split('.')))

__all__ = [
    'Redis', 'StrictRedis', 'ConnectionPool', 'BlockingConnectionPool',
    'Connection', 'SSLConnection', 'UnixDomainSocketConnection', 'from_url',
    'AuthenticationError', 'BusyLoadingError', 'ConnectionError', 'DataError',
    'InvalidResponse', 'PubSubError', 'ReadOnlyError', 'RedisError',
    'ResponseError', 'TimeoutError', 'WatchError'
]
