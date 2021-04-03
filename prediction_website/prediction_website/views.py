from django.shortcuts import render

def home(request):
    return render(request, 'index.html')


def getPredictions(request):
    if request.method=='POST':
        print('yesssssss')
        a = request.POST.get('symptom_one')
        b = request.POST.get('symptom_two')
        c = request.POST.get('symptom_three')
        d = request.POST.get('symptom_four')
        e = request.POST.get('symptom_five')
        f = request.POST.get('symptom_six')
        predict_input = [a,b,c,d,e,f,0,0,0,0,0,0,0,0,0,0,0]
        print(predict_input)
    return render(request, 'predict.html', {'a':'helloooooooooooo'})

    # import pickle
    # model = pickle.load(open())
    # scaled = pickle.load(open())
    # prediction = model.predict()

def covidPredict(request):
    if request.method=='POST':
        a = request.POST.get('symptom_1')
        b = request.POST.get('symptom_2')
        c = request.POST.get('symptom_3')
        d = request.POST.get('symptom_4')
        e = request.POST.get('symptom_5')
        f = request.POST.get('Abroad travel')
        g = request.POST.get('Contact with COVID Patient')
        h = request.POST.get('Attended Large Gathering')
        i = request.POST.get('Visited Public Exposed Places')
        j = request.POST.get('Family working in Public Exposed Places')
        covid_input = [a,b,c,d,e,f,g,h,i,j]
        print(covid_input)
    return render(request, 'covid.html', {'b':'covid'})
        

def result(request):
    return None