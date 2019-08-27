from utilities.git import git_get_changed_files, git_get_untracked_files, git_get_encodings


def get_files():
    file_collection = {}
    changed_files = git_get_changed_files().split("\n")
    untracked_files = git_get_untracked_files().split("\n")
    changed_files.remove("")
    untracked_files.remove("")
    for file in changed_files:
        try:
            status = file.split("\t")[0]
            filename = file.split("\t")[1]
            encodings = git_get_encodings(filename)
            file_collection[filename] = {
                "status": status
            }
            if 'git-encoding' in encodings:
                file_collection[filename]['git-encoding'] = encodings['git-encoding']
            if 'zos-working-tree-encoding' in encodings:
                file_collection[filename]['zos-working-tree-encoding'] = encodings['zos-working-tree-encoding']
        except Exception as e:
            pass

    for file in untracked_files:
        try:
            status = "A"
            filename = file
            encodings = git_get_encodings(file)
            file_collection[file] = {
                "status": status
            }
            if 'git-encoding' in encodings:
                file_collection[filename]['git-encoding'] = encodings['git-encoding']
            if 'zos-working-tree-encoding' in encodings:
                file_collection[filename]['zos-working-tree-encoding'] = encodings['zos-working-tree-encoding']
        except Exception as e:
            pass

    return file_collection


def build_file_dictionary(changed_files):
    file_dictionary = {}
    file_list = str(changed_files).split("\n")
    for file in file_list:
        try:
            status = file.split("\t")[0]
            filename = file.split("\t")[1]
            encodings = git_get_encodings(filename)
            file_dictionary[filename] = {
                "status": status
            }
            if 'git-encoding' in encodings:
                file_dictionary[filename]['git-encoding'] = encodings['git-encoding']
            if 'zos-working-tree-encoding' in encodings:
                file_dictionary[filename]['zos-working-tree-encoding'] = encodings['zos-working-tree-encoding']
        except Exception as e:
            pass
    return file_dictionary
