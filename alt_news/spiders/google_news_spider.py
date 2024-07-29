import scrapy
import json
from scrapy.selector import Selector

class AltNewsSpiderSpider(scrapy.Spider):
    name = "google_news_spider"
    start_urls = ["https://www.altnews.in/"]

    start_urls = ['https://www.altnews.in/']

    headers = {
        "Host": "www.altnews.in",
        "Connection": "keep-alive",
        "sec-ch-ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
        "Accept": "*/*",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "X-Requested-With": "XMLHttpRequest",
        "sec-ch-ua-mobile": "?0",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
        "sec-ch-ua-platform": "'Windows'",
        "Origin": "https://www.altnews.in",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://www.altnews.in/",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "en-US,en;q=0.9",
    }

    post_not_in = ""

    def start_requests(self):
        body_content =  f"action=wp_post_blocks%2Fget_block_data&security=42af3cf506&args%5Bpost_type%5D=post&args%5Bcategory__not_in%5D%5B%5D=121&args%5Btag__not_in%5D%5B%5D=693&args%5Bposts_per_page%5D=2&args%5Border%5D=DESC&args%5Borderby%5D=date{self.post_not_in}&settings%5Bblock_id%5D=pbs-6685461fe1119&settings%5Btitle%5D=Recent+Posts&settings%5Bclass%5D=pbs+pbs-dual+post-blocks&settings%5Binfo%5D=byline-alt&settings%5Binfo_above%5D=date&settings%5Bthumb_cat%5D=true&settings%5Bexcerpt_length%5D=30&settings%5Bsmall_title%5D=true&settings%5Bnavigation%5D=infinite_scroll&settings%5Bthumb_style%5D=default&settings%5Bwrapper%5D=section&settings%5Btime_period%5D=default&settings%5Badvanced_orderby%5D=default&settings%5Bfilter_by%5D=none&settings%5Buid%5D=pbs-6685461fe1119&settings%5Breact%5D=post_block_dual&settings%5Bnonce%5D=42af3cf506"
        body = (
            body_content
        )
        yield scrapy.Request("https://www.altnews.in/?wp_pbs_ajaxify=1", method="POST", headers=self.headers,body=body, callback=self.parse)

    def parse(self, response):
        self.log(f"Response status: {response.status}")
        if response.status != 200:
            return
        
        try:
            data = json.loads(response.body)

            ids = data.get("ids", [])

            html_content = data.get("html", "")
            html_selector = Selector(text=html_content)
            images_urls = []
            for id in ids:
                post = html_selector.xpath(f"//article[contains(@class, 'post-{id}')]")

                self.log(post.xpath(".//time/@datetime").extract_first())
                self.log(post.xpath(".//h4/a/@href").extract_first())
                self.log(post.xpath(".//h4/a/text()").extract_first())
                self.log(post.xpath(".//span[contains(@class,'author')]/a/text()").extract_first())
                images_urls.append(post.xpath(".//div[contains(@class,'thumb-w')]/img/@src").extract()[-1])
                self.log(images_urls)
                
            yield {
                'image_urls' : images_urls
            }

           
        except json.JSONDecodeError as e:
            self.log(f"Failed to parse JSON: {e}")


