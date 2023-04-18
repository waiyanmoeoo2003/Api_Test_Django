from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings
import os
import csv

def get_challenges(request):
    challenges_list = []

    file_path = os.path.join(settings.BASE_DIR,'API_TEST.csv')

    with open(file_path,'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            temp = {'id':row[0],'challenge_name':row[1],'challenge_success_rate':row[2]}
            challenges_list.append(temp)

    response_data = {'status':'success','data':challenges_list}
    return JsonResponse(response_data, status=200)


def get_challenge_by_id(request,id):
    challenge_data = {}

    file_path = os.path.join(settings.BASE_DIR,'API_TEST.csv')

    with open(file_path,'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            if int(row[0]) == id:
                challenge_data = {'id':row[0],'challenge_name':row[1],'challenge_success_rate':row[2]}
    
    if challenge_data:
        response_data = {'status':'success','data':challenge_data}
        return JsonResponse(response_data, status=200)
    else:
        response_data = {'status':'failed','data':[]}
        return JsonResponse(response_data, status=200)
        


    