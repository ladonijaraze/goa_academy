const questions = [
    {
        question: "Which language is used for web development?",
        answers: ["Python", "Java", "JavaScript", "C++"],
        correct: 2
    },
    {
        question: "Which language was developed by Guido van Rossum?",
        answers: ["C", "Java", "Python", "Ruby"],
        correct: 2
    },
    {
        question: "Which language is mainly used for Android app development?",
        answers: ["C#", "Swift", "Kotlin", "PHP"],
        correct: 2
    },
    {
        question: "Which language is known for its ease of use and readability?",
        answers: ["JavaScript", "Go", "Python", "C"],
        correct: 2
    },
    {
        question: "Which language was created by Bjarne Stroustrup?",
        answers: ["C#", "Java", "C++", "Swift"],
        correct: 2
    }
];

let currentQuestionIndex = 0;
let correctAnswers = 0;

function startGame() {
    currentQuestionIndex = 0;
    correctAnswers = 0;
    document.getElementById('result-container').classList.add('hidden');
    document.getElementById('question-container').classList.remove('hidden');
    showQuestion();
}

function showQuestion() {
    const question = questions[currentQuestionIndex];
    document.getElementById('question').textContent = question.question;
    const answerButtons = document.querySelectorAll('.answer-btn');
    
    for (let i = 0; i < answerButtons.length; i++) {
        answerButtons[i].textContent = question.answers[i];
    }
}

function checkAnswer(answerIndex) {
    const question = questions[currentQuestionIndex];
    if (answerIndex === question.correct) {
        correctAnswers++;
    }

    currentQuestionIndex++;

    if (currentQuestionIndex < questions.length) {
        showQuestion();
    } else {
        showResults();
    }
}

function showResults() {
    document.getElementById('question-container').classList.add('hidden');
    const resultText = `You got ${correctAnswers} out of ${questions.length} correct!`;
    document.getElementById('correct-answers').textContent = correctAnswers;
    document.getElementById('result-container').classList.remove('hidden');
}

function startNewGame() {
    startGame();
}

startGame();
