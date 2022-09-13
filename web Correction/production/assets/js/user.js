var form = document.getElementById("planForm");
function addPlan(event) {
    event.preventDefault(); 
    var select = document.getElementById("income_name");
    var income_name = select.options[select.selectedIndex].text;
    var deduction_plan = document.getElementById("deduction_plan");
    var deduced_amount = document.getElementById("deduced_amount").value;
    var start_date = document.getElementById("start_date").value;
    var end_date = document.getElementById("end_date").value;
    document.querySelector('#income_stream').insertAdjacentHTML(
        'beforebegin',
        '<div class="row">\
        <div class="col">\
        <ul>\
          <li>\
            <div class="stream-item">\
              <span class="success">'+ income_name +'</span>\
              <p>Deduce  '+ deduced_amount + '/=<br>\
                <span style="color:green">Start: '+ start_date + '</span>\
                <br> <span style="color:red">End: '+ end_date + '</span>\
              </p>\
            </div>\
          </li>\
        </ul>\
      </div>\
      <div class="col">\
        <button class="text-btn1 success" style="margin:0 0 0 auto">Edit</button><br>\
        <button class="text-btn2 danger" onclick="removePlan(this)" style="margin:0 0 0 auto">Remove</button>\
      </div>')
  } 
form.addEventListener('submit', addPlan);

function removePlan(input){
    input.parentNode.parentNode.remove()
}


