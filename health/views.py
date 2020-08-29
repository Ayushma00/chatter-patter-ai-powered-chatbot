from django.shortcuts import render
from . import health

def health_bot(request):
    if request.session.get('ques3') is None:
        request.session['ques3'] = []
        request.session['ans3'] = []
        ques=[]
        ans=[]
    if request.method == "POST":
        if request.POST['button'] == 'Clear History':
            request.session['ques3'] = []
            request.session['ans3'] = []
            ques= []
            ans= []
        else:
            user_ques = request.POST.get('ques')
            bot_ans = health.chatbot_response(user_ques)
            ques = request.session['ques3']
            ques.append(user_ques)
            request.session['ques3'] = ques
            ans = request.session['ans3']
            ans.append(bot_ans)
            request.session['ans3'] = ans    
    fuse = zip(request.session['ques3'], request.session['ans3'])
    return render(request, 'health/index.html', {'fuse': fuse})
