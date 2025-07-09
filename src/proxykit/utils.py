# utils/key_mapping.py


from proxykit.exceptions import InvalidProxyError
from proxykit.loader.proxy_loader import ProxyDataFormat
from proxykit.models import ProxyServer
from proxykit.parser.csv_parser import CsvProxyParser
from proxykit.parser.ip_parser import IpProxyParser
from proxykit.parser.json_parser import JsonProxyParser


def extract_keys(key_mapping: dict[str, str] = {}) -> dict[str, str]:
    """
    Normalize key mapping with default fallbacks.
    """
    if key_mapping is None:
        key_mapping = {}

    return {
        "ip": key_mapping.get("ip", "ip"),
        "port": key_mapping.get("port", "port"),
        "protocol": key_mapping.get("protocol", "protocol"),
        "anonymity": key_mapping.get("anonymity", "anonymity"),
        "username": key_mapping.get("username", "username"),
        "password": key_mapping.get("password", "password"),
        "country": key_mapping.get("country", "country"),
        "latency": key_mapping.get("latency", "latency"),
        "is_working": key_mapping.get("is_working", "is_working"),
    }


def parse_data(
    data: list[str],
    format: ProxyDataFormat,
    key_mapping: dict[str, str] = {},
    entry: list[str] = [],
) -> list[ProxyServer]:
    if format == ProxyDataFormat.IP:
        return IpProxyParser.parse("\n".join(data))
    if format == ProxyDataFormat.JSON:
        return JsonProxyParser.parse("".join(data), key_mapping, entry)
    if format == ProxyDataFormat.CSV:
        return CsvProxyParser.parse("\n".join(data), key_mapping)
    raise InvalidProxyError("Invalid use of Custom ProxyDataFormat")
