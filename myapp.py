import instagrapi

class MyApp:
    def __init__(self,url):
        self.url = url
        self.client = instagrapi.Client()
        self.media_pk = self.client.media_pk_from_url(self.url)
        self.media_info = self.client.media_info(self.media_pk).dict()
        self.media_type = self.media_info['media_type']
        self.product_type = self.media_info['product_type']

    def get_link(self):
        media_type = self.media_type
        media_info = self.media_info

        if media_type == 1:
            return media_info['thumbnail_url']
        elif media_type == 2:
            return media_info['video_url']
        elif media_type == 8:
            urls = []
            resources = media_info['resources']
            for post in resources:
                loc_type = post['media_type']
                if loc_type == 1:
                    urls.append(post['thumbnail_url'])
                elif loc_type == 2:
                    urls.append(post['video_url'])

            return urls
