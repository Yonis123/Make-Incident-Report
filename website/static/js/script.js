// code for form to move back and forth when I press next or previous 

const multiStepForm = document.querySelector('[data-multi-step]')

const formSteps = [...multiStepForm.querySelectorAll("[data-step]")]

const circles = document.querySelector('[circles]')
const circle_arr = [...circles.querySelectorAll("[circle]")]





let currentStep = formSteps.findIndex(step => {
    return step.classList.contains("active")
})

// showCurrentStep(currentStep)

if (currentStep < 0){
    currentStep = 0
    formSteps[currentStep].classList.add("active")
    showCurrentStep()

    circle_arr[currentStep].style.backgroundColor = 'hwb(209 55% 5%)'
}

multiStepForm.addEventListener("click", e => { 
    let incrementor
    if (e.target.matches("[data-next]")){
        incrementor = 1
        
    } else if (e.target.matches("[data-previous]")){
        incrementor = -1
    }
        
   if (incrementor == null) return
    

    const inputs = [...formSteps[currentStep].querySelectorAll("input")]
    

    const allValid = inputs.every(input => input.reportValidity())
    

    if (allValid){
        currentStep += incrementor
        showCurrentStep()
        changeCircleColor(incrementor)
    }
})




function showCurrentStep(){
    formSteps.forEach((step, index) => {
        
        step.classList.toggle("active", index == currentStep)
        
    })
    
}



// code for when I press Yes on if the incident is revolved within the form


// add an event listener on the yes, so if its clicked, then the we will make form group we will add the class active and enables in css
// if its clicked again we will then add the class active and enables 

const radio1 = document.getElementById('resolved_yes');
const radio2 = document.getElementById('resolved_no');

const yes = document.getElementById('yes');
const no = document.getElementById('no');

const other = document.getElementById('resolved_other')
const resolved = document.getElementById('resolved_incident')


// Add event listeners
radio1.addEventListener('change', function() {
  if (radio1.checked) {
    other.classList.remove('do_not_show')
    resolved.style.marginBottom = '0px'
    yes.style.backgroundColor = 'pink'
    no.style.backgroundColor = 'white'
  }
});

radio2.addEventListener('change', function() {
  if (radio2.checked) {
    other.classList.add('do_not_show')
    resolved.style.marginBottom = '24px'
    no.style.backgroundColor = 'pink'
    yes.style.backgroundColor = 'white'

  }
});


// depending on choice of people involved, add the amount of people to fill in ///////////////////////////////////////////////////////////////////


let people_involved = document.getElementById("people_involved");


people_involved.addEventListener("change", function() {
  // Get the value of the selected option
  let selectedOption = this.value
  console.log(selectedOption)


  const people_involved_form = document.querySelector('[form-witness]')
  
  const potential_people_involved =[...people_involved_form.querySelectorAll('[witness-step]')]
    
  if (selectedOption == 0){
    potential_people_involved.forEach(element => {
        element.classList.add('do_not_show')
    })
  }else if (selectedOption == 1){
    potential_people_involved.forEach(element => {
        element.classList.add('do_not_show')
    })
    potential_people_involved[0].classList.remove('do_not_show')

  }else if (selectedOption == 2){
    potential_people_involved.forEach(element => {
        element.classList.add('do_not_show')
    })
    potential_people_involved[0].classList.remove('do_not_show')
    potential_people_involved[1].classList.remove('do_not_show')
  } else if(selectedOption == 3){
    potential_people_involved[0].classList.remove('do_not_show')
    potential_people_involved[1].classList.remove('do_not_show')
    potential_people_involved[2].classList.remove('do_not_show')
  } else{
    //we need to make a pop up that tells them to add the people names and any relevant information to the comments portion or something
  }

})



function changeCircleColor(incrementor){
//  make previous color transparent


  let previous 
  if (incrementor == -1) {
      previous = currentStep + 1
  } else{
    previous = currentStep - 1
  }

  circle_arr[previous].style.backgroundColor = 'transparent'
  circle_arr[currentStep].style.backgroundColor = 'hwb(209 55% 5%)'

}




// circle_arr[2].style.backgroundColor = 'red'

