from django.shortcuts import render, redirect, get_object_or_404
from .models import Test
from .TestForms import Testform

def tests(request):
    test = Test.objects.all() # ამის გარეშე არ მუშაობდა, მიწერდა is not iterable
    return render(request, 'tests.html', context= {'test': test})

def test(request, pk):
    test = get_object_or_404(Test, pk=pk)
    return render(request, 'test.html', context= {'test': test})
    
def create_test(request):
    testfrom = Testform
    if request.method == 'POST':
        testfrom = Testform(request.POST)
        if testfrom.is_valid:
            testfrom.save()
            return redirect('create_test')
    return render(request, 'create_test.html', context= {'form': testfrom})

def update_test(request, pk):
    test = get_object_or_404(Test, pk=pk)

    testfrom = Testform(instance=test)
    if request.method == 'POST':
        testfrom = Testform(request.POST, instance=test) 
        if testfrom.is_valid():
            testfrom.save()
            return redirect('tests') 
    return render(request, 'update_test.html', context={'form': testfrom})

def delete_test(request, pk):
    test = get_object_or_404(Test, pk=pk)
    test.delete()
    return redirect('tests')