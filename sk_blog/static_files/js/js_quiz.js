var quizStartDiv = document.getElementById('start-quiz-div')
var quizImage = document.getElementById('quiz-image')
var quizContainer = document.getElementById('quiz-container')
var quizStartBtn = document.getElementById('start-quiz-btn')
var quizNextBtn = document.getElementById('next-btn')
var quizCheckBtn = document.getElementById('check-btn')
var quizEndBtn = document.getElementById('end-btn')
var question = document.getElementById('question-quiz')
var answerCheckboxes = document.getElementsByClassName('answer')
var resultMaxpoint = document.getElementById('result-maxpoint')
var resultResult = document.getElementById('result-result')
var resultComment = document.getElementById('result-comment')

var questionsAnswers = quizJSON.questions
var currQuestion;

var currIndex = 0;
var endIndex = questionsAnswers.length;
var playerResult = 0;

// Functions

function start(){
    quizStartDiv.classList.add('hidden');
    quizImage.classList.add('hidden');
    quizNextBtn.classList.add('hidden');
    quizEndBtn.classList.add('hidden');
    quizContainer.classList.remove('hidden');
    setQuestion();
}

function check(){
    var i = 0;
    while(answerCheckboxes[i].checked != true){
        ++i;
    }
    var selected = document.getElementById('answer' + (i+1).toString() + '_label');
    var selectedNum = parseInt(answerCheckboxes[i].id.split('_')[1]);

    i = 0;
    while(currQuestion.answers[i].number != selectedNum){
        ++i;
    }

    if(currQuestion.answers[i].correct == true){
        selected.classList.add('success');
        selected.innerHTML += ' - Correct!'
        ++playerResult;
    }
    else{
        selected.classList.add('error');
        selected.innerHTML += ' - Wrong!'

        i = 0;
        while(currQuestion.answers[i].correct != true){
            ++i;
        }
        document.getElementById('answer' + (currQuestion.answers[i].number).toString() + '_label')
        .classList.add('success');
    }

    quizCheckBtn.classList.add('hidden');
    if(currIndex < endIndex-1){
        quizNextBtn.classList.remove('hidden');
    }
    else{
        quizEndBtn.classList.remove('hidden');

        resultMaxpoint.value = endIndex;
        resultResult.value = playerResult;

        switch(true) {
            case (playerResult == endIndex):
                resultComment.value = "Perfect result! Like Annie, you must be a Number One Fan!";
            break;
            case (playerResult < endIndex && playerResult >= endIndex*0.75):
                resultComment.value = "Well done! Almost perfect, you really know the King's work!";
            break;
            case (playerResult < endIndex * 0.75 && playerResult >= endIndex*0.5):
                resultComment.value = "Nice try! A little read-in and it will ne better next time!";
            break;
            case (playerResult < endIndex * 0.5 && playerResult >= endIndex*0.25):
                resultComment.value = "Not bad! After a new (re)read, it can get even better!";
            break;
            default:
                resultComment.value = "A (re)read may be useful and is always a fun!";
        }
    }
}

function next(){
    for(var i = 0; i < currQuestion.answers.length; i++){
        var curr = document.getElementById('answer' + (currQuestion.answers[i].number).toString() + '_label');
        curr.classList.remove('success');
        curr.classList.remove('error');
        answerCheckboxes[i].checked = false;
    }

    ++currIndex;
    quizNextBtn.classList.add('hidden');
    quizCheckBtn.classList.remove('hidden');
    setQuestion();
}

function setQuestion(){
    currQuestion = questionsAnswers[currIndex];
    question.innerHTML = currQuestion.number + '. ' + currQuestion.question;
    setAnswer('1');
    setAnswer('2');
    setAnswer('3');
    setAnswer('4');
}

function setAnswer(number){
    var name = 'answer' + number + '_label';
    var index = parseInt(number)-1;
    document.getElementById(name).innerHTML =
    currQuestion.answers[index].number + '. ' + currQuestion.answers[index].answer;
}

// Event listeners

quizStartBtn.addEventListener('click', () => {
    start();
});

quizCheckBtn.addEventListener('click', () => {
    check();
});

quizNextBtn.addEventListener('click', () => {
    next();
});

document.querySelectorAll('.answer').forEach(item => {
  item.addEventListener('click', event => {
    for(var i = 0; i < answerCheckboxes.length; i++){
        if(answerCheckboxes[i].id != item.id){
            answerCheckboxes[i].checked = false;
        }
    }
  })
})