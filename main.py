import requests

def test_proxy(proxy):
    url = "http://www.google.com"
    ip, port, username, password = proxy.split(":")
    proxies = {
        "http": f"http://{username}:{password}@{ip}:{port}",
        "https": f"https://{username}:{password}@{ip}:{port}"
    }

    try:
        response = requests.get(url, proxies=proxies, timeout=5)
        return response.status_code
    except requests.RequestException as e:
        return str(e)

def main():
    with open("proxies.txt", "r") as file:
        proxies = [line.strip() for line in file.readlines()]

    for proxy in proxies:
        response_code = test_proxy(proxy)
        print(f"Proxy: {proxy}, Response Code: {response_code}")

if __name__ == "__main__":
    main()
