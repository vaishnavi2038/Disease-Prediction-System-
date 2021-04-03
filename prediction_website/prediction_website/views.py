from django.shortcuts import render

def home(request):
    return render(request, 'index.html')


def getPredictions(request):
    if request.method=='POST':
        #print('yesssssss')
        request.POST.get('symptom_one')
        request.POST.get('symptom_two')
        request.POST.get('symptom_three')
        request.POST.get('symptom_four')
        request.POST.get('symptom_five')
        request.POST.get('symptom_six')
    return render(request, 'predict.html', {'a':'helloooooooooooo'})

    # '''import pickle
    # model = pickle.load(open())
    # scaled = pickle.load(open())
    # prediction = model.predict()'''

def covidPredict(request):
    if request.method=='POST':
        request.POST.get('symptom_1')
        request.POST.get('symptom_2')
        request.POST.get('symptom_3')
        request.POST.get('symptom_4')
        request.POST.get('symptom_5')
        request.POST.get('Abroad travel')
        request.POST.get('Contact with COVID Patient')
        request.POST.get('Attended Large Gathering')
        request.POST.get('Visited Public Exposed Places')
        request.POST.get('Family working in Public Exposed Places')
    return render(request, 'covid.html', {'b':'covid'})
        

def result(request):
    return None