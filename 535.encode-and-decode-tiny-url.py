#
# @lc app=leetcode id=535 lang=python3
#
# [535] Encode and Decode TinyURL
#

# @lc code=start
class Codec:
    prefix = 'http://tinyurl.com/'
    chars = [chr(i) for i in range(ord('0'), ord('9') + 1)] \
        + [chr(i) for i in range(ord('A'), ord('Z') + 1)] \
        + [chr(i) for i in range(ord('a'), ord('z') + 1)]

    cache = {}

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        while True:
            s = ''.join(random.choice(self.chars) for _ in range(6))
            if s not in self.cache:
                self.cache[s] = longUrl
                return self.prefix + s

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        s = shortUrl.replace(self.prefix, '')
        return self.cache[s] if s in self.cache else None


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
# @lc code=end

