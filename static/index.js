function siatype(){
	if (document.getElementById('sia_type1').checked || document.getElementById('sia_type2').checked ){
		document.getElementById('sia1').style.display='unset';
				//document.getElementById('sia3').style.display='unset';
				document.getElementById('sia2').style.display='none';} 
				if (document.getElementById('sia_type3').checked )
					{document.getElementById('sia1').style.display='none';
				document.getElementById('sia2').style.display='unset';
				document.getElementById('sia3').style.display='unset';
			}}
function ssa(){
				if (document.getElementById('phased_yes').checked){
					document.getElementById('sia3').style.display='unset';
				} else if (document.getElementById('phased_no').checked){
					document.getElementById('sia3').style.display='none';
				}
			}

function querySIA(){
				var country=document.getElementById('country');
				var iso3=country.options[country.selectedIndex].value;

				var request=new XMLHttpRequest();
				var previousSIA=document.getElementById('previousSIA');
				request.open('POST','/querySIA',true);
				request.onload=function(){
					if (this.readyState ==4 && this.status==200){
						console.log(request.response);
						console.log(request.responseText);
						previousSIA.innerHTML=this.responseText;
					}
				}
				var data=new FormData();
				data.append('iso3',iso3)
				request.send(data);
			}


window.onload = function() {
  document.getElementById('dataform').addEventListener('submit', function() {
    Array.prototype.forEach.call(this.elements, function(el) {
      el.disabled = el.value == '';
    });
  }, false);
};


function test(){
	var request=new XMLHttpRequest()
	request.open('POST','/test')
	request.onload=function(){
		if(this.readyState==4 && this.status==200){
			console.log(request.response);
			console.log(request.responseText);
		}
	}
	request.send("lalalala");
		}

