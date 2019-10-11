from django.contrib.admin import AdminSite


class CustomSite(AdminSite):
    site_header = 'Typeidea'
    site_title = 'Typeidea 关联后台'
    index_title = '首页'


custom_site = CustomSite(name='cus_admin')
