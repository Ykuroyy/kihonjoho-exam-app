from flask import render_template, session, request, redirect, url_for, flash
import uuid
from app.exam import bp
from app.models import Question, UserAnswer, Choice
from app import db
from collections import defaultdict

@bp.route('/questions')
def question_list():
    if 'session_id' not in session:
        session['session_id'] = str(uuid.uuid4())
    
    category = request.args.get('category')
    if category:
        questions = Question.query.filter_by(category=category).order_by(Question.number).all()
    else:
        questions = Question.query.order_by(Question.number).all()
    
    return render_template('exam/question_list.html', questions=questions)

@bp.route('/question/<int:question_id>')
def question_detail(question_id):
    if 'session_id' not in session:
        session['session_id'] = str(uuid.uuid4())
    
    question = Question.query.get_or_404(question_id)
    
    # 既に解答済みかチェック
    session_id = session['session_id']
    existing_answer = UserAnswer.query.filter_by(
        session_id=session_id,
        question_id=question_id
    ).first()
    
    show_result = False
    is_correct = False
    correct_choice = None
    
    if existing_answer:
        show_result = True
        is_correct = existing_answer.is_correct
        correct_choice = Choice.query.filter_by(
            question_id=question_id,
            is_correct=True
        ).first()
    
    # 次の問題を取得
    next_question = Question.query.filter(
        Question.number > question.number
    ).order_by(Question.number).first()
    
    return render_template('exam/question_detail.html',
                         question=question,
                         show_result=show_result,
                         is_correct=is_correct,
                         correct_choice=correct_choice,
                         next_question=next_question)

@bp.route('/question/<int:question_id>/submit', methods=['POST'])
def submit_answer(question_id):
    if 'session_id' not in session:
        session['session_id'] = str(uuid.uuid4())
    
    question = Question.query.get_or_404(question_id)
    choice_id = request.form.get('choice_id')
    
    if not choice_id:
        flash('選択肢を選んでください。', 'error')
        return redirect(url_for('exam.question_detail', question_id=question_id))
    
    choice = Choice.query.get_or_404(choice_id)
    session_id = session['session_id']
    
    # 既存の解答をチェック
    existing_answer = UserAnswer.query.filter_by(
        session_id=session_id,
        question_id=question_id
    ).first()
    
    if not existing_answer:
        # 新規解答
        answer = UserAnswer(
            session_id=session_id,
            question_id=question_id,
            selected_choice_id=choice_id,
            is_correct=choice.is_correct
        )
        db.session.add(answer)
        db.session.commit()
    
    return redirect(url_for('exam.question_detail', question_id=question_id))

@bp.route('/results')
def my_results():
    if 'session_id' not in session:
        session['session_id'] = str(uuid.uuid4())
    
    session_id = session['session_id']
    user_answers = UserAnswer.query.filter_by(session_id=session_id)\
        .join(Question).order_by(Question.number).all()
    
    total_questions = len(user_answers)
    correct_answers = sum(1 for answer in user_answers if answer.is_correct)
    
    # カテゴリー別集計
    category_stats = defaultdict(lambda: {'total': 0, 'correct': 0})
    for answer in user_answers:
        category = answer.question.category
        category_stats[category]['total'] += 1
        if answer.is_correct:
            category_stats[category]['correct'] += 1
    
    return render_template('exam/results.html', 
                         user_answers=user_answers,
                         total_questions=total_questions,
                         correct_answers=correct_answers,
                         category_stats=dict(category_stats))

@bp.route('/reset-session', methods=['POST'])
def reset_session():
    if 'session_id' in session:
        # 現在のセッションの解答を削除
        UserAnswer.query.filter_by(session_id=session['session_id']).delete()
        db.session.commit()
        
        # 新しいセッションIDを生成
        session['session_id'] = str(uuid.uuid4())
        flash('成績をリセットしました。', 'success')
    
    return redirect(url_for('exam.question_list'))