import json
import urllib
import urllib2
import time
from datetime import date, timedelta
import nltk
import re
from nltk.corpus import stopwords
import string
import unicodedata



n_of_articles=1000
articles=[]
today = date.today()
n_calls=0


out_file=open("articles.txt","w")






while(len(articles)<n_of_articles):

    day_to_cons = today - timedelta(days=n_calls)
    start_date = end_date = str(day_to_cons).replace("-","")
    #print start_date
    #print end_date
    myParameters = { "facet_field" : "day_of_week", "begin_date" : start_date, "end_date" : end_date, "api-key" : "90e57f838b0b4e57918c4ab531e400ce" }
    myURL = "http://api.nytimes.com/svc/search/v2/articlesearch.json?%s" % (urllib.urlencode(myParameters))
    json_str = urllib2.urlopen(myURL).read()
    full_doc = json.loads(json_str)
    response = full_doc["response"]
    docs= response["docs"]





    for article in docs:

        headline = ""
        ID=""
        abstract=""
        url = ""

        if(len(articles)>=n_of_articles):
            break;


        if(article["_id"]is not None and len(article["_id"])!=0):
            if(article["headline"]['main']is not None and len(article["headline"]['main'])!=0):
                if(article["snippet"] is not None and len(article["snippet"])!=0):
                    if(article["web_url"] is not None and len(article["web_url"])!=0):



                               headline = article["headline"]['main'].encode('utf-8')
                               ID = article["_id"].encode('utf-8')
                               abstract=article["snippet"].encode('utf-8')
                               url=article["web_url"]
                               #abstract = unicodedata.normalize('NFKD', article["snippet"]).encode('ascii','ignore')
                               #url = unicodedata.normalize('NFKD', article["web_url"]).encode('ascii','ignore')
                               #ID = unicodedata.normalize('NFKD', article["_id"]).encode('ascii','ignore')

                               if(ID not in articles):



                                        articles.append(ID)
                                        out_file.write(headline)
                                        out_file.write("|")
                                        out_file.write(abstract)
                                        out_file.write("|")
                                        out_file.write(url)
                                        out_file.write("\n")








            else: print "No info available, skipping article."



    n_calls+=1
    print "- "+str(n_calls)+" calls done, articles size = "+str(len(articles))
    print "- waiting 1 seconds, then call again."
    time.sleep(0.8)








out_file.close()
print "Aritcles saved! Check 'articles.txt' file."
