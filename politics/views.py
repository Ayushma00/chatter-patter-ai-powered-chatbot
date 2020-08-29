from django.shortcuts import render
from . import politics

def politics_bot(request):
    if request.session.get('ques4') is None:
        request.session['ques4'] = []
        request.session['ans4'] = []
        ques=[]
        ans=[]
    if request.method == "POST":
        if request.POST['button'] == 'Clear History':
            request.session['ques4'] = []
            request.session['ans4'] = []
            ques= []
            ans= []
        else:
            user_ques = request.POST.get('ques')
            bot_ans = politics.chatbot_response(user_ques)
            ques = request.session['ques4']
            ques.append(user_ques)
            request.session['ques4'] = ques
            ans = request.session['ans4']
            ans.append(bot_ans)
            request.session['ans4'] = ans    
    fuse = zip(request.session['ques4'], request.session['ans4'])
    return render(request, 'politics/index.html', {'fuse': fuse})
