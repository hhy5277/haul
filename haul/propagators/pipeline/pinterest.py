# coding: utf-8

import re


def original_image_propagator(pipeline_index, finder_image_urls, *args, **kwargs):
    """
    Example:
    http://media-cache-ec0.pinimg.com/70x/50/9b/bd/509bbd5c6543d473bc2b49befe75f4c6.jpg
    http://media-cache-ec0.pinimg.com/236x/50/9b/bd/509bbd5c6543d473bc2b49befe75f4c6.jpg
    http://media-cache-ec0.pinimg.com/736x/50/9b/bd/509bbd5c6543d473bc2b49befe75f4c6.jpg
    to
    http://media-cache-ec0.pinimg.com/originals/50/9b/bd/509bbd5c6543d473bc2b49befe75f4c6.jpg
    """

    pre_propagator_image_urls = kwargs.get('propagator_image_urls', [])
    now_propagator_image_urls = []

    search_re = re.compile(r'.com/\d+x/', re.IGNORECASE)

    for image_url in finder_image_urls:
        if 'pinimg.com/' in image_url.lower():
            if search_re.search(image_url):
                propagator_image_url = search_re.sub('.com/originals/', image_url, count=1)
                now_propagator_image_urls.append(propagator_image_url)

    output = {}
    output['propagator_image_urls'] = pre_propagator_image_urls + now_propagator_image_urls

    return output
