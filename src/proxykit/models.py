from dataclasses import dataclass
from enum import Enum


class ProxyProtocol(Enum):
    HTTP = "http"
    HTTPS = "https"
    SOCKS4 = "socks4"
    SOCKS5 = "socks5"


class AnonymityLevel(Enum):
    ELITE = "elite"
    ANONYMOUS = "anonymous"
    TRANSPARENT = "transparent"
    UNKNOWN = "unknown"


class ProxyDataFormat(Enum):
    JSON = "json"
    CSV = "csv"
    IP = "ip"
    CUSTOM = "custom"


@dataclass
class ProxyServer:
    host: str
    port: int
    country: str | None = None
    latency: float | None = None
    username: str | None = None
    password: str | None = None
    protocol: ProxyProtocol = ProxyProtocol.HTTP
    # provider:str = "local"
    anonymity: AnonymityLevel = AnonymityLevel.UNKNOWN
    is_working: bool = True
