// code for form to move back and forth when I press next or previous 

const multiStepForm = document.querySelector('[data-multi-step]')

const formSteps = [...multiStepForm.querySelectorAll("[data-step]")]



let currentStep = formSteps.findIndex(step => {
    return step.classList.contains("active")
})

// showCurrentStep(currentStep)

if (currentStep < 0){
    currentStep = 0
    formSteps[currentStep].classList.add("active")
    showCurrentStep()
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

const other = document.getElementById('resolved_other')

// Add event listeners
radio1.addEventListener('change', function() {
  if (radio1.checked) {
    other.classList.remove('do_not_show')
  }
});

radio2.addEventListener('change', function() {
  if (radio2.checked) {
    other.classList.add('do_not_show')
  }
});


