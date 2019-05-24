from icrawler.builtin import BaiduImageCrawler 
from icrawler.builtin import GreedyImageCrawler

def baiduCatch(keyword):
    # 爬取google图片上相应关键词的图片
    """
    parser_threads：解析器线程数目，最大为cpu数目
    downloader_threads：下载线程数目，最大为cpu数目
    storage：存储地址，使用字典格式。key为root_dir
    keyword:浏览器搜索框输入的关键词
    max_num:最大下载图片数目
    """

    baidu_storage = {'root_dir':'images/'+keyword}
    baidu_crawler = BaiduImageCrawler(parser_threads=4,
                                        downloader_threads=4,
                                        storage=baidu_storage)
                
    baidu_crawler.crawl(keyword=keyword,max_num=1000)


def normalCatch(url):
    # 爬取普通网站上的图片
    storage= {'images'}
    greedy_crawler = GreedyImageCrawler(storage=storage)
    greedy_crawler.crawl(domains=url, 
                        max_num=1000)

            
if __name__ == "__main__":
    names = ["杨紫","郑爽","王俊凯","罗云熙"]
    for name in names:
        baiduCatch(name)