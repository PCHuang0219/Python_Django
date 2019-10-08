from django.db import models

# Create your models here.
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class Assets(models.Model):
#id = models.AutoField(primary_key=True)# Added by default, not required explicitly
    assetid = models.IntegerField(null=True)
    type = models.CharField(max_length=24)
    commonname = models.CharField(max_length=30)
    expired = models.CharField(max_length=4, blank=True)
    modelnum = models.CharField(max_length=30, blank=True)

    modelid = models.CharField(max_length=30, blank=True)
    swversion = models.CharField(max_length=16, blank=True)
    serialno = models.CharField(max_length=30, blank=True)
    longtitude = models.CharField(max_length=16, blank=True)
    latitude = models.CharField(max_length=16, blank=True)

    ip = models.GenericIPAddressField(max_length=20, null=True)
    netmask = models.CharField(max_length=16, blank=True)
    ip6 = models.CharField(max_length=30)
    pos_inrack = models.IntegerField(null=True)
    rackid = models.IntegerField(null=True)

    rowid = models.IntegerField(null=True)
    roomid = models.IntegerField(null=True)
    fl_sessid = models.IntegerField(null=True)

    addrid = models.IntegerField(null=True)
    siteid = models.IntegerField(null=True)

    corpid = models.IntegerField(null=True)
    address = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=16, blank=True)
    state = models.CharField(max_length=2, blank=True)
    zip = models.IntegerField(null=True)

    country = models.CharField(max_length=24, blank=True)

#objects = models.Manager()# Added by default, to required explicitly
#def __str__(self):
#    return str(self.commonname)

