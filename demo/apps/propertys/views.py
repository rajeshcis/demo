# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import get_model
from propertys.models import Property, Apartment, LandProperty
from django.contrib.auth.decorators import login_required

modelsname = {'Multistorey Apartment': 'Apartment', 'Builder Floor Apartment': 'Apartment', 'Residential House': 'Apartment',
				'Villa': 'Apartment', 'Penthouse': 'Apartment', 'Studio Apartment': 'Apartment','Service Apartment': 'Apartment',
				 'Commercial Office Space': 'Apartment', 'Office in IT Park/ SEZ': 'Apartment', 'Commercial Shop': 'Apartment',
				 'Space in Shopping Mall': 'Apartment', 'Commercial Showroom': 'Apartment',	'Kiosk': 'Apartment','Business Centre': 'Apartment',
				 'Warehouse/ Godown': 'Apartment', 'Guest House': 'Apartment','Hotel': 'Apartment', 'Farm House': 'Apartment', 
				 'Industrial Building': 'Apartment', 'Hotel Sites': 'LandProperty', 'Industrial Land': 'LandProperty',
				 'Commercial Land': 'LandProperty', 'Residential Plot': 'LandProperty', 'Industrial Shed': 'LandProperty', 'Agricultural Land': 'LandProperty',
    }

def index(request):
	return render(request, 'propertys/index.html')

def detailview(request, p_id):
	propertys = Property.objects.get(pk=p_id)
	propertytype = propertys.propertytype
	propertysmodel = get_model('propertys', modelsname[propertytype])
	propertysvalue = propertysmodel.objects.filter(propertyid=propertys)
	

	context = {'propertysvalue' : propertysvalue[0], 'modelsn' : modelsname[propertytype]}
	return render(request, 'propertys/detailview.html', context)

def viewproperty(request):
	propertys = Property.objects.all()


	#import pdb;pdb.set_trace()
	context = {'propertys':propertys}
	return render(request, 'propertys/viewproperty.html', context)

@login_required(login_url='/login/')
def saleproperty(request):
	if request.method == 'POST':
		requestdata = request.POST
		pr = get_model('propertys', requestdata['modelsname'])
		relatedobj = pr().get_related_FK()
		odict = inserttoobj(relatedobj['foreignkey'], requestdata)
		otherdict = {}
		if relatedobj['otherkey']:
			for oi in relatedobj['otherkey'][1:]:
				if oi.endswith('id'):
					otherdict[oi] = odict[oi.split('id')[0]]
				else:
					otherdict[oi] = requestdata.has_key(oi) and requestdata[oi] or 'null'
		obj = pr(**otherdict)
		obj.save()
	return render(request, 'propertys/saleproperty.html')

def inserttoobj(robj, requestdata):
	objdict = {}
	for i in robj:
		allfields = get_all_field(i)
		tempdict = {}
		for j in allfields:
			if requestdata.has_key(j):
				tempdict[j] = requestdata[j]
		o = i(**tempdict)		
		o.save()
		objdict[o._meta.object_name.lower()] = o
	return objdict

def get_all_field(obj):
    allfields = obj()._meta.get_all_field_names()
    return allfields