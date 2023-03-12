from beautifultable import BeautifulTable


def base_interface():
    interface = BeautifulTable()
    interface.rows.append(["SCREEN"])
    interface.rows.append(["ACTIONS"])
    interface.set_style(BeautifulTable.STYLE_BOX)
    return interface


def create_playertable():
    table = BeautifulTable()
    table.columns.header = ["COL 1", "COL 2"]
    table.rows.append(["DATA1", "DATA2"])
    table.set_style(BeautifulTable.STYLE_BOX)
    table.border.left = ""
    table.border.right = ""
    table.border.top = ""
    table.border.bottom = ""
    table.rows.separator = ""

    return table


def add_to_interface(interface, subtable, **kwargs):
    interface.rows[0][0] = subtable
    if kwargs:
        interface.rows[1][0] = "ACTIONS\n" + kwargs["actions"]


interface = base_interface()
player_table = create_playertable()
actions1 = "[1] Action\n[2] Action"

add_to_interface(interface, player_table, actions=actions1)

print(interface)
