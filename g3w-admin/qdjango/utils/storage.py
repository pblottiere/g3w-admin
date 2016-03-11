from django.core.files.storage import FileSystemStorage
from django.core.urlresolvers import reverse
from django.conf import settings
import os


class OverwriteStorage(FileSystemStorage):
    """Custom file system storage, overwrite file if existing.

    See http://djangosnippets.org/snippets/976/
    """

    def get_available_name(self, name):
        """Return a filename for new content to be written to.

        If file already exist, overwrite it.
        """

        if self.exists(name):
            os.remove(os.path.join(settings.MEDIA_ROOT, name))
        return name

class QgisFileOverwriteStorage(OverwriteStorage):

    def url(self, name):
        return reverse('project-qgisfile', args=(name,))
