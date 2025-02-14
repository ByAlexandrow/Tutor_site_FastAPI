from sqladmin import Admin, ModelView

from .models import PriceList


def init_admin(app, engine):
    admin = Admin(app, engine)


    class PriceListAdmin(ModelView, model=PriceList):
        column_list = [PriceList.id, PriceList.pricelist_title, PriceList.pricelist_description, PriceList.price]
        column_labels = {
            PriceList.id: 'ID',
            PriceList.pricelist_title: 'Название',
            PriceList.pricelist_description: 'Описание',
            PriceList.price: 'Стоимость (руб)'
        }

    admin.add_view(PriceListAdmin)
