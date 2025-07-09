# from proxykit.loader import ProxyLoader
# from proxykit.models import ProxyDataFormat
from proxykit import ProxyLoader, ProxyKit
from proxykit.models import ProxyDataFormat


def main():
    """Main function to execute the script."""
    # path = "test.json"
    # path = "https://proxylist.geonode.com/api/proxy-list?protocols=http%2Chttps&limit=500&page=1&sort_by=lastChecked&sort_type=desc#"
    # path = "test.txt"
    # ProxyKit.clear_all_data()

    # ProxyLoader.load(
    #     path,
    #     format=ProxyDataFormat.IP,
    #     entry=["data"],
    #     key_mapping={
    #         "anonymity": "anonymityLevel",
    #     },
    # )

    with ProxyKit() as pk:
        print(pk.get_random_proxy())


if __name__ == "__main__":
    main()
