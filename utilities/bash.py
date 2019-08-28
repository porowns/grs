from concurrent.futures import ThreadPoolExecutor
from subprocess import Popen  # ended up being way faster than subprocess.run


def bash_upload_file(user, host, absolute_remote_directory, local_file, remote_file):
    p1 = Popen(['scp', local_file, "%s@%s:%s/%s" %
                (user, host, absolute_remote_directory, remote_file)])
    return [p1]


def bash_convert_file_to_encoding(user, host, absolute_remote_directory, remote_file, encoding):
    p1 = Popen(
        ['ssh', '%s@%s' % (user, host), 'iconv', '-f',
         "IBM-1047", '-t', encoding, "%s/%s.temp" % (absolute_remote_directory, remote_file), ">", "%s/%s" % (absolute_remote_directory, remote_file)]
    )
    p2 = Popen(
        ['ssh', '%s@%s' % (user, host), 'chtag', '-tc', encoding, "%s/%s" %
         (absolute_remote_directory, remote_file)],
    )
    p3 = Popen(
        ['ssh', '%s@%s' % (user, host), 'rm', "%s/%s.temp" %
         (absolute_remote_directory, remote_file)],
    )
    return [p1, p2, p3]


def bash_remove_file(user, host, absolute_remote_directory, remote_file):
    p1 = Popen(
        ['ssh', '%s@%s' % (user, host), 'rm', "%s/%s" %
         (absolute_remote_directory, remote_file)], stdout=FNULL
    )
    return [p1]


def bash_tag_file(user, host, absolute_remote_directory, remote_file, encoding):
    p1 = Popen(
        ['ssh', '%s@%s' % (user, host), 'chtag', '-tc', encoding, "%s/%s" %
         (absolute_remote_directory, remote_file)],
    )
    return [p1]
