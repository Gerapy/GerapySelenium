# Gerapy Selenium

This is a package for supporting selenium in Scrapy, also this
package is a module in [Gerapy](https://github.com/Gerapy/Gerapy).

## Installation

```shell script
pip3 install gerapy-selenium
```

## Usage

You can use `SeleniumRequest` to specify a request which uses selenium to render.

For example:

```python
yield SeleniumRequest(detail_url, callback=self.parse_detail)
```

And you also need to enable `SeleniumMiddleware` in `DOWNLOADER_MIDDLEWARES`:

```python
DOWNLOADER_MIDDLEWARES = {
    'gerapy_selenium.downloadermiddlewares.SeleniumMiddleware': 543,
}
```

Congratulate, you've finished the all of the required configuration.

If you run the Spider again, Selenium will be started to render every
web page which you configured the request as SeleniumRequest.

## Settings

GerapySelenium provides some optional settings.

### Concurrency 

You can directly use Scrapy's setting to set Concurrency of Selenium,
for example:

```python
CONCURRENT_REQUESTS = 3
```

### Pretend as Real Browser

Some website will detect WebDriver or Headless, GerapySelenium can 
pretend Chromium by inject scripts. This is enabled by default.

You can close it if website does not detect WebDriver to speed up:

```python
GERAPY_SELENIUM_PRETEND = False
```

Also you can use `pretend` attribute in `SeleniumRequest` to overwrite this 
configuration.

### Logging Level

By default, Selenium will log all the debug messages, so GerapySelenium
configured the logging level of Selenium to WARNING.

If you want to see more logs from Selenium, you can change the this setting: 

```python
import logging
GERAPY_SELENIUM_LOGGING_LEVEL = logging.DEBUG
```

### Download Timeout

Selenium may take some time to render the required web page, you can also change this setting, default is `30s`:

```python
# selenium timeout
GERAPY_SELENIUM_DOWNLOAD_TIMEOUT = 30
```

### Headless

By default, Selenium is running in `Headless` mode, you can also 
change it to `False` as you need, default is `True`:

```python
GERAPY_SELENIUM_HEADLESS = False 
```

### Window Size

You can also set the width and height of Selenium window:

```python
GERAPY_SELENIUM_WINDOW_WIDTH = 1400
GERAPY_SELENIUM_WINDOW_HEIGHT = 700
```

Default is 1400, 700.

## SeleniumRequest

`SeleniumRequest` provide args which can override global settings above.

* url: request url
* callback: callback
* wait_for: wait for some element to load, also supports dict
* script: script to execute
* proxy: use proxy for this time, like `http://x.x.x.x:x`
* sleep: time to sleep after loaded, override `GERAPY_SELENIUM_SLEEP`
* timeout: load timeout, override `GERAPY_SELENIUM_DOWNLOAD_TIMEOUT`
* pretend: pretend as normal browser, override `GERAPY_SELENIUM_PRETEND`
* screenshot: ignored resource types, see
        https://miyakogi.github.io/selenium/_modules/selenium/page.html#Page.screenshot,
        override `GERAPY_SELENIUM_SCREENSHOT`

For example, you can configure SeleniumRequest as:

```python
from gerapy_selenium import SeleniumRequest

def parse(self, response):
    yield SeleniumRequest(url, 
        callback=self.parse_detail,
        wait_for='title',
        script='() => { console.log(document) }',
        sleep=2)
```

Then Selenium will:
* wait for title to load
* execute `console.log(document)` script
* sleep for 2s
* return the rendered web page content

## Example

For more detail, please see [example](./example).

Also you can directly run with Docker:

```
docker run germey/gerapy-selenium-example
```

Outputs:

```shell script
2020-07-13 01:49:13 [scrapy.utils.log] INFO: Scrapy 2.2.0 started (bot: example)
2020-07-13 01:49:13 [scrapy.utils.log] INFO: Versions: lxml 4.3.3.0, libxml2 2.9.9, cssselect 1.1.0, parsel 1.6.0, w3lib 1.22.0, Twisted 20.3.0, Python 3.7.7 (default, May  6 2020, 04:59:01) - [Clang 4.0.1 (tags/RELEASE_401/final)], pyOpenSSL 19.1.0 (OpenSSL 1.1.1d  10 Sep 2019), cryptography 2.8, Platform Darwin-19.4.0-x86_64-i386-64bit
2020-07-13 01:49:13 [scrapy.utils.log] DEBUG: Using reactor: twisted.internet.asyncioreactor.AsyncioSelectorReactor
2020-07-13 01:49:13 [scrapy.crawler] INFO: Overridden settings:
{'BOT_NAME': 'example',
 'CONCURRENT_REQUESTS': 3,
 'NEWSPIDER_MODULE': 'example.spiders',
 'RETRY_HTTP_CODES': [403, 500, 502, 503, 504],
 'SPIDER_MODULES': ['example.spiders']}
2020-07-13 01:49:13 [scrapy.extensions.telnet] INFO: Telnet Password: 83c276fb41754bd0
2020-07-13 01:49:13 [scrapy.middleware] INFO: Enabled extensions:
['scrapy.extensions.corestats.CoreStats',
 'scrapy.extensions.telnet.TelnetConsole',
 'scrapy.extensions.memusage.MemoryUsage',
 'scrapy.extensions.logstats.LogStats']
2020-07-13 01:49:13 [scrapy.middleware] INFO: Enabled downloader middlewares:
['scrapy.downloadermiddlewares.httpauth.HttpAuthMiddleware',
 'scrapy.downloadermiddlewares.downloadtimeout.DownloadTimeoutMiddleware',
 'scrapy.downloadermiddlewares.defaultheaders.DefaultHeadersMiddleware',
 'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware',
 'gerapy_selenium.downloadermiddlewares.SeleniumMiddleware',
 'scrapy.downloadermiddlewares.retry.RetryMiddleware',
 'scrapy.downloadermiddlewares.redirect.MetaRefreshMiddleware',
 'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware',
 'scrapy.downloadermiddlewares.redirect.RedirectMiddleware',
 'scrapy.downloadermiddlewares.cookies.CookiesMiddleware',
 'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware',
 'scrapy.downloadermiddlewares.stats.DownloaderStats']
2020-07-13 01:49:13 [scrapy.middleware] INFO: Enabled spider middlewares:
['scrapy.spidermiddlewares.httperror.HttpErrorMiddleware',
 'scrapy.spidermiddlewares.offsite.OffsiteMiddleware',
 'scrapy.spidermiddlewares.referer.RefererMiddleware',
 'scrapy.spidermiddlewares.urllength.UrlLengthMiddleware',
 'scrapy.spidermiddlewares.depth.DepthMiddleware']
2020-07-13 01:49:13 [scrapy.middleware] INFO: Enabled item pipelines:
[]
2020-07-13 01:49:13 [scrapy.core.engine] INFO: Spider opened
2020-07-13 01:49:13 [scrapy.extensions.logstats] INFO: Crawled 0 pages (at 0 pages/min), scraped 0 items (at 0 items/min)
2020-07-13 01:49:13 [scrapy.extensions.telnet] INFO: Telnet console listening on 127.0.0.1:6023
2020-07-13 01:49:13 [example.spiders.book] INFO: crawling https://dynamic5.scrape.center/page/1
2020-07-13 01:49:13 [gerapy.selenium] DEBUG: processing request <GET https://dynamic5.scrape.center/page/1>
2020-07-13 01:49:13 [gerapy.selenium] DEBUG: set options {'headless': True, 'dumpio': False, 'devtools': False, 'args': ['--window-size=1400,700', '--disable-extensions', '--hide-scrollbars', '--mute-audio', '--no-sandbox', '--disable-setuid-sandbox', '--disable-gpu']}
2020-07-13 01:49:14 [gerapy.selenium] DEBUG: crawling https://dynamic5.scrape.center/page/1
2020-07-13 01:49:19 [gerapy.selenium] DEBUG: waiting for .item .name finished
2020-07-13 01:49:20 [gerapy.selenium] DEBUG: wait for .item .name finished
2020-07-13 01:49:20 [gerapy.selenium] DEBUG: close selenium
2020-07-13 01:49:20 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://dynamic5.scrape.center/page/1> (referer: None)
2020-07-13 01:49:20 [gerapy.selenium] DEBUG: processing request <GET https://dynamic5.scrape.center/detail/26898909>
2020-07-13 01:49:20 [gerapy.selenium] DEBUG: processing request <GET https://dynamic5.scrape.center/detail/26861389>
2020-07-13 01:49:20 [gerapy.selenium] DEBUG: processing request <GET https://dynamic5.scrape.center/detail/26855315>
2020-07-13 01:49:20 [gerapy.selenium] DEBUG: set options {'headless': True, 'dumpio': False, 'devtools': False, 'args': ['--window-size=1400,700', '--disable-extensions', '--hide-scrollbars', '--mute-audio', '--no-sandbox', '--disable-setuid-sandbox', '--disable-gpu']}
2020-07-13 01:49:20 [gerapy.selenium] DEBUG: set options {'headless': True, 'dumpio': False, 'devtools': False, 'args': ['--window-size=1400,700', '--disable-extensions', '--hide-scrollbars', '--mute-audio', '--no-sandbox', '--disable-setuid-sandbox', '--disable-gpu']}
2020-07-13 01:49:21 [gerapy.selenium] DEBUG: set options {'headless': True, 'dumpio': False, 'devtools': False, 'args': ['--window-size=1400,700', '--disable-extensions', '--hide-scrollbars', '--mute-audio', '--no-sandbox', '--disable-setuid-sandbox', '--disable-gpu']}
2020-07-13 01:49:21 [gerapy.selenium] DEBUG: crawling https://dynamic5.scrape.center/detail/26855315
2020-07-13 01:49:21 [gerapy.selenium] DEBUG: crawling https://dynamic5.scrape.center/detail/26861389
2020-07-13 01:49:21 [gerapy.selenium] DEBUG: crawling https://dynamic5.scrape.center/detail/26898909
2020-07-13 01:49:24 [gerapy.selenium] DEBUG: waiting for .item .name finished
2020-07-13 01:49:24 [gerapy.selenium] DEBUG: wait for .item .name finished
2020-07-13 01:49:24 [gerapy.selenium] DEBUG: close selenium
2020-07-13 01:49:24 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://dynamic5.scrape.center/detail/26861389> (referer: https://dynamic5.scrape.center/page/1)
2020-07-13 01:49:24 [gerapy.selenium] DEBUG: processing request <GET https://dynamic5.scrape.center/page/2>
2020-07-13 01:49:24 [gerapy.selenium] DEBUG: set options {'headless': True, 'dumpio': False, 'devtools': False, 'args': ['--window-size=1400,700', '--disable-extensions', '--hide-scrollbars', '--mute-audio', '--no-sandbox', '--disable-setuid-sandbox', '--disable-gpu']}
2020-07-13 01:49:25 [scrapy.core.scraper] DEBUG: Scraped from <200 https://dynamic5.scrape.center/detail/26861389>
{'name': '壁穴ヘブンホール',
 'score': '5.6',
 'tags': ['BL漫画', '小基漫', 'BL', '『又腐又基』', 'BLコミック']}
2020-07-13 01:49:25 [gerapy.selenium] DEBUG: waiting for .item .name finished
2020-07-13 01:49:25 [gerapy.selenium] DEBUG: crawling https://dynamic5.scrape.center/page/2
2020-07-13 01:49:26 [gerapy.selenium] DEBUG: wait for .item .name finished
2020-07-13 01:49:26 [gerapy.selenium] DEBUG: close selenium
2020-07-13 01:49:26 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://dynamic5.scrape.center/detail/26855315> (referer: https://dynamic5.scrape.center/page/1)
2020-07-13 01:49:26 [gerapy.selenium] DEBUG: processing request <GET https://dynamic5.scrape.center/detail/27047626>
2020-07-13 01:49:26 [gerapy.selenium] DEBUG: set options {'headless': True, 'dumpio': False, 'devtools': False, 'args': ['--window-size=1400,700', '--disable-extensions', '--hide-scrollbars', '--mute-audio', '--no-sandbox', '--disable-setuid-sandbox', '--disable-gpu']}
2020-07-13 01:49:26 [scrapy.core.scraper] DEBUG: Scraped from <200 https://dynamic5.scrape.center/detail/26855315>
{'name': '冒险小虎队', 'score': '9.4', 'tags': ['冒险小虎队', '童年', '冒险', '推理', '小时候读的']}
2020-07-13 01:49:26 [gerapy.selenium] DEBUG: waiting for .item .name finished
2020-07-13 01:49:26 [gerapy.selenium] DEBUG: crawling https://dynamic5.scrape.center/detail/27047626
2020-07-13 01:49:27 [gerapy.selenium] DEBUG: wait for .item .name finished
2020-07-13 01:49:27 [gerapy.selenium] DEBUG: close selenium
...
```
