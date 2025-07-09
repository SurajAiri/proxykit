# from proxykit.models import ProxyServer
# from proxykit.parser.base import BaseProxyParser

# from .base import BaseProxyLoader


# class LocalProxyLoader(BaseProxyLoader):
#     """
#     Loads proxy data from a local file.
#     """

#     def __init__(self, file_path: str, parser: BaseProxyParser):
#         """
#         Initialize the LocalProxyLoader with a file path and a parser.

#         Args:
#             file_path (str): The path to the local file containing proxy data.
#             parser (BaseProxyParser): An instance of a parser that implements the parse method.
#         """  # noqa: E501
#         self.file_path = file_path
#         self.parser = parser

#     def load(self) -> list[ProxyServer]:
#         """
#         Load proxy data from the local file and return a list of ProxyServer objects.

#         Returns:
#             list: A list of ProxyServer objects.
#         """
#         with open(self.file_path, "r") as file:
#             data = self.parser.parse(file.read())

#         print(data)
#         return data
