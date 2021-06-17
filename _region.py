"""
Region:
    the second level widget, put it on the GUI, including the following categories:
    title_bar(title), navigation_bar(navigation), keyboard, dialpad, list_items(list), data_picker(data)
"""

FORM = """{indent}<Region>
\t{indent}<name>{name}</name>
\t{indent}<type>{type}</type>
\t{indent}<bndbox>
\t\t{indent}<xmin>{x1}</xmin>
\t\t{indent}<ymin>{y1}</ymin>
\t\t{indent}<xmax>{x2}</xmax>
\t\t{indent}<ymax>{y2}</ymax>
\t{indent}</bndbox>
{group}{basics}{indent}</Region>
"""


class Region:
    type_names = [
        'title',
        'navigation',
        'keyboard',
        'dialpad',
        'list',
        'data'
    ]

    def __init__(self, pos: tuple, _type, name):
        self.pos = pos  # region's position -> tuple(x1, y1, x2, y2)
        self.type = _type  # region's type in type_names
        self.name = name  # region's name if its type is title
        self.group = []  # contains all groups which on this region
        self.basic = []  # contains all basic widgets which isn't in other lower level widgets

    @classmethod
    def is_region(cls, widget):
        """
        check whether a widget belongs to Region
        :param widget: object
        :return: bool
        """
        try:
            # prevent it from having no type attribute
            return widget.type in cls.type_names
        except Exception as e:
            print(e)
            return False

    def add_group(self, group):
        """
        add a Group into this Region
        :param group: Group object
        :return:
        """
        self.group.append(group)

    def add_basic(self, basic):
        """
        add a Basic widget into this Region
        :param basic: Basic object
        :return:
        """
        self.basic.append(basic)

    def xml(self, indent=0):
        """
        xml print
        :return: string
        """
        group_string = ''
        basic_string = ''
        for g in self.group:
            group_string += g.xml(indent + 1)
        for b in self.basic:
            basic_string += b.xml(indent + 1)

        return FORM.format(
            name=self.name,
            type=self.type,
            x1=self.pos[0], y1=self.pos[1], x2=self.pos[2], y2=self.pos[3],
            group=group_string,
            basics=basic_string,
            indent='\t'*indent
        )


if __name__ == '__main__':
    r = Region((2, 2, 3, 4), 'list', 'bar')
    print(Region.is_region(r))  # test is_region()
    print(r.xml())
    pass
