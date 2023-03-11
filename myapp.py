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
        product_type = self.product_type

        if media_type == 1:
            return {'photo':media_info['thumbnail_url']}
        elif media_type == 2:
            if product_type == 'feed':
                return {'video':media_info['video_url']}
            elif product_type == 'igtv':
                return {'igtv':media_info['video_url']}
            elif product_type == 'clips':
                return {'reels':media_info['video_url']}

        elif media_type == 8:
            photos = []
            videos = []
            urls = {}
            resources = media_info['resources']

            for post in resources:
                if post['media_type'] == 1:
                    photos.append(post['thumbnail_url'])
                elif post['media_type'] == 2:
                    videos.append(post['video_url'])
            return {'photo':photos,'videos':videos}

