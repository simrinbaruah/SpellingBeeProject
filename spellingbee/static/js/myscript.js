document.getElementById('answerBox').addEventListener("keypress", checkEnter);

function checkEnter(event){
    if(event.keyCode == 13){
        element = document.getElementById('playGameForm');
        element.action = 'check';
    }
}

function myFunction(){
	element=document.getElementById('demo')
	if(element.innerHTML=="Hello"){
		element.innerHTML="JAVASCRIPT"
	}else{
		element.innerHTML="Hello"
	}
}

function myFunction2(){
	element=document.getElementById('demo')
	if(!(element.style.display)||element.style.display=="none"){
		element.style.display="block"
	}else{
		element.style.display="none"
	}
}

function myFunction3(){
	element=document.getElementById('pic')
	console.log(element.src)
	if(element.src=="/static/img/Spring Poster.png"){
		element.src="/static/img/dog.jpg"
	}else{
		element.src="/static/img/Spring Poster.png"
	}
}
