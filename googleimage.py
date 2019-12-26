from google_images_download import google_images_download

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

def imageCrawling(keyword,dir):
    response = google_images_download.googleimagesdownload()

    arguments={"keywords":keyword,
               "limit":600,
               "format":'jpg',
               "print_urls":True,
               "no_directory":True,
               "chromedriver":'chromedriver.exe',
               "output_directory":dir}

    paths = response.download(arguments)
    print(paths)

imageCrawling('ShihTzu','E:\\ShihTzu')
imageCrawling('retriever','E:\\retriever')
