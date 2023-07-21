$(function () {
  $('#dnsrecord_table').DataTable();

  $('#dnsrecord_table').on('click', '.del-record', function () {
    let id = $(this).data("id")

    let idNode = $(this).data("idnode")
    idNode = idNode.replace(/'/g, '"');
    idNode = JSON.parse(idNode);

    let ipNode = $(this).data("ipnode")
    ipNode = ipNode.replace(/'/g, '"');
    ipNode = JSON.parse(ipNode);

    let node = $(this).data("node")
    node = node.replace(/'/g, '"');
    node = JSON.parse(node);

    $("#idDnsRecordDel").val(id);

    idNode.forEach((element, index) => {
      let html = `
      <tr>
        <td>
          <div class="form-check">
            <input class="form-check-input" name="idNode" type="checkbox" value="${element}">
          </div>
        </td>
        <td>
          <span>${node[index]}</span>
        </td>
        <td>
          <span>${ipNode[index]}</span>
        </td>
      </tr>
    `
      $("#listDNSRecordDel").append(html);
    });
  })

  $('#modelDeleteRecord').on('hidden.bs.modal', function (e) {
    $("#idDnsRecordDel").val("");
    $("#listDNSRecordDel").empty();
  })

  $('.btn-submit-dnsrecord').click(function (e) {
    e.preventDefault();
    let domain = $('.domain-dnsrecord').val();
    let ipaddress = $('.ip-dnsrecord').val();

    $('.domain-dnsrecord').keyup(function () {
      $('.domain-dnsrecord-err').css({ "display": "none" });
    });

    $('.ip-dnsrecord').keyup(function () {
      $('.ip-dnsrecord-err').css({ "display": "none" });
    });

    if (!ValidateNull(domain)) {
      $('.domain-dnsrecord-err').text("Required fields !");
      $('.domain-dnsrecord-err').css({ "display": "block" });
    }

    if (!ValidateNull(ipaddress)) {
      $('.ip-dnsrecord-err').text("IP address is required !");
      $('.ip-dnsrecord-err').css({ "display": "block" });
    } else if (!ValidateIPaddress(ipaddress)) {
      $('.ip-dnsrecord-err').text("Invalid IP address !");
      $('.ip-dnsrecord-err').css({ "display": "block" });
    }

    let checked = $('.checkbox-dnsrecord:checked').length;

    if (checked <= 0) {
      $('.checkbox-dnsrecord-err').text("Required fields !");
      $('.checkbox-dnsrecord-err').css({ "display": "block" });
    }

    if (ValidateNull(domain)  && ValidateNull(ipaddress) && ValidateIPaddress(ipaddress) && checked > 0) {
      $('.form-add-dnsrecord').submit();
    }
  });

  // function ValidateDomain(domain) {
  //   if (/^[a-zA-Z0-9][a-zA-Z0-9-]{1,61}[a-zA-Z0-9](?:\.[a-zA-Z]{2,})+$/.test(domain)) {
  //     return (true)
  //   }
  //   return (false)
  // }

  function ValidateNull(data) {
    data = data.trim().length;
    if (data && data > 0) {
      return (true)
    }
    return (false)
  }

  function ValidateIPaddress(ipaddress) {
    if (/^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$/.test(ipaddress)) {
      return (true)
    }
    return (false)
  }
});