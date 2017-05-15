import requests
import json
import time
url = 'http://weibo.com/aj/message/add?ajwvr=6'
headers = {
	'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.22 Safari/537.36 SE 2.X MetaSr 1.0',
'Referer':'http://weibo.com/message/history?uid=2186989853&name=ROY_zhc',
	'Cookie':'SINAGLOBAL=7760669112226.401.1481772111468; UM_distinctid=15aa349569f19-0c778aad0b69cb-414a0229-100200-15aa34956a0ac; wb_publish_fist100_3210522890=1; TC-V5-G0=6fd5dedc9d0f894fec342d051b79679e; SCF=AjVnYn5w5MVRKBChxLVFcVRWP9YlRAZbNSb6l1VItKaZUPR09LuXEUpFfur0pa5tscPx-kXVs6LPyUuRhpvQtKg.; SUB=_2A250F7r6DeRhGeVM6lIU8izEwjyIHXVXZKsyrDV8PUNbmtAKLUv3kW95PZMAv25aOsQYoLVmMRpT4EIEeQ..; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WhQMFyM94ynlSl9JBZenkS15JpX5KMhUgL.FoeEeK5feozR1K52dJLoI7D8MJLoIEfeKX4G; SUHB=0YhRkWbZguwv8S; ALF=1526005289; SSOLoginState=1494469290; _s_tentry=login.sina.com.cn; Apache=6183013138093.139.1494469353621; ULV=1494469353701:116:7:4:6183013138093.139.1494469353621:1494382437762; TC-Page-G0=4e714161a27175839f5a8e7411c8b98c; UOR=,,news.ifeng.com; TC-Ugrow-G0=e66b2e50a7e7f417f6cc12eec600f517; wvr=6'
}

#uid_list=['5984587131', '1958558130', '2950425052', '5540137231', '3176834701', '1888373567', '5947276567', '5928035261', '1909360484', '1713926427', '1974658370', '3616320471', '2610803413', '6032191682', '5998047873', '5672878948']
with open('uid.txt','r') as f:
	for i in f:
		data = {
		'location':'msgdialog',
		'module':'msgissue',
		'style_id':'1',
		'text':'''亲，马上到母亲节了，咱们可以根据节日配合您的活动专题做一个推广物料或者推广活动，比如：母亲节特惠，等这种物料或者活动，有需要我帮助的可以联系我''',
		'uid':i.strip(),
		'tovfids':'',
		'fids':'',
		'el':'[object HTMLDivElement]',
		'_t:0':'0'
		}
		try:
			res = requests.post(url,data,headers=headers)
			a = json.loads(res.text)['msg']
			if '恭喜' in a:
				print(a)
			else:
				print(a + i)
		except Exception as e:
			print(e,i)


