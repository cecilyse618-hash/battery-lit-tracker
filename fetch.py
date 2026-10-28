import requests
response = requests.get("http://export.arxiv.org/api/query?search_query=all:lithium+AND+all:electrolyte&max_results=2")

print(response.status_code)
print(response.text)

response.text[:300]
