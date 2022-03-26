import requests

url = 'https://trends.zhiweidata.com/hotSearchTrend/search/keyWordSearch'
detail_url = 'https://trends.zhiweidata.com/hotSearchTrend/search/queryHotSearchTrend'
params = {
    'keyWord':' 微软',
    'pageNumber':' 1',
    'type':' weibo'
}
headers = {
    'Origin':' https://trends.zhiweidata.com',
    'Referer':' https://trends.zhiweidata.com/seaResult?keyword=%E5%BE%AE%E8%BD%AF',
    'User-Agent':' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36 Edg/99.0.1150.46'
}
response = requests.get(url = url ,headers=headers,params = params).json()
for data in response['data']['data']:
    name = data['name']
    high_rank = data['highestRank']
    duration = data['duration']/60
    high_count = data['highestCount']