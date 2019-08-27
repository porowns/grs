import argparse
parser = argparse.ArgumentParser(description="Load settings for GRS program")

parser.add_argument('-u', '--user',
                    action="store",
                    dest="user",
                    help="user to remote host",
                    required=True)

parser.add_argument('-ip', '--host',
                    action="store",
                    dest="host",
                    help="hostname to remote host",
                    required=True)

parser.add_argument('-rd', '--remote_directory',
                    action="store",
                    dest="remote_directory",
                    help="directory to remote host",
                    required=True)
