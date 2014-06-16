from django.db import models

# Create your models here.
PROPERTY_TYPE = (
    ('Multistorey Apartment', 'Multistorey Apartment'),
    ('Builder Floor Apartment', 'Builder Floor Apartment'),
    ('Residential House', 'Residential House'),
    ('Villa', 'Villa'),
    ('Residential Plot', 'Residential Plot'),
    ('Penthouse', 'Penthouse'),
    ('Studio Apartment', 'Studio Apartment'),
    ('Service Apartment', 'Service Apartment'),
    ('Commercial Office Space', 'Commercial Office Space'),
    ('Office in IT Park/ SEZ', 'Office in IT Park/ SEZ'),
    ('Commercial Shop', 'Commercial Shop'),
    ('Space in Shopping Mall', 'Space in Shopping Mall'),
    ('Commercial Showroom', 'Commercial Showroom'),
    ('Kiosk', 'Kiosk'),
    ('Business Centre', 'Business Centre'),
    ('Commercial Land', 'Commercial Land'),
    ('Warehouse/ Godown', 'Warehouse/ Godown'),
    ('Guest House', 'Guest House'),
    ('Hotel', 'Hotel'),
    ('Hotel Sites', 'Hotel Sites'),
    ('Industrial Land', 'Industrial Land'),
    ('Industrial Building', 'Industrial Building'),
    ('Industrial Shed', 'Industrial Shed'),
    ('Agricultural Land', 'Agricultural Land'),
    ('Farm House', 'Farm House'),
)

POSTTYPE = (
    ('Sale', 'Sale'),
    ('Rent', 'Rent'),
)

TRANSATIONTYPE = (
    ('New Property', 'New Property'),
    ('Resale', 'Resale')    
)

PROPERTY_UNIT = (
    ('Sq-ft', 'Sq-ft'),
    ('Sq-yrd', 'Sq-yrd'),
    ('Sq-m', 'Sq-m'),
    ('Acre', 'Acre'),
    ('Bigha', 'Bigha'),
    ('Hectare', 'Hectare'),
    ('Marla', 'Marla'),
    ('Kanal', 'Kanal'),
    ('Biswa1', 'Biswa1'),
    ('Biswa2', 'Biswa2'),
    ('Ground', 'Ground'),
    ('Aankadam', 'Aankadam'),
    ('Rood', 'Rood'),
    ('Chatak', 'Chatak'),
    ('Kottah', 'Kottah'),
    ('Cent', 'Cent'),
    ('Perch', 'Perch'),
    ('Guntha', 'Guntha'),
    ('Are', 'Are'),
)

ROOMNOS = tuple( [(str(i),str(i)) for i in range(1,11)] + [('>10','>10')])
FURNISHED = (
    ('Furnished', 'Furnished'),
    ('Unfurnished','Unfurnished'),
    ('Semi-Furnished', 'Semi-Furnished'),
)

PASSESSIONSTATUS = (
    ('Under Construction', 'Under Construction'),
    ('Ready to Move', 'Ready to Move'),
)


SELECTTYPE = (
    ('Project', 'Project'),
    ('Society', 'Society'),
)

FLOORSTR = [('Lower Basement','Lower Basement'), ('Upper Basement','Upper Basement'), ('Ground','Ground')]

FLOORNO = tuple( FLOORSTR + [(str(i),str(i)) for i in range(1,201)])

BOOL_CHOICES = ((True, 'Yes'), (False, 'No'))

class Property(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    postfor = models.CharField(max_length=20, choices=POSTTYPE, blank=True, null=True)
    propertytype = models.CharField(max_length=50, choices=PROPERTY_TYPE, blank=True, null=True)
    transationtype = models.CharField(max_length=50, choices=TRANSATIONTYPE, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    locality = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    is_showuser = models.BooleanField(default=True, choices=BOOL_CHOICES)
    totalprice = models.CharField(max_length=50,  blank=True, null=True )
    perunitprice = models.CharField(max_length=20, null=True, blank=True)
    perunit = models.CharField(max_length=20, null=True, blank=True, choices=PROPERTY_UNIT)
    possessionstatus = models.CharField(max_length=20, null=True, blank=True)
    possessiondate = models.DateField(null=True, blank=True)


    
class Propertyimage(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField("Property Pic", upload_to="images/", blank=True, null=True)
    is_setdefault = models.BooleanField(default=False)

class Housecommon(models.Model):
    """docstring for Housecommen"""
    bedrooms = models.CharField(max_length=5, choices=ROOMNOS)
    bathrooms = models.CharField(max_length=5, choices=ROOMNOS)
    furnished = models.CharField(max_length=20, choices=FURNISHED)
    floorno = models.CharField(max_length=20, choices=FLOORNO)
    totalfloors = models.CharField(max_length=20)


class LandArea(models.Model):
    """docstring for LandArea"""
    coverdarea = models.CharField(max_length=20)
    coverdareaunit = models.CharField(max_length=20, choices=PROPERTY_UNIT)
    landarea = models.CharField(max_length=20)
    landareaunit = models.CharField(max_length=20, choices=PROPERTY_UNIT)
    carpetarea = models.CharField(max_length=20)
    carpetareaunit = models.CharField(max_length=20, choices=PROPERTY_UNIT)



class LandProperty(models.Model):
    """docstring for LandProperty"""
    propertyid = models.ForeignKey(Property)
    landareaid = models.ForeignKey(LandArea)
    nameofselecttype = models.CharField(max_length=50, null=True, blank=True)
    selecttype = models.CharField(max_length=20, choices=SELECTTYPE, null=True, blank=True)

    def get_related_FK(self):
        related_objects = {'foreignkey': [], 'otherkey': []}
        for field in self._meta.fields:
            if field.__class__ is models.fields.related.ForeignKey:
                related_objects['foreignkey'].append(field.related.parent_model)
                related_objects['otherkey'].append(field.name)
            else:
                related_objects['otherkey'].append(field.name)
        return related_objects




class Apartment(models.Model):
    """This is for sale Apartment property"""
    propertyid = models.ForeignKey(Property, related_name='Property')
    housecommonid = models.ForeignKey(Housecommon)
    landareaid = models.ForeignKey(LandArea)    
    nameofselecttype = models.CharField(max_length=50, null=True, blank=True)
    selecttype = models.CharField(max_length=20, choices=SELECTTYPE, null=True, blank=True)

    

    def get_related_FK(self):
        related_objects = {'foreignkey': [], 'otherkey': []}
        for field in self._meta.fields:
            if field.__class__ is models.fields.related.ForeignKey:
                related_objects['foreignkey'].append(field.related.parent_model)
                related_objects['otherkey'].append(field.name)
            else:
                related_objects['otherkey'].append(field.name)
        return related_objects


