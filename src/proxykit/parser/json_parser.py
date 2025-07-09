import json
from collections.abc import Iterable

from proxykit.exceptions import InvalidProxyError
from proxykit.models import AnonymityLevel, ProxyProtocol, ProxyServer

from .base import BaseProxyParser


class JsonProxyParser(BaseProxyParser):
    """
    Parses proxy data in JSON format.
    """

    # todo: flexibly handle little change in key names in json data
    def parse(self, data: str) -> list[ProxyServer]:
        """
        Parse the given JSON data and return a list of ProxyServer objects.

        Args:
            data (str): The raw proxy data in JSON format, where each item is a dictionary containing proxy details.

        Returns:
            list: A list of ProxyServer objects.

        """  # noqa: E501
        val: dict = json.loads(data) if isinstance(data, str) else data
        proxy_servers = []

        for proxy in val:
            try:
                if "ip" in proxy and ":" in proxy["ip"]:
                    host = proxy["ip"].split(":")[0]
                    port = int(proxy["ip"].split(":")[1])
                else:
                    host = proxy["ip"]
                    port = int(proxy["port"])

                server = ProxyServer(
                    host=host,
                    port=port,
                    country=proxy.get("country"),
                    latency=proxy.get("latency"),
                    username=proxy.get("username"),
                    password=proxy.get("password"),
                    # provider=proxy.get('provider', 'local'),
                    protocol=ProxyProtocol(proxy.get("protocol", "http")),
                    anonymity=AnonymityLevel(proxy.get("anonymity", "unknown")),
                    is_working=proxy.get("is_working", True),
                )
                proxy_servers.append(server)
            except KeyError as e:
                # raise ValueError(f"Missing required field: {e}")
                raise InvalidProxyError(f"Missing required field: {e}") from e

        return proxy_servers
