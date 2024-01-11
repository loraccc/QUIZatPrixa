from django.shortcuts import render,redirect
from .models import Category, Question,Answer
from django.contrib import messages
import random


# Create your views here.
def quiz_category_selection(request):
    categories = Category.objects.all()
    return render(request, 'quiz_category_selection.html', {'categories': categories})

def quiz_view(request, category_id):
    category = Category.objects.get(pk=category_id)
    questions = Question.objects.filter(category=category)
    questions_list = list(questions)
    selected_questions = random.sample(questions_list, min(len(questions), 10))
    return render(request, 'quiz_template.html', {'category': category, 'questions': selected_questions})

def submit_quiz(request, category_id):
    if request.method == 'POST':
        category = Category.objects.get(pk=category_id)
        questions = Question.objects.filter(category=category)
        score = 0

        for question in questions:
            selected_answer_id = request.POST.get(f'question_{question.id}')
            print(f"Selected Answer ID for Question {question.id}: {selected_answer_id}")

            try:
                selected_answer = Answer.objects.get(pk=selected_answer_id)
                if selected_answer.is_correct:
                    score += 5
            except Answer.DoesNotExist:
                print(f"Answer with ID {selected_answer_id} does not exist.")

        if score > 0:
            messages.success(request, f'Your score is {score}')
        else:
            messages.error(request, 'You did not score any points.')

    return redirect('quiz_result')



def quiz_result(request):
    messages.success(request, 'You have completed the quiz!')
    return render(request, 'quiz_result_template.html')