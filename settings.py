SQL = {
    'host': 'xx.xx.xx.xx',
    'user': 'xxx',
    'password': 'xxx',
    'database': 'yhd',
    'charset': 'utf8'
}
table_name = 'items_table'

url_index = 'mbname-b/a-s1-v4-p{}-price-d0-f0b-m1-rt0-pid-mid0-color-size-k/'
url_item = 'https://item.yhd.com/{}.html'
url_score = 'https://item.yhd.com/squ/comment/getFuzzyProductCommentSummarys.do?productId={}&callback=experienceCountAndRateCallback'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
}

class1_dict = {'生鲜': 'https:http://search.yhd.com/c12218-0-0', '饮料': 'https://search.yhd.com/c0-0-1003766/',
               '酒类': 'https://search.yhd.com/c0-0-1003646/', '休闲零食': 'https://search.yhd.com/c0-0-1003327/',
               '粮油干货': 'https://search.yhd.com/c0-0-1004912/', '厨房调料': 'https://search.yhd.com/c0-0-1003339/',
               '饼干糕点': 'https://search.yhd.com/c0-0-1003746/', '牛奶乳品': 'https://search.yhd.com/c0-0-1003847/',
               '茶冲咖啡': 'https://search.yhd.com/c0-0-1003801/', '肉蛋海鲜': 'https://search.yhd.com/c0-0-1008414/',
               '新鲜蔬果': 'https://search.yhd.com/c0-0-1008407/', '方便速食': 'https://search.yhd.com/c0-0-1003553/',
               '乳品速食': 'https://search.yhd.com/c0-0-1004802/', '母婴': 'https:https://search.yhd.com/c1319-0-0',
               '玩具': 'https://search.yhd.com/c6233-0-0', '童装': 'https:http://search.yhd.com/c11842-0-0',
               '奶粉': 'https:https://search.yhd.com/c1523-0-0', '营养辅食': 'https:https://search.yhd.com/c1524-0-0',
               '尿裤湿巾': 'https:https://search.yhd.com/c1525-0-0', '洗护用品': 'https:https://search.yhd.com/c1527-0-0',
               '喂养用品': 'https:https://search.yhd.com/c1526-0-0', '妈妈专区': 'https://search.yhd.com/c4997-0-0',
               '寝具服饰': 'https://search.yhd.com/c6313-0-0', '童车童床': 'https://search.yhd.com/c1528-0-0',
               '乐器': 'https://search.yhd.com/c6291-0-0', '童装/童鞋': 'https://search.yhd.com/c0-0-1007405',
               '纸巾': 'https:http://search.yhd.com/c1671-0-0', '厨卫清洁': 'https:http://sale.yhd.com/act/8zwSJDcQ0gLT.html',
               '宠物': 'https:http://search.yhd.com/c6994-0-0', '纸品湿巾': 'https://search.yhd.com/c0-0-1003297/',
               '衣物清洁': 'https://search.yhd.com/c0-0-1003313/', '家庭清洁': 'https://search.yhd.com/c0-0-1003309/',
               '清洁用具': 'https://search.yhd.com/c1667-0-0', '驱虫除湿': 'https://search.yhd.com/c0-0-1004868/',
               '皮具护理': 'https://search.yhd.com/c0-0-1005419/', '宠物生活': 'https://search.yhd.com/c0-0-1004415/',
               '绿植园艺': 'https://search.yhd.com/c0-0-1006020/', '厨具': 'https:http://search.yhd.com/c0-0-1003989/',
               '家具': 'https:http://search.yhd.com/c0-0-1004247/', '床上用品': 'https://search.yhd.com/c15249-0-0',
               '生活日用': 'https://search.yhd.com/c1624-0-0',
               '锅具水具': 'https://search.yhd.com/c0-0/k%25E9%2594%2585%25E5%2585%25B7%25E6%25B0%25B4%25E5%2585%25B7/',
               '厨具刀具': 'https://search.yhd.com/c0-0/k%25E5%258E%25A8%25E5%2585%25B7%25E5%2588%2580%25E5%2585%25B7/',
               '茶具餐具': 'https://search.yhd.com/c0-0/k%25E8%258C%25B6%25E5%2585%25B7%25E9%25A4%2590%25E5%2585%25B7/',
               '家装软饰': 'https://search.yhd.com/c11158-0-0', '品质家具': 'https://search.yhd.com/c9847-0-0',
               '家装建材': 'https://search.yhd.com/c9855-0-0', '美妆': 'https:https://search.yhd.com/c1316-0-0',
               '个人清洁': 'https:http://search.yhd.com/c16750-0-0', '美发护发': 'https://search.yhd.com/c0-0-1003626/',
               '女性护理': 'https://search.yhd.com/c0-0-1003628/', '沐浴清洁': 'https://search.yhd.com/c0-0-1003624/',
               '口腔护理': 'https://search.yhd.com/c0-0-1003627/', '面部护理': 'https://search.yhd.com/c0-0-1003615/',
               '缤纷彩妆': 'https://search.yhd.com/c0-0-1003616/', '身体护理': 'https://search.yhd.com/c0-0-1003631/',
               '男士护理': 'https://search.yhd.com/c0-0-1003629/', '美容工具': 'https://search.yhd.com/c0-0-1003617/',
               '女装': 'https:http://search.yhd.com/c0-0/k%25E5%25A5%25B3%25E8%25A3%2585/',
               '男装': 'https:http://search.yhd.com/c0-0/k%25E7%2594%25B7%25E8%25A3%2585/',
               '内衣': 'https:http://search.yhd.com/c0-0/k%25E5%2586%2585%25E8%25A1%25A3/',
               '珠宝': 'https:http://search.yhd.com/c6144-0-0',
               '时尚裙装': 'https://search.yhd.com/c0-0/k%25E6%2597%25B6%25E5%25B0%259A%25E8%25A3%2599%25E8%25A3%2585/',
               '女士上衣': 'https://search.yhd.com/c0-0/k%25E5%25A5%25B3%25E5%25A3%25AB%25E4%25B8%258A%25E8%25A1%25A3/',
               '女士裤子': 'https://search.yhd.com/c0-0/k%25E5%25A5%25B3%25E5%25A3%25AB%25E8%25A3%25A4%25E5%25AD%2590/',
               '品质内衣': 'https://search.yhd.com/c1345-0-0', '型格男装': 'https://search.yhd.com/c1342-0-0',
               '珠宝首饰': 'https://search.yhd.com/c6144-0-0', '钟表/眼镜': 'https://search.yhd.com/c0-0-1004183/',
               '鞋靴': 'https:http://search.yhd.com/c11729-0-0', '箱包': 'https:http://search.yhd.com/c1672-0-0',
               '运动户外': 'https:http://search.yhd.com/c1318-0-0', '时尚女鞋': 'https://search.yhd.com/c11731-0-0',
               '潮流女包': 'https://search.yhd.com/c2575-0-0', '奢侈大牌': 'https://search.yhd.com/c2615-0-0',
               '功能箱包': 'https://search.yhd.com/c2577-0-0', '品质男鞋': 'https://search.yhd.com/c11730-0-0',
               '精品男包': 'https://search.yhd.com/c2576-0-0', '运动鞋服': 'https://search.yhd.com/c0-0-1003953/',
               '健身器材': 'https://search.yhd.com/c1463-0-0', '户外装备': 'https://search.yhd.com/c1318-0-0/',
               '手机': 'https://search.yhd.com/c0-0-1005412/', '数码': 'https:http://search.yhd.com/c652-0-0',
               '电脑办公': 'https:http://search.yhd.com/c670-0-0', '手机配件': 'https://search.yhd.com/c0-0-1004136/',
               '摄影影像': 'https://search.yhd.com/c0-0-1004268/', '影音电教': 'https://search.yhd.com/c0-0-1004357/',
               '智能设备': 'https://search.yhd.com/c0-0-1004388/', '数码配件': 'https://search.yhd.com/c0-0-1004304/',
               '电脑整机': 'https://search.yhd.com/c0-0-1003312/', '网络外设': 'https://search.yhd.com/c0-0-1003329/',
               '办公设备': 'https://search.yhd.com/c0-0-1003407/', '汽车用品': 'https:http://search.yhd.com/c6728-0-0',
               '厨房小电': 'https://search.yhd.com/c0-0-1004270/', '生活电器': 'https://search.yhd.com/c0-0-1004301/',
               '个护健康': 'https://search.yhd.com/c0-0-1004354/', '电视空调': 'https://search.yhd.com/c0-0-1005509/',
               '厨卫大电': 'https://search.yhd.com/c0-0-1004806/', '冰箱': 'https://search.yhd.com/c0-0-1004239/',
               '洗衣机': 'https://search.yhd.com/c0-0-1004241/', '维修保养': 'https://search.yhd.com/c0-0-1005430/',
               '汽车装饰': 'https://search.yhd.com/c6745-0-0', '车载产品': 'https://search.yhd.com/c0-0-1005437/',
               '家用器械': 'https://search.yhd.com/c0-0-1004717/', '隐形眼镜': 'https://search.yhd.com/c0-0-1004406/',
               '图书': 'https:http://search.yhd.com/c1713-0-0', '少儿': 'https://search.yhd.com/c3263-0-0',
               '教育': 'https://search.yhd.com/c0-0-1004443/', '文艺': 'https://search.yhd.com/c0-0-1004591/',
               '经管励志': 'https://search.yhd.com/c0-0-1004470/', '人文社科': 'https://search.yhd.com/c0-0-1004641/',
               '生活': 'https://search.yhd.com/c0-0-1004637/', '科技': 'https://search.yhd.com/c0-0-1004627/',
               '刊/原版': 'https://search.yhd.com/c0-0-1004490/', '音像': 'https://search.yhd.com/c4053-0-0/'}

item_obj = {
    'uid': None,  # 爬虫id
    'skuId': None,  # 商品id
    'title': None,  # 标题
    'money': None,  # 价格
    'class1': None,  # 一级分类
    'class2': None,  # 二级分类
    'class3': None,  # 三级分类
    'shop': None,  # 店铺
    'averageScore': None,  # 平均分
    'sales': None,  # 销售量
    'goodCount': None,  # 好评数
    'generalCount': None,  # 中评数
    'poorCount': None,  # 差评数
    'url': None,  # url
}
