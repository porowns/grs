import subprocess


def bash_upload_file(user, host, absolute_remote_directory, local_file, remote_file):
    respnse = subprocess.run(
        ['ssh', '%s@%s' % (user, host), 'mkdir', '-p',
         absolute_remote_directory]
    )
    response = subprocess.run(
        ['scp', local_file, "%s@%s:%s/%s" %
            (user, host, absolute_remote_directory, remote_file)]
    )


def bash_convert_file_to_encoding(user, host, absolute_remote_directory, remote_file, encoding):
    response = subprocess.run(
        ['ssh', '%s@%s' % (user, host), 'iconv', '-f',
         "IBM-1047", '-t', encoding, "%s/%s.temp" % (absolute_remote_directory, remote_file), ">", "%s/%s" % (absolute_remote_directory, remote_file)]
    )
    response = subprocess.run(
        ['ssh', '%s@%s' % (user, host), 'chtag', '-tc', encoding, "%s/%s" %
         (absolute_remote_directory, remote_file)],
    )
    response = subprocess.run(
        ['ssh', '%s@%s' % (user, host), 'rm', "%s/%s.temp" %
         (absolute_remote_directory, remote_file)],
    )


def bash_remove_file(user, host, absolute_remote_directory, remote_file):
    response = subprocess.run(
        ['ssh', '%s@%s' % (user, host), 'rm', "%s/%s" %
         (absolute_remote_directory, remote_file)], stdout=FNULL
    )


def bash_tag_file(user, host, absolute_remote_directory, remote_file, encoding):
    response = subprocess.run(
        ['ssh', '%s@%s' % (user, host), 'chtag', '-tc', encoding, "%s/%s" %
         (absolute_remote_directory, remote_file)],
    )
