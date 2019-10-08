from django.shortcuts import render
from . import models

# Import component model class
from pod_manager.components.models import Assets


def index(request, level):
    if level == 1:
        return render(request, "components/components_level1.html")
    elif level == 2:
        return render(request, "components/components_level2.html")
    # same as level 2, in my case
    elif level == 3:
        return render(request, "components/components_level3.html")
    elif level == 4:
        return render(request, "components/components_level4.html")
    # same as level 4, in my case
    elif level == 5:
        return render(request, "components/components_level5.html")
    # my one and original one
    elif level == 6:
        return render(request, "components/components_level6.html")
        #return render(request, "components/components_level6.html")

    elif level == 7:
        return render(request, "components/components_level7.html")
    # in table format
    elif level == 8:
        #models.init_data()
        # Create a model asset instance
        #asset_101 = Assets(assetid=1001,country="Taiwan",pos_inrack = 1)
        #asset_101.save()
        a_list = Assets.objects.in_bulk()
        #type(a_list) = <class 'django.db.models.query.QuerySet'>
        pData = a_list
        #for p in a_list:

        # Outputs: <QuerySet [<Store: Corporate (San Diego,CA)>, <Store: Downtown
        # (San Diego,CA)>, <Store: Uptown (San Diego,CA)>, <Store: Midtown (San Diego,CA)>]>

        # Store.objects.in_bulk()
        # Outputs: {1: <Store: Corporate (San Diego,CA)>, 2: <Store: Downtown
        # (San Diego,CA)>, 3: <Store: Uptown (San Diego,CA)>, 4: <Store: Midtown (San Diego,CA)>}

        # Query with in_bulk() all
        #Store.objects.in_bulk()
        # Outputs: {1: <Store: Corporate (San Diego,CA)>, 2: <Store: Downtown
        # (San Diego,CA)>, 3: <Store: Uptown (San Diego,CA)>, 4: <Store: Midtown (San Diego,CA)>}

        # Compare in_bulk query to all() that produces QuerySet
        #Store.objects.all()
        # Outputs: <QuerySet [<Store: Corporate (San Diego,CA)>, <Store: Downtown
        # (San Diego,CA)>, <Store: Uptown (San Diego,CA)>, <Store: Midtown ([1San Diego,CA)>]>

        # Query to get single Store by id
        #Store.objects.in_bulk([1])
        # Outputs: {1: <Store: Corporate (San Diego,CA)>}

        # Query to get multiple Stores by id
        #Store.objects.in_bulk([2, 3])
        # Outputs: {2: <Store: Downtown (San Diego,CA)>, 3: <Store: Uptown (San Diego,CA)>}

        return render(request, "components/components_level8.html",
                                {'bodytext': "Bodytext",
                                'emptytext': True,
                                'rmmdics': a_list,
                                'val_1': request.path,
                                }
                      )
    # in JSON format
    elif level == 9:
        return render(request, "components/components_level9.html")




# request.GET.get('message')
#
#

# Create your views here.
# My default view
# def index(request):
#    return render(request, "components/components.html")

# http://127.0.0.1:8000/components/view
# My default configuration
def index0(request):
    return render(request, "components/components.html")

def index1(request):
    return render(request, "components/components_level1.html")

# Level 2: based on address(site ID = 102, location ID = 1, sometimes address includes floor number)
def index2(request):
    return render(request, "components/components_level2.html")

# Level 4: decompose location ID into floors
def index4(request):
    return render(request, "components/components_level4.html")

# Level 5: based on room concept, if zoom has too many rows, we should adjust them.
def index5(request):
    return render(request, "components/components_level5.html")


# level 1: Google map (site ID = 102)
# :8000/components/view?level=1&id=102&list=2
# :8000/components/view?level=2&id=102&list=2
# :8000/components/view?level=3&id=102&list=2
# :8000/components/view?level=4&id=102&list=2
# :8000/components/view?level=5&id=102&list=2
# :8000/components/view?level=6&id=102&list=2
# :8000/components/view?level=7&id=102&list=2
# :8000/components/view?level=8&id=102&list=2














