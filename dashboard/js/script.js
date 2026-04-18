const ctx = document.getElementById("sensorChart");

const chart = new Chart(ctx, {

type:"line",

data:{

labels:[],

datasets:[

{
label:"Temperature",
data:[],
borderColor:"red"
},

{
label:"RPM",
data:[],
borderColor:"blue"
},

{
label:"Load",
data:[],
borderColor:"green"
}

]

},

options:{responsive:true}

});


function updateChart(data){

chart.data.labels.push("");

chart.data.datasets[0].data.push(data.temperature);
chart.data.datasets[1].data.push(data.rpm);
chart.data.datasets[2].data.push(data.load);

if(chart.data.labels.length>20){

chart.data.labels.shift();

chart.data.datasets.forEach(d=>d.data.shift());

}

chart.update();

}


function updateAlerts(data){

let alertBox=document.getElementById("alerts");

alertBox.innerHTML="";

if(data.vibration>0){

alertBox.innerHTML +=
"<div class='alert'>High Vibration Detected</div>";

}

if(data.surface_defect>0.7){

alertBox.innerHTML +=
"<div class='alert red'>Surface Defect Risk</div>";

}

if(data.surface_defect<0.7 && data.vibration==0){

alertBox.innerHTML +=
"<div class='alert green'>No Active Alerts</div>";

}

}


function updateData(){

fetch("http://127.0.0.1:5000/machine-data")

.then(res=>res.json())

.then(data=>{

document.getElementById("temp").innerText =
data.temperature+" °C";

document.getElementById("rpm").innerText =
data.rpm;

document.getElementById("load").innerText =
data.load;

document.getElementById("vibration").innerText =
data.vibration;

document.getElementById("surface").innerText =
(data.surface_defect*100).toFixed(2)+"%";

document.getElementById("internal").innerText =
(data.internal_defect*100).toFixed(2)+"%";

document.getElementById("health").innerText =
data.health_score+"%";

document.getElementById("status").innerText =
"Machine Status: "+data.machine_status;

updateChart(data);

updateAlerts(data);

});

}

setInterval(updateData,2000);