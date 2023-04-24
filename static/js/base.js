function searchBlock() {
  const searchBar = document.getElementById('search-bar');
  const search = document.getElementById('search-btn');
  const exit = document.getElementById('close');

  searchBar.classList.toggle('hide');
  search.classList.toggle('hide');
  exit.classList.remove('hide');
}

function reHide() {
  const exit = document.getElementById('close');
  const search = document.getElementById('search-btn');
  const searchBar = document.getElementById('search-bar');

  exit.classList.add('hide')
  search.classList.remove('hide');
  searchBar.classList.add('hide');
  
}

// When user click footer btn returns to top of page

function backToTop() {
  window.scrollTo({
    top: 0,
    behavior: 'smooth'
  });
}

backToTop();

  /* Makes key info sticky to top of page */
  window.addEventListener('scroll', function () {
    const scrollPosition = window.pageYOffset || document.documentElement.scrollTop || document.body
        .scrollTop || 0;
    const viewportHeight = window.innerHeight || document.documentElement.clientHeight || document.body
        .clientHeight || 0;
    const fixedTour = document.getElementById('fix-tour');

    // Check if the scroll position is greater than the viewport height
    if (scrollPosition > viewportHeight) {
        fixedTour.classList.add('position-fixed', 'top-0', 'start-0');
    } else {
        fixedTour.classList.remove('position-fixed', 'top-0', 'start-0');
    }
});