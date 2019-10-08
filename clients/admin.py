from django.contrib import admin
from .models import Equipamento, CLP, Client
from django.db.models import Q



class InputFilter(admin.SimpleListFilter):
    template = 'clients/input_filter.html'

    def lookups(self, request, model_admin):
        # Dummy, required to show the filter.
        return ((),)

    def choices(self, changelist):
        # Grab only the "all" option.
        all_choice = next(super().choices(changelist))
        all_choice['query_parts'] = (
            (k, v)
            for k, v in changelist.get_filters_params().items()
            if k != self.parameter_name
        )
        yield all_choice

class UIDFilter(InputFilter):
    parameter_name = 'client'
    title = ('CLIENT')
 
    def queryset(self, request, queryset):
        if self.value() is not None:
            client = self.value()
            return queryset.filter(
                
                Q(client=client)
            )

class TransactionAdmin(admin.ModelAdmin):
    ...
    list_filter = (
        UIDFilter,
    )

admin.site.register(Client)
admin.site.register(CLP)
admin.site.register(Equipamento, TransactionAdmin)