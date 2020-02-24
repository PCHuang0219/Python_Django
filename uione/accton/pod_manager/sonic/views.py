from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .database.csv import Database
from .database.article import Article_Database
from .database.article_tag import *
from .database.message import *
from .utility.time import *
from .database.message_user import *
from .database.user import *
from .database.sonic_image_version import *
from .database.getDatabase import *
from ..decorators import *

database = Database()
article_database = Article_Database()
article_tag_database = Article_Tag_Database()
message_database = Message_Database()
message_user_database = Message_User_Database()
sonic_image_version_database = Sonic_Image_Version_Database()
# Create your views here.
def index(request):
    return render(request, "sonic/sonic.html")

def supported_devices(request):
    return render(request, "sonic/supported-devices.html")
def advantage(request):
    return render(request, "sonic/advantage.html")
def products(request):
    return render(request, "sonic/products.html")

# 注意注意注意！ do refactoring later
def wheretobuy(request):
    return render(request, "sonic/where-tobuy.html")
def sales_contact(request):
    return render(request, "sonic/sales_contact.html")
def buynow(request):
    return render(request, "sonic/buynow.html")
def contactus(request):
    return render(request, "sonic/accton/contactus.html")
def products10g(request):
    return render(request, "sonic/10g.html")
def products25g(request):
    return render(request, "sonic/25g.html")
def products40g(request):
    return render(request, "sonic/40g.html")
def products100g(request):
    return render(request, "sonic/100g.html")
def products400g(request):
    return render(request, "sonic/400g.html")
def products10g1(request):
    return render(request, "sonic/model/10g/as5512-54x.html")
def products10g2(request):
    return render(request, "sonic/model/10g/as5712-54x.html")
def products10g3(request):
    return render(request, "sonic/model/10g/as5812-54t.html")
def products10g4(request):
    return render(request, "sonic/model/10g/as5812-54x.html")
def products25g1(request):
    return render(request, "sonic/model/25g/as7312-54xs.html")
def products25g2(request):
    return render(request, "sonic/model/25g/as7326-56x.html")
def products40g1(request):
    return render(request, "sonic/model/40g/as6700-32x.html")
def products40g2(request):
    return render(request, "sonic/model/40g/as6701-32x.html")
def products40g3(request):
    return render(request, "sonic/model/40g/as6712-32x.html")
def products40g4(request):
    return render(request, "sonic/model/40g/as6812-32x.html")
def products100g1(request):
    return render(request, "sonic/model/100g/as7712-32x.html")
def products100g2(request):
    return render(request, "sonic/model/100g/as7726-32x.html")
def products100g3(request):
    return render(request, "sonic/model/100g/as7816-64x.html")
def products100g4(request):
    return render(request, "sonic/model/100g/wedge100bf-32x.html")
def products100g5(request):
    return render(request, "sonic/model/100g/wedge100bf-65x.html")
def products100g6(request):
    return render(request, "sonic/model/100g/wedge100s-32x.html")
def products400g1(request):
    return render(request, "sonic/model/400g/as8000.html")
def products400g2(request):
    return render(request, "sonic/model/400g/as9716-32d.html")

def video(request):
    return render(request, "sonic/accton/videos.html")
def webinar(request):
    return render(request, "sonic/accton/webinar.html")
def whitepaper(request):
    return render(request, "sonic/accton/resources/whitepaper.html")
def download(request):
    return render(request, "sonic/accton/download/download.html")
def learn_more(request):
    return render(request, "sonic/accton/download/learn_more.html")
def faq(request):
    return render(request, "sonic/accton/faq.html")
def knowledgebase(request):
    return render(request, "sonic/accton/knowledgebase.html")

@login_required(login_url='/accounts/login/')
def forum(request):
    return render(request, "sonic/accton/forum/forum.html")
    
def accton(request):
    return render(request, "sonic/accton/accton.html")
def sonic_now(request):
    return render(request, "sonic/accton/sonic_now.html")
def wiki(request):
    return render(request, "sonic/accton/wiki/data_center.html")
def roadmap(request):
    return render(request, "sonic/roadmap.html")



#--------------------------------------------------------------------
def device_future(request):
    return render(request, "sonic/device_feture.html")

@api_view(['GET'])
def get_device_data(request):
    data_list = get_device()
    return Response(data_list)

def compatible_softWare(request):
    return render(request, "sonic/compatible_sofotware.html")

@api_view(['GET'])
def get_software_data(request):
    data_list = get_software()
    return Response(data_list)

def firmware(request):
    return render(request, "sonic/firware.html")
#--------------------------------------------------------------------



def support(request):
    return render(request, "sonic/support.html")
def wiki_mainpage(request):
    return render(request, "sonic/accton/wiki/data_center.html")
def data_center(request):
    return render(request, "sonic/accton/wiki/data_center.html")
def network_switch(request):
    return render(request, "sonic/accton/wiki/network_switch.html")
def sonic_wiki(request):
    return render(request, "sonic/accton/wiki/sonic_wiki.html")
def onie(request):
    return render(request, "sonic/accton/wiki/onie.html")
def leaf_spine(request):
    return render(request, "sonic/accton/wiki/leaf_spine.html")
def open_source_sdn(request):
    return render(request, "sonic/accton/wiki/open_source_sdn.html")
def network_operating_system(request):
    return render(request, "sonic/accton/wiki/network_operating_system.html")
