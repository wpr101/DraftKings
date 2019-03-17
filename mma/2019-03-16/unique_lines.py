uniqlines = set(open('finishes_upload.txt').readlines())
bar = open('finishes_unique_upload.txt', 'w').writelines(set(uniqlines))
bar.close()
