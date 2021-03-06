from django.contrib import admin

from .models import Profile, CartOrder, CartOrderItems, AddressBook

admin.site.register(Profile)

# Order
class CartOrderAdmin(admin.ModelAdmin):
	list_editable=('paid_status', 'order_status')
	list_display=('user', 'total_amt', 'paid_status', 'order_dt', 'order_status')
admin.site.register(CartOrder,CartOrderAdmin)

class CartOrderItemsAdmin(admin.ModelAdmin):
	list_display=('invoice_no', 'item', 'image_tag', 'quantity', 'price', 'total')
admin.site.register(CartOrderItems,CartOrderItemsAdmin)

class AddressBookAdmin(admin.ModelAdmin):
	list_display=('user','address','status')
admin.site.register(AddressBook, AddressBookAdmin)