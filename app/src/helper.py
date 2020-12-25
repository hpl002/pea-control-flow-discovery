import os.path
import os
import glob


def wipe_dir(pPath):
    """[deletes all filed in dir]

    Args:
        path ([string]): [absolute path to dir]
    """
    files = glob.glob(os.path.join(pPath, "*"))
    for f in files:
        os.remove(f)


def mv_file_to_export_dir(pCurrent, pFilename):
    """[heplper that moves file from root to export dir]

    Args:
        pCurrent ([string]): [CWD]
        pFilename ([string]): [filename with ext]
    """
    os.rename(os.path.join(pCurrent, pFilename),
              os.path.join(pCurrent, "export", pFilename))


def get_filename_from_dir(pPath):
    """[get filename from dir]

    Args:
        path ([string]): [absolute path to dir]
    """
    files = glob.glob(os.path.join(pPath, "*"))
    for f in files:
        return f


def allowed_file(filename, extentions):
    """[checks filename for allowed extension]

    Args:
        filename ([string]): [filename]
        extentions ([arr:string]): [arr of extensions, w/o dot]

    Returns:
        [type]: [boolean]
    """
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in extentions