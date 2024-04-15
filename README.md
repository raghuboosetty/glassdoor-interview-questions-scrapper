# [Aborted] Glassdoor Interview Questions Scrapper
The project is aborted. Many issues are there that prevented scrapping, some of them are resolved but others cannot be:
1. ChromiumDriver used in Selenium is a test driver and Google doesn't allow proper user sign-in. Tried to run a Chrome instance in a different port and use the same port from the code but that too didn't work (Chrome driver isn't picking the port or the port is not used by Selenium - mismatch). 
> $ /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222
> 
> $ chromedriver_mac_arm64/chromedriver --remote-debugging-port=9515
> 
> $/opt/homebrew/bin/chromedriver --remote-debugging-port=9515
2. Another way was to avoid Google detecting the test Chrome browser by installing **_undetected_chromedriver_** driver. This allowed me to sign in to my Google account, but testing became difficult every time with _2-step-verification_ from Google.
> python3 -m pip install undetected_chromedriver
3. To solve the above problem had to venture into _Cookies_, which would preserve the session for about 30 mins.
> [def loadCookies(self):](https://github.com/raghuboosetty/glassdoor-interview-questions-scrapper/blob/28fca773528808ed8515e93a49c0f283c26b90e5/glassdoor.py#L35)
> 
> [def saveCookies(self):](https://github.com/raghuboosetty/glassdoor-interview-questions-scrapper/blob/28fca773528808ed8515e93a49c0f283c26b90e5/glassdoor.py#L26)
4. The above worked fine however, now the issue is with the HTML. Glassdoor never loads the entire page. And, for some reason, the elements are not identified by Selenium.

Considering the above issues I've aborted the project. Other alternatives would be to write a [Chrome Extension](https://developer.chrome.com/docs/extensions/get-started) in jQuery. And, it is out of scope for this project at the moment (15/04/2024).


