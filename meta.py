import re


class MetaNew(type):
    def __new__(cls, name, bases, classdict):
        get_regexp = r'\bget_\w+'
        set_regexp = r'\bset_\w+'

        temp_classdict = {}
        for class_obj in classdict:
            if re.fullmatch(get_regexp, class_obj):
                new_attr = class_obj.split('_')[1]
                if temp_classdict.get(new_attr):
                    descrips= cls._get_descriptors(temp_classdict[new_attr])
                    descrips[0] = classdict[class_obj]
                    temp_classdict[new_attr] = property(*descrips)
                else:
                    temp_classdict[new_attr] = property(classdict[class_obj])
            elif re.fullmatch(set_regexp, class_obj):
                new_attr = class_obj.split('_')[1]
                if temp_classdict.get(new_attr):
                    descrips= cls._get_descriptors(temp_classdict[new_attr])
                    descrips[1] = classdict[class_obj]
                    temp_classdict[new_attr] = property(*descrips)
                else:
                    temp_classdict[new_attr] = property(None, classdict[class_obj])

        classdict = {**classdict, **temp_classdict}
        return type.__new__(cls, name, bases, classdict)

    @staticmethod
    def _get_descriptors(prop):
        descriptors = []
        if isinstance(prop, property):
            descriptors.append(prop.fget)
            descriptors.append(prop.fset)
            descriptors.append(prop.fdel)
        return descriptors


class New(metaclass=MetaNew):
    def __init__(self, x):
        self._x = x

    def get_x(self):
        return self._x

    def set_x(self, val):
        self._x = val
        print('set val')

    def get_y(self):
        return 'y'

a = New(42)
print(a.x)
a.x = 33
print(a.x)
print(a.y)
