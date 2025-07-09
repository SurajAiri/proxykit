# from proxykit.loader import ProxyLoader
# from proxykit.models import ProxyDataFormat
from proxykit.models import ProxyServer
from proxykit.storage import CacheManager


def main():
    """Main function to execute the script."""
    # path = "test.json"
    # path = "https://proxylist.geonode.com/api/proxy-list?protocols=http%2Chttps&limit=500&page=1&sort_by=lastChecked&sort_type=desc#"
    # path = "test.txt"
    # ProxyLoader.load(
    #     path,
    #     format=ProxyDataFormat.IP,
    #     entry=["data"],
    #     key_mapping={
    #         "anonymity": "anonymityLevel",
    #     },
    # )

    c1 = CacheManager()
    c2 = CacheManager(verbose=True)

    c1.append_proxies([ProxyServer("32.3242.342", 343)])
    c2.get_proxies()
    c1.clear_cache()


if __name__ == "__main__":
    main()

# 18
# 57.129.81.201:8080
# 51.81.245.3:17981
# 8.219.97.248:80
# 47.252.29.28:11222
# 198.199.86.11:8080
# 43.216.75.140:42761
# 161.35.70.249:8080
# 138.68.60.8:80
# 18.60.111.249:6698
# 8.222.17.214:1080
# 3.101.76.84:18242
# 193.151.141.17:8080
# 47.245.117.43:80
# 118.71.245.74:16000
# 116.203.139.209:5678
# 139.59.1.14:80
# 103.26.177.35:1080
# 103.180.118.207:7777


# 17
# 113.160.132.195:8080
# 57.129.81.201:8080
# 51.81.245.3:17981
# 176.126.103.194:44214
# 18.171.55.201:3128
# 198.199.86.11:8080
# 18.226.200.222:51568
# 200.174.198.86:8888
# 51.44.85.200:3128
# 161.35.70.249:8080
# 138.68.60.8:80
# 8.222.17.214:1080
# 209.97.150.167:8080
# 139.59.1.14:80
# 103.125.174.62:8080
# 128.199.202.122:8080
# 103.155.198.141:1080
