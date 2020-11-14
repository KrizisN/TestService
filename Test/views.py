from django.http import HttpResponse
from django.shortcuts import render, redirect
from .form import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import *


@unauthenticated_user
def register_page(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            messages.success(request, 'Аккант был создан для' + username)
            return redirect('login')
    context = {'form': form}
    return render(request, 'accounts/register.html', context)


@unauthenticated_user
def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Имя пользователя или пароль не верны')
    context = {}
    return render(request, 'accounts/login.html', context)


def logout_page(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
@allowed_users(allow_users=['admin', 'customer'])
def home(request):
    topics = Topic.objects.all()
    context = {'topic': topics}
    return render(request, 'home.html', context)


@login_required(login_url='login')
@allowed_users(allow_users=['admin', 'customer'])
def topic(request, pk):
    test_kits = Test_kits.objects.filter(topic_id=pk)
    context = {'test_kits': test_kits}
    return render(request, 'topic_kits.html', context)


def test_ready(request, pk):
    test_kits = Test_kits.objects.get(id=pk)
    topic = Topic.objects.get(test_kits__id=pk)
    user_results = UsersTest.objects.filter(user=request.user, test_kits__test_kits_id=pk)
    if len(user_results) == 0:
        context = {'test_kits': test_kits, 'topic': topic}
        return render(request, 'ready_for_test.html', context)
    else:
        messages.info(request, 'Вы уже отвечали на этот тест!')
        return redirect('topic', topic.id)


def test_answer(request, pk):
    que = Test.objects.filter(test_kits_id=pk)
    user = request.user
    topic = Test_kits.objects.get(id=pk)
    context = {'que': que, 'user': user, 'topic': topic}
    return render(request, 'test_topic.html', context)


def testing(request, pk):
    question = Test.objects.get(id=pk)
    answer = Answer.objects.filter(question_id=pk)
    all_answer_by_user = UsersTest.objects.filter(user=request.user, test_kits=question)
    topic = Test_kits.objects.get(topic__test_kits__test__id=pk)
    print(topic)
    if len(all_answer_by_user) == 0:
        if request.method == 'POST':
            try:
                answer_id_from_user = request.POST['answer']
                answer_from_user = Answer.objects.get(id=answer_id_from_user)
                UsersTest.objects.create(user=request.user,
                                         test_kits=question,
                                         usersanswer=Answer.objects.get(id=answer_id_from_user),
                                         )
            except:
                messages.warning(request, 'Вы не выбрали вариант ответа!')
                return redirect('testing', topic.id)
            return redirect('testing', topic.id)
    else:
        messages.info(request, 'Вы уже отвечали на этот тест')
        return redirect('testing', topic.id)
    context = {'answer': answer, 'question': topic, }
    return render(request, 'test_now.html', context)


def result(request, pk, pk2):
    topic = Topic.objects.get(test_kits__id=pk2)
    all_tests = Test.objects.filter(test_kits_id=pk2)
    test_kits = Test_kits.objects.get(id=pk2)
    print(len(all_tests))
    user = User.objects.get(id=pk)
    user_results = UsersTest.objects.filter(user=user, test_kits__test_kits_id=pk2)
    print(len(user_results))
    user_correct_answer = 0
    if len(user_results) == len(all_tests):
        for i in user_results:
            if i.usersanswer.right_answer:
                user_correct_answer += 1
        per_cent_of_correct_answer = user_correct_answer / len(user_results) * 100
        context = {'user_results': len(user_results),
                   'user_correct_answer': user_correct_answer,
                   'per_cent_of_correct_answer': per_cent_of_correct_answer,
                   'test_kits': topic
                   }
        UsersResults.objects.update_or_create(user=request.user,
                                              test_kits=test_kits,
                                              all_tests=len(all_tests),
                                              right_tests=user_correct_answer)
        return render(request, 'result.html', context)
    else:
        messages.info(request, 'Сперва ответьте на все тесты')
        return redirect('testing', pk2)


def solved_tests(request, pk):
    all_solved_tests = list(set(Test_kits.objects.filter(test__answer__userstest__user__id=pk)))
    if len(all_solved_tests) > 0:
        context = {'all_solved_tests': all_solved_tests}
        return render(request, 'solved_tests.html', context)
    else:
        context = {'all_solved_tests': len(all_solved_tests)}
        return render(request, 'solved_tests.html', context)


@allowed_users(allow_users=['admin'])
def delete_test_of_student(request, pk, pk2):
    user_results = UsersTest.objects.filter(user=pk, test_kits__test_kits_id=pk2)
    user_results.delete()
    return redirect('testing', pk2)
