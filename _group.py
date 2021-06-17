"""
Group:
    the second or third level widget, put it on the GUI or Region, including the following categories:
    button(must contains text), semantic_combination(combine), input_box(input)
"""
FORM = """{indent}<Group>
\t{indent}<name>{name}</name>
\t{indent}<type>{type}</type>
\t{indent}<bndbox>
\t\t{indent}<xmin>{x1}</xmin>
\t\t{indent}<ymin>{y1}</ymin>
\t\t{indent}<xmax>{x2}</xmax>
\t\t{indent}<ymax>{y2}</ymax>
\t{indent}</bndbox>
{basics}{indent}</Group>
"""


class Group:
    type_names = [
        'button',
        'combine',
        'input'
    ]

    def __init__(self, pos: tuple, _type, name):
        self.pos = pos  # group's position -> tuple(x1, y1, x2, y2)
        self.type = _type  # group's type in type_names
        self.name = name  # group's name if it's not a blank input
        self.basic = []  # contains all basic widgets which on this group

    @classmethod
    def is_group(cls, widget):
        """
        check whether a widget belongs to Group
        :param widget: object
        :return: bool
        """
        try:
            # prevent it from having no type attribute
            return widget.type in cls.type_names
        except Exception as e:
            print(e)
            return False

    def add_basic(self, basic):
        """
        add a Basic widget into this Group
        :param basic: Basic object
        :return:
        """
        self.basic.append(basic)

    def xml(self, indent=0):
        """
        xml print
        :return: string
        """
        string = ''
        for b in self.basic:
            string += b.xml(indent+1)
        return FORM.format(
            name=self.name,
            type=self.type,
            x1=self.pos[0], y1=self.pos[1], x2=self.pos[2], y2=self.pos[3],
            basics=string,
            indent='\t'*indent
        )


if __name__ == '__main__':
    g = Group((1, 1, 2, 3), 'button', '1')
    g2 = Group((1, 1, 2, 3), 'title', '2')
    from _basic import Basic
    b = Basic((1, 1, 2, 2), 'text', 'listening')
    g.add_basic(b)
    g.add_basic(b)

    print(Group.is_group(g))
    print(Group.is_group(g2))
    print(g.xml(2))
    print(g.xml())
    pass


