# Testing 

Testing was done site-wide, all tests undertaken are shown below: 

## Contents 

- [Functional Testing](#functional-testing)
- [WAVE](#wave)
- [Validator Testing](#validator-testing)
  + [HTML](#html)
  + [CSS](#CSS)
  + [JavaScript](#javascript)
  + [PEP8](#pep8-online)
- [Lighthouse](#lighthouse)
  + [Desktop Results](#desktop-results)
  + [Mobile Results](#mobile-results)
- [Colour Contrast](#colour-contrast)
- [Browser Compatibility](#browser-compatibility)
- [Responsivity](#responsivity)
- [Stripe](#stripe)
  + [Dummy Card Information](#dummy-card-information)
- [Issues/ Bugs Found & Resolved](#issues-bugs-found-resolved)

## Functional Testing 

![Functional Tests User](documents/images/functional_testing/functional_test_1.png)

![Functional Tests Admin](documents/images/functional_testing/functional_test_2.png)

Please follow this [link](https://docs.google.com/spreadsheets/d/1xx5Dkv36HNJfljd7qT-q4SbN8Jt4fcDM39XUS-Ybc3o/edit?usp=drive_link) to spreadsheet of all functional testing carried out, click the Testing tab if the screenshots are not clear.

## WAVE

## Validator Testing

### HTML

[W3C HTML Validator link](https://validator.w3.org/)

### CSS

[W3C CSS Validator link](https://jigsaw.w3.org/css-validator/#validate_by_input+with_options)

### JavaScript

[JSHint](https://jshint.com/)

- Both files were Tested, they highlighted minimal issues and pulled errors with the Materialize script.

### PEP8

[PEP8](http://ww7.pep8online.com/)

- This validation tested python code, in the app.py and was used throughout the development giving key indications of what was not compliant and the reason for this. This helped keep the code clean and readable throughout the development.

## Ligthouse

[Lighthouse](https://developer.chrome.com/docs/lighthouse/)

Lighthouse, a powerful Chrome DevTools feature, provided invaluable insights into the functionality, layout, and overall readability of my site. It allowed me to evaluate key aspects such as performance, accessibility, and best practices, ensuring a seamless and engaging user experience. By analyzing the site’s structure and styles, Lighthouse highlighted areas where the layout could be optimized for various screen sizes, helping to create a responsive design that looks great on all devices.

### Desktop Results

### Mobile Results

## Colour Contrast 

## Responsivity

- Point > Point, is made easily accessible on all devices with help from the Materialize framework. Test through Google Developer Tools, on devices: 
    - iPhone SE
    - iPhone XR
    - Pixel 5
    - Samsung S8+
    - iPad Mini
    - iPad Air 
    - iPad Pro
    - Surface Duo

- The site was also tested for full responsive functionality manually on the below devices: 
    - Asus Zenbook
    - Google Pixel 7 pro
    - ASUS ZenScreen (portable screen)
    - Macbook Pro

## Stripe
### Dummy Card Information

The following test card details were used for testing Stripe:

  | **Field**    | **Value**              |
  |--------------|------------------------|
  | **Card Number** | 4242 4242 4242 4242   |
  | **Date**     | 04/42                  |
  | **CVC**      | 242                    |
  | **Postcode** | 42424                  |

## Issues/ Bugs Found & Resolved