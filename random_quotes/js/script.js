// Assumed to make an ajax request. Afte
// I assume the index.html loaded and the quotes.js is created anew,
// the script.js does not have access to it anymore.


//New qoute generated after timeout
const refreshTimer = () => intervalId  = setTimeout(printQuote, 30000);

function getRandomRGB() {
	const red = Math.floor(Math.random()* 256);
	const green = Math.floor(Math.random()* 256);
	const blue = Math.floor(Math.random()* 256);
	return rgbColor = 'rgb(' + red + ',' + green + ',' + blue + ')';
}

console.log(quotes);

//calls getRandomQuote function and stores it in a variable
function printQuote() {
	var quote = quotes.quote;
	const backgroundRGB = getRandomRGB();
	var message = '';
	print(quote)
	message += '<p class="quote">' + quote.quote + '</p>';
	message += '<p class="source">' + quote.source + '';
	if (quote.citation !== '') {
		message += '<span class="citation">' + quote.citation + '</span>';
	}
	if (quote.year !== '') {
		message += '<span class="year">' + quote.year + '</span>';
	}
	message += '</p>';
	document.getElementById('quote-box').innerHTML = message;
	document.body.style.backgroundColor = backgroundRGB;
}
