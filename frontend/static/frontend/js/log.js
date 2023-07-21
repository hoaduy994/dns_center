$(function () {
  getLog();

  setInterval(function () {
    getLog();
  }, 3000);
});

function getLog() {
  let url = "datalog";
  $.ajax({
    type: 'GET',
    url: url,
    dataType: 'json',
    success: (response) => {
      data = response.results;
      $(".log-table").html("")
      data.forEach(element => {
        var html = `
        <tr class="row-log">
          <td style="width: 30%; text-align: left; padding: 15px 0 15px 30px; font-size: 16px;">${element.date}</td>
          <td style="width: 70%; text-align: left; padding: 15px 0 15px 30px; font-size: 16px;">${element.data}</td>
        </tr>
        `
        $(".log-table").append(html)
      });
    },
    error: (error) => {
    }
  });
}