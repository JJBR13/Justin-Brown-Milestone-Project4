function nextStep(step) {

    var currentStep = document.getElementById('step-' + (step - 1));
    
    if (!validateStep(currentStep)) {
        return false;  // Prevent moving to the next step if validation fails
    }
    
    // Hides all steps
    document.querySelectorAll('.checkout-step').forEach(function(element) {
        element.style.display = 'none';
    });
    
    // Show the next step
    document.getElementById('step-' + step).style.display = 'block';
    
    updateProgressBar(step);
}

function validateStep(stepElement) {
    var isValid = true;
    
    // Find all required fields within the current step
    var requiredFields = stepElement.querySelectorAll('[required]');
    
    requiredFields.forEach(function(field) {
        if (!field.value) {
            field.classList.add('is-invalid');  // Highlight the field with an error
            isValid = false;
        } else {
            field.classList.remove('is-invalid');
        }
    });
    
    return isValid;
}

function prevStep(step) {
    document.querySelectorAll('.checkout-step').forEach(function (element) {
        element.style.display = 'none';
    });
    document.getElementById('step-' + step).style.display = 'block';
    updateProgressBar(step);
}

function updateProgressBar(step) {
    const progressBar = document.getElementById('progress-bar');
    let percentage = 33;
    let stepText = 'Step 1 of 3';
    
    if (step === 2) {
        percentage = 66;
        stepText = 'Step 2 of 3';
    } else if (step === 3) {
        percentage = 100;
        stepText = 'Step 3 of 3';
    }
    
    progressBar.style.width = percentage + '%';
    progressBar.setAttribute('aria-valuenow', percentage);
    progressBar.textContent = stepText;
}
