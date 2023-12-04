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

function hover(){
   this.style.backgroundColor = 'rgba(223, 223, 223, 0.92)'
}
function hover_out(){
   this.style.backgroundColor = 'white'
}

// Add event listeners
radio1.addEventListener('change', function() {
  if (radio1.checked) {
    yes.removeEventListener('mouseover', hover)
    yes.removeEventListener('mouseout', hover_out)
    other.classList.remove('do_not_show')
    resolved.style.marginBottom = '0px'
    yes.style.backgroundColor = 'rgba(223, 223, 223, 0.92)'
    yes.style.border = '2px solid black'
    no.style.backgroundColor = 'white'
    no.style.border = '1px solid black'
    no.addEventListener('mouseover', hover)
    no.addEventListener('mouseout', hover_out )

  }
});


// fix this issue 

radio2.addEventListener('change', function() {
  if (radio2.checked) {
    no.removeEventListener('mouseover', hover)
    no.removeEventListener('mouseout', hover_out)
    other.classList.add('do_not_show')
    resolved.style.marginBottom = '24px'
    no.style.backgroundColor = 'rgba(223, 223, 223, 0.92)'
    no.style.border = '2px solid black'
    yes.style.backgroundColor = 'white'
    yes.style.border = '1px solid black'
    yes.addEventListener('mouseover', hover)
    yes.addEventListener('mouseout', hover_out )
  }
});


// depending on choice of people involved, add the amount of people to fill in ///////////////////////////////////////////////////////////////////


let people_involved = document.getElementById("people_involved");

const people_involved_form = document.querySelector('[form-witness]')

  
const potential_people_involved =[...people_involved_form.querySelectorAll('[witness-step]')]

potential_people_involved.forEach(element => {
        // element.classList.add('do_not_show !important')
        element.remove()
    })

people_involved.addEventListener("change", function() {
  // Get the value of the selected option
  let selectedOption = this.value
  console.log(selectedOption)

  const selector_wit = document.getElementById('people_involved')
    
  if (selectedOption == 0){
      potential_people_involved.forEach(element => {
          // element.classList.add('do_not_show !important')
          element.remove()
      })

      selector_wit.style.marginBottom = '40px'
      
  }else if (selectedOption == 1){
      potential_people_involved.forEach(element => {
          element.remove()
      })
      
      people_involved_form.appendChild(potential_people_involved[0])

      selector_wit.style.marginBottom = '10px'

  }else if (selectedOption == 2){
      potential_people_involved.forEach(element => {
          element.remove()
      })
      people_involved_form.appendChild(potential_people_involved[0])
      people_involved_form.appendChild(potential_people_involved[1])

      selector_wit.style.marginBottom = '10px'

  } else if(selectedOption == 3){
      potential_people_involved.forEach(element => {
          element.remove()
      })
      people_involved_form.appendChild(potential_people_involved[0])
      people_involved_form.appendChild(potential_people_involved[1])
      people_involved_form.appendChild(potential_people_involved[2])

      selector_wit.style.marginBottom = '10px'
      
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


//  arrival part


const fire = document.getElementById('the_fireAlarm')



