# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        res = []
        stack = [startUrl]
        seen = set()
        while stack:
            print(stack)
            url = stack.pop()
            c = htmlParser.getUrls(url)
            for url in c:
                if url in seen:
                    continue
                seen.add(url)
                if startUrl.split("/")[2] == url.split("/")[2]:
                    stack.append(url)
                    res.append(url)
        if startUrl not in seen:                         
            res.append(startUrl)
        return res

                
            