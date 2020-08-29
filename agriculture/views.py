from django.shortcuts import render
from . import agriculture

def agriculture_bot(request):
    if request.session.get('ques') is None:
        request.session['ques'] = []
        request.session['ans'] = []
        ques= []
        ans= []
    if request.method == "POST":
        if request.POST['button'] == 'Clear History':
            request.session['ques'] = []
            request.session['ans'] = []
            ques= []
            ans= []
        else:
            user_ques = request.POST.get('ques')
            bot_ans = agriculture.chatbot_response(user_ques)
            ques = request.session['ques']
            ques.append(user_ques)
            request.session['ques'] = ques
            ans = request.session['ans']
            ans.append(bot_ans)
            request.session['ans'] = ans
    fuse = zip(request.session['ques'], request.session['ans'])
    return render(request, 'agriculture/index.html', {'fuse': fuse})
