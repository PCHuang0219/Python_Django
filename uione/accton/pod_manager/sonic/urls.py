from django.urls import include, path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.index, name='sonic'),
    path('supported-devices',views.supported_devices, name="supported devices list"),
    path('advantage',views.advantage, name="advantage"),
    path('products',views.products, name="products"),
    path('wheretobuy',views.wheretobuy, name="where to buy"),
    path('sales_contact',views.sales_contact, name="sales contact"),
    path('buynow',views.buynow, name="buy now"),
    
    path('products/10g',views.products10g, name="10g"),
    path('products/25g',views.products25g, name="25g"),
    path('products/40g',views.products40g, name="40g"),
    path('products/100g',views.products100g, name="100g"),
    path('products/400g',views.products400g, name="400g"),

    path('products/10g/as5512-54x',views.products10g1, name="products10g1"),
    path('products/10g/as5712-54x',views.products10g2, name="products10g2"),
    path('products/10g/as5812-54t',views.products10g3, name="products10g3"),
    path('products/10g/as5812-54x',views.products10g4, name="products10g4"),

    path('products/25g/as7312-54xs',views.products25g1, name="products25g1"),
    path('products/25g/as7326-56x',views.products25g2, name="products25g2"),

    path('products/40g/as6700-32x',views.products40g1, name="products40g1"),
    path('products/40g/as6701-32x',views.products40g2, name="products40g2"),
    path('products/40g/as6712-32x',views.products40g3, name="products40g3"),
    path('products/40g/as6812-32x',views.products40g4, name="products40g4"),

    path('products/100g/as7712-32x',views.products100g1, name="products100g1"),
    path('products/100g/as7726-32x',views.products100g2, name="products100g2"),
    path('products/100g/as7816-64x',views.products100g3, name="products100g3"),
    path('products/100g/wedge100bf-32x',views.products100g4, name="products100g4"),
    path('products/100g/wedge100bf-65x',views.products100g5, name="products100g5"),
    path('products/100g/wedge100s-32x',views.products100g6, name="products100g6"),

    path('products/400g/as8000',views.products400g1, name="products400g1"),
    path('products/400g/as9716-32d',views.products400g2, name="products400g2"),
    
    path('accton/download',views.download, name="download"),
    path('accton/download/learn_more',views.learn_more, name="learn more"),
    path('accton/faq',views.faq, name="faq"),
    path('accton/kb',views.knowledgebase, name="knowledgebase"),
    path('accton/forum',views.forum, name="forum"),
    path('accton/videos',views.video, name="video"),
    path('accton/webinar',views.webinar, name="webinar"),
    path('accton/sonic_now',views.sonic_now, name="sonic_now"),
    path('accton',views.accton, name="accton"),
    path('accton/contact_us',views.contactus, name="contact us"),

    

    path('accton/wiki',views.wiki, name="wiki"),
    path('accton/wiki/data_center',views.data_center, name="wiki-data center"),
    path('accton/wiki/network_switch',views.network_switch, name="wiki-network switch"),
    path('accton/wiki/sonic_wiki',views.sonic_wiki, name="sonic"),
    path('accton/wiki/onie',views.onie, name="onie"),
    path('accton/wiki/leaf-spine',views.leaf_spine, name="leaf spine"),
    path('accton/wiki/wiki_mainpage',views.wiki_mainpage, name="leaf spine"),
    path('accton/wiki/network_operating_system',views.network_operating_system, name="net os"),
    path('accton/wiki/open_source_sdn',views.open_source_sdn, name="sdn"),
    path('accton/wiki/open_source_SDN',views.open_source_sdn, name="sdn"),
    path('accton/wiki/index_wiki',views.index_wiki, name="wiki index"),
    path('accton/wiki/glossary',views.glossary, name="glossary"),

    path('accton/resources/whitepaper',views.whitepaper, name="whitepaper"),


    path('roadmap',views.roadmap, name="road_map"),
    path('support',views.support, name="support"),
    path('accton/forum/newArticle',login_required(views.newArticle), name="newArticle"),
    path('accton/forum/showArticle',views.showArticle, name="showArticle"),
    
    path('data/platformList/',views.get_platform_list),
    path('data/documentList/',views.get_document_list),
    path('data/videoList/',views.get_video_list),
    
    path('forum/postNewArticle/',views.post_new_article),
    path('forum/getArticleList/',views.get_article_list_forum),
    path('forum/getArticleListLength/',views.get_article_list_length),
    path('forum/getArticle/',views.get_article),
    path('forum/getArticleMessage/',views.get_article_message),
    path('forum/postNewReply/',login_required(views.post_new_reply)),
    path('forum/putMessageAwesome/',views.put_message_awesome),
    path('forum/putMessageBad/',views.put_message_bad),
    path('forum/deleteMessageAwesome/',views.delete_message_awesome),
    path('forum/deleteMessageBad/',views.delete_message_bad),
    path('forum/getJudgeMessage/',views.get_judge_message),
    path('forum/putArticleViews/',views.put_article_views),
    path('forum/getAllTagName/',views.get_all_tag_name),
    path('downloads/getSonicImageVersionData/',views.get_sonic_image_version_data),
    path('downloads/getAcctonSonicImage/',views.get_accton_sonic_image),


    path('carrier_access',views.carrier_access, name="carrier access"),
    path('iot',views.iot, name="IoT Integration"),
    path('ioT',views.iot, name="IoT Integration"),
    path('Iot',views.iot, name="IoT Integration"),
    path('IoT',views.iot, name="IoT Integration"),
    path('sd_wan',views.sd_wan, name="sd wan"),

    path('about_us',views.introduction, name="same as introduction"),
    path('about_us/introduction',views.introduction, name="introduction"),
    path('about_us/arts_foundation',views.art, name="Accton Arts Foundation"),
    path('about_us/charitable',views.charitable, name="charitable"),
    path('about_us/news',views.news, name="news"),
    path('about_us/investor',views.investor, name="investor"),
    
    path('about_us/news/20190528',views.news20190528, name="news20190528"),
    path('about_us/news/20190522',views.news20190522, name="news20190522"),
    path('about_us/news/20190521',views.news20190521, name="news20190521"),
    path('about_us/news/20190418',views.news20190418, name="news20190418"),
    path('about_us/news/20190314',views.news20190314, name="news20190314"),
    path('about_us/news/20190225',views.news20190225, name="news20190225"),
    path('about_us/news/20190225-2',views.news20190225_2, name="news20190225-2"),

    path('about_us/investor/q&full2018',views.qfull2018, name="Quarter and Full Year 2018 Results"),
    
    path('get/partnersData/',views.get_partners_data),
]

