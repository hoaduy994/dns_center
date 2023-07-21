$(function () {
  var labels = [];
  var labelsToltip = [];
  var block = [];
  var white = [];
  getData()
  getIndexQueries()
  function getData() {
    labels = [];
    labelsToltip = [];
    block = [];
    white = [];
    let url = "dashboarddata";
    $.ajax({
      type: 'GET',
      url: url,
      dataType: 'json',
      success: function (response) {
        let chart = response.White_Block_Char;

        chart.forEach(element => {
          labelsToltip.push(element.time)

          if (element.time.slice(-2) == "00") {
            labels.push(element.time.slice(-5))
          } else {
            labels.push("")
          }

          block.push(element.block_chart)
          white.push(element.white_chart)
        });

        labelsToltip.reverse();
        block.reverse();
        white.reverse();
        labels.reverse()

        myLineChart.data.datasets[0].data = white;
        myLineChart.data.datasets[1].data = block;
        myLineChart.data.labels = labels;
        myLineChart.update();
      },
      error: function (response) {
      }
    });
  }

  // chart
  var canvas = document.getElementById('myChart');

  var data = {
    datasets: [
      {
        label: "Domain allowed",
        backgroundColor: "rgba(36, 178, 75, 1)",
        borderColor: "rgba(36, 178, 75, 1)",
        pointBorderColor: "rgba(36, 178, 75, 1)",
        pointHoverBackgroundColor: "rgba(36, 178, 75, 1)",
        pointHoverBorderColor: "rgba(36, 178, 75, 1)",
        fill: false,
        lineTension: 0.0,
        borderCapStyle: 'butt',
        borderDash: [],
        borderDashOffset: 0.0,
        borderJoinStyle: 'miter',
        pointBackgroundColor: "#fff",
        pointBorderWidth: 1,
        pointHoverRadius: 2,
        pointHoverBorderWidth: 1,
        pointRadius: 2,
        pointHitRadius: 2
      },
      {
        label: "Domain blocked",
        backgroundColor: "rgba(229, 74, 64, 1)",
        borderColor: "rgba(229, 74, 64, 1)",
        pointBorderColor: "rgba(229, 74, 64, 1)",
        pointHoverBackgroundColor: "rgba(229, 74, 64, 1)",
        pointHoverBorderColor: "rgba(229, 74, 64, 1)",
        fill: false,
        lineTension: 0.0,
        borderCapStyle: 'butt',
        borderDash: [],
        borderDashOffset: 0.0,
        borderJoinStyle: 'miter',
        pointBackgroundColor: "#fff",
        pointBorderWidth: 1,
        pointHoverRadius: 2,
        pointHoverBorderWidth: 1,
        pointRadius: 2,
        pointHitRadius: 2
      }
    ]
  };

  const footer = (tooltipItems) => {
    // let sum = 0;

    // tooltipItems.forEach(function(tooltipItem) {
    //   sum += tooltipItem.parsed.y;
    // });
    return 'Sum:';
  };

  var option = {
    responsive: true,
    maintainAspectRatio: false,
    showLines: true,
    scales: {
      yAxes: [{
        display: true,
        ticks: {
          beginAtZero: true,
          // min: 0,
        },
      }],
      xAxes: [{
        ticks: {
          autoSkip: false,
          maxRotation: 90,
          minRotation: 0
        }
      }],
    },
  };

  var myLineChart = Chart.Line(canvas, {
    data: data,
    options: option
  });

  function getIndexQueries() {
    let url = "indexqueries";
    $.ajax({
      type: 'GET',
      url: url,
      dataType: 'json',
      success: function (response) {
        let data = response.results
        $("#totalQueriesIndex").text(data.total_queries.toString().replace(/\B(?=(\d{3})+(?!\d))/g, '.'));
        $("#queriesBlockedIndex").text(data.Queries_Blocked.toString().replace(/\B(?=(\d{3})+(?!\d))/g, '.'));
        $("#percentBlockedIndex").text(data.Percent_Blocked.toString().replace(/\B(?=(\d{3})+(?!\d))/g, '.'));
        $("#percentDomainListIndex").text(data.Domain_Blocklist.toString().replace(/\B(?=(\d{3})+(?!\d))/g, '.'));
      },
      error: function (response) {
      }
    });
  }


  setInterval(function () {
    getIndexQueries()
    getData();
  }, 30000);

});
// function daterangepicker() {
//   $('.filter-type-chart').val() == 1 ? $('#inputFilterDashboard').prop('disabled', true) : $('#inputFilterDashboard').prop('disabled', false);
//   $('.filter-type-chart').change(function () {
//     $('.filter-type-chart').val() == 1 ? $('#inputFilterDashboard').prop('disabled', true) : $('#inputFilterDashboard').prop('disabled', false);
//   });
//   $('#inputFilterDashboard').daterangepicker(
//     {
//       // autoUpdateInput: false,
//       locale: {
//         format: 'MM/DD/YY',
//       },
//       // autoApply: false,
//       timePicker24Hour: true,
//     });
//   $('#inputFilterDashboard').val('');
//   $('#btnFilterDashboard').click(function () {
//     $('#inputFilterDashboard').val('');
//   }
//   );
// }
