from django.shortcuts import render
from . import culture

def culture_bot(request):
    if request.session.get('ques1') is None:
        request.session['ques1'] = []
        request.session['ans1'] = []
        ques=[]
        ans=[]
    if request.method == "POST":
        if request.POST['button'] == 'Clear History':
            request.session['ques1'] = []
            request.session['ans1'] = []
            ques= []
            ans= []
        else:
            user_ques = request.POST.get('ques')
            bot_ans = culture.chatbot_response(user_ques)
            ques = request.session['ques1']
            ques.append(user_ques)
            request.session['ques1'] = ques
            ans = request.session['ans1']
            ans.append(bot_ans)
            request.session['ans1'] = ans
    fuse = zip(request.session['ques1'], request.session['ans1'])
    return render(request, 'culture/index.html', {'fuse': fuse})
