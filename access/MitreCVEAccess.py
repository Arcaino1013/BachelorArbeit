import requests


def search_nvd(keyword):
    url = f"https://services.nvd.nist.gov/rest/json/cves/2.0?keywordSearch={keyword}&resultsPerPage=5"
    headers = {
        "Accept": "application/json"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None


if __name__ == "__main__":
    keyword = "html"
    data = search_nvd(keyword)

    if data:
        for vuln in data.get('vulnerabilities', []):
            cve = vuln['cve']
            print(f"{cve['id']} - {cve['descriptions'][0]['value']}")
