class reader:
    def read_data(self, fpath):
        fp = open(fpath)
        data = fp.readlines()
        fp.close()
        return data