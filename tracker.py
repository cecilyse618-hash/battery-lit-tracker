import argparse
import requests

parser = argparse.ArgumentParser(description="电池文献追踪工具")
parser.add_argument("keyword", help="搜索关键词")
parser.add_argument("--max", type=int, default=5, help="最多返回几条")
parser.add_argument("--days", type=int, default=30, help="只检索最近 N 天")
args = parser.parse_args()

# 关键词防坑：把 "lithium electrolyte" 变成 all:lithium+AND+all:electrolyte
words = args.keyword.split()
query = "+AND+".join("all:" + w for w in words)

# 拼网址
url = f"http://export.arxiv.org/api/query?search_query={query}&max_results={args.max}"

# 发请求
response = requests.get(url)
print(response.status_code)
print(response.text[:800])