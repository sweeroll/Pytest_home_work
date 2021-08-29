def valid_email(email):
    """
    Check is email correct
    :param email:
    :return: bool
    """
    import re
    return bool(re.search(r"^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$", email))


def log(file_name, text):
    """
    Write log to file
    :param file_name:
    :param text:
    """
    with open(file_name, 'w') as f_obj:
        f_obj.write(text)
