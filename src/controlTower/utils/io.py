import json

class io:
    def to_json(self, obj):
        json.loads(
            json.dumps(obj, default=lambda o: getattr(o, '__dict__', str(o)))
        )

    def read_data(self, fpath):
        fp = open(fpath)
        data = fp.readlines()
        fp.close()
        return data

    def write_data(self, fpath, data):
        try:
            with open(fpath, "w") as f:
                f.write(data)
        except:
            return False
        else:
            return True
