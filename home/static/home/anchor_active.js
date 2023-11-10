function dodajAktywne(year) {
	// get all 'a' elements
	var a = document.getElementsByTagName('a');
	// loop through all 'a' elements
	for (i = 0; i < a.length; i++) {
		// Remove the class 'active' if it exists
		a[i].classList.remove('active');
		// add 'active' classs to the element that was clicked
		if (a[i].innerHTML === year) {
			elem.classList.add('active');
		}
	}
}

dodajAktywne('2004');
