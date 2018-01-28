
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
    myQuestions.forEach((currentQuestion, questionNumber) => {
      if (questionNumber === 0){
      	output.push(
        // Change to IMG Tag
        `<div class="slide">
        	<p style="color: #fff">Place Demonstration Card in front of subject. The distance should be the distance to the elbow of the subject's arm when his fist rests on his chin. Ask the tester to call out the numbers on the screen as quickly as possible from left to right following the arrows on the demonstration card.</p>
          <br>
          <p style="color: #fff">When you feel the tester understands the process, start the screening procedure</p>
          <img class = question src="${currentQuestion.link}"/>
         </div>`
      );	
      }
      else
      {
      	output.push(
        // Change to IMG Tag
        `<div class="slide">
        	<img class = question src="${currentQuestion.link}"/> 	
         </div>`
      );	
      }

      
    });

    // finally combine our output list into one string of HTML and put it on the page
    quizContainer.innerHTML = output.join("");
  }

  function showSlide(n) {
    slides[currentSlide].classList.remove("active-slide");
    
    nextButton.style.display = "inline-block";
    previousButton.style.display = "inline-block";

    if(n === 0)
    {
      previousButton.style.display = "none";
    }
    if(n === myQuestions.length - 1){
      nextButton.style.display = "none";
    }
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

  function showPreviousSlide(){
    showSlide(currentSlide - 1);
  }

  const quizContainer = document.getElementById("quiz");
  // display quiz right away
  buildQuiz();

  const nextButton = document.getElementById("next");
  const previousButton = document.getElementById("previous");
  const slides = document.querySelectorAll(".slide");
  let currentSlide = 0;

  showSlide(0);

  // on submit, show results
  nextButton.addEventListener("click", showNextSlide);
  previousButton.addEventListener("click", showPreviousSlide);

})();