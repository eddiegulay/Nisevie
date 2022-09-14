var form = document.getElementById("planForm");

function addPlan(event) {
    event.preventDefault(); 
    var select = document.getElementById("income_name");
    var income_name = select.options[select.selectedIndex].text;
    var deduced_amount = document.getElementById("deduced_amount").value;
    var start_date = document.getElementById("start_date").value;
    var end_date = document.getElementById("end_date").value;

    document.querySelector('#income_stream').insertAdjacentHTML(
        'beforebegin',
        '<div class="row">\
        <div class="col" id="frank">\
        <ul>\
          <li>\
            <div class="stream-item">\
              <span class="success">'+ income_name +'</span><br>\
              Deduce <span> '+ deduced_amount +'</span><br>\
              Start: <span class="success">'+ start_date +'</span><br>\
              End: <span class="danger">'+ end_date +'</span>\
            </div>\
          </li>\
        </ul>\
      </div>\
      <div class="col">\
        <button class="text-btn1 success" onclick="editPlan(this)" style="margin:0 0 0 auto">Edit</button><br>\
        <button class="text-btn2 danger" onclick="removePlan(this)" style="margin:0 0 0 auto">Remove</button>\
      </div>')
      alert('Plan Submitted');
    }

form.addEventListener('submit', addPlan);

function removePlan(input){
    input.parentNode.parentNode.remove()
}

function editPlan(self){
    self.parentNode.parentNode.style.opacity = "";
    var plan = self.parentNode.previousElementSibling;
    var span = plan.getElementsByTagName("span");
    var select = form.getElementsByTagName("select");
    var input = form.getElementsByTagName("input");
    input[0].value = span[1].innerText;
    for (var i=0;i<select[0].options.length;i++){
        if (select[0].options[i].innerText == span[0].innerText){
            select[0].selectedIndex = i;
            }
        }
    }
    
