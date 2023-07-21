$(function () {
  let url = window.location.pathname;
  let id = url.substring(url.lastIndexOf('/') + 1);

  var labels = [];
  var labelsTooltip = [];
  var ram = [];
  var cpu = [];
  var disk = [];
  getData();

  function getData() {
    $.ajax({
      type: 'GET',
      url: '/chartdnsdetail',
      dataType: 'json',
      success: function (response) {
        let dataChart = response.chart.chart_dnsnode;
        dataChart.forEach(element => {
          if (Object.keys(element)[0] === id)
            dataChart = element[id]
        });

        dataChart.forEach(element => {
          // labelsTooltip.push(element.time)
          if (element.time.slice(-2) == "00") {
            labels.push(element.time.slice(-5))
          } else {
            labels.push("")
          }

          cpu.push(element.cpu);
          disk.push(element.disk);
          ram.push(element.ram);
        });

        myBarChart.data.datasets[0].data = ram;
        myBarChart.data.datasets[1].data = cpu;
        myBarChart.data.datasets[2].data = disk;
        myBarChart.data.labels = labels;

        myBarChart.update();

      },
      error: function (response) {
      }
    });
  }


  var canvas = document.getElementById("barChart");
  var ctx = canvas.getContext('2d');
  var labels = [];

  // Global Options:
  Chart.defaults.global.defaultFontColor = 'lato';
  Chart.defaults.global.defaultFontSize = 16;


  // Data with datasets options
  var data = {
    datasets: [
      {
        label: 'RAM',
        backgroundColor: "#1569b2",
        data: ram,
        barThickness: 8,
      }, {
        label: 'CPU',
        backgroundColor: "#f27228",
        data: disk,
        barThickness: 8,
      }, {
        label: 'Disk',
        backgroundColor: "#24b24b",
        data: cpu,
        barThickness: 8,
      }
    ]
  };

  // Notice how nested the beginAtZero is
  var options = {
    tooltips: {
      callbacks: {
        // title: function (tooltipItem, data) {
        //   return labelsTooltip[tooltipItem.index];
        // },
        label: function (tooltipItem, data) {
          console.log(tooltipItem.index, labelsTooltip[tooltipItem.index]);
          return data.datasets[tooltipItem.datasetIndex].label + ': ' + tooltipItem.yLabel + '%';
        },
      },
    },
    responsive: true,
    maintainAspectRatio: false,
    title: {
      display: false,
    },
    scales: {
      yAxes: [{
        ticks: {
          beginAtZero: true,
        }
      }],
      xAxes: [{
        ticks: {
          autoSkip: false,
          maxRotation: 90,
          minRotation: 0
        }
      }],
    },
    style: {
      strokewidth: 10
    },
  };

  Chart.Legend.prototype.afterFit = function () {
    this.height = this.height + 30;
  };

  // Chart declaration:
  var myBarChart = new Chart(ctx, {
    type: 'bar',
    data: data,
    options: options
  });

});
