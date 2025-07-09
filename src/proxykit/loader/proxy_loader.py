from enum import Enum

from proxykit.models import ProxyServer

from .internal_loader import _InternalProxyLoader


class ProxyDataFormat(Enum):
    JSON = "json"
    CSV = "csv"
    IP = "ip"
    CUSTOM = "custom"


class ProxyLoader:
    """
    ProxyLoader is a class that provides methods to load proxy data from various formats
    It supports JSON, CSV, IP formats and custom formats.
    """

    @staticmethod
    def load(
        source: str,
        format: ProxyDataFormat = ProxyDataFormat.JSON,
        key_mapping: dict[str, str] = {},
        entry: list[str] = [],
        token: str | None = None,
    ):
        """
        Load proxy data from the specified source in the given format.

        Args:
            source (str): The source of the proxy data (URL for remote access or local file path).
                 URLs must start with http or https.
            format (ProxyDataFormat): The format of the proxy data.
            key_mapping (dict[str, str]): Optional mapping of keys for parsing.
            entry (list[str]): Optional entry point for nested data structures.
            token (str | None): Optional token for authentication or access control.

        Returns:
            list: A list of parsed proxy server objects.
        """  # noqa: E501

        if source.startswith("http://") or source.startswith("https://"):
            _InternalProxyLoader.load_remote(
                url=source,
                format=format,
                key_mapping=key_mapping,
                entry=entry,
            )
        else:
            _InternalProxyLoader.load_local(
                path=source,
                format=format,
                key_mapping=key_mapping,
                entry=entry,
            )

    @staticmethod
    def custom_load(data: list[ProxyServer]):
        """
        Assuming data is already in the form of ProxyServer objects,
        data will be validated and then stored in the internal storage.
        """
        _InternalProxyLoader.validate_and_save_data(data)
