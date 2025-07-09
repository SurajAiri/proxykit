import httpx

from proxykit.exceptions import InvalidProxyError
from proxykit.loader.proxy_loader import ProxyDataFormat
from proxykit.models import ProxyServer
from proxykit.utils import parse_data


class _InternalProxyLoader:
    """
    This have implementation of loading proxy data from various formats, called from ProxyLoader class.
    """  # noqa: E501

    @staticmethod
    def load_local(
        path: str,
        format: ProxyDataFormat = ProxyDataFormat.IP,
        key_mapping: dict[str, str] = {},
        entry: list[str] = [],
    ):
        try:
            with open(path, "r") as f:
                data = f.readlines()

            values = parse_data(
                data,
                format,
                key_mapping=key_mapping,
                entry=entry,
            )

            _InternalProxyLoader.validate_and_save_data(values)

        except Exception as e:
            raise InvalidProxyError(f"Failed to load from path with {e}") from e

    @staticmethod
    def load_remote(
        url: str,
        format: ProxyDataFormat = ProxyDataFormat.IP,
        key_mapping: dict[str, str] = {},
        entry: list[str] = [],
    ):
        try:
            response = httpx.get(url)
            response.raise_for_status()
            data = response.text.splitlines()

            values = parse_data(
                data,
                format,
                key_mapping=key_mapping,
                entry=entry,
            )

            _InternalProxyLoader.validate_and_save_data(values)

        except httpx.HTTPError as e:
            raise InvalidProxyError(f"Failed to load from URL with {e}") from e

    @staticmethod
    def validate_and_save_data(data: list[ProxyServer]):
        """
        Assuming data is already in the form of ProxyServer objects,
        data will be validated and then stored in the internal storage.
        """
        if not isinstance(data, list) or not all(
            isinstance(d, ProxyServer) for d in data
        ):
            raise InvalidProxyError(
                "Invalid proxy data format. Expected a list of ProxyServer objects."
            )

        # Here you would implement the logic to save the validated data
        # to your internal storage.
        print("Data validated and ready to be saved:", data)