class init_data():
    #if no data, load initial data
    # Import model class
    # return "%s (%s)" % (self.commonname, self.type)

    # Create model store instances
    asset_1 = Assets(assetid=1, type='switch', commonname='8th_fl_switch', expired='n/a', modelnum='ECS4120-28F-v2',
                    modelid='ECS4120-28F', swversion='2.0.0.100', serialno='m120879498', longtitude='41.234567',
                    latitude='120.897686', ip='192.168.2.122', netmask='255.255.255.0', ip6='n/a', pos_inrack=2,
                    rackid=1, rowid=1, roomid=1, fl_sessid=8, addrid=1, siteid=1, corpid=1,
                    address='102 Guangfu S. Rd., Daan District, Taipei 10694', city='Taipei', state='na', zip=10694,
                    country='Taiwan')

    asset_2 = Assets(assetid=1, type='switch', commonname='10th_fl_switch', expired='n/a', modelnum='ECS4120-28F-v2',
                    modelid='as4610', swversion='2.0.0.100', serialno='m120879498', longtitude='41.234567',
                    latitude='120.897686', ip='192.168.2.122', netmask='255.255.255.0', ip6='n/a', pos_inrack=2,
                    rackid=1, rowid=1, roomid=1, fl_sessid=10, addrid=1, siteid=1, corpid=1,
                    address='102 Guangfu S. Rd., Daan District, Taipei 10694', city='Taipei', state='na', zip=10694,
                    country='Taiwan')

    asset_3 = Assets(assetid=1, type='switch', commonname='13th_fl_switch', expired='n/a', modelnum='ECS4120-28F-v2',
                    modelid='as4610', swversion='2.0.0.100', serialno='m120879498', longtitude='41.234567',
                    latitude='120.897686', ip='192.168.2.122', netmask='255.255.255.0', ip6='n/a', pos_inrack=2,
                    rackid=1, rowid=1, roomid=1, fl_sessid=13, addrid=1, siteid=1, corpid=1,
                    address='102 Guangfu S. Rd., Daan District, Taipei 10694', city='Taipei', state='na', zip=10694,
                    country='Taiwan')

    asset_4 = Assets(assetid=1, type='switch', commonname='5th_fl_switch', expired='n/a', modelnum='ECS4120-28F-v2',
                    modelid='as4610', swversion='2.0.0.100', serialno='m120879498', longtitude='41.234567',
                    latitude='120.897686', ip='192.168.2.122', netmask='255.255.255.0', ip6='n/a', pos_inrack=2,
                    rackid=1, rowid=1, roomid=1, fl_sessid=1, addrid=2, siteid=1, corpid=1,
                    address='102 Guangfu S. Rd., Daan District, Taipei 10694', city='Taipei', state='na', zip=10694,
                    country='Taiwan')

    asset_5 = Assets(assetid=1, type='switch', commonname='1st_fl_switch', expired='n/a', modelnum='ECS4100-52T',
                    modelid='ECS4100-52T', swversion='2.0.0.100', serialno='m120869502', longtitude='41.234567',
                    latitude='120.897686', ip='192.168.2.122', netmask='255.255.255.0', ip6='n/a', pos_inrack=2,
                    rackid=1, rowid=1, roomid=1, fl_sessid=1, addrid=1, siteid=2, corpid=1,
                    address='5F, No. 367. Fuxing N. Rd., Taipei 105', city='Taipei', state='na', zip=105,
                    country='Taiwan')

    asset_6 = Assets(assetid=1, type='switch', commonname='1st_fl_switch', expired='n/a', modelnum='as4610',
                    modelid='as4610', swversion='2.0.0.100', serialno='m120879498', longtitude='41.234567',
                    latitude='120.897686', ip='192.168.2.122', netmask='255.255.255.0', ip6='n/a', pos_inrack=2,
                    rackid=1, rowid=1, roomid=1, fl_sessid=2, addrid=4, siteid=2, corpid=1,
                    address='1 Creation Rd 3, Hsinchu Science Park, Hsinchu 30077', city='Hsinchu', state='na',
                    zip=30077, country='Taiwan')
    asset_7 = Assets(assetid=1, type='switch', commonname='2nd_fl_switch', expired='n/a', modelnum='as4610',
                    modelid='as4610', swversion='2.0.0.100', serialno='m120879498', longtitude='41.234567',
                    latitude='120.897686', ip='192.168.2.122', netmask='255.255.255.0', ip6='n/a', pos_inrack=2,
                    rackid=1, rowid=1, roomid=1, fl_sessid=2, addrid=4, siteid=2, corpid=1,
                    address='1 Creation Rd 3, Hsinchu Science Park, Hsinchu 30077', city='Hsinchu', state='na',
                    zip=30077, country='Taiwan')
    asset_8 = Assets(assetid=1, type='switch', commonname='3rd_fl_switch', expired='n/a', modelnum='as4610',
                    modelid='as4610', swversion='2.0.0.100', serialno='m120879498', longtitude='41.234567',
                    latitude='120.897686', ip='192.168.2.122', netmask='255.255.255.0', ip6='n/a', pos_inrack=2,
                    rackid=1, rowid=1, roomid=1, fl_sessid=3, addrid=4, siteid=2, corpid=1,
                    address='1 Creation Rd 3, Hsinchu Science Park, Hsinchu 30077', city='Hsinchu', state='na',
                    zip=30077, country='Taiwan')
    asset_9 = Assets(assetid=1, type='switch', commonname='4th_fl', expired='n/a', modelnum='as4610', modelid='as4610',
                    swversion='2.0.0.100', serialno='m120879498', longtitude='41.234567', latitude='120.897686',
                    ip='10.3.0.7', netmask='255.255.255.0', ip6='n/a', pos_inrack=2, rackid=1, rowid=1, roomid=1,
                    fl_sessid=4, addrid=4, siteid=2, corpid=1,
                    address='1 Creation Rd 3, Hsinchu Science Park, Hsinchu 30077', city='Hsinchu', state='na',
                    zip=30077, country='Taiwan')

    asset_10 = Assets(assetid=1, type='switch', commonname='1st_fl', expired='n/a', modelnum='as4610', modelid='as4610',
                     swversion='2.0.0.100', serialno='m120879498', longtitude='41.234567', latitude='120.897686',
                     ip='10.3.0.9', netmask='255.255.255.0', ip6='n/a', pos_inrack=2, rackid=1, rowid=1, roomid=1,
                     fl_sessid=1, addrid=5, siteid=3, corpid=1, address='No. 2-107 Wucheng Rd., Taizhong 403',
                     city='Taizhong', state='na', zip=403, country='Taiwan')

    asset_11 = Assets(assetid=1, type='switch', commonname='1st_fl', expired='n/a', modelnum='as4610', modelid='as4610',
                     swversion='2.0.0.100', serialno='m120879498', longtitude='41.234567', latitude='120.897686',
                     ip='10.3.0.102', netmask='255.255.255.0', ip6='n/a', pos_inrack=2, rackid=1, rowid=1, roomid=1,
                     fl_sessid=1, addrid=6, siteid=4, corpid=1,
                     address='3rd Fl, No. 3 NanKer Rd 3, Tainan industrial Science Park, Tainan 74147', city='Tainan',
                     state='na', zip=74147, country='Taiwan')

    # Create store list
    #assets_list = [asset_1, asset_2, asset_3, asset_4, asset_5, asset_6, asset_7, asset_8, asset_9, asset_10, asset_11]

    # Call bulk_create to create records in a single call
    # Store.objects.bulk_create(store_list)

    # Loop over each store and invoke save() on each entry
    # save() method called on each list member to create record
    #for store in assets_list:
    #    store.save()
