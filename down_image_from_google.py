from google_images_download import google_images_download

def downloadimages(query, format="jpg", limit=30, size="medium", aspect_ratio="panoramic", print_urls=True):
    """
    aspect_ratio : indique le ration entre la hauteur et la largeur de l'image dont :
        - tall
        - square
        - wide
        - panoramic (par défaut)
    """
    resp = google_images_download.googleimagesdownload()

    arguments = {
        "keywords": query,
        "format": format,
        "limit": limit,
        "print_urls": print_urls,
        "size": size,
        "aspect ratio": aspect_ratio
    }

    try:
        resp.download(arguments)
    except FileNotFoundError:
        arguments = {
            "keywords": query,
            "format": format,
            "limit": limit,
            "print_urls": print_urls,
            "size": size,
        }

        try:
            resp.download(arguments)
        except:
            pass


# searc_queries =[
#     'pizza',
#     'bread',
#     'door',
#     'café'
# ]
searc_queries =[
    'hotdog'
]


for query in searc_queries:
    downloadimages(query=query, limit=100)
    print()
