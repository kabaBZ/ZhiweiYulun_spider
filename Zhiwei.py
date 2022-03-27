# coding:utf-8
import json
import requests
import copy

url = 'https://trends.zhiweidata.com/hotSearchTrend/search/keyWordSearch'
detail_url = 'https://trends.zhiweidata.com/hotSearchTrend/search/queryHotSearchTrend'
params = {
    "keyWord": "微软",
    "type":"weibo",
    "pageNumber":1
}
detail_params = {
    'name':'微软公布Office2021定价',
    'startTime': 0,
    'type':'weibo'
}
headers = {
    'Accept':'application/json, text/plain, */*',
    'Accept-Encoding':'gzip, deflate, br',
    'Accept-Language':'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Connection':'keep-alive',
    'Content-Length':'50',
    'Content-Type':'application/json;charset=UTF-8',
    'Cookie': 'JSESSIONID=802DCDF0609E1BD08A49FB1111780460; Hm_lvt_788fd773be4d685a7ab20271ceee31ab=1648300546; UM_distinctid=17fc65e5ad317-01e365e4444f0a-5617185b-1fa400-17fc65e5ad4ad8; CNZZDATA1278728418=2103552014-1648300545-%7C1648359152; Hm_lpvt_788fd773be4d685a7ab20271ceee31ab=1648364448',
    'Host':'trends.zhiweidata.com',
    'Origin':'https://trends.zhiweidata.com',
    'Referer':'https://trends.zhiweidata.com/seaResult?keyword=%E5%BE%AE%E8%BD%AF',
    'sec-ch-ua':'Not A;Brand";v="99", "Chromium";v="99", "Microsoft Edge";v="99',
    'sec-ch-ua-mobile':'?0',
    'sec-ch-ua-platform':'Windows',
    'Sec-Fetch-Dest':'empty',
    'Sec-Fetch-Mode':'cors',
    'Sec-Fetch-Site':'same-origin',
    'token':'eyJhbGciOiJIUzI1NiJ9.eyJ1aWQiOiJ0ZXN0dWlkIiwic3ViIjoie1wiY3JlYXRlX0F0XCI6MTY0ODMxNDE0NDU5NCxcImVudGVycHJpc2VcIjpmYWxzZSxcImZlbnNpXCI6MCxcImZpcnN0TG9naW5cIjowLFwiZ3VhbnpodVwiOjAsXCJpZFwiOlwiNjIzZjQ3MjBhOTI2ZTYwMDAxZjkxYTlmXCIsXCJpbnNpZGVcIjpmYWxzZSxcImxvY2F0aW9uXCI6XCLmnKrnn6XlnLDljLpcIixcImxvZ2luQnlMYXN0VGltZVwiOjE2NDgzMTQxNDQ2MDEsXCJwYXNzd29yZFwiOlwiQjE4OUM1QTMyNzE4NDY2QjI0QkU4QzdDMURDQ0MyQjlcIixcInBob25lXCI6XCIxODEwMDE3NjcyMVwiLFwicmVMaW1pdFwiOjUsXCJzZXhXQlwiOlwi5pyq55-l5oCn5YirXCIsXCJzdGFyXCI6MCxcInRhZ3NcIjpcIlwiLFwidXNlUHJvZHVjdFwiOltcInRyZW5kc1wiXSxcInVzZXJUeXBlXCI6XCJ0cmVuZFwiLFwidXNlcl9pbWdcIjpcIuacquefpeWktOWDj-WcsOWdgFwiLFwidXNlcm5hbWVcIjpcIuaJi-acuueUqOaItzE4MTAwMTc2NzIxXCIsXCJ2dHlwZVwiOi0zLFwid2VpZG91XCI6MH0iLCJ1c2VyX25hbWUiOiJqand0Iiwibmlja19uYW1lIjoiZWZ0b2tlbiIsImlzcyI6InpoaXdlaWRhdGEiLCJleHAiOjE2NDgzNjg3MTksImlhdCI6MTY0ODM2MTUxOSwianRpIjoiODAyRENERjA2MDlFMUJEMDhBNDlGQjExMTE3ODA0NjAifQ.8AdMyD0t5wRSFRm35gACAzkEJTGpixUxBAuHC6m8t2E',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36 Edg/99.0.1150.46'
}
detail_headers = {
    'Origin':'https://trends.zhiweidata.com',
    'Referer':'https://trends.zhiweidata.com/seaResult?keyword=%E5%BE%AE%E8%BD%AF',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36 Edg/99.0.1150.46',
    'Content-Type': 'application/json;charset=UTF-8',
    'Cookie': 'JSESSIONID=802DCDF0609E1BD08A49FB1111780460; Hm_lvt_788fd773be4d685a7ab20271ceee31ab=1648300546; UM_distinctid=17fc65e5ad317-01e365e4444f0a-5617185b-1fa400-17fc65e5ad4ad8; CNZZDATA1278728418=2103552014-1648300545-%7C1648359152; Hm_lpvt_788fd773be4d685a7ab20271ceee31ab=1648364448',
    'token': 'eyJhbGciOiJIUzI1NiJ9.eyJ1aWQiOiJ0ZXN0dWlkIiwic3ViIjoie1wiY3JlYXRlX0F0XCI6MTY0ODMxNDE0NDU5NCxcImVudGVycHJpc2VcIjpmYWxzZSxcImZlbnNpXCI6MCxcImZpcnN0TG9naW5cIjowLFwiZ3VhbnpodVwiOjAsXCJpZFwiOlwiNjIzZjQ3MjBhOTI2ZTYwMDAxZjkxYTlmXCIsXCJpbnNpZGVcIjpmYWxzZSxcImxvY2F0aW9uXCI6XCLmnKrnn6XlnLDljLpcIixcImxvZ2luQnlMYXN0VGltZVwiOjE2NDgzNjM1OTQ2OTUsXCJwYXNzd29yZFwiOlwiQjE4OUM1QTMyNzE4NDY2QjI0QkU4QzdDMURDQ0MyQjlcIixcInBob25lXCI6XCIxODEwMDE3NjcyMVwiLFwicmVMaW1pdFwiOjUsXCJzZXhXQlwiOlwi5pyq55-l5oCn5YirXCIsXCJzdGFyXCI6MCxcInRhZ3NcIjpcIua0u-i3g1wiLFwidXNlUHJvZHVjdFwiOltcInRyZW5kc1wiXSxcInVzZXJUeXBlXCI6XCJ0cmVuZFwiLFwidXNlcl9pbWdcIjpcIuacquefpeWktOWDj-WcsOWdgFwiLFwidXNlcm5hbWVcIjpcIuaJi-acuueUqOaItzE4MTAwMTc2NzIxXCIsXCJ2dHlwZVwiOi0zLFwid2VpZG91XCI6MH0iLCJ1c2VyX25hbWUiOiJqand0Iiwibmlja19uYW1lIjoiZWZ0b2tlbiIsImlzcyI6InpoaXdlaWRhdGEiLCJleHAiOjE2NDgzNzE2NDcsImlhdCI6MTY0ODM2NDQ0NywianRpIjoiODAyRENERjA2MDlFMUJEMDhBNDlGQjExMTE3ODA0NjAifQ.woDOrlz9mTGt5BrU22ZVIsfs7JfzmGBSKq4M8E9gptU'
}

data_dic = {}
data_list = []

def parse():
    response_data = requests.post(url = url ,headers = headers,data = json.dumps(params))
    response = response_data.json()
    for data in response['data']['data']:
        data_dic['name'] = data['name']
        data_dic['high_rank'] = data['highestRank']
        data_dic['duration'] = data['duration']/60
        data_dic['high_count'] = data['highestCount']
        startTime = data['startTime']
        detail_dic = parse_detail(data_dic['name'],startTime)
        data_dic['riseSpeed'] = detail_dic['riseSpeed']
        # data_dic['downText'] = detail_dic['downText'] #downText不是普遍属性
        data_dic['day'] = detail_dic['day']
        print(data_dic)
        data_list.append(copy.deepcopy(data_dic))
    print(data_list)


def parse_detail(name,startTime):
    dic = {}
    detail_params['name'] = name
    detail_params['startTime'] = startTime
    response_text = requests.post(url = detail_url ,headers=detail_headers,data = json.dumps(detail_params))
    response = response_text.json()
    riseSpeed = response['data']['riseSpeed']
    day = response['data']['data'][0]['day']
    dic['riseSpeed'] = riseSpeed
    dic['day'] = day
    return dic
parse()