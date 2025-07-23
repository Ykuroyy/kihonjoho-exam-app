from flask import render_template, session, request, redirect, url_for, flash
from app.exam import bp
from app.data import get_all_questions, get_question_by_id, get_questions_by_category, get_correct_choice
from collections import defaultdict

@bp.route('/questions')
def question_list():
    # セッションで解答状態を初期化
    if 'answers' not in session:
        session['answers'] = {}
    
    category = request.args.get('category')
    if category:
        questions = get_questions_by_category(category)
    else:
        questions = get_all_questions()
    
    return render_template('exam/question_list.html', questions=questions)

@bp.route('/question/<int:question_id>')
def question_detail(question_id):
    if 'answers' not in session:
        session['answers'] = {}
    
    question = get_question_by_id(question_id)
    if not question:
        flash('問題が見つかりません。', 'error')
        return redirect(url_for('exam.question_list'))
    
    # 既に解答済みかチェック
    show_result = str(question_id) in session['answers']
    is_correct = False
    correct_choice = get_correct_choice(question)
    
    if show_result:
        selected_choice_symbol = session['answers'][str(question_id)]
        is_correct = selected_choice_symbol == correct_choice['symbol']
    
    # 次の問題を取得
    all_questions = get_all_questions()
    next_question = None
    for i, q in enumerate(all_questions):
        if q['id'] == question_id and i + 1 < len(all_questions):
            next_question = all_questions[i + 1]
            break
    
    return render_template('exam/question_detail.html',
                         question=question,
                         show_result=show_result,
                         is_correct=is_correct,
                         correct_choice=correct_choice,
                         next_question=next_question)

@bp.route('/question/<int:question_id>/submit', methods=['POST'])
def submit_answer(question_id):
    if 'answers' not in session:
        session['answers'] = {}
    
    question = get_question_by_id(question_id)
    if not question:
        flash('問題が見つかりません。', 'error')
        return redirect(url_for('exam.question_list'))
    
    choice_symbol = request.form.get('choice_symbol')
    
    if not choice_symbol:
        flash('選択肢を選んでください。', 'error')
        return redirect(url_for('exam.question_detail', question_id=question_id))
    
    # セッションに解答を保存
    session['answers'][str(question_id)] = choice_symbol
    session.modified = True
    
    return redirect(url_for('exam.question_detail', question_id=question_id))

@bp.route('/results')
def my_results():
    if 'answers' not in session:
        session['answers'] = {}
    
    answers = session['answers']
    all_questions = get_all_questions()
    
    # 解答した問題のみを集計
    answered_questions = []
    correct_answers = 0
    
    for question in all_questions:
        question_id_str = str(question['id'])
        if question_id_str in answers:
            selected_symbol = answers[question_id_str]
            correct_choice = get_correct_choice(question)
            is_correct = selected_symbol == correct_choice['symbol']
            
            answered_questions.append({
                'question': question,
                'selected_symbol': selected_symbol,
                'is_correct': is_correct
            })
            
            if is_correct:
                correct_answers += 1
    
    total_questions = len(answered_questions)
    
    # カテゴリー別集計
    category_stats = defaultdict(lambda: {'total': 0, 'correct': 0})
    for answer_data in answered_questions:
        category = answer_data['question']['category']
        category_stats[category]['total'] += 1
        if answer_data['is_correct']:
            category_stats[category]['correct'] += 1
    
    return render_template('exam/results.html', 
                         answered_questions=answered_questions,
                         total_questions=total_questions,
                         correct_answers=correct_answers,
                         category_stats=dict(category_stats))

@bp.route('/reset-session', methods=['POST'])
def reset_session():
    # セッションから解答をクリア
    session.pop('answers', None)
    flash('成績をリセットしました。', 'success')
    return redirect(url_for('exam.question_list'))