$(function () {
  // dns node
  $.ajax({
    type: 'GET',
    url: '/dnsnodedata',
    dataType: 'json',
    success: function (response) {
      let data = response.results;
      data.forEach((element, index) => {
        let html = `
        <tr class="dnsnode">
          <td class="dnsnodeNo">${index + 1}</td>
          <td><a class="dns-name dnsnodeHostname" href="/dnsnode/${element.id}">${element.name_dns}</a></td>
          <td class="dnsnodeIp">${element.ip}</td>
          <td class="dnsnodeRam">${element.ram}%</td>
          <td class="dnsnodeCpu">${element.cpu}%</td>
          <td class="dnsnodeDisk">${element.disk}%</td>
          <td><span id="${element.id}" class="dnsnodeStatus"></span></td>
        </tr>
        `
        $("#dnsnode_body").append(html);
        let id = "#" + String(element.id);
        if (element.status.trim() === "Enable") {
          $(id).addClass('green-dot-icon');
        } else {
          $(id).addClass('grey-dot-icon');
        }
      });
      $('#list_dns_table').DataTable();
    },
    error: function (response) {
    }
  });
});
