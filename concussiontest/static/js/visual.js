
(function() {
  const myQuestions = [
    {
      link: "Did the player lose consciousness or are they unresponsive?"
    },
    {
      link: "Does player display any disorientation or inability to respond appropriately to questions?"
    },
    {
      link: "Does the player display any signs of retrograde or anterograde amnesia?"
    },
    {
      link: "Does the player display any new or persistent symptoms?"
    },
    {
      link: "Does the player display any abnormal neurological finding?"
    },
    {
      link: "Does the player display progressive, persistent or worsening symptoms?"
    }
  ];

  function buildQuiz() {
    
    const output = [];
    myQuestions.forEach((currentQuestion) => {
      output.push(
        // Change to IMG Tag
        `<div class="slide">
           <div class="question"> ${currentQuestion.link} </div>
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