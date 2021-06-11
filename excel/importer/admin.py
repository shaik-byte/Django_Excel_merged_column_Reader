from django.contrib import admin
# from .models import shaik
from .models import aparajitha3, Common_Setting1




# Register your models here.
@admin.register(aparajitha3)
class aparajitha(admin.ModelAdmin):
    list_display = ['Range_ID',
    'From_Value','To_Value', 'Contribution_Setting_Id',]


@admin.register(Common_Setting1)
class aparajitha(admin.ModelAdmin):
    list_display = ['Applicable_at_the_Country_Level',
    'Setting_Title','State', 'District','Threshold_limit','Applicable_Regular_Employee','Applicable_Trainee',
    'Applicable_Contract_Worker','Applicable_International_Worker','Group_Level',
    'Legal_Entity_Level','Unit_Level','Periodicity','DOR_1_Day','DOR_1_Month','DOR_2_Day','DOR_2_Month',
    'DOR_3_Day','DOR_3_Month','DOR_4_Day','DOR_4_Month','Is_Last_Day_of_Every_Month','Custom_Day','Contribution_period_starts_on','Effective_From','Primary_Setting_Name','Range_Based_on','Range_ID']

