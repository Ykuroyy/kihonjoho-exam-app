from app import create_app, db
from app.models import Question, Choice, UserAnswer

app = create_app()

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Question': Question, 
            'Choice': Choice, 'UserAnswer': UserAnswer}

if __name__ == '__main__':
    app.run(debug=True)