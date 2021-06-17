"""
Basic:
    the highest level widget, put it on all widget, including the following categories:
    back, search, icon, text, image, checkbox_on, checkbox_off, radiobox_on, radiobox_off,
    switch_on, switch_off
"""

# xml print form
FORM = '''{indent}<Basic>
\t{indent}<name>{name}</name>
\t{indent}<type>{type}</type>
\t{indent}<bndbox>
\t\t{indent}<xmin>{x1}</xmin>
\t\t{indent}<ymin>{y1}</ymin>
\t\t{indent}<xmax>{x2}</xmax>
\t\t{indent}<ymax>{y2}</ymax>
\t{indent}</bndbox>
{indent}</Basic>
'''


class Basic:

    type_names = [
        'back',
        'search',
        'icon',
        'text',
        'image',
        'checkbox_on',
        'checkbox_off',
        'radiobox_on',
        'radiobox_off',
        'switch_on',
        'switch_off'
    ]

    def __init__(self, pos: tuple, _type, name):
        self.pos = pos  # basic's position -> tuple(x1, y1, x2, y2)
        self.type = _type  # basic's type in type_names
        self.name = name  # basic's name

    @classmethod
    def is_basic(cls, widget):
        """
        check whether a widget belongs to Basic if type()
        :param widget: object
        :return: bool
        """
        try:
            # prevent it from having no type attribute
            return widget.type in cls.type_names
        except Exception as e:
            print(e)
            return False

    def xml(self, indent=0):
        """
        xml print
        :return: string
        """
        return FORM.format(
            name=self.name,
            type=self.type,
            x1=self.pos[0], y1=self.pos[1], x2=self.pos[2], y2=self.pos[3],
            indent='\t'*indent
        )


if __name__ == '__main__':
    b = Basic((1, 1, 2, 2), 'text', 'listening')
    print(b.xml(4))  # test xml print
    print(b.xml())  # test xml print
    print(Basic.is_basic(b))  # test is_basic()
    pass
