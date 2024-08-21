function nextStep(step) {
    document.querySelectorAll('.checkout-step').forEach(function (element) {
        element.style.display = 'none';
    });
    document.getElementById('step-' + step).style.display = 'block';
    updateProgressBar(step);
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
