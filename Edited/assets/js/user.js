function createPlan(){
    document.getElementById("main").style.visibility = "visible";
    document.getElementById("main").style.opacity = "1";
    document.getElementById("newplan").style.display = "none";
  }
  function toggleDeductionPlan(input) {
    var y = input.parentNode.nextElementSibling;
    var z = input.parentNode.nextElementSibling.nextElementSibling;

    if (input.value === "opt1"){
      y.style.display = "block";
      z.style.display = "none";
    }
    else{
      y.style.display = "none";
      z.style.display = "block";
    }
  }
  
  function addAmount(input) {
    input.parentNode.parentNode.insertAdjacentHTML(
    'beforeend',
    '<div class="row" style="margin-top:5px">\
    <input type="number" class="form-control text-center" placeholder="Amount" style="width:70%;margin-left: 20px">\
    <button  onclick="removeRow(this)" class="text-btn2 danger" style="width:80px;font-size:12px"><i class="bx bxs-trash"></i>Remove</button>\
    </div>'
  )
}

    function removeRow (input) {
      input.parentNode.remove()
    }

    function removeSource (input) {
      input.parentNode.parentNode.remove()
    }

    function addSource(){
    document.querySelector('#addsource').insertAdjacentHTML(
      'afterbegin',
      '<div style="width:350px;margin:0 auto 20px auto" data-aos="zoom-in" data-aos-delay="5">\
          <div class="row">\
          <button class="edit text-btn1 success" onclick="editNewForm(this)" style="width:80px;display:none"><i class="bx bxs-edit-alt"></i>Edit</button>\
          <button onclick="removeSource(this)" class="text-btn2 danger" style="width:100px;margin: 0 0 0 auto"><i class="bx bxs-trash"></i>Remove</button>\
          </div>\
        <form >\
          <div class="form-outline mb-4 text-center">\
            <label class="form-label text-center" for="form6Example3">Income Source</label>\
            <select name="place" style="margin: auto;width: 100%" id="form6Example3" class="form-control text-center">\
              <option value="volvo">Salary</option>\
              <option value="saab">Student Meals &amp; Accomodation</option>\
              <option value="opel">Other</option>\
            </select>\
          </div>\
          <div class="form-outline mb-4 text-center">\
            <label class="form-label" for="form6Example4">Income Source Account</label>\
            <input type="text" class="form-control" />\
          </div>\
          <div class="form-outline mb-4 text-center">\
            <label class="form-label" for="form6Example5">Deduction Plan</label>\
            <select style="margin: auto;width: 100%" id="amountType" class="form-control text-center" onclick="toggleDeductionPlan(this)">\
              <option value="opt1" >Same Amount Each time</option>\
              <option value="opt2">Different Amount Each time</option>\
            </select>\
          </div>\
        <div class="form-outline mb-4 text-center" id="amount1">\
          <div class="col"><label class="form-label" for="form6Example6">Amount</label></div>\
          <input type="number" class="form-control" />\
        </div>\
         <div class="form-outline mb-4" id="amount2" style="display:none">\
          <div class="row mb-4" style="margin-left: 95px">\
            <button type="button" class="crdb-btn crdb-color1" onclick="addAmount(this)" style="width:25%">Add</button>\
          </div>\
          <input type="number" class="form-control text-center" placeholder="Amount" style="width:75%;margin-left: 9px">\
        </div>\
          <div class="row mb-4">\
            <div class="col">\
              <div class="form-outline text-center">\
                <label class="form-label" for="form6Example1">From</label>\
                <input type="date" id="form6Example1" class="form-control" value="2018-07-22" min="2018-01-01" max="2018-12-31">\
              </div>\
            </div>\
            <div class="col">\
              <div class="form-outline text-center">\
                <label class="form-label" for="form6Example2">To</label>\
                <input type="date" id="form6Example1" class="form-control" value="2018-07-22" min="2018-01-01" max="2018-12-31">\
              </div>\
            </div>\
          </div>'
          )
        }
        function submitPlans(){
          var f = document.forms;
          var j;
          var i;
          var x = document.getElementsByClassName("edit");
          for(i=0;i<x.length;i++){
            x[i].style.display = "block";
            }
          for(j=0;j<f.length;j++){
            for(var i=0;i<f[j].length;i++){
              if (f[j].elements[i] === "input"){
                  f[j].elements[i].readOnly = true;//As @oldergod noted, the "O" must be upper case
                }
              else {
                    f[j].elements[i].disabled = true;
                  }
              }
          }
        }
        function editForm(input){
          var f = input.nextElementSibling;
          for(var i=0;i<f.elements.length;i++){
            if (f.elements[i] === "input"){
                f.elements[i].readOnly = false;//As @oldergod noted, the "O" must be upper case
              }
            else {
                  f.elements[i].disabled = false;
                }
            }
            input.style.display = "none"
        }
        function editNewForm(input){
          var f = input.parentNode.nextElementSibling;
          for(var i=0;i<f.elements.length;i++){
            if (f.elements[i] === "input"){
                f.elements[i].readOnly = false;//As @oldergod noted, the "O" must be upper case
              }
            else {
                  f.elements[i].disabled = false;
                }
            }
          input.style.display = "none"
        }