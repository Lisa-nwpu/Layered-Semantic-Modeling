from _gui import GUI
from _region import Region
from _group import Group
from _basic import Basic
from setting import Pos, Line


def get_data(filename):
    """
    get every line data from file, and use nametuple to store
    :param filename: relative file path like '../text/10.txt'
    :return: Line nametuple list
    """
    elems = []
    with open(filename, 'r', encoding='utf-8') as fp:
        lines = fp.readlines()
        for li in lines:
            elem = li.replace('\n', '').split(' ')
            pos = Pos(elem[1], elem[2], elem[3], elem[4])
            # judge whether this line has texts
            if len(elem) == 6:
                line = Line(pos, elem[5], '')
            else:
                tmp_string = ' '.join(elem[6:])
                line = Line(pos, elem[5], tmp_string)
            elems.append(line)
    return elems


def create_object(elems: list):
    """
    use nametuple Line list to create object
    :param elems: Line list
    :return: objects dic
    """
    objects = {
        'Basic': [],
        'Group': [],
        'Region': [],
        'GUI': []
    }
    try:
        obj = ''
        for i in elems:
            # print(i)  # print for testing
            if Basic.is_basic(i):
                obj = Basic(i.pos, i.type, i.name)
                objects['Basic'].append(obj)
            elif Group.is_group(i):
                obj = Group(i.pos, i.type, i.name)
                objects['Group'].append(obj)
            elif Region.is_region(i):
                obj = Region(i.pos, i.type, i.name)
                objects['Region'].append(obj)
            elif GUI.is_gui(i):
                obj = GUI()
                objects['GUI'].append(obj)
        return objects
    except Exception as e:
        print(e)
        raise SyntaxError


def on(bottom, top):
    """
    judge whether top widget is on bottom widget
    :param bottom: bottom widget
    :param top: top widget
    :return: bool
    """
    try:
        b = [int(i) for i in bottom.pos]
        t = [int(i) for i in top.pos]
        return (
            (b[0] <= t[0]) and
            (b[1] <= t[1]) and
            (b[2] >= t[2]) and
            (b[3] >= t[3])
        )
    except Exception as e:
        print(e)
        raise SyntaxError


def attach(gui, objs):
    objs['GUI'].append(gui)

    for x in objs['Basic']:
        if x.type == 'text':
            objs['GUI'][0].info[x.name] = x.pos

    print('#' * 10, 'Basic', '#' * 10)
    # 1. add and delete some basic on group or region or gui
    for o in objs:
        if o == 'Basic':
            continue
        tmp = []
        print('-----', o, '-----')
        print(len(objs['Basic']))
        for b in objs['Basic']:
            flag = True
            for w in objs[o]:
                if on(w, b):
                    flag = False
                    w.add_basic(b)
                    break
            if flag:
                # flag = true, so this basic isn't on all groups
                tmp.append(b)
        print(len(tmp))
        objs['Basic'] = tmp  # update no Group basic list

    for x in objs['Group']:
        if x.type == 'combine' or x.type == 'button':
            for m in x.basic:
                if m.type == 'text':
                    x.name = m.name

    print('#' * 10, 'Group', '#' * 10)
    # 2. add and delete some group on region or gui
    for o in objs:
        if o == 'Basic' or o == 'Group':
            continue
        tmp = []
        print('-----', o, '-----')
        print(len(objs['Group']))
        for g in objs['Group']:
            flag = True
            for w in objs[o]:
                if on(w, g):
                    flag = False
                    w.add_group(g)
                    break
            if flag:
                # flag = true, so this group isn't on all regions
                tmp.append(g)
        print(len(tmp))
        objs['Group'] = tmp  # update no Region group list

    for x in objs['Region']:
        if x.type == 'title':
            for m in x.basic:
                if m.type == 'text':
                    x.name = m.name

    # 3. add all region on gui
    for r in objs['Region']:
        gui.add_region(r)

    tap = 0
    for ta in gui.region:
        if ta.type == 'data':
            tap=1
            break

    if gui.ifIn('data') or gui.ifIn('datas') or tap == 1:
        gui.name = 'data_picker'
    elif gui.ifIn('login'):
        gui.name = 'log_in'
    elif gui.ifIn('sign in'):
        gui.name = 'sign_in'
    elif gui.ifIn('book') or gui.ifIn('booking'):
        gui.name = 'book'
    elif gui.ifIn('user') or gui.ifIn('users'):
        gui.name = 'user'
    elif gui.ifIn('departure') or gui.ifIn('departing') or gui.ifIn('department') or gui.ifIn('arrival') or gui.ifIn('flying to') or gui.ifIn('flying from'):
        gui.name = 'arrival_and_departure'
    elif gui.ifIn('passenger') or gui.ifIn('passengers'):
        gui.name = 'passengers'
    elif gui.ifIn('payment'):
        gui.name = 'payment'
    elif gui.ifIn('travel') or gui.ifIn('flight') or gui.ifIn('city') or gui.ifIn('airport') or gui.ifIn('origin'):
        gui.name = 'flight'
    else:
        gui.name='others'


def write_xml(filename, content):
    with open(filename, 'w', encoding='utf-8') as fp:
        fp.write(content)
    print(filename, 'finished!')


if __name__ == '__main__':
    elements = get_data('../text/000027.txt')
    objs = create_object(elements)

    main_gui = GUI()
    attach(main_gui, objs)

    xml = main_gui.xml()
    write_xml('../xml/000027.xml', xml)



