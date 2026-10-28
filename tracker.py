import argparse

parser=argparse.ArgumentParser(description="工具是干什么的")
parser.add_argument("keyword",help="搜索关键词")
parser.add_argument("--max",type=int,default=5,help="最多返回几条")
parser.add_argument("--days",type=int,default=30,help="自己写一句说人话的")
args=parser.parse_args()


print(args.keyword,args.max,args.days)