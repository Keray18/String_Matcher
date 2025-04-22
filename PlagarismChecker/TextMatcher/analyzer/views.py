
from django.shortcuts import render
from .algorithms import rabin_karp, kmp

def index(request):
    return render(request, 'analyzer/index.html')

def analyze(request):
    if request.method == 'POST':
        text = request.POST['text']
        pattern = request.POST['pattern']
        algo = request.POST['algo']

        if algo == 'kmp':
            matches = kmp(pattern, text)
        else:
            matches = rabin_karp(pattern, text)

        return render(request, 'analyzer/result.html', {
            'matches': matches,
            'pattern': pattern,
            'text': text,
            'algo': algo.upper()
        })
    return render(request, 'analyzer/index.html')
