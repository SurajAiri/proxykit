# from enum import Enum

# from proxykit.models import ProxyServer


# # todo: remove if not used later
# class DataFormat(Enum):
#     """
#     Enum for supported data formats.
#     """

#     JSON = "json"
#     CSV = "csv"
#     IP = "ip"


# class BaseProxyLoader:
#     """
#     Base class for loading proxy data from various sources.
#     Subclasses should implement the `load` method.
#     """

#     def load(self) -> list[ProxyServer]:
#         """
#         Load proxy data and return a list of ProxyServer objects.

#         Returns:
#             list: A list of ProxyServer objects.
#         """
#         raise NotImplementedError("Subclasses must implement this method.")
