from django.shortcuts import render
from django.http import HttpResponse,HttpResponseBadRequest,HttpResponseRedirect
from django import forms
from .models import aparajitha3,Common_Setting1

# Create your views here.
import pandas as pd

class UploadFileForm(forms.Form):
   file = forms.FileField()

def import_sheet(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST,
                          request.FILES)
       
        if form.is_valid():
            # print(request.FILES['file'])
            df = pd.read_excel(request.FILES['file'],sheet_name="Range_Setting")
            first_header = df.columns

            df.set_axis(df.iloc[0].values, axis=1, inplace=True)

            second_header = []
            for count, values in enumerate(df.columns):

                if isinstance(values, float):
                    second_header.insert(count, first_header[count])

                else:
                    second_header.insert(count, values)

            df.columns = second_header

            df = df.drop([0, 1])
            # print(df)
            entries = []
            for e in df.T.to_dict().values():
                entries.append(aparajitha3(**e))
            aparajitha3.objects.bulk_create(entries) 
        
        if form.is_valid():
            # print(request.FILES['file'])
            df = pd.read_excel(request.FILES['file'],sheet_name="Common_Setting")
            first_header = df.columns

            df.set_axis(df.iloc[0].values, axis=1, inplace=True)

            second_header = []
            for count, values in enumerate(df.columns):

                if isinstance(values, float):
                    second_header.insert(count, first_header[count])

                else:
                    second_header.insert(count, values)

            df.columns = second_header

            df = df.drop([0, 1])
            # print(df)
            entries = []
            for e in df.T.to_dict().values():
                entries.append(Common_Setting1(**e))
            Common_Setting1.objects.bulk_create(entries) 
         
            return HttpResponse('Data Has Stored Sucessfully')
        else:
            return HttpResponseBadRequest

    else:
        form = UploadFileForm()
        return render(
            request,
            'upload_form.html',
            {'form': form,
             'title': 'Excel file upload',
             'header': 'Please choose a valid excel file'
             })
def delete_records(request):
    PersonalInfo.objects.all().delete()
    return HttpResponse('Data deleted')


