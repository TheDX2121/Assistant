from version import VERSION


def current_version():

    return VERSION



def compare_version(
    old_version
):

    if old_version == VERSION:

        return True


    return False