from poium import Page,PageElement

class Baidusearch(Page):
    # serchinput = PageElement(id='kw')
    # serchbutton = PageElement(id='su')

    search_input= PageElement(id_="kw", describe="搜索框")
    search_button= PageElement(id_="su", describe="搜索按钮")