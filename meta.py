"""
HW -- 8.

Metaclass implemetation.
"""

import re


class MetaNew(type):
    """Metaclass to convert get_*/ set_* methods to property."""

    def __new__(cls, name, bases, classdict):
        """__new__ method."""
        get_regexp = r'\bget_\w+'
        set_regexp = r'\bset_\w+'

        temp_classdict = {}

        for class_obj in classdict:
            new_descriptor = {}
            new_attr = ''

            if re.fullmatch(get_regexp, class_obj) or re.fullmatch(set_regexp, class_obj):
                operation, attr, *_ = class_obj.split('_')
                new_descriptor[operation] = classdict[class_obj]
                new_attr = attr

            old_descriptor = cls._get_descriptors(temp_classdict.get(new_attr))
            if old_descriptor:
                new_descriptor = {**old_descriptor, **new_descriptor}

            if new_attr:
                temp_classdict[new_attr] = property(
                    fget=new_descriptor.get('get'),
                    fset=new_descriptor.get('set'),
                    fdel=new_descriptor.get('delete'),
                )
        classdict = {**classdict, **temp_classdict}
        return type.__new__(cls, name, bases, classdict)

    @staticmethod
    def _get_descriptors(prop):
        """Get descriptors from property."""
        descriptor = {}
        if isinstance(prop, property):
            descriptor['get'] = prop.fget
            descriptor['set'] = prop.fset
            descriptor['delete'] = prop.fdel
        return descriptor
