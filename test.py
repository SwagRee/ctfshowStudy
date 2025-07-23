import requests
from bs4 import BeautifulSoup
import re

# 爬虫模板
def scrape_website(url):
    try:
        # 发送HTTP请求获取网页内容
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # 检查是否有请求错误

        # 解析HTML内容
        soup = BeautifulSoup(response.text, 'html.parser')

        # 示例：提取标题
        title = soup.title.string if soup.title else "No title found"
        print(f"Title: {title}")

        # 示例：提取所有链接
        links = [a['href'] for a in soup.find_all('a', href=True)]
        # print(f"Found {len(links)} links.")
        specific_div = soup.find('div', {'id': 'dataCollectionId', 'class': 'position-filter-type'})
        #
        specific_div = soup.find('div', { 'class': 'position-filter-type'})
        if specific_div:
            # 在特定的div中找到所有的a标签
            a_tags = specific_div.find_all('a')
            for a_tag in a_tags:
                # 打印a标签的href属性，即链接
                city = a_tag.get('href')
                city = city.replace("https://wz.ganji.com/", "").replace("job/","").replace("/","")


                print(city)
        else:
            print("没有找到特定的div")
        # for link in links:
        #     if link.startswith('https://wz.ganji.com/'):
        #         print(f"{link.replace("https://wz.ganji.com/","").replace("/job","")}")
        # for link in links:
        #     print(link)

        # 提取以 <div class="title" 开头的元素
        title_divs = soup.find_all('div', class_=re.compile(r'^title'))
        print(f"Found {len(title_divs)} <div class='title'> elements.")
        for title_div in title_divs:
            original_text = title_div.text.strip()  # 原始文本
            modified_text = original_text.replace("title", "")  # 将“有限公司”替换为空
            # print(modified_text)
        # 打印并提取内容
        # for div in title_divs:
        #     print(div.text.strip())

        # 返回爬取的数据
        return {
            "title": title,
            "links": links,
            "title_divs_texts": [div.text.strip() for div in title_divs]
        }
    except requests.exceptions.RequestException as e:
        # print(f"Request failed: {e}")
        return None


if __name__ == "__main__":
    # 替换为你要爬取的网址
    website_url = "https://wz.ganji.com/longgangshi/job/"
    data = scrape_website(website_url)
    if data:
        print("Scraping completed successfully.")
