import mimetypes
import os
from _sha1 import sha1
from random import choice
from urllib import parse
from wsgiref.util import FileWrapper
from PIL import Image, ImageOps

from django.http import HttpResponse

from dcxt_django import settings


def generate_safe_pk(self):
    def wrapped(self):
        while 1:
            skey = getattr(settings, 'SECRET_KEY', 'asidasdas3sfvsanfja242aako;dfhdasd&asdasi&du7')
            pk = sha1('%s%s' % (skey, ''.join([choice('0123456789') for i in range(11)]))).hexdigest()

            try:
                self.__class__.objects.get(pk=pk)
            except:
                return pk

    return wrapped


def get_thumbnail(img, thumb_size, quality=80, format='JPG'):

    thumb_size = thumb_size.split('x')

    img.seek(0)  # see http://code.djangoproject.com/ticket/8222 for details
    image = Image.open(img)

    # Convert to RGB if necessary
    if image.mode not in ('L', 'RGB'):
        image = image.convert('RGB')

    # get size
    thumb_w = int(thumb_size[0])
    thumb_h = int(thumb_size[1])
    image2 = ImageOps.fit(image, (thumb_w, thumb_h), Image.ANTIALIAS)

    # raise Exception( img )
    split = img.path.rsplit('.', 1)
    try:
        thumb_url = '%s.%sx%s.%s' % (split[0], thumb_w, thumb_h, split[1])
    except:
        thumb_url = '%s.%sx%s' % (split, thumb_w, thumb_h)
    # PNG and GIF are the same, JPG is JPEG
    if format.upper() == 'JPG':
        format = 'JPEG'

    image2.save(thumb_url, format, quality=quality)
    return thumb_url.replace(settings.MEDIA_ROOT, settings.MEDIA_URL).replace('//', '/')


#Getting files here
def format_file_extensions(extensions):
    return  ".(%s)$" % "|".join(extensions)


class FileResponse(HttpResponse):
    def __init__(self, request, filepath, filename=None, status=None):

        if settings.DEBUG:
            wrapper = FileWrapper(open(filepath, 'rb'))
            super(FileResponse,self).__init__(wrapper, status=status)
        else:
            super(FileResponse,self).__init__(status=status)
            self['X-Accel-Redirect'] = filepath
            self['XSendfile'] = filepath

        if not filename:
            filename = os.path.basename(filepath)

        type, encoding = mimetypes.guess_type(filepath)

        if type is None:
            type = 'application/octet-stream'

        self['Content-Type'] = type
        self['Content-Length'] = os.path.getsize(filepath)

        if encoding is not None:
            self['Content-Encoding'] = encoding

        # To inspect details for the below code, see http://greenbytes.de/tech/tc2231/
        if u'WebKit' in request.META['HTTP_USER_AGENT']:
            # Safari 3.0 and Chrome 2.0 accepts UTF-8 encoded string directly.
            filename_header = 'filename=%s' % filename.encode('utf-8')
        elif u'MSIE' in request.META['HTTP_USER_AGENT']:
            # IE does not support internationalized filename at all.
            # It can only recognize internationalized URL, so we do the trick via routing rules.
            filename_header = ''
        else:
            # For others like Firefox, we follow RFC2231 (encoding extension in HTTP headers).
            filename_header = 'filename*=UTF-8\'\'%s' % parse.quote(filename.encode('utf-8'))

        self['Content-Disposition'] = 'attachment; ' + filename_header