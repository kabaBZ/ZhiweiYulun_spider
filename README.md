# ZhiweiYulun
 知微舆论场关键字搜索爬虫练习

post请求中总是会遇到提交的data json格式不正确服务器返回400错误

需要对data进行json.dumps()处理

headers中的cookie并没有登录功能

登录状态在headers中的token键值中，如不登录只能查看五次数据

