
(function() {

  const myQuestions = [
    {
    	link: "https://github.com/rafibarash/minnehack2018/blob/master/concussiontest/static/img/demonstration-card.png?raw=true"
    },
    {
    	link: "https://github.com/rafibarash/minnehack2018/blob/master/concussiontest/static/img/card1.png?raw=true"
    },
    {
    	link: "https://github.com/rafibarash/minnehack2018/blob/master/concussiontest/static/img/card2.png?raw=true"
    },
    {
    	link: "https://github.com/rafibarash/minnehack2018/blob/master/concussiontest/static/img/card3.png?raw=true"
    }
  ];

  function buildQuiz() {
    

    const output = [];
    myQuestions.forEach((currentQuestion) => {
      output.push(
        // Change to IMG Tag
        `<div class="slide">
        	<img class = question src="${currentQuestion.link}"/>
         </div>`
      );
    });

    // finally combine our output list into one string of HTML and put it on the page
    quizContainer.innerHTML = output.join("");
  }

  function showSlide(n) {
    slides[currentSlide].classList.remove("active-slide");
    if (n >= myQuestions.length){
    	nextButton.style.display = "none";
		document.getElementById("quiz").innerHTML = "You've cleared the Visual Test!"
    }
    else{
    	slides[n].classList.add("active-slide");
    	currentSlide = n;
    }
  }

  function showNextSlide() {
   	showSlide(currentSlide + 1);
  }

  const quizContainer = document.getElementById("quiz");
  // display quiz right away
  buildQuiz();

  const nextButton = document.getElementById("next");
  const slides = document.querySelectorAll(".slide");
  let currentSlide = 0;

  showSlide(0);

  // on submit, show results
  nextButton.addEventListener("click", showNextSlide);

})();