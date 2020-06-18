exports.url ="http://localhost/lab-website/hp/hp.html";
exports.loop = [{
check: function(){
	return true;
},
next: function() {
	const first0 = document.querySelector("html > body > div:nth-of-type(3) > div > div:nth-of-type(2) > a:nth-of-type(3)");
	first0.click();
}
},
{
check: function(){
	return true;
},
next: function() {
	const first1 = document.querySelector("html > body > div:nth-of-type(3) > div > div:nth-of-type(2) > a:nth-of-type(2)");
	first1.click();
}
},
{
check: function(){
	return true;
},
next: function() {
	const first2 = document.querySelector("html > body > div:nth-of-type(3) > div > div:nth-of-type(2) > ");
	first2.click();
}
}];