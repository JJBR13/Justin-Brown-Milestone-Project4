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
