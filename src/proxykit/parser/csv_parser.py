import csv
from io import StringIO

from proxykit.exceptions import InvalidProxyError
from src.proxykit.models import AnonymityLevel, ProxyProtocol, ProxyServer

from .base import BaseProxyParser


class CsvProxyParser(BaseProxyParser):
    """
    Parses proxy data in CSV format.
    Expected CSV headers: host, port, [ protocol, country, latency, username, password, provider, anonymity, is_working ](optional)
    Only 'host' and 'port' are required.
    """  # noqa: E501

    def parse(self, data: str) -> list:
        proxy_servers = []
        reader = csv.DictReader(StringIO(data))

        for row in reader:
            try:
                server = ProxyServer(
                    host=row["host"].strip(),
                    port=int(row["port"]),
                    protocol=ProxyProtocol(row.get("protocol", "http")),
                    latency=float(row["latency"]) if row.get("latency") else None,
                    country=row.get("country"),
                    username=row.get("username"),
                    password=row.get("password"),
                    # provider=row.get('provider', 'local'),
                    anonymity=AnonymityLevel(row.get("anonymity", "unknown")),
                    is_working=row.get("is_working", "True").lower() == "true",
                )
                proxy_servers.append(server)
            except KeyError as e:
                raise InvalidProxyError(f"Missing required field: {e}") from e
            except ValueError as ve:
                raise InvalidProxyError(
                    f"Invalid value in proxy CSV row: {row}"
                ) from ve

        return proxy_servers
