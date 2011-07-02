"""
jQuery-File-Upload package
"""

from os.path import join, dirname

try:
    from xstatic.main import XStatic
except ImportError:
    class XStatic(object):
        """
        just a dummy for the time when setup.py is running and
        for the case that xstatic is not already installed.
        """

class JQueryFileUpload(XStatic):
    name = 'jquery_file_upload' # short, all lowercase name
    display_name = 'jQuery-File-Upload' # official name, upper/lowercase allowed
    version = '4.4.0' # for simplicity, use same version x.y.z as bundled files
                        # additionally we append .b for our build number, so we
                        # can release new builds with fixes for xstatic stuff.

    base_dir = join(dirname(__file__), 'data')
    # linux package maintainers just can point to their file locations like this:
    # base_dir = '/usr/share/javascript/jquery-file-upload'

    description = "%s (XStatic packaging standard)" % display_name

    platforms = 'any'
    classifiers = []
    keywords = '%s xstatic' % name

    # this all refers to the XStatic-* package:
    author = 'Thomas Waldmann'
    author_email = 'tw@waldmann-edv.de'
    # XXX shall we have another bunch of entries for the bundled files?
    # like upstream_author/homepage/download/...?
    # note: distutils/register can't handle author and maintainer at once.

    # this refers to the project homepage of the stuff we packaged:
    homepage = 'http://plugins.jquery.com/project/jQuery-File-Upload'

    # this refers to all files:
    license = '(same a %s)' % display_name

    locations = {
    }

