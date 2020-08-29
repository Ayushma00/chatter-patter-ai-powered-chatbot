from django.shortcuts import render
from . import economics

def economics_bot(request):
    if request.session.get('ques2') is None:
        request.session['ques2'] = []
        request.session['ans2'] = []
        ques=[]
        ans=[]
    if request.method == "POST":
        if request.POST['button'] == 'Clear History':
            request.session['ques2'] = []
            request.session['ans2'] = []
            ques= []
            ans= []
        else:
            user_ques = request.POST.get('ques')
            bot_ans = economics.chatbot_response(user_ques)
            ques = request.session['ques2']
            ques.append(user_ques)
            request.session['ques2'] = ques
            ans = request.session['ans2']
            ans.append(bot_ans)
            request.session['ans2'] = ans
    fuse = zip(request.session['ques2'], request.session['ans2'])
    return render(request, 'economics/index.html', {'fuse': fuse})
