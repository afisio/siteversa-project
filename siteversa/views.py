from django.shortcuts import render

def home(request):
	return render(request, 'home.html')

def reverse(request):
	user_text = request.GET['usertext']
	words = user_text.split()
	num = len(words)
	reversed_text = user_text[::-1]
	wor = reversed_text.split()
	nums = len(wor)
	return render(request, 'reverse.html', {'revtxt':nums, 'usertext':user_text, 'reversedtext':reversed_text, 'numberofwords':num})
