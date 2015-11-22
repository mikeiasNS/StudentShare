var ctx = document.getElementById("CVperfil_atuacao").getContext("2d");
	
var profileMap = #{profileBean.jsonProfile()};
var myGrades = #{profileBean.jsonGrades()};
var topMatchList = #{profileBean.jsonTopM()};
var topMatchGrades = {};

for(var i = 0; i < topMatchList.length; i++){
	topMatchGrades[topMatchList[i]] = #{profileBean.jsonGrades(10, topMatchList[i])}
}

var profiles = [];
var profileGrades = [];
var sum = 0;
for(var key in profileMap){
	profiles.push(key);
	profileGrades.push(profileMap[key].toFixed(4));
	sum += profileMap[key];
}

var avg = sum / grades.length;

var profileData = {
    labels: profiles,
    datasets: [
        {
            label: "Perfis de Atuação",
            fillColor: "rgba(50,80,220,0.5)",
            strokeColor: "rgba(220,220,220,0.8)",
            highlightFill: "rgba(50,80,220,0.75)",
            highlightStroke: "rgba(220,220,220,1)",
            data: profileGrades
        }
    ]
};

for(var key in topMatchGrades){
	for (var k in topMatchGrades[key]) {

	};
	var topMatchData = {
    labels: ,
    datasets: [
        {
            label: "Perfis de Atuação",
            fillColor: "rgba(50,80,220,0.5)",
            strokeColor: "rgba(220,220,220,0.8)",
            highlightFill: "rgba(50,80,220,0.75)",
            highlightStroke: "rgba(220,220,220,1)",
            data: profileGrades
        }
    ]
};
}

var profileChart = new Chart(ctx).Bar(profileData);
document.getElementById("avg").innerHTML = avg.toFixed(2);