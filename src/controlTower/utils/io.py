from pathlib import Path

class IO:

    def pretty_print(self, obj, types):
        prettydict={}
        if getattr(obj, '__dict__', None) is not None:
            for attr, value in obj.__dict__.items():
                tmp_dict={}
                if isinstance(value, types):
                    tmp_dict[attr] = self.pretty_print(value, types)
                elif isinstance(value, list):
                    l=[]
                    for item in value:
                        if isinstance(item, types):
                            l.append(self.pretty_print(item, types))
                        else:
                            l.append(item)
                    tmp_dict[attr] = l
                else:
                    tmp_dict[attr] = value
                prettydict.update(tmp_dict)
            return prettydict
        else:
            if isinstance(obj, dict):
                tmp_dict={}
                for key in obj:
                    tmp_dict[key] = self.pretty_print(obj[key], types)
                return tmp_dict
            else:
                return obj

    def read_data(self, fpath):
        fp = open(fpath)
        data = fp.readlines()
        fp.close()
        return ''.join(data)

    def write_data(self, fpath, data):
        Path('/'.join(fpath.split("/")[0:-1])).mkdir(parents=True, exist_ok=True)
        try:
            with open(fpath, "w") as f:
                f.write(data)
        except:
            return False
        else:
            return True