def index_wiki(request):
    return render(request, "sonic/accton/wiki/index_wiki.html")
def glossary(request):
    return render(request, "sonic/accton/wiki/glossary.html")

def newArticle(request):
    return render(request, "sonic/accton/forum/newArticle.html")
def showArticle(request):
    return render(request, "sonic/accton/forum/showArticle.html")

def carrier_access(request):
    return render(request, "sonic/solution/carrier_access.html")
def iot(request):
    return render(request, "sonic/solution/IoT.html")
def sd_wan(request):
    return render(request, "sonic/solution/sd_wan.html")
def introduction(request):
    return render(request, "sonic/about_us/introduction.html")
def art(request):
    return render(request, "sonic/about_us/art.html")
def charitable(request):
    return render(request, "sonic/about_us/charitable.html")
def news(request):
    return render(request, "sonic/about_us/news.html")
def investor(request):
    return render(request, "sonic/about_us/investor.html")

def news20190528(request):
    return render(request, "sonic/about_us/news/20190528.html")
def news20190522(request):
    return render(request, "sonic/about_us/news/20190522.html")
def news20190521(request):
    return render(request, "sonic/about_us/news/20190521.html")
def news20190418(request):
    return render(request, "sonic/about_us/news/20190418.html")
def news20190314(request):
    return render(request, "sonic/about_us/news/20190314.html")
def news20190225(request):
    return render(request, "sonic/about_us/news/20190225.html")
def news20190225_2(request):
    return render(request, "sonic/about_us/news/20190225_2.html")

def qfull2018(request):
    return render(request, "sonic/about_us/investor/q&full2018.html")

@login_required(login_url='/accounts/login/')
@api_view(['POST'])
def post_new_article(request):
    print(request.user.id)
    data_list = dict(request.data)
    article_title = data_list["article_title"][0]
    article_content = data_list["article_content"][0]
    article_id = article_database.create(request.user.id,article_title,article_content)
    try:
        article_tag = data_list["article_tag[]"]
        article_tag_database.create_Article_Tag(article_id,article_tag)
    except Exception as e:
        print(e)
    return Response({"status":"ok"})

@login_required(login_url='/accounts/login/')
@api_view(['POST'])
def post_new_reply(request):
    data_list = request.data
    article_id = data_list["article_id"]
    message_id = data_list["message_id"]
    content = data_list["content"]
    message_database.create_Message(request.user.id,article_id,message_id,content)
    return Response({"status":"ok"})

@api_view(['GET'])
def get_platform_list(request):
    return Response({"platformList":database.get_platform_table()})

@api_view(['GET'])
def get_document_list(request):
    return Response({"documentList":database.get_document_table()})

@api_view(['GET'])
def get_video_list(reauest):
    return Response({"videoList":database.get_video_table()})

@api_view(['GET'])
def get_article_list_forum(request):
    page_number = request.query_params.get('page_number')
    tag_name = request.query_params.get('tag_name')
    start_index = int((int(page_number)-1) * 10)
    if(tag_name == "all" or tag_name == None):
        return article_database.get_list(start_index)
    else:
        return article_database.get_list_by_tag(start_index,tag_name)

@api_view(['GET'])
def get_article_list_length(request):
    return article_database.get_list_length()

@api_view(['GET'])
def get_article(request):
    article_id = request.query_params.get('article_id')
    return article_database.get_info_by_id(article_id)

@api_view(['GET'])
def get_article_message(request):
    article_id = request.query_params.get('article_id')
    return message_database.get_message_by_article_id(article_id)

@api_view(['GET'])
def get_judge_message(request):
    article_id = request.query_params.get('article_id')
    return message_user_database.get_judge_message_by_article_id(request.user.id,article_id)

@login_required(login_url='/accounts/login/')
@api_view(['POST'])
def put_message_awesome(request):
    message_id = request.data["message_id"]
    article_id = request.data["article_id"]
    return message_database.put_message_method(request.user.id,message_id,article_id,"awesome")

@login_required(login_url='/accounts/login/')
@api_view(['POST'])
def put_article_views(request):
    article_id = request.data["article_id"]
    return article_database.put_views_by_article_id(article_id)

@login_required(login_url='/accounts/login/')
@api_view(['POST'])
def put_message_bad(request):
    message_id = request.data["message_id"]
    article_id = request.data["article_id"]
    return message_database.put_message_method(request.user.id,message_id,article_id,"bad")

@login_required(login_url='/accounts/login/')
@api_view(['POST'])
def delete_message_awesome(request):
    message_id = request.data["message_id"]
    return message_database.delete_message_method(request.user.id,message_id,"awesome")

@login_required(login_url='/accounts/login/')
@api_view(['POST'])
def delete_message_bad(request):
    message_id = request.data["message_id"]
    return message_database.delete_message_method(request.user.id,message_id,"bad")

@api_view(['get'])
def get_sonic_image_version_data(request):
    return sonic_image_version_database.get_Image_Version_data()

@sonic_download_required
@api_view(['get'])
def get_accton_sonic_image(request):
    return sonic_image_version_database.get_Image_Version_data()

@api_view(['get'])
def get_all_tag_name(request):
    return article_tag_database.get_all_tag_name()


@api_view(["GET"])
def get_partners_data(request):
    data_list = database.get_partners_data()
    return Response({"data":data_list})
