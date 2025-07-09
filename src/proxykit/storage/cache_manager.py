import random

from proxykit.models import ProxyServer

from .appdirs_manager import AppDirsManager


class CacheManager:
    def __init__(self):
        self.cache = {}

    def get_proxies(self) -> list[ProxyServer]:
        """
        Get the cached proxies.
        Returns:
            dict: The cached proxies.
        """
        return self.cache.get("proxies", [])

    def get_random_proxy(self) -> ProxyServer | None:
        """
        Get a random proxy from the cache.
        Returns:
            ProxyServer | None: A random proxy if available, otherwise None.
        """
        if not self.cache.get("proxies"):
            return None
        return random.choice(self.cache["proxies"])

    def append_proxies(self, proxies: list[ProxyServer]):
        """
        Append proxies to the cache.
        Args:
            proxies (list[ProxyServer]): The list of proxies to append.
        """
        # don't append duplicates
        self.cache["proxies"] = self.cache.get("proxies", []) + proxies

    def save_proxies(self):
        """
        Save the cached proxies to the appdirs cache.
        """
        AppDirsManager.save_data({"proxies": self.get_proxies()}, "proxies.json")

    def load_proxies(self):
        """
        Load the cached proxies from the appdirs cache.
        """
        data = AppDirsManager.load_cached_data("proxies.json")
        self.cache["proxies"] = data.get("proxies", [])

    def clear_cache(self):
        """
        Clear the cache.
        """
        self.cache = {}
        AppDirsManager.remove_cached_data("proxies.json")

    def delete_proxy(self, proxy: ProxyServer):
        """
        Delete a specific proxy from the cache.
        Args:
            proxy (ProxyServer): The proxy to delete.
        """
        self.cache["proxies"] = [p for p in self.cache.get("proxies", []) if p != proxy]
        self.save_proxies()
