from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS

def get_exif_data(image):
    """EXIFデータを取得"""
    exif_data = {}
    try:
        info = image._getexif()
        if info:
            for tag, value in info.items():
                tag_name = TAGS.get(tag, tag)
                exif_data[tag_name] = value
    except AttributeError:
        # EXIFデータがない場合
        pass
    return exif_data

def get_geotagging(exif_data):
    """GPS情報を抽出"""
    if 'GPSInfo' not in exif_data:
        return None

    geotags = {}
    for key in exif_data['GPSInfo'].keys():
        name = GPSTAGS.get(key, key)
        geotags[name] = exif_data['GPSInfo'][key]
    return geotags

def get_coordinates(geotags):
    """GPS情報を緯度・経度に変換"""
    def _convert_to_degrees(value):
        d = value[0]
        m = value[1] / 60.0
        s = value[2] / 3600.0
        return d + m + s

    lat = geotags.get('GPSLatitude')
    lat_ref = geotags.get('GPSLatitudeRef')
    lon = geotags.get('GPSLongitude')
    lon_ref = geotags.get('GPSLongitudeRef')

    if not lat or not lon or not lat_ref or not lon_ref:
        return None

    lat = _convert_to_degrees(lat)
    if lat_ref != 'N':
        lat = -lat

    lon = _convert_to_degrees(lon)
    if lon_ref != 'E':
        lon = -lon

    return lat, lon
