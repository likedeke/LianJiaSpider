# - - - - - - - - - - - 
# @author like
# @since 2021-02-26 9:46
# @email 980650920@qq.com
# 配置文件
from matplotlib import font_manager

# 爬取多少页
SPIDER_PAGE_NUM = 10
# 启动多少线程
THREAD_COUNT = 15
# 保存路径
FILE_PATH = '..\\resource\\链家数据.csv'
# 保存文件的编码格式
FILE_ENCODING = 'gbk'
# 画图使用的中文字体
chFont = font_manager.FontProperties(family="SimHei")