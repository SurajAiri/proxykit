# from collections.abc import Iterable

# from proxykit.exceptions import InvalidProxyError
# from proxykit.models import ProxyServer

# from .base import BaseProxyParser

# class CsvProxyParser(BaseProxyParser):
#     """
#     Parses proxy data in CSV format.
#     """

#     def parse(self, data: Iterable) -> list[ProxyServer]:
#         """
#         Parse the given CSV data and return a list of ProxyServer objects.

#         Args:
#             data (Iterable): The raw proxy data in CSV format, where each item is a string in the format "host:port".

#         Returns:
#             list: A list of ProxyServer objects.
#         """
#         proxies = []
#         for value in data:
#             try:
#                 host, port = value.strip().split(':')
#                 server = ProxyServer(host=host, port=int(port))
#                 proxies.append(server)
#             except ValueError as e:
#                 raise InvalidProxyError(f"Invalid proxy format: {e}")
#         return proxies