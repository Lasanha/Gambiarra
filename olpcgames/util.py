import os.path

try:
    from sugar.activity.activity import get_bundle_path
except ImportError:
    def get_bundle_path():
        return ''
        
def data_path(file_name):
    """Return the full path to a file in the data directory."""
    return os.path.join(get_bundle_path(), 'data', file_name)