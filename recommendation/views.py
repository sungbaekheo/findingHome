from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.conf import settings

from rest_framework.decorators import api_view
from rest_framework.response import Response

from sklearn.metrics.pairwise import cosine_similarity

import pandas as pd
import pickle
import json
from .models import sentence_vectorizer, make_bigram, userInput_tokenizer

# Create your views here.
# @api_view(['POST'])
# def recommender(request):
#     with open('rec_model.pickle', 'rb') as f:
#         model = pickle.load(f)
#         print(model.wv.most_similar(request.data['input']))
#     return Response(model.wv.most_similar(request.data['input']))
def main_page(request):
    return render(request, 'kakaomap.html')

def login_page(request):
    with open('fasttext_model_uni_1220.pickle', 'rb') as f:
        global model
        model = pickle.load(f)
    with open('seoulroom_list_1220.pickle', 'rb') as f:
        global df
        df = pickle.load(f)
    global okt
    return render(request, 'login.html')

@api_view(['GET'])
def recommender(request):
    userInput = request.GET.get('userInput')
    words = userInput_tokenizer(userInput)
    input_vector = sentence_vectorizer(model.wv[words])
    cosine_similarities = cosine_similarity(list(df.vector_uni), [input_vector])
    sim_scores = list(enumerate(cosine_similarities))
    sim_scores = sorted(sim_scores, key = lambda x : x[1], reverse = True)

    rec_index = [i[0] for i in sim_scores]
    rec_index = rec_index[:10]

    recommend = df.iloc[rec_index]
    context = {
        'lat' : list(recommend['lat'].values),
        'lng' : list(recommend['lng'].values),
        'url' : list(recommend['url'].values),
        'pic' : list(recommend['picture'].values),
        'type' : list(recommend['type'].values),
        'detail' : list(recommend['detail'].values),
        }
    roomInfo = json.dumps(context)
    return render(request,'kakaomap.html', {'roomInfo' : roomInfo})
