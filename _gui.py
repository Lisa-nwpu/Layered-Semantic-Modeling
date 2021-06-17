"""
GUI:
    the lowest level widget，containing 3 kinds of widgets: Region,Group and Basic.
"""

FORM = """{indent}<GUI>
\t{indent}<info>{info}</info>
\t{indent}<name>{name}</name>
\t{indent}<type>{type}</type>
\t{indent}<bndbox>
\t\t{indent}<xmin>{x1}</xmin>
\t\t{indent}<ymin>{y1}</ymin>
\t\t{indent}<xmax>{x2}</xmax>
\t\t{indent}<ymax>{y2}</ymax>
\t{indent}</bndbox>
{region}{group}{basics}{indent}</GUI>
"""


class GUI:

    type_names = []

    def __init__(self):
        self.pos = (0, 0, 1080, 1920)  # gui's position -> tuple(x1, y1, x2, y2)
        self.name = ''  # Interface's name can describe its function
        self.type = 'GUI'  # useless attr, for uniformity
        self.info = {}  # All text in this interface
        self.region = []  # contains all regions on this interface
        self.group = []  # contains all groups which isn't in other lower level widgets
        self.basic = []  # contains all basic widgets which isn't in other lower level widgets

    @classmethod
    def is_gui(cls, widget):
        """
        judge whether a widget belongs to GUI
        :param widget: object
        :return: bool
        """
        try:
            # prevent it from having no type attribute
            return type(widget) == cls
        except Exception as e:
            print(e)
            return False

    def add_region(self, region):
        """
        add a Region into this GUI
        :param region: Region object
        :return:
        """
        self.region.append(region)

    def add_group(self, group):
        """
        add a Group into this GUI
        :param group: Group object
        :return:
        """
        self.group.append(group)

    def add_basic(self, basic):
        """
        add a Basic widget into this GUI
        :param basic: Basic object
        :return:
        """
        self.basic.append(basic)

    def ifIn(self,string:str):
        '''
        if a string in the info
        :param string:
        :return:
        '''
        return string in self.info

    def __repr__(self):
        """
        return all text
        :return: string object
        """
        return self.info

    def xml(self, indent=0):
        """
        xml print
        :return: string
        """
        region_string = ''
        group_string = ''
        basic_string = ''
        for r in self.region:
            region_string += r.xml(indent + 1)
        for g in self.group:
            group_string += g.xml(indent + 1)
        for b in self.basic:
            basic_string += b.xml(indent + 1)

        return FORM.format(
            info=self.info,
            name=self.name,
            type=self.type,
            x1=self.pos[0], y1=self.pos[1], x2=self.pos[2], y2=self.pos[3],
            region=region_string,
            group=group_string,
            basics=basic_string,
            indent='\t' * indent
        )


if __name__ == '__main__':
    g = GUI()
    print(GUI.is_gui(g))
    pass
